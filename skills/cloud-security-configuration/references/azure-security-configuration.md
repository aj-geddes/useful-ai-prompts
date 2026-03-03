# Azure Security Configuration

## Azure Security Configuration

```bash
# Enable Azure Security Center
az security auto-provisioning-setting update \
  --auto-provision on

# Enable Azure Defender
az security atp storage update \
  --storage-account myaccount \
  --is-enabled true

# Configure NSG rules
az network nsg rule create \
  --resource-group mygroup \
  --nsg-name mynsg \
  --name AllowHTTPS \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 443

# Enable Azure Policy
az policy assignment create \
  --name EnforceHttps \
  --policy /subscriptions/{subscription}/providers/Microsoft.Authorization/policyDefinitions/{policyId}

# Create Key Vault
az keyvault create \
  --resource-group mygroup \
  --name mykeyvault \
  --enable-rbac-authorization
```
