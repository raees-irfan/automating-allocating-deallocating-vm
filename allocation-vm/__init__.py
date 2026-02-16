import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import os

def main(mytimer: func.TimerRequest) -> None:
    logging.info("▶️  VM Start function triggered at 6:00 AM")

    subscription_id = os.environ["Azure subscription 1"]
    resource_group  = os.environ["learning-project"]
    vm_name         = os.environ["vm-scheduller"]

    credential = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credential, subscription_id)

    logging.info(f"Starting VM: {vm_name} in resource group: {resource_group}")

    poller = compute_client.virtual_machines.begin_start(resource_group, vm_name)
    poller.result()

    logging.info(f"✅ VM '{vm_name}' has been started successfully.")