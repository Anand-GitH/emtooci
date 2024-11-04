import oci
import json
import time


############################################Initialization starts##################################################
"""
Stack Monitoring Discovery type includes
1.ADD
2.ADD_WITH_RETRY
3.REFRESH

Agent ID can be fetched by querying agents with host name
ListManagementAgents
https://docs.oracle.com/en-us/iaas/api/#/en/management-agent/20200202/ManagementAgent/ListManagementAgents
"""
l_compartmentID = ""
l_resourcename = "" #To add custom name from Remedy it can be done here
l_dbhostname = ""
l_dbport= ""
l_dbservicename= ""
l_dbusername= ""   #Encoded in base64
l_dbpassword= ""  #Encoded in base64
l_dbrole= ""   #Encoded in base64
l_agentid= ""
l_discoverytype= "ADD"
l_discoveryclient= "EMtoOCIDiscovery" #user defined name to identify from where discovery was initiated 

"""
Grouping of targets can be done using the user defined tags 
OracleHealth is the tag namespace and it has two tags 
environment : Values include Prod,UAT,Dev
lob : Values include backoffice,frontoffice
"""

l_environment = "Prod" 
l_lob = "backoffice"

#####################################Initialization is complete##################################################

config = oci.config.from_file()

print("Initialize the Stack Monitoring Client")


# Initialize Stack Monitoring service client with default config file 
stack_monitoring_client = oci.stack_monitoring.StackMonitoringClient(config)

print("Calling Discovery Job for the Database:"+ l_resourcename)
#Initiate Discovery Job 
create_discovery_job_response = stack_monitoring_client.create_discovery_job(
    create_discovery_job_details=oci.stack_monitoring.models.CreateDiscoveryJobDetails(
        compartment_id= l_compartmentID,
        discovery_details=oci.stack_monitoring.models.DiscoveryDetails(
            agent_id=l_agentid,
            resource_type="ORACLE_DATABASE",
            resource_name=l_resourcename,
            properties=oci.stack_monitoring.models.PropertyDetails(
                properties_map={
                      "database_host_name": l_dbhostname,
                      "database_port": l_dbport,
                      "database_protocol": "tcp",
                      "database_service_name": l_dbservicename,
                      "ebs_long_running_request_threshold": "60",
                      "is_asm_discovery": "false"}),
            license="ENTERPRISE_EDITION",
            credentials=oci.stack_monitoring.models.CredentialCollection(
                items=[
                    oci.stack_monitoring.models.CredentialDetails(
                        credential_name="U1FMQ3JlZHM=",
                        credential_type="REJDcmVkcw==",
                        properties=oci.stack_monitoring.models.PropertyDetails(
                        properties_map={
                        "DBUserName": l_dbusername,
                        "DBPassword": l_dbpassword,
                        "DBRole": l_dbrole}
    ))])),
        discovery_type=l_discoverytype,
        discovery_client=l_discoveryclient,
        should_propagate_tags_to_discovered_resources=True,
        freeform_tags={
            'createdby': 'Automation'},
        defined_tags={
            'OracleHealth': {
                'environment': l_environment,
                'lob': l_lob}}))


response = json.loads(str(create_discovery_job_response.data))
discovery_status=response["status"]
discoveryjobid=response["id"]
print("Discovery job submitted and current job status:"+ discovery_status)

while discovery_status in ["CREATED","INPROGRESS"]:
    print("-"*3)
    time.sleep(120)
    get_discovery_job_response = stack_monitoring_client.get_discovery_job(
    discovery_job_id=discoveryjobid)

    response = json.loads(str(get_discovery_job_response.data))
    discovery_status=response["status"]

print("Discovery Job Status:"+discovery_status)

print("Fetch External Non Container Database OCID from stack monitoring query service")


search_monitored_resources_response = stack_monitoring_client.search_monitored_resources(
    search_monitored_resources_details=oci.stack_monitoring.models.SearchMonitoredResourcesDetails(
        compartment_id=l_compartmentID,
        lifecycle_states=["ACTIVE"],
        name=l_resourcename,
       ))

response = json.loads(str(search_monitored_resources_response.data))
external_dbid = response["items"][0]["external_id"]

print ("Get External DB Name and Connector to enable DBM and OPs Insights")
database_client = oci.database.DatabaseClient(config)

get_external_non_container_database_response = database_client.get_external_non_container_database(
    external_non_container_database_id=external_dbid)

response = json.loads(str(get_external_non_container_database_response.data))
db_connectorid = response["stack_monitoring_config"]["stack_monitoring_connector_id"]

# Enable DBM 
print('Enable Database Management Service')
enable_external_non_container_database_database_management_response = database_client.enable_external_non_container_database_database_management(
    external_non_container_database_id=external_dbid,
    enable_external_non_container_database_database_management_details=oci.database.models.EnableExternalNonContainerDatabaseDatabaseManagementDetails(
        license_model="BRING_YOUR_OWN_LICENSE",
        external_database_connector_id=db_connectorid)
        )

get_external_non_container_database_response = database_client.get_external_non_container_database(
    external_non_container_database_id=external_dbid)

response = json.loads(str(get_external_non_container_database_response.data))
lifecycle_state = response["lifecycle_state"]

while lifecycle_state in ["UPDATING"]:
    print("-"*3)
    time.sleep(120)
    get_external_non_container_database_response = database_client.get_external_non_container_database(
    external_non_container_database_id=external_dbid)

    response = json.loads(str(get_external_non_container_database_response.data))
    lifecycle_state = response["lifecycle_state"]

print("Lifecycle Status of DB:"+lifecycle_state)


# Enable Ops Insights
print('Enable Operations Insights Service')
enable_external_non_container_database_operations_insights_response = database_client.enable_external_non_container_database_operations_insights(
    external_non_container_database_id=external_dbid,
    enable_external_non_container_database_operations_insights_details=oci.database.models.EnableExternalNonContainerDatabaseOperationsInsightsDetails(
        external_database_connector_id=db_connectorid))


get_external_non_container_database_response = database_client.get_external_non_container_database(
    external_non_container_database_id=external_dbid)

response = json.loads(str(get_external_non_container_database_response.data))
lifecycle_state = response["lifecycle_state"]

while lifecycle_state in ["UPDATING"]:
    print("-"*3)
    time.sleep(120)
    get_external_non_container_database_response = database_client.get_external_non_container_database(
    external_non_container_database_id=external_dbid)

    response = json.loads(str(get_external_non_container_database_response.data))
    lifecycle_state = response["lifecycle_state"]

print("Lifecycle Status of DB:"+lifecycle_state)


get_external_non_container_database_response = database_client.get_external_non_container_database(
    external_non_container_database_id=external_dbid)

print("")
response = json.loads(str(get_external_non_container_database_response.data))
operations_insights_status = response["operations_insights_config"]["operations_insights_status"]
stack_monitoring_status = response["stack_monitoring_config"]["stack_monitoring_status"]
database_management_status = response["database_management_config"]["database_management_status"]
display_name = response["display_name"]


print("For the database:"+display_name)
print("Database Management Status:", database_management_status)
print("Operations Insights Status:", operations_insights_status)
print("Stack Monitoring Status:", stack_monitoring_status)





