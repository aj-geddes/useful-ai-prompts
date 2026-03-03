# Azure Functions with Terraform

## Azure Functions with Terraform

```hcl
# functions.tf
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {
    virtual_machine {
      delete_os_disk_on_delete            = true
      graceful_shutdown                   = false
      skip_shutdown_and_force_delete       = false
    }
  }
}

variable "environment" {
  default = "dev"
}

variable "location" {
  default = "eastus"
}

# Resource group
resource "azurerm_resource_group" "main" {
  name     = "myapp-rg-${var.environment}"
  location = var.location
}

# Storage account for Function App
resource "azurerm_storage_account" "function_storage" {
  name                     = "myappstore${var.environment}"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  identity {
    type = "SystemAssigned"
  }

  tags = {
    environment = var.environment
  }
}

# Application Insights
resource "azurerm_application_insights" "main" {
  name                = "myapp-insights-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  application_type    = "web"

  retention_in_days = 30
}

# App Service Plan
resource "azurerm_service_plan" "function_plan" {
  name                = "myapp-plan-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "Y1" # Consumption plan

  tags = {
    environment = var.environment
  }
}

# Function App
resource "azurerm_linux_function_app" "main" {
  name                = "myapp-function-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.function_plan.id

  storage_account_name       = azurerm_storage_account.function_storage.name
  storage_account_access_key = azurerm_storage_account.function_storage.primary_access_key

  app_settings = {
    APPINSIGHTS_INSTRUMENTATIONKEY             = azurerm_application_insights.main.instrumentation_key
    APPLICATIONINSIGHTS_CONNECTION_STRING      = azurerm_application_insights.main.connection_string
    AzureWebJobsStorage                        = azurerm_storage_account.function_storage.primary_blob_connection_string
    WEBSITE_NODE_DEFAULT_VERSION               = "~18"
    FUNCTIONS_EXTENSION_VERSION                = "~4"
    FUNCTIONS_WORKER_RUNTIME                   = "node"
    ENABLE_INIT_LOGGING                        = true
    WEBSITE_RUN_FROM_PACKAGE                   = 1
  }

  site_config {
    application_insights_key             = azurerm_application_insights.main.instrumentation_key
    application_insights_connection_string = azurerm_application_insights.main.connection_string

    cors {
      allowed_origins = ["https://example.com"]
    }

    http2_enabled = true
  }

  https_only = true
  identity {
    type = "SystemAssigned"
  }

  tags = {
    environment = var.environment
  }
}

# Key Vault for secrets
resource "azurerm_key_vault" "function_secrets" {
  name                = "myappkv${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = azurerm_linux_function_app.main.identity[0].principal_id

    secret_permissions = [
      "Get",
      "List"
    ]
  }

  tags = {
    environment = var.environment
  }
}

# Store database password in Key Vault
resource "azurerm_key_vault_secret" "db_password" {
  name         = "db-password"
  value        = "MySecurePassword123!"
  key_vault_id = azurerm_key_vault.function_secrets.id
}

# Diagnostic settings
resource "azurerm_monitor_diagnostic_setting" "function_logs" {
  name               = "function-logs"
  target_resource_id = azurerm_linux_function_app.main.id

  log_analytics_workspace_id = azurerm_log_analytics_workspace.main.id

  enabled_log {
    category = "FunctionAppLogs"
  }

  metric {
    category = "AllMetrics"
  }
}

# Log Analytics Workspace
resource "azurerm_log_analytics_workspace" "main" {
  name                = "myapp-logs-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku                 = "PerGB2018"

  retention_in_days = 30
}

data "azurerm_client_config" "current" {}

output "function_app_url" {
  value = "https://${azurerm_linux_function_app.main.default_hostname}"
}

output "app_insights_key" {
  value     = azurerm_application_insights.main.instrumentation_key
  sensitive = true
}
```
