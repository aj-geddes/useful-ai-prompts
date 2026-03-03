# AWS Cost Optimization with AWS CLI

## AWS Cost Optimization with AWS CLI

```bash
# Enable Cost Explorer
aws ce get-cost-and-usage \
  --time-period Start=2024-01-01,End=2024-01-31 \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE

# List EC2 instances for right-sizing
aws ec2 describe-instances \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,LaunchTime,Tag]' \
  --output table

# Find unattached EBS volumes
aws ec2 describe-volumes \
  --filters Name=status,Values=available \
  --query 'Volumes[*].[VolumeId,Size,State,CreateTime]'

# Identify unattached Elastic IPs
aws ec2 describe-addresses \
  --query 'Addresses[?AssociationId==null]'

# Get RDS instance costs
aws rds describe-db-instances \
  --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceClass,StorageType,AllocatedStorage]'

# Create budget alert
aws budgets create-budget \
  --account-id 123456789012 \
  --budget BudgetName=MyBudget,BudgetLimit='{Amount=1000,Unit=USD}',TimeUnit=MONTHLY,BudgetType=COST \
  --notifications-with-subscribers \
    'Notification={NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=80},Subscribers=[{SubscriptionType=EMAIL,Address=user@example.com}]'

# List savings plans
aws savingsplans describe-savings-plans

# Get reserved instances
aws ec2 describe-reserved-instances \
  --query 'ReservedInstances[*].[ReservedInstancesId,InstanceType,State,OfferingType,Duration]'
```
