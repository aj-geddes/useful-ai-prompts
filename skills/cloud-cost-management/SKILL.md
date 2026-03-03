---
name: cloud-cost-management
description: >
  Optimize and manage cloud costs across AWS, Azure, and GCP using reserved
  instances, spot pricing, and cost monitoring tools.
---

# Cloud Cost Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

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

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [AWS Cost Optimization with AWS CLI](references/aws-cost-optimization-with-aws-cli.md) | AWS Cost Optimization with AWS CLI |
| [Terraform Cost Management Configuration](references/terraform-cost-management-configuration.md) | Terraform Cost Management Configuration |
| [Azure Cost Management](references/azure-cost-management.md) | Azure Cost Management |
| [GCP Cost Optimization](references/gcp-cost-optimization.md) | GCP Cost Optimization |
| [Cost Monitoring Dashboard](references/cost-monitoring-dashboard.md) | Cost Monitoring Dashboard |

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
