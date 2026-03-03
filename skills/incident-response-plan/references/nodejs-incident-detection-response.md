# Node.js Incident Detection & Response

## Node.js Incident Detection & Response

```javascript
// incident-detector.js
const winston = require("winston");
const axios = require("axios");

class IncidentDetector {
  constructor() {
    this.logger = winston.createLogger({
      level: "info",
      format: winston.format.json(),
      transports: [new winston.transports.File({ filename: "incidents.log" })],
    });

    this.thresholds = {
      failedLogins: 5,
      timeWindow: 300000, // 5 minutes
      errorRate: 0.1, // 10%
      responseTime: 5000, // 5 seconds
    };

    this.metrics = {
      failedLogins: new Map(),
      errors: 0,
      requests: 0,
    };
  }

  /**
   * Detect brute force attack
   */
  detectBruteForce(username, ip) {
    const key = `${username}-${ip}`;
    const now = Date.now();

    if (!this.metrics.failedLogins.has(key)) {
      this.metrics.failedLogins.set(key, []);
    }

    const attempts = this.metrics.failedLogins.get(key);
    attempts.push(now);

    // Clean old attempts
    const validAttempts = attempts.filter(
      (time) => now - time < this.thresholds.timeWindow,
    );

    this.metrics.failedLogins.set(key, validAttempts);

    if (validAttempts.length >= this.thresholds.failedLogins) {
      this.createIncident({
        type: "brute_force_attack",
        severity: "high",
        description: `Brute force detected: ${validAttempts.length} failed attempts`,
        source: ip,
        target: username,
        indicators: validAttempts.map((t) => new Date(t).toISOString()),
      });

      return true;
    }

    return false;
  }

  /**
   * Detect anomalous behavior
   */
  detectAnomalies(userId, action, metadata) {
    const anomalies = [];

    // Unusual time access
    const hour = new Date().getHours();
    if (hour < 6 || hour > 22) {
      anomalies.push("Access during unusual hours");
    }

    // Unusual location
    if (metadata.country && metadata.country !== "US") {
      anomalies.push(`Access from unexpected location: ${metadata.country}`);
    }

    // Privilege escalation attempt
    if (action.includes("admin") && !metadata.isAdmin) {
      anomalies.push("Privilege escalation attempt");
    }

    if (anomalies.length > 0) {
      this.createIncident({
        type: "anomalous_behavior",
        severity: "medium",
        description: `Suspicious activity detected for user ${userId}`,
        anomalies,
        userId,
        action,
        metadata,
      });

      return true;
    }

    return false;
  }

  /**
   * Detect data exfiltration
   */
  detectDataExfiltration(userId, downloadSize, filesAccessed) {
    const sizeThreshold = 100 * 1024 * 1024; // 100 MB
    const filesThreshold = 50;

    if (downloadSize > sizeThreshold || filesAccessed > filesThreshold) {
      this.createIncident({
        type: "data_exfiltration",
        severity: "critical",
        description: "Potential data exfiltration detected",
        userId,
        downloadSize: `${(downloadSize / 1024 / 1024).toFixed(2)} MB`,
        filesAccessed,
      });

      return true;
    }

    return false;
  }

  /**
   * Create incident and trigger response
   */
  createIncident(incident) {
    const incidentId = `INC-${Date.now()}`;

    const fullIncident = {
      id: incidentId,
      timestamp: new Date().toISOString(),
      ...incident,
    };

    this.logger.error("Security incident detected", fullIncident);

    // Send to SIEM/monitoring system
    this.sendToSIEM(fullIncident);

    // Trigger automated response
    this.automatedResponse(fullIncident);

    // Send notifications
    this.sendNotifications(fullIncident);

    return incidentId;
  }

  /**
   * Automated incident response
   */
  async automatedResponse(incident) {
    console.log(`\n🚨 Automated response for ${incident.type}`);

    switch (incident.type) {
      case "brute_force_attack":
        // Block IP address
        console.log(`Blocking IP: ${incident.source}`);
        // await this.blockIP(incident.source);
        break;

      case "data_exfiltration":
        // Disable user account
        console.log(`Disabling account: ${incident.userId}`);
        // await this.disableAccount(incident.userId);
        break;

      case "anomalous_behavior":
        // Require MFA
        console.log(`Requiring MFA for: ${incident.userId}`);
        // await this.requireMFA(incident.userId);
        break;
    }
  }

  /**
   * Send to SIEM system
   */
  async sendToSIEM(incident) {
    try {
      await axios.post("https://siem.example.com/api/incidents", incident);
    } catch (error) {
      console.error("Failed to send to SIEM:", error.message);
    }
  }

  /**
   * Send notifications
   */
  async sendNotifications(incident) {
    const webhookUrl = process.env.SLACK_WEBHOOK_URL;

    if (!webhookUrl) return;

    const message = {
      text: `🚨 Security Incident: ${incident.type}`,
      attachments: [
        {
          color: incident.severity === "critical" ? "danger" : "warning",
          fields: [
            { title: "Incident ID", value: incident.id, short: true },
            { title: "Severity", value: incident.severity, short: true },
            { title: "Description", value: incident.description },
          ],
        },
      ],
    };

    try {
      await axios.post(webhookUrl, message);
    } catch (error) {
      console.error("Failed to send notification:", error.message);
    }
  }
}

// Usage
const detector = new IncidentDetector();

// Simulate brute force detection
detector.detectBruteForce("admin", "192.168.1.100");
detector.detectBruteForce("admin", "192.168.1.100");
detector.detectBruteForce("admin", "192.168.1.100");
detector.detectBruteForce("admin", "192.168.1.100");
detector.detectBruteForce("admin", "192.168.1.100");

// Simulate data exfiltration
detector.detectDataExfiltration("user123", 150 * 1024 * 1024, 75);

module.exports = IncidentDetector;
```
