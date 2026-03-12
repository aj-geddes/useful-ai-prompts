---
name: canary-deployment
description: >
  Implement canary deployment strategies to gradually roll out new versions to.
  Use when low-risk gradual rollouts, real-world testing with live traffic, automatic rollback on errors, or user impact minimization.
  subset of users with automatic rollback based on metrics.
---

# Canary Deployment

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Deploy new versions gradually to a small percentage of users, monitor metrics for issues, and automatically rollback or proceed based on predefined thresholds.

## When to Use

- Low-risk gradual rollouts
- Real-world testing with live traffic
- Automatic rollback on errors
- User impact minimization
- A/B testing integration
- Metrics-driven deployments
- High-traffic services

## Quick Start

Minimal working example:

```yaml
# canary-deployment-istio.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-v1
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: v1
  template:
    metadata:
      labels:
        app: myapp
        version: v1
    spec:
      containers:
        - name: myapp
          image: myrepo/myapp:1.0.0
          ports:
            - containerPort: 8080

---
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Istio-based Canary Deployment](references/istio-based-canary-deployment.md) | Istio-based Canary Deployment |
| [Kubernetes Native Canary Script](references/kubernetes-native-canary-script.md) | Kubernetes Native Canary Script |
| [Metrics-Based Canary Analysis](references/metrics-based-canary-analysis.md) | Metrics-Based Canary Analysis |
| [Automated Canary Promotion](references/automated-canary-promotion.md) | Automated Canary Promotion |

## Best Practices

### ✅ DO

- Start with a small traffic percentage (1-5%) and increase incrementally based on metric thresholds
- Define clear success criteria (error rate, latency p99, saturation) before beginning the rollout
- Automate rollback triggers so the canary is pulled back within seconds when thresholds are breached
- Use consistent request routing (sticky sessions or header-based) so individual users don't flip between versions mid-session
- Compare canary metrics against a baseline from the stable version, not just absolute thresholds

### ❌ DON'T

- Skip the bake time — let each traffic increment run long enough to surface slow-burn regressions
- Route all traffic to the canary at once; that defeats the purpose of gradual rollout
- Ignore infrastructure metrics (CPU, memory, GC pauses) and focus only on HTTP error rates
- Deploy canary changes that include backward-incompatible database migrations
