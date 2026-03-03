# Grafana API Client

## Grafana API Client

```javascript
// grafana-api-client.js
const axios = require("axios");

class GrafanaClient {
  constructor(baseUrl, apiKey) {
    this.baseUrl = baseUrl;
    this.client = axios.create({
      baseURL: baseUrl,
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
    });
  }

  async createDashboard(dashboard) {
    const response = await this.client.post("/api/dashboards/db", {
      dashboard: dashboard,
      overwrite: true,
    });
    return response.data;
  }

  async getDashboard(uid) {
    const response = await this.client.get(`/api/dashboards/uid/${uid}`);
    return response.data;
  }

  async createAlert(alert) {
    const response = await this.client.post("/api/alerts", alert);
    return response.data;
  }

  async listDashboards() {
    const response = await this.client.get("/api/search?query=");
    return response.data;
  }
}

module.exports = GrafanaClient;
```
