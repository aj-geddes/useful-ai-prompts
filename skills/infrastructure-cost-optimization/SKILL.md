---
name: infrastructure-cost-optimization
description: Optimize cloud infrastructure costs through resource rightsizing, reserved instances, spot instances, and waste reduction strategies.
---

# Infrastructure Cost Optimization

## Overview

Reduce infrastructure costs through intelligent resource allocation, reserved instances, spot instances, and continuous optimization without sacrificing performance.

## When to Use

- Cloud cost reduction
- Budget management and tracking
- Resource utilization optimization
- Multi-environment cost allocation
- Waste identification and elimination
- Reserved instance planning
- Spot instance integration

## Implementation Examples

### 1. **AWS Cost Optimization Configuration**

```yaml
# cost-optimization-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cost-optimization-scripts
  namespace: operations
data:
  analyze-costs.sh: |
    #!/bin/bash
    set -euo pipefail

    echo "=== AWS Cost Analysis ==="

    # Get daily cost trend
    echo "Daily costs for last 7 days:"
    aws ce get-cost-and-usage \
      --time-period Start=$(date -d '7 days ago' +%Y-%m-%d),End=$(date +%Y-%m-%d) \
      --granularity DAILY \
      --metrics "BlendedCost" \
      --group-by Type=DIMENSION,Key=SERVICE \
      --query 'ResultsByTime[*].[TimePeriod.Start,Total.BlendedCost.Amount]' \
      --output table

    # Find unattached resources
    echo -e "\n=== Unattached EBS Volumes ==="
    aws ec2 describe-volumes \
      --filters Name=status,Values=available \
      --query 'Volumes[*].[VolumeId,Size,CreateTime]' \
      --output table

    echo -e "\n=== Unattached Elastic IPs ==="
    aws ec2 describe-addresses \
      --filters Name=association-id,Values=none \
      --query 'Addresses[*].[PublicIp,AllocationId]' \
      --output table

    echo -e "\n=== Unused RDS Instances ==="
    aws rds describe-db-instances \
      --query 'DBInstances[?DBInstanceStatus==`available`].[DBInstanceIdentifier,DBInstanceClass,Engine,AllocatedStorage]' \
      --output table

    # Estimate savings with Reserved Instances
    echo -e "\n=== Reserved Instance Savings Potential ==="
    aws ce get-reservation-purchase-recommendation \
      --service "EC2" \
      --lookback-period THIRTY_DAYS \
      --query 'Recommendations[0].[RecommendationSummary.TotalEstimatedMonthlySavingsAmount,RecommendationSummary.TotalEstimatedMonthlySavingsPercentage]' \
      --output table

  optimize-resources.sh: |
    #!/bin/bash
    set -euo pipefail

    echo "Starting resource optimization..."

    # Remove unattached volumes
    echo "Removing unattached volumes..."
    aws ec2 describe-volumes \
      --filters Name=status,Values=available \
      --query 'Volumes[*].VolumeId' \
      --output text | \
    while read volume_id; do
      echo "Deleting volume: $volume_id"
      aws ec2 delete-volume --volume-id "$volume_id" 2>/dev/null || true
    done

    # Release unused Elastic IPs
    echo "Releasing unused Elastic IPs..."
    aws ec2 describe-addresses \
      --filters Name=association-id,Values=none \
      --query 'Addresses[*].AllocationId' \
      --output text | \
    while read alloc_id; do
      echo "Releasing EIP: $alloc_id"
      aws ec2 release-address --allocation-id "$alloc_id" 2>/dev/null || true
    done

    # Modify RDS to smaller instances
    echo "Analyzing RDS for downsizing..."
    # Implement logic to check CloudWatch metrics and downsize if needed

    echo "Optimization complete"

---
# Terraform cost optimization
resource "aws_ec2_instance" "spot" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"

  # Use spot instances for non-critical workloads
  instance_market_options {
    market_type = "spot"

    spot_options {
      max_price                      = "0.05"  # Set max price
      spot_instance_type             = "persistent"
      interrupt_behavior             = "terminate"
      valid_until                    = "2025-12-31T23:59:59Z"
    }
  }

  tags = {
    Name = "spot-instance"
    CostCenter = "engineering"
  }
}

# Reserved instance for baseline capacity
resource "aws_ec2_instance" "reserved" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"

  # Tag for reserved instance matching
  tags = {
    Name = "reserved-instance"
    ReservationType = "reserved"
  }
}

resource "aws_ec2_fleet" "mixed" {
  name = "mixed-capacity"

  launch_template_configs {
    launch_template_specification {
      launch_template_id = aws_launch_template.app.id
      version            = "$Latest"
    }

    overrides {
      instance_type       = "t3.medium"
      weighted_capacity   = "1"
      priority            = 1  # Reserved
    }

    overrides {
      instance_type       = "t3.large"
      weighted_capacity   = "2"
      priority            = 2  # Reserved
    }

    overrides {
      instance_type       = "t3a.medium"
      weighted_capacity   = "1"
      priority            = 3  # Spot
    }

    overrides {
      instance_type       = "t3a.large"
      weighted_capacity   = "2"
      priority            = 4  # Spot
    }
  }

  target_capacity_specification {
    total_target_capacity  = 10
    on_demand_target_capacity = 6
    spot_target_capacity = 4
    default_target_capacity_type = "on-demand"
  }

  fleet_type = "maintain"
}
```

### 2. **Kubernetes Cost Optimization**

```yaml
# k8s-cost-optimization.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cost-optimization-policies
  namespace: kube-system
data:
  policies.yaml: |
    # Resource quotas per namespace
    apiVersion: v1
    kind: ResourceQuota
    metadata:
      name: compute-quota
      namespace: production
    spec:
      hard:
        requests.cpu: "100"
        requests.memory: "200Gi"
        limits.cpu: "200"
        limits.memory: "400Gi"
        pods: "500"
      scopeSelector:
        matchExpressions:
          - operator: In
            scopeName: PriorityClass
            values: ["high", "medium"]

---
# Pod Disruption Budget for cost-effective scaling
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: cost-optimized-pdb
  namespace: production
spec:
  minAvailable: 1
  selector:
    matchLabels:
      tier: backend

---
# Prioritize spot instances with taints/tolerations
apiVersion: v1
kind: Node
metadata:
  name: spot-node-1
spec:
  taints:
    - key: cloud.google.com/gke-preemptible
      value: "true"
      effect: NoSchedule

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cost-optimized-app
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      # Tolerate spot instances
      tolerations:
        - key: cloud.google.com/gke-preemptible
          operator: Equal
          value: "true"
          effect: NoSchedule

      # Prefer nodes with lower cost
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: karpenter.sh/capacity-type
                    operator: In
                    values: ["spot"]

      containers:
        - name: app
          image: myapp:latest
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi
```

### 3. **Cost Monitoring Dashboard**

```python
# cost-monitoring.py
import boto3
import json
from datetime import datetime, timedelta

class CostOptimizer:
    def __init__(self):
        self.ce_client = boto3.client('ce')
        self.ec2_client = boto3.client('ec2')
        self.rds_client = boto3.client('rds')

    def get_daily_costs(self, days=30):
        """Get daily costs for past N days"""
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)

        response = self.ce_client.get_cost_and_usage(
            TimePeriod={
                'Start': str(start_date),
                'End': str(end_date)
            },
            Granularity='DAILY',
            Metrics=['BlendedCost'],
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'SERVICE'}
            ]
        )

        return response

    def find_underutilized_instances(self):
        """Find EC2 instances with low CPU usage"""
        cloudwatch = boto3.client('cloudwatch')
        instances = []

        ec2_instances = self.ec2_client.describe_instances()
        for reservation in ec2_instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']

                # Check CPU utilization
                response = cloudwatch.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='CPUUtilization',
                    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                    StartTime=datetime.now() - timedelta(days=7),
                    EndTime=datetime.now(),
                    Period=3600,
                    Statistics=['Average']
                )

                if response['Datapoints']:
                    avg_cpu = sum(d['Average'] for d in response['Datapoints']) / len(response['Datapoints'])
                    if avg_cpu < 10:  # Less than 10% average
                        instances.append({
                            'InstanceId': instance_id,
                            'Type': instance['InstanceType'],
                            'AverageCPU': avg_cpu,
                            'Recommendation': 'Downsize or terminate'
                        })

        return instances

    def estimate_reserved_instance_savings(self):
        """Estimate potential savings from reserved instances"""
        response = self.ce_client.get_reservation_purchase_recommendation(
            Service='EC2',
            LookbackPeriod='THIRTY_DAYS',
            PageSize=100
        )

        total_savings = 0
        for recommendation in response.get('Recommendations', []):
            summary = recommendation['RecommendationSummary']
            savings = float(summary['EstimatedMonthlyMonthlySavingsAmount'])
            total_savings += savings

        return total_savings

    def generate_report(self):
        """Generate comprehensive cost optimization report"""
        print("=== Cost Optimization Report ===\n")

        # Daily costs
        print("Daily Costs:")
        costs = self.get_daily_costs(7)
        for result in costs['ResultsByTime']:
            date = result['TimePeriod']['Start']
            total = result['Total']['BlendedCost']['Amount']
            print(f"  {date}: ${total}")

        # Underutilized instances
        print("\nUnderutilized Instances:")
        underutilized = self.find_underutilized_instances()
        for instance in underutilized:
            print(f"  {instance['InstanceId']}: {instance['AverageCPU']:.1f}% CPU - {instance['Recommendation']}")

        # Reserved instance savings
        print("\nReserved Instance Savings Potential:")
        savings = self.estimate_reserved_instance_savings()
        print(f"  Estimated Monthly Savings: ${savings:.2f}")

# Usage
if __name__ == '__main__':
    optimizer = CostOptimizer()
    optimizer.generate_report()
```

## Cost Optimization Strategies

### ✅ DO
- Use reserved instances for baseline
- Leverage spot instances
- Right-size resources
- Monitor cost trends
- Implement auto-scaling
- Use multi-region pricing
- Tag resources consistently
- Schedule non-essential resources

### ❌ DON'T
- Over-provision resources
- Ignore unused resources
- Neglect cost monitoring
- Run all on-demand
- Forget to release EIPs
- Mix cost centers
- Ignore savings opportunities
- Deploy without budgets

## Cost Saving Opportunities

- **Reserved Instances**: 40-70% savings
- **Spot Instances**: 70-90% savings
- **Committed Use Discounts**: 25-55% savings
- **Right-sizing**: 10-30% savings
- **Resource cleanup**: 5-20% savings

## Resources

- [AWS Cost Optimization](https://aws.amazon.com/architecture/cost-optimization/)
- [GCP Cost Optimization](https://cloud.google.com/cost-management)
- [Azure Cost Management](https://docs.microsoft.com/en-us/azure/cost-management-billing/)
- [Kubernetes Cost Optimization](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-cost/)
