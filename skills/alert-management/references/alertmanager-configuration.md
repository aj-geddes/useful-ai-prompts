# Alertmanager Configuration

## Alertmanager Configuration

```yaml
# /etc/alertmanager/alertmanager.yml
global:
  resolve_timeout: 5m
  slack_api_url: "${SLACK_WEBHOOK_URL}"

templates:
  - "/etc/alertmanager/templates/*.tmpl"

route:
  receiver: "default"
  group_by: ["alertname", "cluster", "service"]
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 4h

  routes:
    - match:
        severity: critical
      receiver: pagerduty
      continue: true
      group_wait: 0s

    - match:
        severity: warning
      receiver: slack

    - match:
        service: payment-service
      receiver: payment-team
      group_wait: 30s

receivers:
  - name: "default"
    slack_configs:
      - channel: "#alerts"
        title: "Alert: {{ .GroupLabels.alertname }}"

  - name: "pagerduty"
    pagerduty_configs:
      - service_key: "${PAGERDUTY_SERVICE_KEY}"
        description: "{{ .GroupLabels.alertname }}"

  - name: "slack"
    slack_configs:
      - channel: "#alerts"
        title: "Warning: {{ .GroupLabels.alertname }}"

  - name: "payment-team"
    pagerduty_configs:
      - service_key: "${PAYMENT_PAGERDUTY_KEY}"
    slack_configs:
      - channel: "#payment-alerts"

inhibit_rules:
  - source_match:
      severity: "critical"
    target_match:
      severity: "warning"
    equal: ["alertname", "service"]
```
