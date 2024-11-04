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
enable_external_non_container_database_database_management_response = database_client.enable_external_non_container_database_database_management(
    external_non_container_database_id="ocid1.externalnoncontainerdatabase.oc1.iad.anuwcljte5xv5jiafkeypigri55sxq6dd3uikntppz674uqcbrpotdkp7gsa",
    enable_external_non_container_database_database_management_details=oci.database.models.EnableExternalNonContainerDatabaseDatabaseManagementDetails(
        license_model="BRING_YOUR_OWN_LICENSE",
        external_database_connector_id="ocid1.externaldatabaseconnector.oc1.iad.anuwcljte5xv5jiazzez5av7jdyvedjhqmuqhfa66nibqyzsal4z7ondsoiq")
        )

# Get the data from response
print(enable_external_non_container_database_database_management_response.headers)