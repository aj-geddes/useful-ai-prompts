# Prometheus Configuration

## Prometheus Configuration

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    monitor: "infrastructure-monitor"
    environment: "production"

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - localhost:9093

# Rule files
rule_files:
  - "alerts.yml"
  - "rules.yml"

scrape_configs:
  # Prometheus itself
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  # Node Exporter for system metrics
  - job_name: "node"
    static_configs:
      - targets:
          - "node1.internal:9100"
          - "node2.internal:9100"
          - "node3.internal:9100"
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance

  # Docker container metrics
  - job_name: "docker"
    static_configs:
      - targets: ["localhost:9323"]
    metrics_path: "/metrics"

  # Kubernetes metrics
  - job_name: "kubernetes-apiservers"
    kubernetes_sd_configs:
      - role: endpoints
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
      - source_labels:
          [
            __meta_kubernetes_namespace,
            __meta_kubernetes_service_name,
            __meta_kubernetes_endpoint_port_name,
          ]
        action: keep
        regex: default;kubernetes;https

  # Application metrics
  - job_name: "application"
    metrics_path: "/metrics"
    static_configs:
      - targets:
          - "app1.internal:8080"
          - "app2.internal:8080"
          - "app3.internal:8080"
    scrape_interval: 10s
    scrape_timeout: 5s

  # PostgreSQL metrics
  - job_name: "postgres"
    static_configs:
      - targets: ["postgres-exporter.internal:9187"]

  # Redis metrics
  - job_name: "redis"
    static_configs:
      - targets: ["redis-exporter.internal:9121"]

  # RabbitMQ metrics
  - job_name: "rabbitmq"
    static_configs:
      - targets: ["rabbitmq.internal:15692"]
```
