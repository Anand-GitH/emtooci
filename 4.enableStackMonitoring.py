import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
database_client = oci.database.DatabaseClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
enable_external_non_container_database_stack_monitoring_response = database_client.enable_external_non_container_database_stack_monitoring(
    external_non_container_database_id="ocid1.externalnoncontainerdatabase.oc1.iad.anuwcljre5xv5jiavcys7s6llzejd7schnltyvxgmhcf3rv5ehs2bp7elx4q",
    enable_external_non_container_database_stack_monitoring_details=oci.database.models.EnableExternalNonContainerDatabaseStackMonitoringDetails(
        external_database_connector_id="ocid1.externaldatabaseconnector.oc1.iad.anuwcljre5xv5jiait2ddli572qi2y43obs6q5wup6p45uuqxskwbi2deqhq"))

# Get the data from response
print(enable_external_non_container_database_stack_monitoring_response.headers)


