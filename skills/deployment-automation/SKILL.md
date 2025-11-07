---
name: deployment-automation
description: Automate deployments across environments using Helm, Terraform, and ArgoCD. Implement blue-green deployments, canary releases, and rollback strategies.
---

# Deployment Automation

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

## Implementation Examples

### 1. **Helm Deployment Chart**

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
  enabled: true
  minReplicas: 2
  maxReplicas: 10
```

### 2. **GitHub Actions Deployment Workflow**

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy to'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: ${{ github.event.inputs.environment || 'staging' }}
    permissions:
      contents: read
      packages: read

    steps:
      - uses: actions/checkout@v3

      - name: Determine target environment
        id: env
        run: |
          if [[ "${{ github.ref }}" == "refs/heads/main" ]]; then
            echo "environment=staging" >> $GITHUB_OUTPUT
          else
            echo "environment=staging" >> $GITHUB_OUTPUT
          fi

      - name: Setup kubectl
        uses: azure/setup-kubectl@v3
        with:
          version: 'latest'

      - name: Configure kubectl
        run: |
          mkdir -p $HOME/.kube
          echo "${{ secrets.KUBE_CONFIG }}" | base64 -d > $HOME/.kube/config
          chmod 600 $HOME/.kube/config

      - name: Deploy with Helm
        run: |
          helm repo add myrepo ${{ secrets.HELM_REPO_URL }}
          helm repo update

          helm upgrade --install myapp myrepo/myapp \
            --namespace ${{ steps.env.outputs.environment }} \
            --create-namespace \
            --values helm/values-${{ steps.env.outputs.environment }}.yaml \
            --set image.tag=${{ github.sha }} \
            --wait \
            --timeout 5m

      - name: Verify deployment
        run: |
          kubectl rollout status deployment/myapp \
            -n ${{ steps.env.outputs.environment }} \
            --timeout=5m
```

### 3. **ArgoCD Deployment**

```yaml
# argocd/myapp-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default

  source:
    repoURL: https://github.com/myorg/helm-charts
    targetRevision: HEAD
    path: myapp
    helm:
      releaseName: myapp
      values: |
        image:
          tag: v1.0.0

  destination:
    server: https://kubernetes.default.svc
    namespace: production

  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

### 5. **Blue-Green Deployment**

```bash
#!/bin/bash
# Deploy green, run tests, switch traffic
helm upgrade --install myapp-green ./chart --set version=v2.0.0 --wait
kubectl run smoke-test --image=postman/newman --rm -- run tests/smoke.json

if [ $? -eq 0 ]; then
  kubectl patch service myapp -p '{"spec":{"selector":{"version":"v2.0.0"}}}'
  echo "✅ Traffic switched to green"
else
  helm uninstall myapp-green
  exit 1
fi
```

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

## Deployment Checklist

```bash
# Pre-deployment verification
- [ ] Run tests in staging
- [ ] Verify database migrations
- [ ] Check infrastructure capacity
- [ ] Review changelog
- [ ] Verify rollback plan
- [ ] Notify stakeholders
- [ ] Monitor error rates
- [ ] Prepare rollback script
```

## Resources

- [Helm Documentation](https://helm.sh/docs/)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [Flagger Canary Releases](https://flagger.app/)
