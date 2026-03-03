# Terraform App Service Configuration

## Terraform App Service Configuration

```hcl
# app-service.tf
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

variable "environment" {
  default = "prod"
}

variable "location" {
  default = "eastus"
}

# Resource group
resource "azurerm_resource_group" "main" {
  name     = "myapp-rg-${var.environment}"
  location = var.location
}

# App Service Plan
resource "azurerm_service_plan" "main" {
  name                = "myapp-plan-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "P1V2"

  tags = {
    environment = var.environment
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

# Application Insights
resource "azurerm_application_insights" "main" {
  name                = "myapp-insights-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  application_type    = "web"

  retention_in_days      = 30
  workspace_id           = azurerm_log_analytics_workspace.main.id
}

# Web App
resource "azurerm_linux_web_app" "main" {
  name                = "myapp-web-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  https_only = true

  app_settings = {
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
    DOCKER_ENABLE_CI                    = true
    APPINSIGHTS_INSTRUMENTATIONKEY      = azurerm_application_insights.main.instrumentation_key
    APPLICATIONINSIGHTS_CONNECTION_STRING = azurerm_application_insights.main.connection_string
    NODE_ENV                            = "production"
    PORT                                = "8080"
  }

  site_config {
    always_on                   = true
    http2_enabled               = true
    minimum_tls_version         = "1.2"
    websockets_enabled          = false
    application_stack {
      node_version = "18-lts"
    }

    cors {
      allowed_origins = ["https://example.com"]
    }
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    environment = var.environment
  }
}

# Deployment slot (staging)
resource "azurerm_linux_web_app_slot" "staging" {
  name            = "staging"
  app_service_id  = azurerm_linux_web_app.main.id
  service_plan_id = azurerm_service_plan.main.id

  https_only = true

  app_settings = {
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
    NODE_ENV                            = "staging"
    PORT                                = "8080"
  }

  site_config {
    always_on           = true
    http2_enabled       = true
    minimum_tls_version = "1.2"

    application_stack {
      node_version = "18-lts"
    }
  }

  identity {
    type = "SystemAssigned"
  }
}

# Autoscale settings
resource "azurerm_monitor_autoscale_setting" "app_service" {
  name                = "app-service-autoscale"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  target_resource_id  = azurerm_service_plan.main.id

  profile {
    name = "default"

    capacity {
      default = 2
      minimum = 1
      maximum = 5
    }

    rule {
      metric_trigger {
        metric_name        = "CpuPercentage"
        metric_resource_id = azurerm_service_plan.main.id
        time_grain         = "PT1M"
        statistic          = "Average"
        time_window        = "PT5M"
        operator           = "GreaterThan"
        threshold          = 75
      }

      scale_action {
        direction = "Increase"
        type      = "ChangeCount"
        value     = 1
        cooldown  = "PT5M"
      }
    }

    rule {
      metric_trigger {
        metric_name        = "CpuPercentage"
        metric_resource_id = azurerm_service_plan.main.id
        time_grain         = "PT1M"
        statistic          = "Average"
        time_window        = "PT5M"
        operator           = "LessThan"
        threshold          = 25
      }

      scale_action {
        direction = "Decrease"
        type      = "ChangeCount"
        value     = 1
        cooldown  = "PT5M"
      }
    }
  }
}

# Diagnostic settings
resource "azurerm_monitor_diagnostic_setting" "app_service" {
  name               = "app-service-logs"
  target_resource_id = azurerm_linux_web_app.main.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.main.id

  enabled_log {
    category = "AppServiceHTTPLogs"
  }

  enabled_log {
    category = "AppServiceAntivirusScanAuditLogs"
  }

  metric {
    category = "AllMetrics"
  }
}

# Key Vault for secrets
resource "azurerm_key_vault" "main" {
  name                = "myappkv${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = azurerm_linux_web_app.main.identity[0].principal_id

    secret_permissions = [
      "Get",
      "List"
    ]
  }

  tags = {
    environment = var.environment
  }
}

# Key Vault secrets
resource "azurerm_key_vault_secret" "database_url" {
  name         = "database-url"
  value        = "postgresql://user:pass@host/db"
  key_vault_id = azurerm_key_vault.main.id
}

resource "azurerm_key_vault_secret" "api_key" {
  name         = "api-key"
  value        = "your-api-key-here"
  key_vault_id = azurerm_key_vault.main.id
}

data "azurerm_client_config" "current" {}

output "app_url" {
  value = "https://${azurerm_linux_web_app.main.default_hostname}"
}

output "app_insights_key" {
  value     = azurerm_application_insights.main.instrumentation_key
  sensitive = true
}
```
