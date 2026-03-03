# Autoscaling Script

## Autoscaling Script

```bash
#!/bin/bash
# autoscaling-setup.sh - Complete autoscaling configuration

set -euo pipefail

ENVIRONMENT="${1:-production}"
DEPLOYMENT="${2:-myapp}"

echo "Setting up autoscaling for $DEPLOYMENT in $ENVIRONMENT"

# Create HPA
cat <<EOF | kubectl apply -f -
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ${DEPLOYMENT}-hpa
  namespace: ${ENVIRONMENT}
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ${DEPLOYMENT}
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
          averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 50
          periodSeconds: 15
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15
EOF

echo "HPA created successfully"

# Monitor autoscaling
echo "Monitoring autoscaling events..."
kubectl get hpa ${DEPLOYMENT}-hpa -n $ENVIRONMENT -w
```
