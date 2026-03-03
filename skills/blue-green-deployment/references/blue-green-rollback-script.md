# Blue-Green Rollback Script

## Blue-Green Rollback Script

```bash
#!/bin/bash
# rollback-blue-green.sh - Rollback to previous environment

set -euo pipefail

NAMESPACE="${1:-production}"
HEALTH_CHECK_TIMEOUT=60

echo "Starting rollback procedure..."

# Get current active environment
CURRENT_ACTIVE=$(kubectl get configmap active-environment -n "$NAMESPACE" \
  -o jsonpath='{.data.active}')

# Target is the previous environment
if [ "$CURRENT_ACTIVE" = "blue" ]; then
  TARGET="green"
else
  TARGET="blue"
fi

echo "Rolling back from $CURRENT_ACTIVE to $TARGET..."

# Verify target environment is healthy
echo "Verifying $TARGET environment health..."
HEALTHY_PODS=$(kubectl get pods -l app=myapp,environment=$TARGET \
  -n "$NAMESPACE" --field-selector=status.phase=Running -o json | \
  jq '.items | length')

if [ "$HEALTHY_PODS" -lt 1 ]; then
  echo "ERROR: No healthy pods in $TARGET environment"
  exit 1
fi

# Switch traffic back
echo "Switching traffic back to $TARGET..."
kubectl patch configmap active-environment -n "$NAMESPACE" \
  -p '{"data":{"active":"'$TARGET'"}}'

# Update load balancer
aws elbv2 modify-listener \
  --listener-arn "arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/myapp-alb/1234567890abcdef/50dc6c495c0c9188" \
  --default-actions Type=forward,TargetGroupArn="arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/myapp-$TARGET/1234567890abcdef"

echo "Rollback complete! Traffic switched to $TARGET"
echo "Previous active environment ($CURRENT_ACTIVE) is still running for analysis"
```
