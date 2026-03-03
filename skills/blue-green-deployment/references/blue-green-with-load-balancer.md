# Blue-Green with Load Balancer

## Blue-Green with Load Balancer

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
