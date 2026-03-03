---
name: alert-management
description: >
  Implement comprehensive alert management with PagerDuty, escalation policies,
  and incident coordination. Use when setting up alerting systems, managing
  on-call schedules, or coordinating incident response.
---

# Alert Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Design and implement sophisticated alert management systems with PagerDuty integration, escalation policies, alert routing, and incident coordination.

## When to Use

- Setting up alert routing
- Managing on-call schedules
- Coordinating incident response
- Creating escalation policies
- Integrating alerting systems

## Quick Start

Minimal working example:

```javascript
// pagerduty-client.js
const axios = require("axios");

class PagerDutyClient {
  constructor(apiToken) {
    this.apiToken = apiToken;
    this.baseUrl = "https://api.pagerduty.com";
    this.eventUrl = "https://events.pagerduty.com/v2/enqueue";

    this.client = axios.create({
      baseURL: this.baseUrl,
      headers: {
        Authorization: `Token token=${apiToken}`,
        Accept: "application/vnd.pagerduty+json;version=2",
      },
    });
  }

  async triggerEvent(config) {
    const event = {
      routing_key: config.routingKey,
      event_action: config.eventAction || "trigger",
      dedup_key: config.dedupKey || `event-${Date.now()}`,
      payload: {
        summary: config.summary,
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [PagerDuty Client Integration](references/pagerduty-client-integration.md) | PagerDuty Client Integration |
| [Alertmanager Configuration](references/alertmanager-configuration.md) | Alertmanager Configuration |
| [Alert Handler Middleware](references/alert-handler-middleware.md) | Alert Handler Middleware |
| [Alert Routing Engine](references/alert-routing-engine.md) | Alert Routing Engine |
| [Docker Compose Alert Stack](references/docker-compose-alert-stack.md) | Docker Compose Alert Stack |

## Best Practices

### ✅ DO

- Set appropriate thresholds
- Implement alert deduplication
- Use clear alert names
- Include runbook links
- Configure escalation properly
- Test alert rules
- Monitor alert quality
- Set repeat intervals
- Track alert metrics
- Document alert meanings

### ❌ DON'T

- Alert on every anomaly
- Ignore alert fatigue
- Set thresholds arbitrarily
- Skip runbooks
- Alert without action
- Disable alerts in production
- Use vague alert names
- Forget escalation policies
- Re-alert too frequently
