# ArgoCD Deployment

## ArgoCD Deployment

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
