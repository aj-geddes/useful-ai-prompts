---
name: multi-cloud-strategy
description: Design and implement multi-cloud strategies spanning AWS, Azure, and GCP with vendor lock-in avoidance, hybrid deployments, and federation.
---

# Multi-Cloud Strategy

## Overview

Multi-cloud strategies enable leveraging multiple cloud providers for flexibility, redundancy, and optimization. Avoid vendor lock-in, optimize costs by comparing cloud services, and implement hybrid deployments with seamless data synchronization.

## When to Use

- Reducing vendor lock-in risk
- Optimizing costs across providers
- Geographic distribution requirements
- Compliance with regional data laws
- Disaster recovery and high availability
- Hybrid cloud deployments
- Multi-region application deployment
- Avoiding single cloud provider dependency

## Implementation Examples

### 1. **Multi-Cloud Abstraction Layer**

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

### 2. **Multi-Cloud Kubernetes Deployment**

```yaml
# Kubernetes deployment across multiple clouds
apiVersion: v1
kind: Namespace
metadata:
  name: multi-cloud-app

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: cloud-config
  namespace: multi-cloud-app
data:
  cloud-provider: "kubernetes" # Abstracted from specific cloud
  region: "global"
  environment: "production"

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
  namespace: multi-cloud-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: multi-cloud-app
      cloud: "any"
  template:
    metadata:
      labels:
        app: multi-cloud-app
        cloud: "any"
    spec:
      # Node affinity for multi-cloud
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 50
              preference:
                matchExpressions:
                  - key: cloud.provider
                    operator: In
                    values: ["aws", "azure", "gcp"]
            - weight: 30
              preference:
                matchExpressions:
                  - key: topology.kubernetes.io/region
                    operator: In
                    values: ["us-east-1", "eastus", "us-central1"]

      containers:
        - name: app
          image: myregistry/my-app:latest
          ports:
            - containerPort: 8080
          env:
            - name: CLOUD_NATIVE
              value: "true"
            - name: LOG_LEVEL
              value: "info"
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi

---
apiVersion: v1
kind: Service
metadata:
  name: app-service
  namespace: multi-cloud-app
spec:
  type: LoadBalancer
  selector:
    app: multi-cloud-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

### 3. **Terraform Multi-Cloud Configuration**

```hcl
# terraform.tf - Multi-cloud setup
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }

  # Multi-cloud state management
  cloud {
    organization = "my-org"
    workspaces {
      name = "multi-cloud"
    }
  }
}

# AWS Provider
provider "aws" {
  region = var.aws_region
}

# Azure Provider
provider "azurerm" {
  features {}
}

# GCP Provider
provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

# Variables
variable "aws_region" {
  default = "us-east-1"
}

variable "azure_region" {
  default = "eastus"
}

variable "gcp_region" {
  default = "us-central1"
}

variable "gcp_project_id" {}

# AWS VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    cloud = "aws"
  }
}

# Azure VNet
resource "azurerm_virtual_network" "main" {
  name                = "main-vnet"
  address_space       = ["10.1.0.0/16"]
  location            = var.azure_region
  resource_group_name = azurerm_resource_group.main.name

  tags = {
    cloud = "azure"
  }
}

# GCP VPC
resource "google_compute_network" "main" {
  name                    = "main-vpc"
  auto_create_subnetworks = true

  tags = ["cloud-gcp"]
}

# AWS EC2 Instance
resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.main.id

  tags = {
    Name  = "app-aws"
    cloud = "aws"
  }
}

# Azure VM
resource "azurerm_linux_virtual_machine" "app" {
  name                = "app-azure"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  size                = "Standard_B1s"

  admin_username = "azureuser"

  admin_ssh_key {
    username   = "azureuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  tags = {
    cloud = "azure"
  }
}

# GCP Compute Instance
resource "google_compute_instance" "app" {
  name         = "app-gcp"
  machine_type = "f1-micro"
  zone         = "${var.gcp_region}-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = 20
    }
  }

  network_interface {
    network = google_compute_network.main.name
  }

  tags = ["cloud-gcp"]
}

# Multi-cloud service mesh (Istio)
resource "helm_release" "istio" {
  name             = "istio"
  repository       = "https://istio-release.storage.googleapis.com/charts"
  chart            = "istiod"
  namespace        = "istio-system"
  create_namespace = true

  depends_on = [
    aws_instance.app,
    azurerm_linux_virtual_machine.app,
    google_compute_instance.app
  ]
}

# Outputs
output "aws_instance_ip" {
  value = aws_instance.app.public_ip
}

output "azure_instance_ip" {
  value = azurerm_linux_virtual_machine.app.public_ip_address
}

output "gcp_instance_ip" {
  value = google_compute_instance.app.network_interface[0].network_ip
}
```

### 4. **Data Synchronization across Clouds**

```python
# Multi-cloud data replication
import boto3
from azure.storage.blob import BlobServiceClient
from google.cloud import storage
import hashlib
from datetime import datetime

class MultiCloudDataSync:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.azure_client = BlobServiceClient.from_connection_string(
            "DefaultEndpointsProtocol=https;..."
        )
        self.gcp_client = storage.Client()

    def sync_object_to_all_clouds(self, source_cloud, source_bucket, key, data):
        """Sync object to all cloud providers"""
        try:
            # Calculate checksum
            checksum = hashlib.sha256(data).hexdigest()

            if source_cloud == "aws":
                # Upload to AWS
                self.s3.put_object(
                    Bucket=source_bucket,
                    Key=key,
                    Body=data,
                    Metadata={'checksum': checksum, 'synced-at': datetime.utcnow().isoformat()}
                )
                # Replicate to Azure
                self._sync_to_azure(key, data, checksum)
                # Replicate to GCP
                self._sync_to_gcp(key, data, checksum)

            elif source_cloud == "azure":
                # Upload to Azure
                container_client = self.azure_client.get_container_client("data")
                container_client.upload_blob(
                    key,
                    data,
                    overwrite=True,
                    metadata={'checksum': checksum, 'synced-at': datetime.utcnow().isoformat()}
                )
                # Replicate to AWS
                self._sync_to_aws(key, data, checksum)
                # Replicate to GCP
                self._sync_to_gcp(key, data, checksum)

            elif source_cloud == "gcp":
                # Upload to GCP
                bucket = self.gcp_client.bucket("my-bucket")
                blob = bucket.blob(key)
                blob.upload_from_string(
                    data,
                    metadata={'checksum': checksum, 'synced-at': datetime.utcnow().isoformat()}
                )
                # Replicate to AWS
                self._sync_to_aws(key, data, checksum)
                # Replicate to Azure
                self._sync_to_azure(key, data, checksum)

            return {
                'status': 'success',
                'key': key,
                'checksum': checksum,
                'synced_clouds': ['aws', 'azure', 'gcp']
            }

        except Exception as e:
            print(f"Error syncing data: {e}")
            return {'status': 'failed', 'error': str(e)}

    def _sync_to_aws(self, key, data, checksum):
        """Sync to AWS S3"""
        self.s3.put_object(
            Bucket='my-bucket',
            Key=key,
            Body=data,
            Metadata={'source': 'multi-cloud-sync', 'checksum': checksum}
        )

    def _sync_to_azure(self, key, data, checksum):
        """Sync to Azure Blob Storage"""
        container_client = self.azure_client.get_container_client("data")
        container_client.upload_blob(
            key,
            data,
            overwrite=True,
            metadata={'source': 'multi-cloud-sync', 'checksum': checksum}
        )

    def _sync_to_gcp(self, key, data, checksum):
        """Sync to GCP Cloud Storage"""
        bucket = self.gcp_client.bucket("my-bucket")
        blob = bucket.blob(key)
        blob.upload_from_string(
            data,
            metadata={'source': 'multi-cloud-sync', 'checksum': checksum}
        )

    def verify_consistency(self, key):
        """Verify data consistency across all clouds"""
        checksums = {}

        # Get from AWS
        try:
            aws_obj = self.s3.get_object(Bucket='my-bucket', Key=key)
            aws_data = aws_obj['Body'].read()
            checksums['aws'] = hashlib.sha256(aws_data).hexdigest()
        except Exception as e:
            checksums['aws'] = f'error: {str(e)}'

        # Get from Azure
        try:
            container_client = self.azure_client.get_container_client("data")
            blob_client = container_client.get_blob_client(key)
            azure_data = blob_client.download_blob().readall()
            checksums['azure'] = hashlib.sha256(azure_data).hexdigest()
        except Exception as e:
            checksums['azure'] = f'error: {str(e)}'

        # Get from GCP
        try:
            bucket = self.gcp_client.bucket("my-bucket")
            blob = bucket.blob(key)
            gcp_data = blob.download_as_bytes()
            checksums['gcp'] = hashlib.sha256(gcp_data).hexdigest()
        except Exception as e:
            checksums['gcp'] = f'error: {str(e)}'

        consistent = len(set(v for v in checksums.values() if not v.startswith('error'))) <= 1

        return {
            'key': key,
            'consistent': consistent,
            'checksums': checksums
        }
```

## Best Practices

### ✅ DO
- Use cloud-agnostic APIs and frameworks
- Implement abstraction layers
- Monitor costs across clouds
- Use Kubernetes for portability
- Plan for data residency requirements
- Test failover scenarios
- Document cloud-specific configurations
- Use infrastructure as code

### ❌ DON'T
- Use cloud-specific services extensively
- Create hard dependencies on one provider
- Ignore compliance requirements
- Forget about data transfer costs
- Neglect network latency issues
- Skip disaster recovery planning

## Multi-Cloud Considerations

- Data residency and compliance
- Network latency and connectivity
- Cost comparison and optimization
- Security and identity management
- Operational complexity
- Service feature parity

## Resources

- [Kubernetes Multi-Cloud](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/)
- [CNCF Landscape](https://landscape.cncf.io/)
- [Cloud Provider Comparison](https://cloud.google.com/docs/compare)
- [Terraform Multi-Cloud](https://www.terraform.io/cloud-docs)
