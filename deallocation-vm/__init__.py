import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import os

def main(mytimer: func.TimerRequest) -> None:
    logging.info("⏹️  VM Stop function triggered at 1:00 PM")

    subscription_id = os.environ["Azure subscription 1"]
    resource_group  = os.environ["learning-project"]
    vm_name         = os.environ["vm-scheduller"]

    credential = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credential, subscription_id)

    logging.info(f"Stopping VM: {vm_name} in resource group: {resource_group}")

    poller = compute_client.virtual_machines.begin_deallocate(resource_group, vm_name)
    poller.result()

    logging.info(f"✅ VM '{vm_name}' has been stopped and deallocated successfully.")