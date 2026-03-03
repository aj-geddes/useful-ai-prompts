# Burp Suite Automation Script

## Burp Suite Automation Script

```javascript
// burp-automation.js - Node.js Burp Suite integration
const axios = require("axios");
const fs = require("fs").promises;

class BurpSuiteAutomation {
  constructor(burpApiUrl = "http://127.0.0.1:1337") {
    this.apiUrl = burpApiUrl;
    this.taskId = null;
  }

  async startScan(targetUrl) {
    console.log(`Starting Burp scan for ${targetUrl}`);

    const scanConfig = {
      urls: [targetUrl],
      scan_configurations: [
        {
          name: "Crawl and Audit - Lightweight",
          type: "NamedConfiguration",
        },
      ],
    };

    try {
      const response = await axios.post(`${this.apiUrl}/v0.1/scan`, scanConfig);

      this.taskId = response.data.task_id;
      console.log(`Scan started with task ID: ${this.taskId}`);

      return this.taskId;
    } catch (error) {
      console.error("Failed to start scan:", error.message);
      throw error;
    }
  }

  async getScanStatus() {
    if (!this.taskId) {
      throw new Error("No active scan task");
    }

    const response = await axios.get(`${this.apiUrl}/v0.1/scan/${this.taskId}`);

    return {
      taskId: this.taskId,
      status: response.data.scan_status,
      metrics: response.data.scan_metrics,
    };
  }

  async waitForCompletion() {
    console.log("Waiting for scan to complete...");

    while (true) {
      const status = await this.getScanStatus();

      console.log(`Progress: ${status.metrics.crawl_requests_made} requests`);

      if (status.status === "succeeded") {
        console.log("Scan completed successfully");
        break;
      } else if (status.status === "failed") {
        throw new Error("Scan failed");
      }

      await new Promise((resolve) => setTimeout(resolve, 10000));
    }
  }

  async getIssues() {
    if (!this.taskId) {
      throw new Error("No active scan task");
    }

    const response = await axios.get(
      `${this.apiUrl}/v0.1/scan/${this.taskId}/issues`,
    );

    return response.data.issues;
  }

  async generateReport() {
    const issues = await this.getIssues();

    const report = {
      summary: {
        high: 0,
        medium: 0,
        low: 0,
        info: 0,
      },
      issues: [],
    };

    for (const issue of issues) {
      report.summary[issue.severity.toLowerCase()]++;

      report.issues.push({
        severity: issue.severity,
        confidence: issue.confidence,
        name: issue.name,
        path: issue.path,
        description: issue.description,
        remediation: issue.remediation,
      });
    }

    await fs.writeFile("burp-report.json", JSON.stringify(report, null, 2));

    return report;
  }
}

// Usage
async function runBurpScan() {
  const burp = new BurpSuiteAutomation();

  await burp.startScan("https://example.com");
  await burp.waitForCompletion();

  const report = await burp.generateReport();

  console.log("\n=== Burp Suite Scan Results ===");
  console.log(`High: ${report.summary.high}`);
  console.log(`Medium: ${report.summary.medium}`);
  console.log(`Low: ${report.summary.low}`);
}

runBurpScan().catch(console.error);
```
