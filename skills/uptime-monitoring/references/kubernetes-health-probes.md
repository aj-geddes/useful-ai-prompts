# Kubernetes Health Probes

## Kubernetes Health Probes

```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
        - name: api-service
          image: api-service:latest

          startupProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 0
            periodSeconds: 10
            failureThreshold: 30

          readinessProbe:
            httpGet:
              path: /readiness
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 5
            failureThreshold: 3

          livenessProbe:
            httpGet:
              path: /liveness
              port: 3000
            initialDelaySeconds: 15
            periodSeconds: 20
            failureThreshold: 3
```
