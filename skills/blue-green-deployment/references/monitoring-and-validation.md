# Monitoring and Validation

## Monitoring and Validation

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
