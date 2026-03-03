# Uptime Monitor with Heartbeat

## Uptime Monitor with Heartbeat

```javascript
// heartbeat.js
const axios = require("axios");

class UptimeMonitor {
  constructor(config = {}) {
    this.checkInterval = config.checkInterval || 60000;
    this.timeout = config.timeout || 5000;
    this.endpoints = config.endpoints || [];
  }

  async checkEndpoint(endpoint) {
    const startTime = Date.now();

    try {
      const response = await axios.get(endpoint.url, {
        timeout: this.timeout,
        validateStatus: (s) => s >= 200 && s < 300,
      });

      const check = {
        endpoint: endpoint.name,
        status: "up",
        responseTime: Date.now() - startTime,
        timestamp: new Date(),
      };

      await this.saveCheck(check);
      return check;
    } catch (error) {
      const check = {
        endpoint: endpoint.name,
        status: "down",
        responseTime: Date.now() - startTime,
        timestamp: new Date(),
        error: error.message,
      };

      await this.saveCheck(check);
      return check;
    }
  }

  async saveCheck(check) {
    try {
      await db.query(
        "INSERT INTO uptime_checks (endpoint, status, response_time, timestamp) VALUES (?, ?, ?, ?)",
        [check.endpoint, check.status, check.responseTime, check.timestamp],
      );
    } catch (error) {
      console.error("Failed to save check:", error);
    }
  }

  async runChecks() {
    return Promise.all(this.endpoints.map((e) => this.checkEndpoint(e)));
  }

  start() {
    this.runChecks();
    this.interval = setInterval(() => this.runChecks(), this.checkInterval);
  }

  stop() {
    if (this.interval) clearInterval(this.interval);
  }

  async getStats(endpoint, hours = 24) {
    const [stats] = await db.query(
      `
      SELECT
        COUNT(*) as total_checks,
        SUM(CASE WHEN status = 'up' THEN 1 ELSE 0 END) as uptime_checks,
        AVG(response_time) as avg_response_time
      FROM uptime_checks
      WHERE endpoint = ? AND timestamp > DATE_SUB(NOW(), INTERVAL ? HOUR)
    `,
      [endpoint, hours],
    );
    return stats[0];
  }
}

module.exports = UptimeMonitor;
```
