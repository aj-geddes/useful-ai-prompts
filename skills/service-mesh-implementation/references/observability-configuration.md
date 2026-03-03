# Observability Configuration

## Observability Configuration

```yaml
# observability-config.yaml
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: custom-logging
  namespace: production
spec:
  metrics:
    - providers:
        - name: prometheus
      dimensions:
        - request.path
        - response.code
        - destination.service.name

---
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: custom-tracing
  namespace: production
spec:
  tracing:
    - providers:
        - name: jaeger
      randomSamplingPercentage: 100.0
      useRequestIdForTraceSampling: true

---
# Grafana Dashboard ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: istio-dashboard
  namespace: monitoring
data:
  istio-mesh.json: |
    {
      "dashboard": {
        "title": "Istio Mesh",
        "panels": [
          {
            "title": "Request Rate",
            "targets": [
              {
                "expr": "rate(istio_requests_total[5m])"
              }
            ]
          },
          {
            "title": "Error Rate",
            "targets": [
              {
                "expr": "rate(istio_requests_total{response_code=~\"5..\"}[5m])"
              }
            ]
          },
          {
            "title": "Latency P95",
            "targets": [
              {
                "expr": "histogram_quantile(0.95, rate(istio_request_duration_milliseconds_bucket[5m]))"
              }
            ]
          }
        ]
      }
    }
```
