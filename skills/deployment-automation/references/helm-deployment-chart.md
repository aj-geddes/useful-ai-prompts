# Helm Deployment Chart

## Helm Deployment Chart

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
