---
name: infrastructure-monitoring
description: >
  Set up comprehensive infrastructure monitoring with Prometheus, Grafana, and.
  Use when real-time performance monitoring, capacity planning and trends, incident detection and alerting, or service health tracking.
  alerting systems for metrics, health checks, and performance tracking.
---

# Infrastructure Monitoring

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Prometheus Configuration](references/prometheus-configuration.md) | Prometheus Configuration |
| [Alert Rules](references/alert-rules.md) | Alert Rules |
| [Alertmanager Configuration](references/alertmanager-configuration.md) | Alertmanager Configuration |
| [Grafana Dashboard](references/grafana-dashboard.md) | Grafana Dashboard |
| [Monitoring Deployment](references/monitoring-deployment.md) | Monitoring Deployment |

## Best Practices

### ✅ DO

- Define alerts on symptoms (error rate, latency, saturation) rather than causes — let dashboards show the cause
- Use the USE method (Utilization, Saturation, Errors) for infrastructure and RED method (Rate, Errors, Duration) for services
- Set retention policies that balance cost with the need for historical trend analysis and capacity planning
- Include runbook links in every alert so on-call responders know the immediate next steps
- Monitor the monitoring stack itself — a silent alerting pipeline is worse than no alerting at all
- Label metrics consistently with service, environment, and instance dimensions for easy filtering

### ❌ DON'T

- Alert on every metric threshold — this creates alert fatigue and trains teams to ignore pages
- Set static thresholds without accounting for normal variance (use anomaly detection or dynamic thresholds where possible)
- Rely solely on pull-based scraping for ephemeral workloads — use push gateways or service mesh telemetry for short-lived jobs
- Store high-cardinality labels (user IDs, request IDs) in Prometheus metrics — use logs or traces for that data
