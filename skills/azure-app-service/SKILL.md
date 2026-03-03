---
name: azure-app-service
description: >
  Deploy and manage web apps using Azure App Service with auto-scaling,
  deployment slots, SSL/TLS, and monitoring. Use for hosting web applications on
  Azure.
---

# Azure App Service

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Azure App Service provides a fully managed platform for building and hosting web applications, REST APIs, and mobile backends. Support multiple programming languages with integrated DevOps, security, and high availability.

## When to Use

- Web applications (ASP.NET, Node.js, Python, Java)
- REST APIs and microservices
- Mobile app backends
- Static website hosting
- Production applications requiring scale
- Applications needing auto-scaling
- Multi-region deployments
- Containerized applications

## Quick Start

Minimal working example:

```bash
# Login to Azure
az login

# Create resource group
az group create --name myapp-rg --location eastus

# Create App Service Plan
az appservice plan create \
  --name myapp-plan \
  --resource-group myapp-rg \
  --sku P1V2 \
  --is-linux

# Create web app
az webapp create \
  --resource-group myapp-rg \
  --plan myapp-plan \
  --name myapp-web \
  --deployment-container-image-name nodejs:18

# Configure app settings
az webapp config appsettings set \
  --resource-group myapp-rg \
  --name myapp-web \
  --settings \
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [App Service Creation with Azure CLI](references/app-service-creation-with-azure-cli.md) | App Service Creation with Azure CLI |
| [Terraform App Service Configuration](references/terraform-app-service-configuration.md) | Terraform App Service Configuration |
| [Deployment Configuration](references/deployment-configuration.md) | Deployment Configuration |
| [Health Check Configuration](references/health-check-configuration.md) | Health Check Configuration |

## Best Practices

### ✅ DO

- Use deployment slots for zero-downtime deployments
- Enable Application Insights
- Configure autoscaling based on metrics
- Use managed identity for Azure services
- Enable HTTPS only
- Store secrets in Key Vault
- Monitor performance metrics
- Implement health checks

### ❌ DON'T

- Store secrets in configuration
- Disable HTTPS
- Ignore Application Insights
- Use single instance for production
- Deploy directly to production
- Ignore autoscaling configuration
