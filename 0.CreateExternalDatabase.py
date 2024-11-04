import oci

config = oci.config.from_file()
# Initialize service client with default config file
database_client = oci.database.DatabaseClient(config)

# Send the request to service, some parameters are not required, see API
# doc for more info
create_external_non_container_database_response = database_client.create_external_non_container_database(
    create_external_non_container_database_details=oci.database.models.CreateExternalNonContainerDatabaseDetails(
        compartment_id="ocid1.compartment.oc1..aaaaaaaabbcyd3setuepewotjhanjsise5kwm6ssws3r3nrf7rcdthc65ohq",
        display_name="financeDB03112024",
        freeform_tags={
            'createdby': 'Automation'},
        defined_tags={
            'OracleHealth': {
                'environment': 'Prod',
                'lob': 'backoffice'}}))

# Get the data from response
print(create_external_non_container_database_response.data)
