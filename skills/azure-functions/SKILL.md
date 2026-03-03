---
name: azure-functions
description: >
  Create serverless functions on Azure with triggers, bindings, authentication,
  and monitoring. Use for event-driven computing without managing
  infrastructure.
---

# Azure Functions

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Azure Functions enables serverless computing on Microsoft Azure. Build event-driven applications with automatic scaling, flexible bindings to various Azure services, and integrated monitoring through Application Insights.

## When to Use

- HTTP APIs and webhooks
- Message-driven processing (Service Bus, Event Hub)
- Scheduled jobs and CRON expressions
- File and blob processing
- Queue-based workflows
- Real-time data processing
- Microservices and backend logic
- Integration with Azure ecosystem services

## Quick Start

Minimal working example:

```bash
# Install Azure Functions Core Tools
curl https://aka.ms/install-artifacts-ubuntu.sh | bash

# Login to Azure
az login

# Create resource group
az group create --name myapp-rg --location eastus

# Create storage account (required for Functions)
az storage account create \
  --name myappstore \
  --location eastus \
  --resource-group myapp-rg \
  --sku Standard_LRS

# Create Function App
az functionapp create \
  --resource-group myapp-rg \
  --consumption-plan-location eastus \
  --runtime node \
  --runtime-version 18 \
  --functions-version 4 \
  --name myapp-function \
  --storage-account myappstore
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Azure Function Creation with Azure CLI](references/azure-function-creation-with-azure-cli.md) | Azure Function Creation with Azure CLI |
| [Azure Function Implementation (Node.js)](references/azure-function-implementation-nodejs.md) | Azure Function Implementation (Node.js) |
| [Azure Functions with Terraform](references/azure-functions-with-terraform.md) | Azure Functions with Terraform |
| [Function Bindings Configuration](references/function-bindings-configuration.md) | Function Bindings Configuration |

## Best Practices

### ✅ DO

- Use managed identity for Azure services
- Store secrets in Key Vault
- Enable Application Insights
- Implement idempotent functions
- Use durable functions for long-running operations
- Handle exceptions and failures
- Monitor function execution
- Use bindings instead of SDK calls

### ❌ DON'T

- Store secrets in code or configuration
- Ignore Application Insights
- Create functions without error handling
- Use blocking operations
- Create long-running functions without Durable Functions
- Ignore monitoring and logging
