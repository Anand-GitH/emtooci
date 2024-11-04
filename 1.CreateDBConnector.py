import oci

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
get_external_database_connector_response = database_client.get_external_database_connector(
    external_database_connector_id="ocid1.externaldatabaseconnector.oc1.iad.anuwcljre5xv5jiampk2i7i5wos7oo7wqu3c222edbknbrcpyqwduiadm66a")

# Get the data from response
print(get_external_database_connector_response.data)
"""

# Send the request to service, some parameters are not required, see API
# doc for more info
create_external_database_connector_response = database_client.create_external_database_connector(
    create_external_database_connector_details=oci.database.models.CreateExternalMacsConnectorDetails(
        connector_type="MACS",
        display_name="financedbconnector202410300757",
        external_database_id="ocid1.externalnoncontainerdatabase.oc1.iad.anuwcljre5xv5jiagfw5j2y4avfmb57kntyjhmdwujknxquuwvl5sicv46ra",
        connection_string=oci.database.models.DatabaseConnectionString(
            hostname="129.80.169.91",
            port=1525,
            service="finance.subnet.vcn.oraclevcn.com",
            protocol="TCP"),
        connection_credentials=oci.database.models.DatabaseSslConnectionCredentials(
            credential_type="DETAILS",
            username="sys",
            password="welcome1",
            role="SYSDBA",
            credential_name="Connector202410300844.991f59cbfb3f4a0b9167e77808d69b8b"),
        connector_agent_id="ocid1.managementagent.oc1.iad.amaaaaaae5xv5jiarqw5htoyk25wnsvqhe4555bhdog4bjocvfmpghjyalqa",
        freeform_tags={
            'createdby': 'Automation'},
        defined_tags={
            }))

# Get the data from response
print(create_external_database_connector_response.data)
