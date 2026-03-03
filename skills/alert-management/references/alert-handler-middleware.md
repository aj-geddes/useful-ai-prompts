# Alert Handler Middleware

## Alert Handler Middleware

```javascript
// alert-handler.js
const PagerDutyClient = require("./pagerduty-client");

const pdClient = new PagerDutyClient(process.env.PAGERDUTY_API_TOKEN);

class AlertHandler {
  constructor() {
    this.alertCache = new Map();
    this.deduplicationWindow = 300000; // 5 minutes
  }

  shouldSendAlert(dedupKey) {
    const cacheEntry = this.alertCache.get(dedupKey);

    if (!cacheEntry) return true;

    const timeSinceLastAlert = Date.now() - cacheEntry.timestamp;
    return timeSinceLastAlert >= this.deduplicationWindow;
  }

  recordAlert(dedupKey) {
    this.alertCache.set(dedupKey, { timestamp: Date.now() });
  }

  determineSeverity(value, thresholds) {
    if (value >= thresholds.critical) return "critical";
    if (value >= thresholds.warning) return "warning";
    return "info";
  }

  async sendAlert(config) {
    const dedupKey =
      config.dedupKey || `alert-${config.alertName}-${Date.now()}`;

    try {
      if (!this.shouldSendAlert(dedupKey)) {
        console.log("Alert recently sent, skipping");
        return;
      }

      const event = {
        routingKey: config.routingKey,
        eventAction: config.eventAction || "trigger",
        dedupKey: dedupKey,
        summary: config.summary,
        severity: config.severity,
        source: config.source || "Monitoring System",
        component: config.component,
        customDetails: {
          ...config.customDetails,
          alertName: config.alertName,
          timestamp: new Date().toISOString(),
        },
      };

      const result = await pdClient.triggerEvent(event);
      this.recordAlert(dedupKey);

      console.log("Alert sent", {
        alertName: config.alertName,
        severity: config.severity,
      });

      return result;
    } catch (error) {
      console.error("Failed to send alert:", error);
      await this.sendSlackAlert(config);
    }
  }

  async sendSlackAlert(config) {
    const axios = require("axios");
    const webhookUrl = process.env.SLACK_WEBHOOK_URL;

    const message = {
      color: config.severity === "critical" ? "danger" : "warning",
      title: config.summary,
      text: config.customDetails?.description || "",
      fields: [
        { title: "Severity", value: config.severity, short: true },
        { title: "Component", value: config.component, short: true },
      ],
    };

    try {
      await axios.post(webhookUrl, { attachments: [message] });
    } catch (error) {
      console.error("Failed to send Slack alert:", error);
    }
  }

  async resolveAlert(dedupKey) {
    try {
      await pdClient.resolveEvent(dedupKey);
      console.log("Alert resolved");
    } catch (error) {
      console.error("Failed to resolve alert:", error);
    }
  }
}

module.exports = new AlertHandler();
```
