# Multi-Cloud Abstraction Layer

## Multi-Cloud Abstraction Layer

```python
# Multi-cloud compute abstraction
from abc import ABC, abstractmethod
from enum import Enum

class CloudProvider(Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"

class ComputeInstance(ABC):
    """Abstract compute instance"""
    @abstractmethod
    def start(self): pass

    @abstractmethod
    def stop(self): pass

    @abstractmethod
    def get_status(self): pass

# AWS implementation
import boto3

class AWSComputeInstance(ComputeInstance):
    def __init__(self, instance_id, region='us-east-1'):
        self.instance_id = instance_id
        self.ec2 = boto3.client('ec2', region_name=region)

    def start(self):
        self.ec2.start_instances(InstanceIds=[self.instance_id])
        return True

    def stop(self):
        self.ec2.stop_instances(InstanceIds=[self.instance_id])
        return True

    def get_status(self):
        response = self.ec2.describe_instances(InstanceIds=[self.instance_id])
        return response['Reservations'][0]['Instances'][0]['State']['Name']

# Azure implementation
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

class AzureComputeInstance(ComputeInstance):
    def __init__(self, instance_id, resource_group, subscription_id):
        self.instance_id = instance_id
        self.resource_group = resource_group
        credential = DefaultAzureCredential()
        self.client = ComputeManagementClient(credential, subscription_id)

    def start(self):
        self.client.virtual_machines.begin_start(
            self.resource_group,
            self.instance_id
        ).wait()
        return True

    def stop(self):
        self.client.virtual_machines.begin_power_off(
            self.resource_group,
            self.instance_id
        ).wait()
        return True

    def get_status(self):
        vm = self.client.virtual_machines.get(
            self.resource_group,
            self.instance_id
        )
        return vm.provisioning_state

# GCP implementation
from google.cloud import compute_v1

class GCPComputeInstance(ComputeInstance):
    def __init__(self, instance_id, zone, project_id):
        self.instance_id = instance_id
        self.zone = zone
        self.project_id = project_id
        self.client = compute_v1.InstancesClient()

    def start(self):
        request = compute_v1.StartInstanceRequest(
            project=self.project_id,
            zone=self.zone,
            resource=self.instance_id
        )
        self.client.start(request=request).result()
        return True

    def stop(self):
        request = compute_v1.StopInstanceRequest(
            project=self.project_id,
            zone=self.zone,
            resource=self.instance_id
        )
        self.client.stop(request=request).result()
        return True

    def get_status(self):
        request = compute_v1.GetInstanceRequest(
            project=self.project_id,
            zone=self.zone,
            resource=self.instance_id
        )
        instance = self.client.get(request=request)
        return instance.status

# Factory pattern for cloud provider
class ComputeInstanceFactory:
    @staticmethod
    def create_instance(provider: CloudProvider, **kwargs):
        if provider == CloudProvider.AWS:
            return AWSComputeInstance(**kwargs)
        elif provider == CloudProvider.AZURE:
            return AzureComputeInstance(**kwargs)
        elif provider == CloudProvider.GCP:
            return GCPComputeInstance(**kwargs)
        else:
            raise ValueError(f"Unknown provider: {provider}")

# Usage
aws_instance = ComputeInstanceFactory.create_instance(
    CloudProvider.AWS,
    instance_id="i-1234567890abcdef0",
    region="us-east-1"
)
aws_instance.start()
```
