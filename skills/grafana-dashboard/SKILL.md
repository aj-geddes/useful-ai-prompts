---
name: grafana-dashboard
description: >
  Create professional Grafana dashboards with visualizations, templating, and
  alerts. Use when building monitoring dashboards, creating data visualizations,
  or setting up operational insights.
---

# Grafana Dashboard

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Design and implement comprehensive Grafana dashboards with multiple visualization types, variables, and drill-down capabilities for operational monitoring.

## When to Use

- Creating monitoring dashboards
- Building operational insights
- Visualizing time-series data
- Creating drill-down dashboards
- Sharing metrics with stakeholders

## Quick Start

Minimal working example:

```json
{
  "dashboard": {
    "title": "Application Performance",
    "description": "Real-time application metrics",
    "tags": ["production", "performance"],
    "timezone": "UTC",
    "refresh": "30s",
    "templating": {
      "list": [
        {
          "name": "datasource",
          "type": "datasource",
          "datasource": "prometheus"
        },
        {
          "name": "service",
          "type": "query",
          "datasource": "prometheus",
          "query": "label_values(requests_total, service)"
        }
      ]
    },
    "panels": [
      {
        "id": 1,
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Grafana Dashboard JSON](references/grafana-dashboard-json.md) | Grafana Dashboard JSON |
| [Grafana Provisioning Configuration](references/grafana-provisioning-configuration.md) | Grafana Provisioning Configuration |
| [Grafana Alert Configuration](references/grafana-alert-configuration.md) | Grafana Alert Configuration |
| [Grafana API Client](references/grafana-api-client.md) | Grafana API Client |
| [Docker Compose Setup](references/docker-compose-setup.md) | Docker Compose Setup |

## Best Practices

### ✅ DO

- Use meaningful dashboard titles
- Add documentation panels
- Implement row-based organization
- Use variables for flexibility
- Set appropriate refresh intervals
- Include runbook links in alerts
- Test alerts before deploying
- Use consistent color schemes
- Version control dashboard JSON

### ❌ DON'T

- Overload dashboards with too many panels
- Mix different time ranges without justification
- Create without runbooks
- Ignore alert noise
- Use inconsistent metric naming
- Set refresh too frequently
- Forget to configure datasources
- Leave default passwords
