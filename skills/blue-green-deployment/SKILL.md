---
name: blue-green-deployment
description: >
  Implement blue-green deployment strategies for zero-downtime releases with
  instant rollback capability and traffic switching between environments.
---

# Blue-Green Deployment

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Deploy applications using blue-green deployment patterns to maintain two identical production environments, enabling instant traffic switching and rapid rollback capabilities.

## When to Use

- Zero-downtime releases
- High-risk deployments
- Complex application migrations
- Database schema changes
- Rapid rollback requirements
- A/B testing with environment separation
- Staged rollout strategies

## Quick Start

Minimal working example:

```yaml
# blue-green-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: blue-green-config
  namespace: production
data:
  switch-traffic.sh: |
    #!/bin/bash
    set -euo pipefail

    CURRENT_ACTIVE="${1:-blue}"
    TARGET="${2:-green}"
    ALB_ARN="arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/myapp-alb/1234567890abcdef"

    echo "Switching traffic from $CURRENT_ACTIVE to $TARGET..."

    # Get target group ARNs
    BLUE_TG=$(aws elbv2 describe-target-groups \
      --load-balancer-arn "$ALB_ARN" \
      --query "TargetGroups[?Tags[?Key=='Name' && Value=='blue']].TargetGroupArn" \
      --output text)

    GREEN_TG=$(aws elbv2 describe-target-groups \
      --load-balancer-arn "$ALB_ARN" \
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Blue-Green with Load Balancer](references/blue-green-with-load-balancer.md) | Blue-Green with Load Balancer |
| [Blue-Green Rollback Script](references/blue-green-rollback-script.md) | Blue-Green Rollback Script |
| [Monitoring and Validation](references/monitoring-and-validation.md) | Monitoring and Validation |

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
