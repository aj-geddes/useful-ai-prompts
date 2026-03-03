# Alertmanager Configuration

## Alertmanager Configuration

```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m
  slack_api_url: "YOUR_SLACK_WEBHOOK_URL"

# Template files
templates:
  - "/etc/alertmanager/templates/*.tmpl"

# Routing tree
route:
  receiver: "default"
  group_by: ["alertname", "cluster", "service"]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h

  routes:
    # Critical alerts
    - match:
        severity: critical
      receiver: "critical-team"
      continue: true
      group_wait: 10s
      repeat_interval: 1h

    # Warning alerts
    - match:
        severity: warning
      receiver: "warning-channel"
      group_wait: 1m

# Receivers
receivers:
  - name: "default"
    slack_configs:
      - channel: "#alerts"
        title: "Alert: {{ .GroupLabels.alertname }}"
        text: "{{ range .Alerts }}{{ .Annotations.description }}{{ end }}"

  - name: "critical-team"
    slack_configs:
      - channel: "#critical-alerts"
        title: "CRITICAL: {{ .GroupLabels.alertname }}"
    email_configs:
      - to: "oncall@mycompany.com"
        from: "alertmanager@mycompany.com"
        smarthost: "smtp.mycompany.com:587"
        auth_username: "alertmanager@mycompany.com"
        auth_password: "secret"

  - name: "warning-channel"
    slack_configs:
      - channel: "#warnings"
        title: "Warning: {{ .GroupLabels.alertname }}"
```
