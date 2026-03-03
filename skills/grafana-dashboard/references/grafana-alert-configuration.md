# Grafana Alert Configuration

## Grafana Alert Configuration

```yaml
# /etc/grafana/provisioning/alerting/alerts.yaml
groups:
  - name: application_alerts
    interval: 1m
    rules:
      - uid: alert_high_error_rate
        title: High Error Rate
        condition: B
        data:
          - refId: A
            model:
              expr: 'sum(rate(requests_total{status_code=~"5.."}[5m]))'
          - refId: B
            conditions:
              - evaluator:
                  params: [0.05]
                  type: gt
                query:
                  params: [A, 5m, now]
        for: 5m
        annotations:
          description: "Error rate is {{ $values.A }}"
        labels:
          severity: critical
          team: platform
```
