import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()

object_storage_client = oci.object_storage.ObjectStorageClient(config)
result = object_storage_client.get_namespace()
print("Current object storage namespace: {}".format(result.data))