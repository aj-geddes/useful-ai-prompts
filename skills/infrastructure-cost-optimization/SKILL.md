---
name: infrastructure-cost-optimization
description: >
  Optimize cloud infrastructure costs through resource rightsizing, reserved
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

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
