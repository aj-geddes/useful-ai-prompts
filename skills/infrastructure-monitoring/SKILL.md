---
name: infrastructure-monitoring
description: >
  Set up comprehensive infrastructure monitoring with Prometheus, Grafana, and
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

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
