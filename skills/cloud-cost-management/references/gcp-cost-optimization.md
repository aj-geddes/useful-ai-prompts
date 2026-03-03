# GCP Cost Optimization

## GCP Cost Optimization

```bash
# Get billing data
gcloud billing accounts list

# Create budget
gcloud billing budgets create \
  --billing-account=BILLING_ACCOUNT_ID \
  --display-name="Monthly Budget" \
  --budget-amount=10000 \
  --threshold-rule=percent=50 \
  --threshold-rule=percent=90 \
  --threshold-rule=percent=100

# List cost recommendations
gcloud compute instances list \
  --format='table(name,machineType.machine_type(),CPUS:format="@(scheduling.nodeAffinities[0].nodeAffinities[0].key): \
  (@(scheduling.nodeAffinities[0].nodeAffinities[0].values[0]))")'

# Enable committed use discounts
gcloud compute commitments create my-commitment \
  --plan=one-year \
  --resources=RESOURCE_TYPE=INSTANCES,RESOURCE_SPEC=MACHINE_TYPE=n1-standard-4,COUNT=10 \
  --region=us-central1

# Get storage cost estimate
gsutil du -s gs://my-bucket
```
