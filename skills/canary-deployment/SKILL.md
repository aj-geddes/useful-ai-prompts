---
name: canary-deployment
description: >
  Implement canary deployment strategies to gradually roll out new versions to
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

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
