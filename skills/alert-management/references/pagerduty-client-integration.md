# PagerDuty Client Integration

## PagerDuty Client Integration

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
        timestamp: new Date().toISOString(),
        severity: config.severity || "error",
        source: config.source || "Monitoring System",
        component: config.component,
        custom_details: config.customDetails || {},
      },
    };

    try {
      const response = await axios.post(this.eventUrl, event);
      return response.data;
    } catch (error) {
      console.error("Failed to trigger PagerDuty event:", error);
      throw error;
    }
  }

  async resolveEvent(dedupKey) {
    const event = {
      routing_key: process.env.PAGERDUTY_ROUTING_KEY,
      event_action: "resolve",
      dedup_key: dedupKey,
    };

    try {
      return await axios.post(this.eventUrl, event);
    } catch (error) {
      console.error("Failed to resolve event:", error);
      throw error;
    }
  }

  async getServices() {
    const response = await this.client.get("/services");
    return response.data.services;
  }

  async getEscalationPolicies() {
    const response = await this.client.get("/escalation_policies");
    return response.data.escalation_policies;
  }

  async createIncident(config) {
    const incident = {
      type: "incident",
      title: config.title,
      service: {
        id: config.serviceId,
        type: "service_reference",
      },
      escalation_policy: {
        id: config.escalationPolicyId,
        type: "escalation_policy_reference",
      },
      body: {
        type: "incident_body",
        details: config.details || "",
      },
    };

    try {
      const response = await this.client.post("/incidents", incident, {
        headers: { From: process.env.PAGERDUTY_EMAIL },
      });
      return response.data.incident;
    } catch (error) {
      console.error("Failed to create incident:", error);
      throw error;
    }
  }

  async acknowledgeIncident(incidentId, userId) {
    try {
      const response = await this.client.put(
        `/incidents/${incidentId}`,
        {
          incidents: [
            {
              id: incidentId,
              type: "incident_reference",
              status: "acknowledged",
            },
          ],
        },
        { headers: { From: process.env.PAGERDUTY_EMAIL } },
      );
      return response.data.incidents[0];
    } catch (error) {
      console.error("Failed to acknowledge:", error);
      throw error;
    }
  }

  async resolveIncident(incidentId) {
    try {
      const response = await this.client.put(
        `/incidents/${incidentId}`,
        {
          incidents: [
            {
              id: incidentId,
              type: "incident_reference",
              status: "resolved",
            },
          ],
        },
        { headers: { From: process.env.PAGERDUTY_EMAIL } },
      );
      return response.data.incidents[0];
    } catch (error) {
      console.error("Failed to resolve:", error);
      throw error;
    }
  }
}

module.exports = PagerDutyClient;
```
