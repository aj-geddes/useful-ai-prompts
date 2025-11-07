---
name: blue-green-deployment
description: Implement blue-green deployment strategies for zero-downtime releases with instant rollback capability and traffic switching between environments.
---

# Blue-Green Deployment

## Overview

Deploy applications using blue-green deployment patterns to maintain two identical production environments, enabling instant traffic switching and rapid rollback capabilities.

## When to Use

- Zero-downtime releases
- High-risk deployments
- Complex application migrations
- Database schema changes
- Rapid rollback requirements
- A/B testing with environment separation
- Staged rollout strategies

## Implementation Examples

### 1. **Blue-Green with Load Balancer**

```yaml
# blue-green-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: blue-green-config
  namespace: production
data:
  switch-traffic.sh: |
    #!/bin/bash
    set -euo pipefail

    CURRENT_ACTIVE="${1:-blue}"
    TARGET="${2:-green}"
    ALB_ARN="arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/myapp-alb/1234567890abcdef"

    echo "Switching traffic from $CURRENT_ACTIVE to $TARGET..."

    # Get target group ARNs
    BLUE_TG=$(aws elbv2 describe-target-groups \
      --load-balancer-arn "$ALB_ARN" \
      --query "TargetGroups[?Tags[?Key=='Name' && Value=='blue']].TargetGroupArn" \
      --output text)

    GREEN_TG=$(aws elbv2 describe-target-groups \
      --load-balancer-arn "$ALB_ARN" \
      --query "TargetGroups[?Tags[?Key=='Name' && Value=='green']].TargetGroupArn" \
      --output text)

    # Get listener ARN
    LISTENER_ARN=$(aws elbv2 describe-listeners \
      --load-balancer-arn "$ALB_ARN" \
      --query "Listeners[0].ListenerArn" \
      --output text)

    # Switch target group
    if [ "$TARGET" = "green" ]; then
      TARGET_ARN=$GREEN_TG
    else
      TARGET_ARN=$BLUE_TG
    fi

    aws elbv2 modify-listener \
      --listener-arn "$LISTENER_ARN" \
      --default-actions Type=forward,TargetGroupArn="$TARGET_ARN"

    echo "Traffic switched to $TARGET"

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: deploy-script
  namespace: production
data:
  deploy-blue-green.sh: |
    #!/bin/bash
    set -euo pipefail

    ENVIRONMENT="${1:-production}"
    VERSION="${2:-latest}"
    HEALTH_CHECK_ENDPOINT="/health"
    HEALTH_CHECK_TIMEOUT=300

    # Determine which environment to deploy to
    CURRENT_ACTIVE=$(kubectl get configmap active-environment -n "$ENVIRONMENT" \
      -o jsonpath='{.data.active}' 2>/dev/null || echo "blue")

    if [ "$CURRENT_ACTIVE" = "blue" ]; then
      TARGET="green"
    else
      TARGET="blue"
    fi

    echo "Current active: $CURRENT_ACTIVE, deploying to: $TARGET"

    # Update deployment with new version
    kubectl set image deployment/myapp-$TARGET \
      myapp=myrepo/myapp:$VERSION \
      -n "$ENVIRONMENT"

    # Wait for rollout
    echo "Waiting for deployment to rollout..."
    kubectl rollout status deployment/myapp-$TARGET \
      -n "$ENVIRONMENT" --timeout=10m

    # Run health checks
    echo "Running health checks on $TARGET..."
    TARGET_PODS=$(kubectl get pods -l app=myapp,environment=$TARGET \
      -n "$ENVIRONMENT" -o jsonpath='{.items[0].metadata.name}')

    for pod in $TARGET_PODS; do
      echo "Health checking pod: $pod"
      kubectl port-forward pod/$pod 8080:8080 -n "$ENVIRONMENT" &
      PF_PID=$!

      if ! timeout 30 bash -c "until curl -f http://localhost:8080$HEALTH_CHECK_ENDPOINT; do sleep 1; done"; then
        kill $PF_PID
        echo "Health check failed for $pod"
        exit 1
      fi

      kill $PF_PID
    done

    # Run smoke tests
    echo "Running smoke tests..."
    kubectl exec -it deployment/myapp-$TARGET -n "$ENVIRONMENT" -- \
      npm run test:smoke || true

    # Update active environment ConfigMap
    kubectl patch configmap active-environment -n "$ENVIRONMENT" \
      -p '{"data":{"active":"'$TARGET'"}}'

    # Switch traffic
    echo "Switching traffic to $TARGET..."
    bash /scripts/switch-traffic.sh "$CURRENT_ACTIVE" "$TARGET"

    echo "Deployment complete! $TARGET is now active"
    echo "Previous version still running on $CURRENT_ACTIVE for rollback"

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-blue
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      environment: blue
  template:
    metadata:
      labels:
        app: myapp
        environment: blue
    spec:
      containers:
        - name: myapp
          image: myrepo/myapp:v1.0.0
          ports:
            - containerPort: 8080
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-green
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      environment: green
  template:
    metadata:
      labels:
        app: myapp
        environment: green
    spec:
      containers:
        - name: myapp
          image: myrepo/myapp:v1.0.0
          ports:
            - containerPort: 8080
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10

---
apiVersion: v1
kind: Service
metadata:
  name: myapp
  namespace: production
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: active-environment
  namespace: production
data:
  active: "blue"
```

### 2. **Blue-Green Rollback Script**

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

### 3. **Monitoring and Validation**

```yaml
# blue-green-monitoring.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: validation-script
  namespace: production
data:
  validate-deployment.sh: |
    #!/bin/bash
    set -euo pipefail

    ENVIRONMENT="${1:-production}"
    DEPLOYMENT="${2:-myapp-green}"
    TIMEOUT=300

    echo "Validating deployment: $DEPLOYMENT"

    # Wait for deployment
    kubectl rollout status deployment/$DEPLOYMENT -n "$ENVIRONMENT" --timeout=${TIMEOUT}s

    # Check pod readiness
    READY_REPLICAS=$(kubectl get deployment $DEPLOYMENT -n "$ENVIRONMENT" \
      -o jsonpath='{.status.readyReplicas}')
    DESIRED_REPLICAS=$(kubectl get deployment $DEPLOYMENT -n "$ENVIRONMENT" \
      -o jsonpath='{.spec.replicas}')

    if [ "$READY_REPLICAS" != "$DESIRED_REPLICAS" ]; then
      echo "ERROR: Not all replicas are ready ($READY_REPLICAS/$DESIRED_REPLICAS)"
      exit 1
    fi

    # Run smoke tests
    echo "Running smoke tests..."
    SMOKE_TEST_POD=$(kubectl get pods -l app=myapp,environment=${DEPLOYMENT#myapp-} \
      -n "$ENVIRONMENT" -o jsonpath='{.items[0].metadata.name}')

    kubectl exec -it $SMOKE_TEST_POD -n "$ENVIRONMENT" -- bash -c '
      echo "Testing health endpoint..."
      curl -f http://localhost:8080/health || exit 1

      echo "Testing API endpoints..."
      curl -f http://localhost:8080/api/version || exit 1

      echo "All smoke tests passed"
    '

    echo "Validation complete: $DEPLOYMENT is healthy"

---
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: blue-green-alerts
  namespace: production
spec:
  groups:
    - name: blue-green-deployment
      rules:
        - alert: HighErrorRateAfterDeployment
          expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "High error rate detected after deployment"
            description: "Error rate is {{ $value | humanizePercentage }}"

        - alert: DeploymentHealthCheckFailed
          expr: up{job="myapp"} == 0
          for: 2m
          labels:
            severity: critical
          annotations:
            summary: "Deployment health check failed"
            description: "Pod is unreachable for 2 minutes"

        - alert: PodRestartingAfterDeployment
          expr: rate(kube_pod_container_status_restarts_total[15m]) > 0.1
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "Pod is restarting frequently after deployment"
```

## Blue-Green Best Practices

### ✅ DO
- Run comprehensive health checks
- Monitor both environments during switching
- Keep previous version running for quick rollback
- Test traffic switching in non-prod first
- Document deployment procedure
- Have rollback plan ready
- Monitor error rates post-switch
- Automate environment sync

### ❌ DON'T
- Switch traffic without health checks
- Tear down old environment immediately
- Mix blue and green traffic
- Skip smoke tests
- Deploy without capacity planning
- Rush traffic switching
- Ignore monitoring post-deployment
- Run different versions in production

## Rollback Scenarios

- **Health Check Failure**: Automatic rollback on failed checks
- **High Error Rate**: Monitor and trigger rollback if error rate exceeds threshold
- **Performance Degradation**: Rollback if latency spikes detected
- **Dependency Failures**: Rollback if external service integration fails

## Resources

- [Blue-Green Deployments Pattern](https://martinfowler.com/bliki/BlueGreenDeployment.html)
- [Kubernetes Deployment Strategies](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy)
- [AWS Blue-Green Deployments](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/)
