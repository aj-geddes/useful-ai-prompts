# Kubernetes Native Canary Script

## Kubernetes Native Canary Script

```bash
#!/bin/bash
# canary-rollout.sh - Canary deployment with k8s native tools

set -euo pipefail

NAMESPACE="${1:-production}"
DEPLOYMENT="${2:-myapp}"
NEW_VERSION="${3:-latest}"
CANARY_WEIGHT=10
MAX_WEIGHT=100
STEP_WEIGHT=10
CHECK_INTERVAL=60
MAX_ERROR_RATE=0.05

echo "Starting canary deployment for $DEPLOYMENT with version $NEW_VERSION"

# Get current replicas
CURRENT_REPLICAS=$(kubectl get deployment $DEPLOYMENT -n "$NAMESPACE" \
  -o jsonpath='{.spec.replicas}')
CANARY_REPLICAS=$((CURRENT_REPLICAS / 10 + 1))

echo "Current replicas: $CURRENT_REPLICAS, Canary replicas: $CANARY_REPLICAS"

# Create canary deployment
kubectl set image deployment/${DEPLOYMENT}-canary \
  ${DEPLOYMENT}=myrepo/${DEPLOYMENT}:${NEW_VERSION} \
  -n "$NAMESPACE"

# Scale up canary gradually
CURRENT_WEIGHT=$CANARY_WEIGHT
while [ $CURRENT_WEIGHT -le $MAX_WEIGHT ]; do
  echo "Setting traffic to canary: ${CURRENT_WEIGHT}%"

  # Update ingress or service to split traffic
  kubectl patch virtualservice ${DEPLOYMENT} -n "$NAMESPACE" --type merge \
    -p '{"spec":{"http":[{"route":[{"destination":{"host":"'${DEPLOYMENT}-stable'"},"weight":'$((100-CURRENT_WEIGHT))'},{"destination":{"host":"'${DEPLOYMENT}-canary'"},"weight":'${CURRENT_WEIGHT}'}]}]}}'

  # Wait and check metrics
  echo "Monitoring metrics for ${CHECK_INTERVAL}s..."
  sleep $CHECK_INTERVAL

  # Check error rate
  ERROR_RATE=$(kubectl exec -it deployment/${DEPLOYMENT}-canary -n "$NAMESPACE" -- \
    curl -s http://localhost:8080/metrics | grep http_requests_total | \
    awk '{print $2}' || echo "0")

  if (( $(echo "$ERROR_RATE > $MAX_ERROR_RATE" | bc -l) )); then
    echo "ERROR: Error rate exceeded threshold: $ERROR_RATE"
    echo "Rolling back canary deployment..."
    kubectl patch virtualservice ${DEPLOYMENT} -n "$NAMESPACE" --type merge \
      -p '{"spec":{"http":[{"route":[{"destination":{"host":"'${DEPLOYMENT}-stable'"},"weight":100}]}]}}'
    exit 1
  fi

  CURRENT_WEIGHT=$((CURRENT_WEIGHT + STEP_WEIGHT))
done

# Promote canary to stable
echo "Canary deployment successful! Promoting to stable..."
kubectl set image deployment/${DEPLOYMENT} \
  ${DEPLOYMENT}=myrepo/${DEPLOYMENT}:${NEW_VERSION} \
  -n "$NAMESPACE"

kubectl rollout status deployment/${DEPLOYMENT} -n "$NAMESPACE" --timeout=5m

echo "Canary deployment complete!"
```
