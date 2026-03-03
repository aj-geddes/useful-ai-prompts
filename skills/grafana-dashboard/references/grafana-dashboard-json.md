# Grafana Dashboard JSON

## Grafana Dashboard JSON

```json
{
  "dashboard": {
    "title": "Application Performance",
    "description": "Real-time application metrics",
    "tags": ["production", "performance"],
    "timezone": "UTC",
    "refresh": "30s",
    "templating": {
      "list": [
        {
          "name": "datasource",
          "type": "datasource",
          "datasource": "prometheus"
        },
        {
          "name": "service",
          "type": "query",
          "datasource": "prometheus",
          "query": "label_values(requests_total, service)"
        }
      ]
    },
    "panels": [
      {
        "id": 1,
        "title": "Request Rate",
        "type": "graph",
        "gridPos": { "x": 0, "y": 0, "w": 12, "h": 8 },
        "targets": [
          {
            "expr": "sum(rate(requests_total{service=\"$service\"}[5m]))",
            "legendFormat": "{{ method }}"
          }
        ],
        "yaxes": [
          {
            "format": "rps",
            "label": "Requests per Second"
          }
        ]
      },
      {
        "id": 2,
        "title": "Error Rate",
        "type": "graph",
        "gridPos": { "x": 12, "y": 0, "w": 12, "h": 8 },
        "targets": [
          {
            "expr": "sum(rate(requests_total{status_code=~\"5..\",service=\"$service\"}[5m])) / sum(rate(requests_total{service=\"$service\"}[5m]))",
            "legendFormat": "Error Rate"
          }
        ]
      },
      {
        "id": 3,
        "title": "Response Latency (p95)",
        "type": "graph",
        "gridPos": { "x": 0, "y": 8, "w": 12, "h": 8 },
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(request_duration_seconds_bucket{service=\"$service\"}[5m]))",
            "legendFormat": "p95"
          }
        ]
      },
      {
        "id": 4,
        "title": "Active Connections",
        "type": "stat",
        "gridPos": { "x": 12, "y": 8, "w": 12, "h": 8 },
        "targets": [
          {
            "expr": "sum(active_connections{service=\"$service\"})"
          }
        ]
      }
    ]
  }
}
```
