---
name: cloud-cost-management
description: Optimize and manage cloud costs across AWS, Azure, and GCP using reserved instances, spot pricing, and cost monitoring tools.
---

# Cloud Cost Management

## Overview

Cloud cost management involves monitoring, analyzing, and optimizing cloud spending. Implement strategies using reserved instances, spot pricing, proper sizing, and cost allocation to maximize ROI and prevent budget overruns.

## When to Use

- Reducing cloud infrastructure costs
- Optimizing compute spending
- Managing database costs
- Storage optimization
- Data transfer cost reduction
- Reserved capacity planning
- Chargeback and cost allocation
- Budget forecasting and alerts

## Implementation Examples

### 1. **AWS Cost Optimization with AWS CLI**

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

### 2. **Terraform Cost Management Configuration**

```hcl
# cost-management.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "monthly_budget" {
  default = 10000
  description = "Monthly budget limit"
}

# CloudWatch Cost Anomaly Detection
resource "aws_ce_anomaly_monitor" "cost_anomaly" {
  monitor_name    = "cost-anomaly-detection"
  monitor_type    = "DIMENSIONAL"
  monitor_dimension = "SERVICE"
  monitor_specification = jsonencode({
    Dimensions = {
      Key          = "SERVICE"
      Values       = ["Amazon EC2", "Amazon RDS", "AWS Lambda"]
    }
  })
}

# Anomaly alert
resource "aws_ce_anomaly_subscription" "cost_alert" {
  account_id    = data.aws_caller_identity.current.account_id
  display_name  = "Cost Alert"
  threshold     = 100
  frequency     = "DAILY"
  monitor_arn   = aws_ce_anomaly_monitor.cost_anomaly.arn
  subscription_type = "EMAIL"

  subscription_notification_type = "FORECASTED"
}

# Budget with alerts
resource "aws_budgets_budget" "monthly" {
  name              = "monthly-budget"
  budget_type       = "COST"
  limit_amount      = var.monthly_budget
  limit_unit        = "USD"
  time_period_start = "2024-01-01_00:00"
  time_period_end   = "2099-12-31_23:59"
  time_unit         = "MONTHLY"

  tags = {
    Name = "monthly-budget"
  }
}

# Budget notification
resource "aws_budgets_budget_notification" "monthly_alert" {
  account_id      = data.aws_caller_identity.current.account_id
  budget_name     = aws_budgets_budget.monthly.name
  comparison_operator = "GREATER_THAN"
  notification_type   = "ACTUAL"
  threshold       = 80
  threshold_type  = "PERCENTAGE"

  notification_subscribers {
    address              = "user@example.com"
    subscription_type    = "EMAIL"
  }
}

# Savings Plan Commitment
resource "aws_savingsplans_savings_plan" "compute" {
  commitment  = 10000
  payment_option = "ALL_UPFRONT"
  plan_type   = "COMPUTE_SAVINGS_PLAN"
  term_in_months = 12

  tags = {
    Name = "compute-savings"
  }
}

# Reserved Instances
resource "aws_ec2_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"

  tags = {
    Name = "app-instance"
  }
}

# Reserve the instance
resource "aws_ec2_capacity_reservation" "app" {
  availability_zone       = "us-east-1a"
  instance_count          = 1
  instance_platform       = "Linux/UNIX"
  instance_type           = aws_ec2_instance.app.instance_type
  reservation_type        = "default"

  tags = {
    Name = "app-reservation"
  }
}

# CloudWatch Dashboard for cost monitoring
resource "aws_cloudwatch_dashboard" "cost_dashboard" {
  dashboard_name = "cost-dashboard"

  dashboard_body = jsonencode({
    widgets = [
      {
        type = "metric"
        properties = {
          metrics = [
            ["AWS/Billing", "EstimatedCharges", { stat = "Average" }]
          ]
          period = 86400
          stat   = "Average"
          region = var.aws_region
          title  = "Estimated Monthly Charges"
          yAxis = {
            left = {
              min = 0
            }
          }
        }
      }
    ]
  })
}

# Data for current account
data "aws_caller_identity" "current" {}

# Tag compliance and cost allocation
resource "aws_ec2_instance" "tagged_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.small"

  tags = {
    Name              = "cost-tracked-instance"
    CostCenter        = "engineering"
    Environment       = "production"
    Project           = "web-app"
    ManagedBy         = "terraform"
    ChargebackEmail   = "ops@example.com"
  }
}
```

### 3. **Azure Cost Management**

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

### 4. **GCP Cost Optimization**

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

### 5. **Cost Monitoring Dashboard**

```python
# Python cost monitoring tool
import boto3
from datetime import datetime, timedelta
from typing import Dict, List
import json

class CloudCostMonitor:
    def __init__(self):
        self.ce_client = boto3.client('ce')
        self.ec2_client = boto3.client('ec2')
        self.rds_client = boto3.client('rds')

    def get_monthly_costs_by_service(self, months=3) -> Dict:
        """Get monthly costs breakdown by service"""
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=30*months)

        response = self.ce_client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.isoformat(),
                'End': end_date.isoformat()
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'SERVICE'}
            ]
        )

        costs = {}
        for result in response['ResultsByTime']:
            for group in result['Groups']:
                service = group['Keys'][0]
                cost = float(group['Metrics']['UnblendedCost']['Amount'])

                if service not in costs:
                    costs[service] = []
                costs[service].append({
                    'date': result['TimePeriod']['Start'],
                    'cost': cost
                })

        return costs

    def identify_savings_opportunities(self) -> Dict:
        """Identify resources that can be optimized"""
        opportunities = {
            'unattached_ebs_volumes': [],
            'unassociated_eips': [],
            'underutilized_instances': [],
            'unattached_network_interfaces': []
        }

        # Check EBS volumes
        volumes_response = self.ec2_client.describe_volumes(
            Filters=[{'Name': 'status', 'Values': ['available']}]
        )

        for volume in volumes_response['Volumes']:
            opportunities['unattached_ebs_volumes'].append({
                'volume_id': volume['VolumeId'],
                'size_gb': volume['Size'],
                'estimated_monthly_cost': volume['Size'] * 0.10
            })

        # Check Elastic IPs
        addresses_response = self.ec2_client.describe_addresses()

        for address in addresses_response['Addresses']:
            if 'AssociationId' not in address:
                opportunities['unassociated_eips'].append({
                    'public_ip': address['PublicIp'],
                    'estimated_monthly_cost': 3.60
                })

        # Check underutilized instances
        instances_response = self.ec2_client.describe_instances()

        for reservation in instances_response['Reservations']:
            for instance in reservation['Instances']:
                opportunities['underutilized_instances'].append({
                    'instance_id': instance['InstanceId'],
                    'instance_type': instance['InstanceType'],
                    'state': instance['State']['Name'],
                    'recommendation': 'Consider downsizing or terminating'
                })

        return opportunities

    def calculate_potential_savings(self, opportunities: Dict) -> Dict:
        """Calculate potential monthly savings"""
        savings = {
            'ebs_volumes': sum(op['estimated_monthly_cost'] for op in opportunities['unattached_ebs_volumes']),
            'eips': sum(op['estimated_monthly_cost'] for op in opportunities['unassociated_eips']),
            'total_monthly': 0
        }

        savings['total_monthly'] = savings['ebs_volumes'] + savings['eips']
        savings['total_annual'] = savings['total_monthly'] * 12

        return savings

    def generate_cost_report(self) -> str:
        """Generate comprehensive cost report"""
        costs_by_service = self.get_monthly_costs_by_service()
        opportunities = self.identify_savings_opportunities()
        savings = self.calculate_potential_savings(opportunities)

        report = f"""
        ===== CLOUD COST REPORT =====
        Generated: {datetime.now().isoformat()}

        CURRENT COSTS BY SERVICE:
        """

        for service, costs in costs_by_service.items():
            total = sum(c['cost'] for c in costs)
            report += f"\n{service}: ${total:.2f}"

        report += f"""

        SAVINGS OPPORTUNITIES:
        - Unattached EBS Volumes: ${savings['ebs_volumes']:.2f}/month
        - Unassociated EIPs: ${savings['eips']:.2f}/month

        POTENTIAL MONTHLY SAVINGS: ${savings['total_monthly']:.2f}
        POTENTIAL ANNUAL SAVINGS: ${savings['total_annual']:.2f}
        """

        return report

# Usage
monitor = CloudCostMonitor()
print(monitor.generate_cost_report())
```

## Best Practices

### ✅ DO
- Use Reserved Instances for stable workloads
- Implement Savings Plans for flexibility
- Right-size instances based on metrics
- Use Spot Instances for fault-tolerant workloads
- Delete unused resources regularly
- Enable detailed billing and cost allocation
- Monitor costs with CloudWatch/Cost Explorer
- Set budget alerts
- Review monthly cost reports

### ❌ DON'T
- Leave unused resources running
- Ignore cost optimization recommendations
- Use on-demand for predictable workloads
- Skip tagging resources
- Ignore data transfer costs
- Forget about storage lifecycle policies

## Cost Optimization Strategies

- Reserved Instances: 20-40% savings
- Spot Instances: 70-90% savings
- Savings Plans: 15-30% savings
- Storage optimization: 30-50% savings
- Data transfer optimization: 10-20% savings

## Resources

- [AWS Cost Management](https://aws.amazon.com/aws-cost-management/)
- [Azure Cost Management](https://docs.microsoft.com/en-us/azure/cost-management-billing/)
- [GCP Cost Optimization](https://cloud.google.com/cost-optimization)
- [FinOps Foundation](https://www.finops.org/)
