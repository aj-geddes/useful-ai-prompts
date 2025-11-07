---
name: prometheus-monitoring
description: Set up Prometheus monitoring for applications with custom metrics, scraping configurations, and service discovery. Use when implementing time-series metrics collection, monitoring applications, or building observability infrastructure.
---

# Prometheus Monitoring

## Overview

Implement comprehensive Prometheus monitoring infrastructure for collecting, storing, and querying time-series metrics from applications and infrastructure.

## When to Use

- Setting up metrics collection
- Creating custom application metrics
- Configuring scraping targets
- Implementing service discovery
- Building monitoring infrastructure

## Instructions

### 1. **Prometheus Configuration**

```yaml
# /etc/prometheus/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: production

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['localhost:9093']

rule_files:
  - '/etc/prometheus/alert_rules.yml'

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']

  - job_name: 'api-service'
    static_configs:
      - targets: ['localhost:8080/metrics']
    scrape_interval: 10s

  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: 'true'
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
```

### 2. **Node.js Metrics Implementation**

```javascript
// metrics.js
const promClient = require('prom-client');
const register = new promClient.Registry();

promClient.collectDefaultMetrics({ register });

const httpRequestDuration = new promClient.Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.1, 0.5, 1, 2, 5],
  registers: [register]
});

const requestsTotal = new promClient.Counter({
  name: 'requests_total',
  help: 'Total requests',
  labelNames: ['method', 'route', 'status_code'],
  registers: [register]
});

// Express middleware
const express = require('express');
const app = express();

app.get('/metrics', (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(register.metrics());
});

app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    httpRequestDuration
      .labels(req.method, req.path, res.statusCode)
      .observe(duration);
    requestsTotal
      .labels(req.method, req.path, res.statusCode)
      .inc();
  });
  next();
});

module.exports = { register, httpRequestDuration, requestsTotal };
```

### 3. **Python Prometheus Integration**

```python
from prometheus_client import Counter, Histogram, start_http_server
from flask import Flask, request
import time

app = Flask(__name__)

request_count = Counter('requests_total', 'Total requests', ['method', 'endpoint'])
request_duration = Histogram('request_duration_seconds', 'Request duration', ['method', 'endpoint'])

@app.before_request
def before():
    request.start_time = time.time()

@app.after_request
def after(response):
    duration = time.time() - request.start_time
    request_count.labels(request.method, request.path).inc()
    request_duration.labels(request.method, request.path).observe(duration)
    return response

if __name__ == '__main__':
    start_http_server(8000)
    app.run(port=5000)
```

### 4. **Alert Rules**

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

### 5. **Docker Compose Setup**

```yaml
version: '3.8'
services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - ./alert_rules.yml:/etc/prometheus/alert_rules.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=30d'

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"

volumes:
  prometheus_data:
```

## Best Practices

### ✅ DO
- Use consistent metric naming conventions
- Add comprehensive labels for filtering
- Set appropriate scrape intervals (10-60s)
- Implement retention policies
- Monitor Prometheus itself
- Test alert rules before deployment
- Document metric meanings

### ❌ DON'T
- Add unbounded cardinality labels
- Scrape too frequently (< 10s)
- Ignore metric naming conventions
- Create alerts without runbooks
- Store raw event data in Prometheus
- Use counters for gauge-like values

## Key Prometheus Queries

```promql
rate(requests_total[5m])  # Request rate
histogram_quantile(0.95, request_duration_seconds)  # p95 latency
rate(requests_total{status_code=~"5.."}[5m])  # Error rate
```
