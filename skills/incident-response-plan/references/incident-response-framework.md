# Incident Response Framework

## Incident Response Framework

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
