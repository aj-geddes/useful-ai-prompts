# Automated Canary Promotion

## Automated Canary Promotion

```bash
#!/bin/bash
# promote-canary.sh - Automatically promote successful canary

set -euo pipefail

NAMESPACE="${1:-production}"
DEPLOYMENT="${2:-myapp}"
MAX_DURATION="${3:-600}"  # Max 10 minutes for canary

start_time=$(date +%s)

echo "Starting automated canary promotion for $DEPLOYMENT"

while true; do
  current_time=$(date +%s)
  elapsed=$((current_time - start_time))

  if [ $elapsed -gt $MAX_DURATION ]; then
    echo "ERROR: Canary exceeded max duration"
    exit 1
  fi

  # Check canary health
  CANARY_REPLICAS=$(kubectl get deployment ${DEPLOYMENT}-canary -n "$NAMESPACE" \
    -o jsonpath='{.status.readyReplicas}')
  CANARY_DESIRED=$(kubectl get deployment ${DEPLOYMENT}-canary -n "$NAMESPACE" \
    -o jsonpath='{.spec.replicas}')

  if [ "$CANARY_REPLICAS" -ne "$CANARY_DESIRED" ]; then
    echo "Waiting for canary pods to be ready..."
    sleep 10
    continue
  fi

  # Run analysis
  if bash /scripts/analyze.sh "$DEPLOYMENT-canary" "$DEPLOYMENT-stable"; then
    echo "Canary analysis passed! Promoting to stable..."

    # Merge canary into stable
    kubectl set image deployment/${DEPLOYMENT} \
      ${DEPLOYMENT}=myrepo/${DEPLOYMENT}:$(kubectl get deployment ${DEPLOYMENT}-canary -n "$NAMESPACE" \
        -o jsonpath='{.spec.template.spec.containers[0].image}' | cut -d: -f2) \
      -n "$NAMESPACE"

    kubectl rollout status deployment/${DEPLOYMENT} -n "$NAMESPACE" --timeout=5m

    echo "Canary promoted successfully!"
    exit 0
  else
    echo "Canary analysis failed. Rolling back..."
    exit 1
  fi
done
```
