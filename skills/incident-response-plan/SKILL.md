---
name: incident-response-plan
description: Create and execute incident response procedures for security breaches, data leaks, and cyber attacks. Use when handling security incidents, creating response playbooks, or conducting forensic analysis.
---

# Incident Response Plan

## Overview

Structured approach to detecting, responding to, containing, and recovering from security incidents with comprehensive playbooks and automation.

## When to Use

- Security breach detection
- Data breach response
- Malware infection
- DDoS attacks
- Insider threats
- Compliance violations
- Post-incident analysis

## Implementation Examples

### 1. **Incident Response Framework**

```python
# incident_response.py
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
import json

class IncidentSeverity(Enum):
    CRITICAL = "critical"  # P1 - Business critical
    HIGH = "high"          # P2 - Major impact
    MEDIUM = "medium"      # P3 - Moderate impact
    LOW = "low"            # P4 - Minor impact

class IncidentStatus(Enum):
    DETECTED = "detected"
    INVESTIGATING = "investigating"
    CONTAINED = "contained"
    ERADICATED = "eradicated"
    RECOVERED = "recovered"
    CLOSED = "closed"

class IncidentType(Enum):
    DATA_BREACH = "data_breach"
    MALWARE = "malware"
    UNAUTHORIZED_ACCESS = "unauthorized_access"
    DDOS = "ddos_attack"
    PHISHING = "phishing"
    INSIDER_THREAT = "insider_threat"
    SYSTEM_COMPROMISE = "system_compromise"

@dataclass
class IncidentAction:
    timestamp: str
    action: str
    performed_by: str
    result: str

@dataclass
class SecurityIncident:
    incident_id: str
    incident_type: IncidentType
    severity: IncidentSeverity
    status: IncidentStatus
    detected_at: str
    description: str
    affected_systems: List[str] = field(default_factory=list)
    affected_data: List[str] = field(default_factory=list)
    indicators_of_compromise: List[str] = field(default_factory=list)
    actions_taken: List[IncidentAction] = field(default_factory=list)
    assigned_to: str = ""
    resolution: str = ""
    lessons_learned: List[str] = field(default_factory=list)

class IncidentResponseSystem:
    def __init__(self):
        self.incidents: Dict[str, SecurityIncident] = {}
        self.playbooks = self.load_playbooks()

    def load_playbooks(self) -> Dict:
        """Load incident response playbooks"""
        return {
            IncidentType.DATA_BREACH: [
                "Activate incident response team",
                "Isolate affected systems",
                "Preserve evidence for forensics",
                "Identify scope of data exposure",
                "Notify legal and compliance teams",
                "Prepare breach notification",
                "Notify affected parties within 72 hours",
                "Conduct post-incident review"
            ],
            IncidentType.MALWARE: [
                "Isolate infected systems from network",
                "Capture memory dump for analysis",
                "Identify malware type and IoCs",
                "Remove malware from systems",
                "Patch vulnerabilities exploited",
                "Reset credentials",
                "Monitor for persistence mechanisms",
                "Update detection rules"
            ],
            IncidentType.UNAUTHORIZED_ACCESS: [
                "Disable compromised accounts",
                "Review access logs",
                "Identify entry point",
                "Check for lateral movement",
                "Reset all credentials",
                "Enable MFA if not present",
                "Review and update access controls",
                "Monitor for further attempts"
            ],
            IncidentType.DDOS: [
                "Activate DDoS mitigation service",
                "Implement rate limiting",
                "Block attack sources",
                "Scale infrastructure if needed",
                "Contact ISP/hosting provider",
                "Monitor traffic patterns",
                "Prepare incident report",
                "Review DDoS protection strategy"
            ]
        }

    def create_incident(
        self,
        incident_type: IncidentType,
        severity: IncidentSeverity,
        description: str,
        affected_systems: List[str] = None
    ) -> SecurityIncident:
        """Create new security incident"""
        incident_id = f"INC-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

        incident = SecurityIncident(
            incident_id=incident_id,
            incident_type=incident_type,
            severity=severity,
            status=IncidentStatus.DETECTED,
            detected_at=datetime.now().isoformat(),
            description=description,
            affected_systems=affected_systems or []
        )

        self.incidents[incident_id] = incident

        # Auto-assign based on severity
        if severity == IncidentSeverity.CRITICAL:
            incident.assigned_to = "security-team-lead"
        else:
            incident.assigned_to = "security-analyst"

        # Log initial action
        self.add_action(
            incident_id,
            "Incident detected and logged",
            "system",
            f"Incident created with severity: {severity.value}"
        )

        # Send notifications
        self.send_notifications(incident)

        return incident

    def add_action(
        self,
        incident_id: str,
        action: str,
        performed_by: str,
        result: str
    ):
        """Add action to incident timeline"""
        incident = self.incidents.get(incident_id)

        if incident:
            incident.actions_taken.append(IncidentAction(
                timestamp=datetime.now().isoformat(),
                action=action,
                performed_by=performed_by,
                result=result
            ))

    def update_status(
        self,
        incident_id: str,
        new_status: IncidentStatus,
        performed_by: str
    ):
        """Update incident status"""
        incident = self.incidents.get(incident_id)

        if incident:
            old_status = incident.status
            incident.status = new_status

            self.add_action(
                incident_id,
                f"Status changed from {old_status.value} to {new_status.value}",
                performed_by,
                "Status updated successfully"
            )

    def get_playbook(self, incident_id: str) -> List[str]:
        """Get response playbook for incident"""
        incident = self.incidents.get(incident_id)

        if incident:
            return self.playbooks.get(incident.incident_type, [])

        return []

    def send_notifications(self, incident: SecurityIncident):
        """Send incident notifications"""
        notification = {
            'incident_id': incident.incident_id,
            'severity': incident.severity.value,
            'type': incident.incident_type.value,
            'description': incident.description,
            'assigned_to': incident.assigned_to
        }

        # Send to appropriate channels based on severity
        if incident.severity == IncidentSeverity.CRITICAL:
            print(f"🚨 CRITICAL ALERT: {json.dumps(notification, indent=2)}")
            # Send to PagerDuty, SMS, email, Slack
        elif incident.severity == IncidentSeverity.HIGH:
            print(f"⚠️ HIGH PRIORITY: {json.dumps(notification, indent=2)}")
            # Send to email, Slack
        else:
            print(f"ℹ️ Incident logged: {json.dumps(notification, indent=2)}")
            # Log to ticketing system

    def generate_incident_report(self, incident_id: str) -> Dict:
        """Generate comprehensive incident report"""
        incident = self.incidents.get(incident_id)

        if not incident:
            return {}

        duration = None
        if incident.status == IncidentStatus.CLOSED:
            detected = datetime.fromisoformat(incident.detected_at)
            closed = datetime.now()
            duration = str(closed - detected)

        return {
            'incident_id': incident.incident_id,
            'type': incident.incident_type.value,
            'severity': incident.severity.value,
            'status': incident.status.value,
            'detected_at': incident.detected_at,
            'duration': duration,
            'description': incident.description,
            'affected_systems': incident.affected_systems,
            'affected_data': incident.affected_data,
            'indicators_of_compromise': incident.indicators_of_compromise,
            'timeline': [
                {
                    'timestamp': action.timestamp,
                    'action': action.action,
                    'performed_by': action.performed_by,
                    'result': action.result
                }
                for action in incident.actions_taken
            ],
            'resolution': incident.resolution,
            'lessons_learned': incident.lessons_learned,
            'assigned_to': incident.assigned_to
        }

    def export_report(self, incident_id: str, filename: str):
        """Export incident report to file"""
        report = self.generate_incident_report(incident_id)

        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

# Usage
if __name__ == '__main__':
    irs = IncidentResponseSystem()

    # Simulate data breach
    incident = irs.create_incident(
        incident_type=IncidentType.DATA_BREACH,
        severity=IncidentSeverity.CRITICAL,
        description="Unauthorized access to customer database detected",
        affected_systems=["db-prod-01", "api-server-03"]
    )

    print(f"\n=== Incident Created: {incident.incident_id} ===")
    print(f"Type: {incident.incident_type.value}")
    print(f"Severity: {incident.severity.value}")

    # Get playbook
    playbook = irs.get_playbook(incident.incident_id)
    print(f"\n=== Response Playbook ===")
    for i, step in enumerate(playbook, 1):
        print(f"{i}. {step}")

    # Execute response actions
    irs.update_status(
        incident.incident_id,
        IncidentStatus.INVESTIGATING,
        "security-analyst"
    )

    irs.add_action(
        incident.incident_id,
        "Isolated affected database server",
        "security-analyst",
        "Server db-prod-01 isolated from network"
    )

    irs.add_action(
        incident.incident_id,
        "Captured forensic evidence",
        "security-analyst",
        "Memory dump and disk images captured"
    )

    # Generate report
    report = irs.generate_incident_report(incident.incident_id)
    print(f"\n=== Incident Report ===")
    print(json.dumps(report, indent=2))
```

### 2. **Node.js Incident Detection & Response**

```javascript
// incident-detector.js
const winston = require('winston');
const axios = require('axios');

class IncidentDetector {
  constructor() {
    this.logger = winston.createLogger({
      level: 'info',
      format: winston.format.json(),
      transports: [
        new winston.transports.File({ filename: 'incidents.log' })
      ]
    });

    this.thresholds = {
      failedLogins: 5,
      timeWindow: 300000, // 5 minutes
      errorRate: 0.1, // 10%
      responseTime: 5000 // 5 seconds
    };

    this.metrics = {
      failedLogins: new Map(),
      errors: 0,
      requests: 0
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
      time => now - time < this.thresholds.timeWindow
    );

    this.metrics.failedLogins.set(key, validAttempts);

    if (validAttempts.length >= this.thresholds.failedLogins) {
      this.createIncident({
        type: 'brute_force_attack',
        severity: 'high',
        description: `Brute force detected: ${validAttempts.length} failed attempts`,
        source: ip,
        target: username,
        indicators: validAttempts.map(t => new Date(t).toISOString())
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
      anomalies.push('Access during unusual hours');
    }

    // Unusual location
    if (metadata.country && metadata.country !== 'US') {
      anomalies.push(`Access from unexpected location: ${metadata.country}`);
    }

    // Privilege escalation attempt
    if (action.includes('admin') && !metadata.isAdmin) {
      anomalies.push('Privilege escalation attempt');
    }

    if (anomalies.length > 0) {
      this.createIncident({
        type: 'anomalous_behavior',
        severity: 'medium',
        description: `Suspicious activity detected for user ${userId}`,
        anomalies,
        userId,
        action,
        metadata
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
        type: 'data_exfiltration',
        severity: 'critical',
        description: 'Potential data exfiltration detected',
        userId,
        downloadSize: `${(downloadSize / 1024 / 1024).toFixed(2)} MB`,
        filesAccessed
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
      ...incident
    };

    this.logger.error('Security incident detected', fullIncident);

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
      case 'brute_force_attack':
        // Block IP address
        console.log(`Blocking IP: ${incident.source}`);
        // await this.blockIP(incident.source);
        break;

      case 'data_exfiltration':
        // Disable user account
        console.log(`Disabling account: ${incident.userId}`);
        // await this.disableAccount(incident.userId);
        break;

      case 'anomalous_behavior':
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
      await axios.post('https://siem.example.com/api/incidents', incident);
    } catch (error) {
      console.error('Failed to send to SIEM:', error.message);
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
      attachments: [{
        color: incident.severity === 'critical' ? 'danger' : 'warning',
        fields: [
          { title: 'Incident ID', value: incident.id, short: true },
          { title: 'Severity', value: incident.severity, short: true },
          { title: 'Description', value: incident.description }
        ]
      }]
    };

    try {
      await axios.post(webhookUrl, message);
    } catch (error) {
      console.error('Failed to send notification:', error.message);
    }
  }
}

// Usage
const detector = new IncidentDetector();

// Simulate brute force detection
detector.detectBruteForce('admin', '192.168.1.100');
detector.detectBruteForce('admin', '192.168.1.100');
detector.detectBruteForce('admin', '192.168.1.100');
detector.detectBruteForce('admin', '192.168.1.100');
detector.detectBruteForce('admin', '192.168.1.100');

// Simulate data exfiltration
detector.detectDataExfiltration('user123', 150 * 1024 * 1024, 75);

module.exports = IncidentDetector;
```

## Best Practices

### ✅ DO
- Maintain incident response plan
- Define clear escalation paths
- Practice incident drills
- Document all actions
- Preserve evidence
- Communicate transparently
- Conduct post-incident reviews
- Update playbooks regularly

### ❌ DON'T
- Panic or rush
- Delete evidence
- Skip documentation
- Work in isolation
- Ignore lessons learned
- Delay notifications

## Incident Response Phases

1. **Preparation**: Plans, tools, training
2. **Detection**: Identify incidents
3. **Containment**: Stop the spread
4. **Eradication**: Remove threat
5. **Recovery**: Restore systems
6. **Lessons Learned**: Improve

## Key Metrics

- **MTTD**: Mean Time To Detect
- **MTTR**: Mean Time To Respond
- **MTTC**: Mean Time To Contain
- **Impact Assessment**: Data/systems affected
- **Recovery Time**: Time to normal operations

## Resources

- [NIST Incident Response Guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf)
- [SANS Incident Handler's Handbook](https://www.sans.org/reading-room/whitepapers/incident/incident-handlers-handbook-33901)
- [AWS Incident Response](https://aws.amazon.com/security/incident-response/)
