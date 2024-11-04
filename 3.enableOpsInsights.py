import oci
import json

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
database_client = oci.database.DatabaseClient(config)

"""
# Send the request to service, some parameters are not required, see API
# doc for more info
enable_external_non_container_database_operations_insights_response = database_client.enable_external_non_container_database_operations_insights(
    external_non_container_database_id="ocid1.externalnoncontainerdatabase.oc1.iad.anuwcljte5xv5jiafkeypigri55sxq6dd3uikntppz674uqcbrpotdkp7gsa",
    enable_external_non_container_database_operations_insights_details=oci.database.models.EnableExternalNonContainerDatabaseOperationsInsightsDetails(
        external_database_connector_id="ocid1.externaldatabaseconnector.oc1.iad.anuwcljte5xv5jiazzez5av7jdyvedjhqmuqhfa66nibqyzsal4z7ondsoiq"))

# Get the data from response
print(enable_external_non_container_database_operations_insights_response.headers)
"""

# doc for more info
get_external_non_container_database_response = database_client.get_external_non_container_database(
    external_non_container_database_id="ocid1.externalnoncontainerdatabase.oc1.iad.anuwcljte5xv5jiafkeypigri55sxq6dd3uikntppz674uqcbrpotdkp7gsa")


# Get the data from response
response = json.loads(str(get_external_non_container_database_response.data))

operations_insights_status = response["operations_insights_config"]["operations_insights_status"]
stack_monitoring_status = response["stack_monitoring_config"]["stack_monitoring_status"]
database_management_status = response["database_management_config"]["database_management_status"]
display_name = response["display_name"]

# Printing the results
print("Operations Insights Status:", operations_insights_status)
print("Stack Monitoring Status:", stack_monitoring_status)
print("Database Management Status:", database_management_status)
print("Display Name:", display_name)