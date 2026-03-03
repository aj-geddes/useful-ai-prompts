# Azure Cost Management

## Azure Cost Management

```bash
# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Get cost analysis
az costmanagement query \
  --timeframe MonthToDate \
  --type Usage \
  --dataset aggregation='{"totalCost":{"name":"PreTaxCost","function":"Sum"}}' \
  --dataset grouping='[{"type":"Dimension","name":"ResourceType"}]'

# Create budget alert
az consumption budget create \
  --name MyBudget \
  --category Cost \
  --amount 5000 \
  --time-grain Monthly \
  --start-date 2024-01-01 \
  --notifications-enabled True

# List recommendations
az advisor recommendation list \
  --category Cost

# Export cost data
az costmanagement export create \
  --name MonthlyExport \
  --dataset aggregation='{"totalCost":{"name":"PreTaxCost","function":"Sum"}}' \
  --timeframe TheLastMonth \
  --schedule-status Active

# Get VM sizing recommendations
az advisor recommendation list \
  --category Performance \
  --query "[?properties.category=='Compute']"
```
