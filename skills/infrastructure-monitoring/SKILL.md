---
name: infrastructure-monitoring
description: Set up comprehensive infrastructure monitoring with Prometheus, Grafana, and alerting systems for metrics, health checks, and performance tracking.
---

# Infrastructure Monitoring

## Overview

Implement comprehensive infrastructure monitoring to track system health, performance metrics, and resource utilization with alerting and visualization across your entire stack.

## When to Use

- Real-time performance monitoring
- Capacity planning and trends
- Incident detection and alerting
- Service health tracking
- Resource utilization analysis
- Performance troubleshooting
- Compliance and audit trails
- Historical data analysis

## Implementation Examples

### 1. **Prometheus Configuration**

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    monitor: 'infrastructure-monitor'
    environment: 'production'

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - localhost:9093

# Rule files
rule_files:
  - 'alerts.yml'
  - 'rules.yml'

scrape_configs:
  # Prometheus itself
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Node Exporter for system metrics
  - job_name: 'node'
    static_configs:
      - targets:
          - 'node1.internal:9100'
          - 'node2.internal:9100'
          - 'node3.internal:9100'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance

  # Docker container metrics
  - job_name: 'docker'
    static_configs:
      - targets: ['localhost:9323']
    metrics_path: '/metrics'

  # Kubernetes metrics
  - job_name: 'kubernetes-apiservers'
    kubernetes_sd_configs:
      - role: endpoints
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
        action: keep
        regex: default;kubernetes;https

  # Application metrics
  - job_name: 'application'
    metrics_path: '/metrics'
    static_configs:
      - targets:
          - 'app1.internal:8080'
          - 'app2.internal:8080'
          - 'app3.internal:8080'
    scrape_interval: 10s
    scrape_timeout: 5s

  # PostgreSQL metrics
  - job_name: 'postgres'
    static_configs:
      - targets: ['postgres-exporter.internal:9187']

  # Redis metrics
  - job_name: 'redis'
    static_configs:
      - targets: ['redis-exporter.internal:9121']

  # RabbitMQ metrics
  - job_name: 'rabbitmq'
    static_configs:
      - targets: ['rabbitmq.internal:15692']
```

### 2. **Alert Rules**

```yaml
# alerts.yml
groups:
  - name: application_alerts
    interval: 30s
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value | humanizePercentage }}"

      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "High request latency"
          description: "P95 latency is {{ $value }}s"

      - alert: ServiceDown
        expr: up{job="application"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Service {{ $labels.instance }} is down"
          description: "Service has been unreachable for 1 minute"

  - name: infrastructure_alerts
    interval: 30s
    rules:
      - alert: HighCPUUsage
        expr: (100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage on {{ $labels.instance }}"
          description: "CPU usage is {{ $value }}%"

      - alert: HighMemoryUsage
        expr: (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100 > 85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High memory usage on {{ $labels.instance }}"
          description: "Memory usage is {{ $value }}%"

      - alert: LowDiskSpace
        expr: (node_filesystem_avail_bytes{fstype!~"tmpfs|fuse.lxcfs|squashfs|vfat"} / node_filesystem_size_bytes) * 100 < 10
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Low disk space on {{ $labels.instance }}"
          description: "Available disk space is {{ $value }}%"

      - alert: NodeNotReady
        expr: kube_node_status_condition{condition="Ready",status="true"} == 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Kubernetes node {{ $labels.node }} is not ready"
          description: "Node has been unready for 5 minutes"

      - alert: PodCrashLooping
        expr: rate(kube_pod_container_status_restarts_total[15m]) > 0.1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Pod {{ $labels.pod }} is crash looping"
          description: "Pod has restarted {{ $value }} times in 15 minutes"
```

### 3. **Alertmanager Configuration**

```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m
  slack_api_url: 'YOUR_SLACK_WEBHOOK_URL'

# Template files
templates:
  - '/etc/alertmanager/templates/*.tmpl'

# Routing tree
route:
  receiver: 'default'
  group_by: ['alertname', 'cluster', 'service']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h

  routes:
    # Critical alerts
    - match:
        severity: critical
      receiver: 'critical-team'
      continue: true
      group_wait: 10s
      repeat_interval: 1h

    # Warning alerts
    - match:
        severity: warning
      receiver: 'warning-channel'
      group_wait: 1m

# Receivers
receivers:
  - name: 'default'
    slack_configs:
      - channel: '#alerts'
        title: 'Alert: {{ .GroupLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'

  - name: 'critical-team'
    slack_configs:
      - channel: '#critical-alerts'
        title: 'CRITICAL: {{ .GroupLabels.alertname }}'
    email_configs:
      - to: 'oncall@mycompany.com'
        from: 'alertmanager@mycompany.com'
        smarthost: 'smtp.mycompany.com:587'
        auth_username: 'alertmanager@mycompany.com'
        auth_password: 'secret'

  - name: 'warning-channel'
    slack_configs:
      - channel: '#warnings'
        title: 'Warning: {{ .GroupLabels.alertname }}'
```

### 4. **Grafana Dashboard**

```json
{
  "dashboard": {
    "title": "Infrastructure Overview",
    "panels": [
      {
        "title": "CPU Usage",
        "targets": [
          {
            "expr": "100 - (avg(rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)"
          }
        ],
        "type": "graph",
        "alert": {
          "name": "CPU Usage Alert",
          "conditions": [
            {
              "evaluator": {
                "type": "gt",
                "params": [80]
              }
            }
          ]
        }
      },
      {
        "title": "Memory Usage",
        "targets": [
          {
            "expr": "(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100"
          }
        ],
        "type": "graph"
      },
      {
        "title": "Request Rate",
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])"
          }
        ],
        "type": "graph"
      },
      {
        "title": "Error Rate",
        "targets": [
          {
            "expr": "rate(http_requests_total{status=~\"5..\"}[5m])"
          }
        ],
        "type": "graph"
      },
      {
        "title": "Response Time P95",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))"
          }
        ],
        "type": "graph"
      },
      {
        "title": "Disk Usage",
        "targets": [
          {
            "expr": "(1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)) * 100"
          }
        ],
        "type": "graph"
      }
    ]
  }
}
```

### 5. **Monitoring Deployment**

```bash
#!/bin/bash
# deploy-monitoring.sh - Deploy Prometheus and Grafana

set -euo pipefail

NAMESPACE="monitoring"
PROMETHEUS_VERSION="v2.40.0"
GRAFANA_VERSION="9.3.2"

echo "Creating monitoring namespace..."
kubectl create namespace "$NAMESPACE" --dry-run=client -o yaml | kubectl apply -f -

# Deploy Prometheus
echo "Deploying Prometheus..."
kubectl apply -f prometheus-configmap.yaml -n "$NAMESPACE"
kubectl apply -f prometheus-deployment.yaml -n "$NAMESPACE"
kubectl apply -f prometheus-service.yaml -n "$NAMESPACE"

# Deploy Alertmanager
echo "Deploying Alertmanager..."
kubectl apply -f alertmanager-configmap.yaml -n "$NAMESPACE"
kubectl apply -f alertmanager-deployment.yaml -n "$NAMESPACE"
kubectl apply -f alertmanager-service.yaml -n "$NAMESPACE"

# Deploy Grafana
echo "Deploying Grafana..."
kubectl apply -f grafana-deployment.yaml -n "$NAMESPACE"
kubectl apply -f grafana-service.yaml -n "$NAMESPACE"

# Wait for deployments
echo "Waiting for deployments to be ready..."
kubectl rollout status deployment/prometheus -n "$NAMESPACE" --timeout=5m
kubectl rollout status deployment/alertmanager -n "$NAMESPACE" --timeout=5m
kubectl rollout status deployment/grafana -n "$NAMESPACE" --timeout=5m

# Port forward for access
echo "Port forwarding to services..."
kubectl port-forward -n "$NAMESPACE" svc/prometheus 9090:9090 &
kubectl port-forward -n "$NAMESPACE" svc/grafana 3000:3000 &

echo "Monitoring stack deployed successfully!"
echo "Prometheus: http://localhost:9090"
echo "Grafana: http://localhost:3000"
```

## Monitoring Best Practices

### ✅ DO
- Monitor key business metrics
- Set appropriate alert thresholds
- Use consistent naming conventions
- Implement dashboards for visualization
- Keep data retention reasonable
- Use labels for better querying
- Test alerting paths regularly
- Document alert meanings

### ❌ DON'T
- Alert on every metric change
- Ignore alert noise
- Store too much unnecessary data
- Set unrealistic thresholds
- Mix metrics from different sources
- Forget to test alert routing
- Alert without runbooks
- Over-instrument without purpose

## Resources

- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Alertmanager Documentation](https://prometheus.io/docs/alerting/latest/overview/)
- [Prometheus Best Practices](https://prometheus.io/docs/practices/instrumentation/)
