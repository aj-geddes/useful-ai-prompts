---
name: prometheus-monitoring
description: >
  Set up Prometheus monitoring for applications with custom metrics, scraping
  configurations, and service discovery. Use when implementing time-series
  metrics collection, monitoring applications, or building observability
  infrastructure.
---

# Prometheus Monitoring

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive Prometheus monitoring infrastructure for collecting, storing, and querying time-series metrics from applications and infrastructure.

## When to Use

- Setting up metrics collection
- Creating custom application metrics
- Configuring scraping targets
- Implementing service discovery
- Building monitoring infrastructure

## Quick Start

Minimal working example:

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
        - targets: ["localhost:9093"]

rule_files:
  - "/etc/prometheus/alert_rules.yml"

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "node"
    static_configs:
      - targets: ["localhost:9100"]

  - job_name: "api-service"
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Prometheus Configuration](references/prometheus-configuration.md) | Prometheus Configuration |
| [Node.js Metrics Implementation](references/nodejs-metrics-implementation.md) | Node.js Metrics Implementation |
| [Python Prometheus Integration](references/python-prometheus-integration.md) | Python Prometheus Integration |
| [Alert Rules](references/alert-rules.md) | Alert Rules |
| [Docker Compose Setup](references/docker-compose-setup.md) | Docker Compose Setup |

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
