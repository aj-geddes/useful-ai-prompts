# Terraform Multi-Cloud Configuration

## Terraform Multi-Cloud Configuration

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
