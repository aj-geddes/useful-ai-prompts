---
name: infrastructure-cost-optimization
description: >
  Optimize cloud infrastructure costs through resource rightsizing, reserved.
  Use when cloud cost reduction, budget management and tracking, resource utilization optimization, or multi-environment cost allocation.
  instances, spot instances, and waste reduction strategies.
---

# Infrastructure Cost Optimization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [AWS Cost Optimization Configuration](references/aws-cost-optimization-configuration.md) | AWS Cost Optimization Configuration |
| [Kubernetes Cost Optimization](references/kubernetes-cost-optimization.md) | Kubernetes Cost Optimization |
| [Cost Monitoring Dashboard](references/cost-monitoring-dashboard.md) | Cost Monitoring Dashboard |

## Best Practices

### ✅ DO

- Rightsize instances based on actual utilization data (CPU, memory, network) over at least 14 days before committing to reservations
- Tag every resource with cost-allocation tags (team, environment, service) to enable accurate chargeback and waste detection
- Use Spot/Preemptible instances for stateless, fault-tolerant workloads and batch jobs
- Schedule non-production environments to shut down outside business hours automatically
- Review Reserved Instance and Savings Plan coverage monthly and adjust for changing workloads
- Set budget alerts at 50%, 80%, and 100% thresholds with automated notifications to the responsible team

### ❌ DON'T

- Purchase Reserved Instances based on peak demand — buy for steady-state baseline and cover spikes with on-demand or Spot
- Leave unattached EBS volumes, idle load balancers, or orphaned snapshots running unreviewed
- Assume last month's cost breakdown still applies — workloads drift and new services appear
- Optimize cost at the expense of reliability without explicit stakeholder sign-off on the trade-off
