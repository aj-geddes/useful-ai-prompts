# Scheduled Synthetic Monitoring

## Scheduled Synthetic Monitoring

```javascript
// scheduled-monitor.js
const cron = require("node-cron");
const SyntheticMonitor = require("./synthetic-tests");
const APISyntheticTests = require("./api-synthetic-tests");
const axios = require("axios");

class ScheduledSyntheticMonitor {
  constructor(config = {}) {
    this.eMonitor = new SyntheticMonitor(config);
    this.apiTests = new APISyntheticTests(config);
    this.alertThreshold = config.alertThreshold || 5000;
  }

  start() {
    cron.schedule("*/5 * * * *", () => this.runE2ETests());
    cron.schedule("*/2 * * * *", () => this.runAPITests());
    cron.schedule("0 * * * *", () => this.runLoadTest());
  }

  async runE2ETests() {
    try {
      const metrics = await this.eMonitor.testUserFlow();
      await this.recordResults("e2e-user-flow", metrics);

      if (metrics.totalTime > this.alertThreshold) {
        await this.sendAlert("e2e-user-flow", metrics);
      }
    } catch (error) {
      console.error("E2E test failed:", error);
    }
  }

  async runAPITests() {
    try {
      const authMetrics = await this.apiTests.testAuthenticationFlow();
      const transactionMetrics = await this.apiTests.testTransactionFlow();

      await this.recordResults("api-auth-flow", authMetrics);
      await this.recordResults("api-transaction-flow", transactionMetrics);

      if (
        authMetrics.status === "failed" ||
        transactionMetrics.status === "failed"
      ) {
        await this.sendAlert("api-tests", { authMetrics, transactionMetrics });
      }
    } catch (error) {
      console.error("API test failed:", error);
    }
  }

  async runLoadTest() {
    try {
      const results = await this.apiTests.testUnderLoad(10, 30000);
      await this.recordResults("load-test", results);

      if (results.failedRequests > 0) {
        await this.sendAlert("load-test", results);
      }
    } catch (error) {
      console.error("Load test failed:", error);
    }
  }

  async recordResults(testName, metrics) {
    try {
      await axios.post("http://monitoring-service/synthetic-results", {
        testName,
        timestamp: new Date(),
        metrics,
      });
      console.log(`Recorded: ${testName}`, metrics);
    } catch (error) {
      console.error("Failed to record results:", error);
    }
  }

  async sendAlert(testName, metrics) {
    try {
      await axios.post("http://alerting-service/alerts", {
        type: "synthetic_monitoring",
        testName,
        severity: "warning",
        message: `Synthetic test '${testName}' has issues`,
        metrics,
        timestamp: new Date(),
      });
      console.log(`Alert sent for ${testName}`);
    } catch (error) {
      console.error("Failed to send alert:", error);
    }
  }
}

module.exports = ScheduledSyntheticMonitor;
```
