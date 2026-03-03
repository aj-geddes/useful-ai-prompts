# Azure Function Creation with Azure CLI

## Azure Function Creation with Azure CLI

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

# Create function in app
func new --name HttpTrigger --template "HTTP trigger"

# Configure authentication
az functionapp auth update \
  --resource-group myapp-rg \
  --name myapp-function \
  --enabled true \
  --action RedirectToLoginPage \
  --default-provider AzureActiveDirectory

# Deploy function
func azure functionapp publish myapp-function

# Check deployment
az functionapp list --output table

# Get function details
az functionapp function show \
  --resource-group myapp-rg \
  --name myapp-function \
  --function-name HttpTrigger
```
