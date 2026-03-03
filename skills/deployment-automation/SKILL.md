---
name: deployment-automation
description: >
  Automate deployments across environments using Helm, Terraform, and ArgoCD.
  Implement blue-green deployments, canary releases, and rollback strategies.
---

# Deployment Automation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Establish automated deployment pipelines that safely and reliably move applications across development, staging, and production environments with minimal manual intervention and risk.

## When to Use

- Continuous deployment to Kubernetes
- Infrastructure as Code deployment
- Multi-environment promotion
- Blue-green deployment strategies
- Canary release management
- Infrastructure provisioning
- Automated rollback procedures

## Quick Start

Minimal working example:

```yaml
# helm/Chart.yaml
apiVersion: v2
name: myapp
description: My awesome application
type: application
version: 1.0.0

# helm/values.yaml
replicaCount: 3
image:
  repository: ghcr.io/myorg/myapp
  pullPolicy: IfNotPresent
  tag: "1.0.0"
service:
  type: ClusterIP
  port: 80
  targetPort: 3000
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
autoscaling:
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Helm Deployment Chart](references/helm-deployment-chart.md) | Helm Deployment Chart |
| [GitHub Actions Deployment Workflow](references/github-actions-deployment-workflow.md) | GitHub Actions Deployment Workflow |
| [ArgoCD Deployment](references/argocd-deployment.md) | ArgoCD Deployment |
| [Blue-Green Deployment](references/blue-green-deployment.md) | Blue-Green Deployment |

## Best Practices

### ✅ DO

- Use Infrastructure as Code (Terraform, Helm)
- Implement GitOps workflows
- Use blue-green deployments
- Implement canary releases
- Automate rollback procedures
- Test deployments in staging first
- Use feature flags for gradual rollout
- Monitor deployment health
- Document deployment procedures
- Implement approval gates for production
- Version infrastructure code
- Use environment parity

### ❌ DON'T

- Deploy directly to production
- Skip testing in staging
- Use manual deployment scripts
- Deploy without rollback plan
- Ignore health checks
- Use hardcoded configuration
- Deploy during critical hours
- Skip pre-deployment validation
- Forget to backup before deploy
- Deploy from local machines
