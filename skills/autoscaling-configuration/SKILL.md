---
name: autoscaling-configuration
description: >
  Configure autoscaling for Kubernetes, VMs, and serverless workloads based on
  metrics, schedules, and custom indicators.
---

# Autoscaling Configuration

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement autoscaling strategies to automatically adjust resource capacity based on demand, ensuring cost efficiency while maintaining performance and availability.

## When to Use

- Traffic-driven workload scaling
- Time-based scheduled scaling
- Resource utilization optimization
- Cost reduction
- High-traffic event handling
- Batch processing optimization
- Database connection pooling

## Quick Start

Minimal working example:

```yaml
# hpa-configuration.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Kubernetes Horizontal Pod Autoscaler](references/kubernetes-horizontal-pod-autoscaler.md) | Kubernetes Horizontal Pod Autoscaler |
| [AWS Auto Scaling](references/aws-auto-scaling.md) | AWS Auto Scaling |
| [Custom Metrics Autoscaling](references/custom-metrics-autoscaling.md) | Custom Metrics Autoscaling |
| [Autoscaling Script](references/autoscaling-script.md) | Autoscaling Script |
| [Monitoring Autoscaling](references/monitoring-autoscaling.md) | Monitoring Autoscaling |

## Best Practices

### ✅ DO

- Set appropriate min/max replicas
- Monitor metric aggregation window
- Implement cooldown periods
- Use multiple metrics
- Test scaling behavior
- Monitor scaling events
- Plan for peak loads
- Implement fallback strategies

### ❌ DON'T

- Set min replicas to 1
- Scale too aggressively
- Ignore cooldown periods
- Use single metric only
- Forget to test scaling
- Scale below resource needs
- Neglect monitoring
- Deploy without capacity tests
