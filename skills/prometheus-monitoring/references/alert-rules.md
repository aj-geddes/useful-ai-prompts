# Alert Rules

## Alert Rules

```yaml
# /etc/prometheus/alert_rules.yml
groups:
  - name: application
    rules:
      - alert: HighErrorRate
        expr: rate(requests_total{status_code=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate: {{ $value }}"

      - alert: HighLatency
        expr: histogram_quantile(0.95, request_duration_seconds) > 1
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "p95 latency: {{ $value }}s"

      - alert: HighMemoryUsage
        expr: node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes < 0.1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Low memory: {{ $value }}"
```
