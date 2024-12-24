import requests
import json
import oci
from oci.signer import Signer

# Replace these values with your specific information
compartment_id = "<COMPARTMENT_OCID>" # Compartment OCID
namespace = "<METRIC_NAMESPACE>" # Metric namespace to use
metric_query = "<METRIC_QUERY>" # Query from Monitoring service
destination_id = "<DESTINATION_OCID>"  # Notification topic OCID
region = "<REGION>"  # Example: us-ashburn-1

# Endpoint for the Monitoring service
monitoring_endpoint = f"https://telemetry.{region}.oraclecloud.com"

# Alarm details
alarm_details = {
    "compartmentId": compartment_id,
    "displayName": "Example Alarm",
    "metricCompartmentId": compartment_id,
    "namespace": namespace,
    "query": metric_query,
    "severity": "CRITICAL",
    "destinations": [destination_id],
    "isEnabled": True,
    "body": "This is an example alarm triggered by metric conditions.",
    "messageFormat": "RAW",
    "resolution": "1m",
    "repeatNotificationDuration": "PT1H",  # Example: 1-hour interval
}

# Initialize a signer using the default OCI config file
config = oci.config.from_file("~/.oci/config", "DEFAULT")  # Update path and profile if needed
signer = Signer(
    tenancy=config["tenancy"],
    user=config["user"],
    fingerprint=config["fingerprint"],
    private_key_file_location=config["key_file"],
    pass_phrase=config.get("pass_phrase"),
)

# Headers for the REST API request
headers = {
    "Content-Type": "application/json",
    "opc-retry-token": "retry-token-example",  # Optional: Used for idempotency
}

# Make the API call
response = requests.post(
    f"{monitoring_endpoint}/20180401/alarms",
    headers=headers,
    auth=signer,
    data=json.dumps(alarm_details),
)

# Check response status
if response.status_code == 201:
    print("Alarm created successfully!")
    print("Response:", json.dumps(response.json(), indent=4))
else:
    print("Failed to create the alarm.")
    print("Status code:", response.status_code)
    print("Response:", response.text)