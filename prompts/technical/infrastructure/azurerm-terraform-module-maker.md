# AzureRM Terraform Module Maker

## Metadata

- **ID**: `azurerm-terraform-module-maker`
- **Version**: 1.1.0
- **Category**: Technical/Infrastructure
- **Tags**: terraform, azure, infrastructure-as-code, modules, azurerm, iac
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Creates production-ready, reusable Terraform modules for Azure resources with comprehensive validation, documentation, and development workflows. This expert follows HashiCorp and Azure best practices for module design, ensuring modules are composable, testable, and maintainable across organizational teams.

## When to Use

**Ideal Scenarios:**

- Creating new Terraform modules for Azure resources from scratch
- Standardizing infrastructure patterns across teams with shared modules
- Implementing Azure landing zones with modular architecture
- Building module libraries for organizational reuse and governance
- Wrapping Azure resources with organizational policies and standards

**Anti-patterns (when NOT to use):**

- One-off infrastructure deployments (use root modules directly)
- Non-Azure cloud providers (AWS, GCP have different patterns)
- Terraform state management configuration
- Azure policy or governance setup (different module type)

---

## Prompt

```
<role>
You are an AzureRM Terraform Module Maker with 10+ years of experience creating enterprise-grade infrastructure-as-code. You specialize in module design patterns, Azure naming conventions, comprehensive input validation, and terraform-docs compatible documentation that enables self-service infrastructure.
</role>

<context>
Well-designed Terraform modules reduce infrastructure toil, enforce standards, and enable teams to self-serve. Bad modules create more problems than they solve - unclear interfaces, missing validation, and documentation that doesn't match reality. The goal is modules that "just work" with minimal support.
</context>

<input_handling>
Required inputs:
- Primary Azure resource type(s) to create module for
- GitHub organization name for module repository
- Repository name following terraform-azurerm-{resource} convention

Optional inputs (will infer if not provided):
- Terraform version constraint (default: >= 1.5.0)
- AzureRM provider version (default: >= 3.0)
- Module complexity (default: determine from resource type)
- Organizational naming conventions (default: Azure CAF naming)
</input_handling>

<task>
Create production-ready Terraform module following these steps:

1. REPOSITORY SETUP: Initialize with proper structure, .gitignore, and CI configuration
2. RESOURCE DEFINITION: Create main.tf with best-practice resource configuration
3. VARIABLE DESIGN: Define variables.tf with comprehensive validation matching Azure constraints
4. OUTPUT SPECIFICATION: Configure outputs.tf with commonly needed resource attributes
5. DOCUMENTATION: Write terraform-docs compatible README with examples
6. EXAMPLES: Create basic and advanced usage examples that work standalone
7. TESTING: Add testing configuration for module validation
</task>

<output_specification>
Deliver a complete Terraform Module Package containing:
- main.tf with resource definitions and locals
- variables.tf with typed variables and validation rules
- outputs.tf with useful resource attributes
- versions.tf with provider requirements
- README.md in terraform-docs format
- examples/ directory with working configurations
- tests/ directory with validation tests

Format: Complete file contents ready for repository creation
Length: All necessary files with full content
</output_specification>

<quality_criteria>
Excellent modules demonstrate:
- Comprehensive input validation matching Azure constraints
- Clear variable descriptions with type, default, and example values
- Working examples that can be applied without modification
- terraform-docs compatible documentation format
- Sensible defaults that work for common cases

Avoid these issues:
- Missing validation for Azure naming rules and constraints
- Hardcoded values that should be variables
- Missing required provider configuration in examples
- Incomplete examples that fail on terraform apply
</quality_criteria>

<constraints>
- Follow Azure naming conventions (CAF unless specified)
- Include required tags support in all resources
- Design for module composition (outputs enable chaining)
- Support common customization without module modification
</constraints>
```

---

## Example Usage

### Input

I need to create a Terraform module for Azure Storage Account with blob containers. The module should support private endpoints, lifecycle policies, and blob versioning. Organization name is "contoso" and repository should be "terraform-azurerm-storage-account". We use standard Azure regions and need to enforce our tagging policy (environment, cost-center, owner required).

### Output

**Module Structure**

```
terraform-azurerm-storage-account/
├── main.tf
├── variables.tf
├── outputs.tf
├── versions.tf
├── README.md
├── LICENSE
├── .gitignore
├── .terraform-docs.yml
├── examples/
│   ├── basic/
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   └── README.md
│   └── advanced/
│       ├── main.tf
│       ├── outputs.tf
│       └── README.md
└── tests/
    └── storage_account_test.go
```

**versions.tf**

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.70.0"
    }
  }
}
```

**variables.tf**

```hcl
variable "name" {
  description = "Name of the storage account. Must be 3-24 characters, lowercase letters and numbers only."
  type        = string

  validation {
    condition     = can(regex("^[a-z0-9]{3,24}$", var.name))
    error_message = "Storage account name must be 3-24 characters, lowercase letters and numbers only."
  }
}

variable "resource_group_name" {
  description = "Name of the resource group where the storage account will be created."
  type        = string
}

variable "location" {
  description = "Azure region for the storage account."
  type        = string

  validation {
    condition = contains([
      "eastus", "eastus2", "westus", "westus2", "westus3",
      "centralus", "northcentralus", "southcentralus",
      "northeurope", "westeurope", "uksouth", "ukwest",
      "eastasia", "southeastasia", "japaneast", "japanwest",
      "australiaeast", "australiasoutheast"
    ], var.location)
    error_message = "Must be a supported Azure region."
  }
}

variable "account_tier" {
  description = "Performance tier of the storage account."
  type        = string
  default     = "Standard"

  validation {
    condition     = contains(["Standard", "Premium"], var.account_tier)
    error_message = "Account tier must be 'Standard' or 'Premium'."
  }
}

variable "account_replication_type" {
  description = "Replication type for the storage account."
  type        = string
  default     = "LRS"

  validation {
    condition     = contains(["LRS", "GRS", "RAGRS", "ZRS", "GZRS", "RAGZRS"], var.account_replication_type)
    error_message = "Must be a valid replication type: LRS, GRS, RAGRS, ZRS, GZRS, or RAGZRS."
  }
}

variable "account_kind" {
  description = "Kind of storage account."
  type        = string
  default     = "StorageV2"

  validation {
    condition     = contains(["BlobStorage", "BlockBlobStorage", "FileStorage", "Storage", "StorageV2"], var.account_kind)
    error_message = "Must be a valid account kind."
  }
}

variable "containers" {
  description = "Map of blob containers to create."
  type = map(object({
    access_type = optional(string, "private")
  }))
  default = {}

  validation {
    condition = alltrue([
      for c in var.containers : contains(["private", "blob", "container"], c.access_type)
    ])
    error_message = "Container access_type must be 'private', 'blob', or 'container'."
  }
}

variable "enable_versioning" {
  description = "Enable blob versioning."
  type        = bool
  default     = false
}

variable "lifecycle_rules" {
  description = "Lifecycle management rules for blobs."
  type = list(object({
    name                   = string
    prefix_match           = optional(list(string), [])
    tier_to_cool_after_days = optional(number)
    tier_to_archive_after_days = optional(number)
    delete_after_days      = optional(number)
  }))
  default = []
}

variable "private_endpoint" {
  description = "Private endpoint configuration. Set to null to disable."
  type = object({
    subnet_id            = string
    private_dns_zone_ids = optional(list(string), [])
  })
  default = null
}

variable "network_rules" {
  description = "Network rules for the storage account."
  type = object({
    default_action             = optional(string, "Deny")
    ip_rules                   = optional(list(string), [])
    virtual_network_subnet_ids = optional(list(string), [])
    bypass                     = optional(list(string), ["AzureServices"])
  })
  default = null
}

# Required tags for organizational compliance
variable "environment" {
  description = "Environment name (required tag)."
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod", "sandbox"], var.environment)
    error_message = "Environment must be dev, staging, prod, or sandbox."
  }
}

variable "cost_center" {
  description = "Cost center code (required tag)."
  type        = string
}

variable "owner" {
  description = "Owner email address (required tag)."
  type        = string

  validation {
    condition     = can(regex("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", var.owner))
    error_message = "Owner must be a valid email address."
  }
}

variable "additional_tags" {
  description = "Additional tags to apply to resources."
  type        = map(string)
  default     = {}
}
```

**main.tf**

```hcl
locals {
  required_tags = {
    environment = var.environment
    cost-center = var.cost_center
    owner       = var.owner
    managed-by  = "terraform"
  }

  tags = merge(local.required_tags, var.additional_tags)
}

resource "azurerm_storage_account" "this" {
  name                     = var.name
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = var.account_tier
  account_replication_type = var.account_replication_type
  account_kind             = var.account_kind

  min_tls_version                 = "TLS1_2"
  allow_nested_items_to_be_public = false
  shared_access_key_enabled       = true

  blob_properties {
    versioning_enabled = var.enable_versioning

    dynamic "delete_retention_policy" {
      for_each = var.enable_versioning ? [1] : []
      content {
        days = 30
      }
    }

    dynamic "container_delete_retention_policy" {
      for_each = var.enable_versioning ? [1] : []
      content {
        days = 7
      }
    }
  }

  dynamic "network_rules" {
    for_each = var.network_rules != null ? [var.network_rules] : []
    content {
      default_action             = network_rules.value.default_action
      ip_rules                   = network_rules.value.ip_rules
      virtual_network_subnet_ids = network_rules.value.virtual_network_subnet_ids
      bypass                     = network_rules.value.bypass
    }
  }

  tags = local.tags
}

resource "azurerm_storage_container" "this" {
  for_each = var.containers

  name                  = each.key
  storage_account_name  = azurerm_storage_account.this.name
  container_access_type = each.value.access_type
}

resource "azurerm_storage_management_policy" "this" {
  count = length(var.lifecycle_rules) > 0 ? 1 : 0

  storage_account_id = azurerm_storage_account.this.id

  dynamic "rule" {
    for_each = var.lifecycle_rules
    content {
      name    = rule.value.name
      enabled = true

      filters {
        prefix_match = rule.value.prefix_match
        blob_types   = ["blockBlob"]
      }

      actions {
        base_blob {
          tier_to_cool_after_days_since_modification_greater_than    = rule.value.tier_to_cool_after_days
          tier_to_archive_after_days_since_modification_greater_than = rule.value.tier_to_archive_after_days
          delete_after_days_since_modification_greater_than          = rule.value.delete_after_days
        }
      }
    }
  }
}

resource "azurerm_private_endpoint" "this" {
  count = var.private_endpoint != null ? 1 : 0

  name                = "${var.name}-pe"
  location            = var.location
  resource_group_name = var.resource_group_name
  subnet_id           = var.private_endpoint.subnet_id

  private_service_connection {
    name                           = "${var.name}-psc"
    private_connection_resource_id = azurerm_storage_account.this.id
    subresource_names              = ["blob"]
    is_manual_connection           = false
  }

  dynamic "private_dns_zone_group" {
    for_each = length(var.private_endpoint.private_dns_zone_ids) > 0 ? [1] : []
    content {
      name                 = "default"
      private_dns_zone_ids = var.private_endpoint.private_dns_zone_ids
    }
  }

  tags = local.tags
}
```

**outputs.tf**

```hcl
output "id" {
  description = "The ID of the storage account."
  value       = azurerm_storage_account.this.id
}

output "name" {
  description = "The name of the storage account."
  value       = azurerm_storage_account.this.name
}

output "primary_blob_endpoint" {
  description = "The primary blob endpoint URL."
  value       = azurerm_storage_account.this.primary_blob_endpoint
}

output "primary_access_key" {
  description = "The primary access key for the storage account."
  value       = azurerm_storage_account.this.primary_access_key
  sensitive   = true
}

output "primary_connection_string" {
  description = "The primary connection string for the storage account."
  value       = azurerm_storage_account.this.primary_connection_string
  sensitive   = true
}

output "container_ids" {
  description = "Map of container names to their resource IDs."
  value       = { for k, v in azurerm_storage_container.this : k => v.id }
}

output "private_endpoint_ip" {
  description = "Private IP address of the private endpoint (if created)."
  value       = try(azurerm_private_endpoint.this[0].private_service_connection[0].private_ip_address, null)
}
```

**examples/basic/main.tf**

```hcl
provider "azurerm" {
  features {}
}

module "storage_account" {
  source = "github.com/contoso/terraform-azurerm-storage-account"

  name                = "stcontosodev001"
  resource_group_name = "rg-storage-dev"
  location            = "eastus"

  containers = {
    "data"   = { access_type = "private" }
    "logs"   = { access_type = "private" }
  }

  # Required tags
  environment = "dev"
  cost_center = "IT-001"
  owner       = "platform-team@contoso.com"
}

output "storage_account_id" {
  value = module.storage_account.id
}
```

**examples/advanced/main.tf**

```hcl
provider "azurerm" {
  features {}
}

module "storage_account" {
  source = "github.com/contoso/terraform-azurerm-storage-account"

  name                     = "stcontosoprod001"
  resource_group_name      = "rg-storage-prod"
  location                 = "eastus"
  account_replication_type = "GRS"

  enable_versioning = true

  containers = {
    "documents" = { access_type = "private" }
    "backups"   = { access_type = "private" }
    "archives"  = { access_type = "private" }
  }

  lifecycle_rules = [
    {
      name                        = "archive-old-backups"
      prefix_match                = ["backups/"]
      tier_to_cool_after_days     = 30
      tier_to_archive_after_days  = 90
      delete_after_days           = 365
    }
  ]

  network_rules = {
    default_action = "Deny"
    ip_rules       = ["203.0.113.0/24"]
    bypass         = ["AzureServices", "Logging", "Metrics"]
  }

  private_endpoint = {
    subnet_id            = "/subscriptions/.../subnets/private-endpoints"
    private_dns_zone_ids = ["/subscriptions/.../privateDnsZones/privatelink.blob.core.windows.net"]
  }

  # Required tags
  environment = "prod"
  cost_center = "PROD-001"
  owner       = "platform-team@contoso.com"

  additional_tags = {
    application = "data-platform"
    criticality = "high"
  }
}
```

---

## Related Prompts

- [Infrastructure Planning Expert](../../technical-workflows/infrastructure-planning-expert.md) - Plan infrastructure requirements
- [DevOps Workflow Design Expert](../../technical-workflows/devops-workflow-design-expert.md) - Set up module CI/CD
- [Cloud Migration Expert](../architecture/cloud-migration-expert.md) - Design Azure architectures
