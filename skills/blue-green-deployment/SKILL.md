---
name: blue-green-deployment
description: >
  Implement blue-green deployment strategies for zero-downtime releases with.
  Use when zero-downtime releases, high-risk deployments, complex application migrations, or database schema changes.
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

- Run a full health-check and smoke-test suite against the idle environment before switching traffic
- Keep both environments identical in infrastructure, config, and dependencies
- Use database migration strategies that are backward-compatible with both blue and green versions
- Automate the traffic switch and rollback via a single idempotent script
- Monitor error rates, latency, and saturation for at least 10 minutes after the switch before decommissioning the old environment

### ❌ DON'T

- Switch traffic without verifying the idle environment passes health checks
- Run destructive database migrations that break the currently-live version (prevents instant rollback)
- Tear down the previous environment immediately — keep it warm until the new deployment is confirmed stable
- Assume DNS-based switching is instant; account for TTL propagation delays
