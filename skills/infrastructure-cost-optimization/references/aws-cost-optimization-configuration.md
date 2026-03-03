# AWS Cost Optimization Configuration

## AWS Cost Optimization Configuration

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
