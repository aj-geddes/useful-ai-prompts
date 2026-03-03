# App Service Creation with Azure CLI

## App Service Creation with Azure CLI

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
    NODE_ENV=production \
    PORT=8080 \
    DATABASE_URL=postgresql://... \
    REDIS_URL=redis://...

# Enable HTTPS only
az webapp update \
  --resource-group myapp-rg \
  --name myapp-web \
  --https-only true

# Configure custom domain
az webapp config hostname add \
  --resource-group myapp-rg \
  --webapp-name myapp-web \
  --hostname www.example.com

# Create deployment slot
az webapp deployment slot create \
  --resource-group myapp-rg \
  --name myapp-web \
  --slot staging

# Swap slots
az webapp deployment slot swap \
  --resource-group myapp-rg \
  --name myapp-web \
  --slot staging

# Get publish profile for deployment
az webapp deployment list-publish-profiles \
  --resource-group myapp-rg \
  --name myapp-web \
  --query "[0].publishUrl"
```
