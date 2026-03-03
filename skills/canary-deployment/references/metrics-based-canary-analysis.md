# Metrics-Based Canary Analysis

## Metrics-Based Canary Analysis

```yaml
# canary-monitoring.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: canary-analysis
  namespace: production
data:
  analyze.sh: |
    #!/bin/bash
    set -euo pipefail

    CANARY_DEPLOYMENT="${1:-myapp-canary}"
    STABLE_DEPLOYMENT="${2:-myapp-stable}"
    THRESHOLD="${3:-0.05}"  # 5% error rate threshold
    NAMESPACE="production"

    echo "Analyzing canary metrics..."

    # Query Prometheus for metrics
    CANARY_ERROR_RATE=$(curl -s 'http://prometheus:9090/api/v1/query' \
      --data-urlencode 'query=rate(http_requests_total{status=~"5..",deployment="'${CANARY_DEPLOYMENT}'"}[5m])' | \
      jq -r '.data.result[0].value[1]' || echo "0")

    STABLE_ERROR_RATE=$(curl -s 'http://prometheus:9090/api/v1/query' \
      --data-urlencode 'query=rate(http_requests_total{status=~"5..",deployment="'${STABLE_DEPLOYMENT}'"}[5m])' | \
      jq -r '.data.result[0].value[1]' || echo "0")

    CANARY_LATENCY=$(curl -s 'http://prometheus:9090/api/v1/query' \
      --data-urlencode 'query=histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{deployment="'${CANARY_DEPLOYMENT}'"}[5m]))' | \
      jq -r '.data.result[0].value[1]' || echo "0")

    STABLE_LATENCY=$(curl -s 'http://prometheus:9090/api/v1/query' \
      --data-urlencode 'query=histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{deployment="'${STABLE_DEPLOYMENT}'"}[5m]))' | \
      jq -r '.data.result[0].value[1]' || echo "0")

    echo "Canary Error Rate: $CANARY_ERROR_RATE"
    echo "Stable Error Rate: $STABLE_ERROR_RATE"
    echo "Canary P95 Latency: ${CANARY_LATENCY}s"
    echo "Stable P95 Latency: ${STABLE_LATENCY}s"

    # Check if canary is within acceptable range
    if (( $(echo "$CANARY_ERROR_RATE > $THRESHOLD" | bc -l) )); then
      echo "FAIL: Canary error rate exceeds threshold"
      exit 1
    fi

    if (( $(echo "$CANARY_LATENCY > $STABLE_LATENCY * 1.2" | bc -l) )); then
      echo "FAIL: Canary latency is 20% higher than stable"
      exit 1
    fi

    echo "PASS: Canary meets quality criteria"
    exit 0

---
apiVersion: batch/v1
kind: Job
metadata:
  name: canary-analysis
  namespace: production
spec:
  template:
    spec:
      containers:
        - name: analyzer
          image: curlimages/curl:latest
          command:
            - sh
            - -c
            - |
              apk add --no-cache bc jq
              bash /scripts/analyze.sh
          volumeMounts:
            - name: scripts
              mountPath: /scripts
      volumes:
        - name: scripts
          configMap:
            name: canary-analysis
      restartPolicy: Never
```
