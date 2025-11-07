---
name: security-compliance-audit
description: Conduct comprehensive security compliance audits for SOC 2, GDPR, HIPAA, PCI-DSS, and ISO 27001. Use when preparing for certification, annual audits, or compliance validation.
---

# Security Compliance Audit

## Overview

Systematic evaluation of security controls, policies, and procedures to ensure compliance with industry standards and regulatory requirements.

## When to Use

- Annual compliance audits
- Pre-certification assessments
- Regulatory compliance validation
- Security posture evaluation
- Third-party audits
- Gap analysis

## Implementation Examples

### 1. **Automated Compliance Checker**

```python
# compliance_auditor.py
from dataclasses import dataclass, field
from typing import List, Dict
from enum import Enum
import json
from datetime import datetime

class ComplianceFramework(Enum):
    SOC2 = "SOC 2"
    GDPR = "GDPR"
    HIPAA = "HIPAA"
    PCI_DSS = "PCI-DSS"
    ISO_27001 = "ISO 27001"

class ControlStatus(Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NOT_APPLICABLE = "not_applicable"

@dataclass
class Control:
    control_id: str
    framework: ComplianceFramework
    category: str
    description: str
    requirement: str
    status: ControlStatus
    evidence: List[str] = field(default_factory=list)
    findings: List[str] = field(default_factory=list)
    remediation: str = ""
    owner: str = ""
    due_date: str = ""

class ComplianceAuditor:
    def __init__(self, framework: ComplianceFramework):
        self.framework = framework
        self.controls: List[Control] = []
        self.load_controls()

    def load_controls(self):
        """Load compliance controls for the framework"""
        if self.framework == ComplianceFramework.SOC2:
            self.load_soc2_controls()
        elif self.framework == ComplianceFramework.GDPR:
            self.load_gdpr_controls()
        elif self.framework == ComplianceFramework.HIPAA:
            self.load_hipaa_controls()
        elif self.framework == ComplianceFramework.PCI_DSS:
            self.load_pci_dss_controls()

    def load_soc2_controls(self):
        """Load SOC 2 Trust Service Criteria"""
        soc2_controls = [
            {
                'control_id': 'CC6.1',
                'category': 'Logical and Physical Access Controls',
                'description': 'Restrict logical access',
                'requirement': 'Implement authentication and authorization mechanisms'
            },
            {
                'control_id': 'CC6.2',
                'category': 'Logical and Physical Access Controls',
                'description': 'Use encryption',
                'requirement': 'Encrypt data in transit and at rest'
            },
            {
                'control_id': 'CC6.6',
                'category': 'Logical and Physical Access Controls',
                'description': 'Restrict physical access',
                'requirement': 'Implement physical access controls'
            },
            {
                'control_id': 'CC7.2',
                'category': 'System Monitoring',
                'description': 'Detect security incidents',
                'requirement': 'Implement monitoring and alerting'
            },
            {
                'control_id': 'CC7.3',
                'category': 'System Monitoring',
                'description': 'Evaluate security events',
                'requirement': 'Review and analyze security logs'
            }
        ]

        for ctrl in soc2_controls:
            self.controls.append(Control(
                control_id=ctrl['control_id'],
                framework=self.framework,
                category=ctrl['category'],
                description=ctrl['description'],
                requirement=ctrl['requirement'],
                status=ControlStatus.NOT_APPLICABLE
            ))

    def load_gdpr_controls(self):
        """Load GDPR requirements"""
        gdpr_controls = [
            {
                'control_id': 'Art.5',
                'category': 'Data Processing Principles',
                'description': 'Lawfulness, fairness, and transparency',
                'requirement': 'Process data lawfully, fairly, and transparently'
            },
            {
                'control_id': 'Art.15',
                'category': 'Data Subject Rights',
                'description': 'Right of access',
                'requirement': 'Provide data subject access to their data'
            },
            {
                'control_id': 'Art.17',
                'category': 'Data Subject Rights',
                'description': 'Right to erasure',
                'requirement': 'Implement data deletion capabilities'
            },
            {
                'control_id': 'Art.25',
                'category': 'Data Protection by Design',
                'description': 'Privacy by design and default',
                'requirement': 'Implement privacy from the start'
            },
            {
                'control_id': 'Art.32',
                'category': 'Security of Processing',
                'description': 'Security measures',
                'requirement': 'Implement appropriate technical and organizational measures'
            },
            {
                'control_id': 'Art.33',
                'category': 'Data Breach',
                'description': 'Breach notification',
                'requirement': 'Notify breaches within 72 hours'
            }
        ]

        for ctrl in gdpr_controls:
            self.controls.append(Control(
                control_id=ctrl['control_id'],
                framework=self.framework,
                category=ctrl['category'],
                description=ctrl['description'],
                requirement=ctrl['requirement'],
                status=ControlStatus.NOT_APPLICABLE
            ))

    def load_pci_dss_controls(self):
        """Load PCI-DSS requirements"""
        pci_controls = [
            {
                'control_id': '1.1',
                'category': 'Build and Maintain Secure Network',
                'description': 'Firewall configuration standards',
                'requirement': 'Install and maintain firewall configuration'
            },
            {
                'control_id': '3.4',
                'category': 'Protect Cardholder Data',
                'description': 'Render PAN unreadable',
                'requirement': 'Encrypt cardholder data'
            },
            {
                'control_id': '6.5',
                'category': 'Maintain Vulnerability Management',
                'description': 'Address common vulnerabilities',
                'requirement': 'Protect against OWASP Top 10'
            },
            {
                'control_id': '8.2',
                'category': 'Implement Strong Access Control',
                'description': 'Multi-factor authentication',
                'requirement': 'Implement MFA for all users'
            },
            {
                'control_id': '10.2',
                'category': 'Regularly Monitor and Test Networks',
                'description': 'Audit trails',
                'requirement': 'Implement audit logging for all access'
            }
        ]

        for ctrl in pci_controls:
            self.controls.append(Control(
                control_id=ctrl['control_id'],
                framework=self.framework,
                category=ctrl['category'],
                description=ctrl['description'],
                requirement=ctrl['requirement'],
                status=ControlStatus.NOT_APPLICABLE
            ))

    def load_hipaa_controls(self):
        """Load HIPAA requirements"""
        hipaa_controls = [
            {
                'control_id': '164.308(a)(1)',
                'category': 'Administrative Safeguards',
                'description': 'Security management process',
                'requirement': 'Implement security management procedures'
            },
            {
                'control_id': '164.312(a)(1)',
                'category': 'Technical Safeguards',
                'description': 'Access control',
                'requirement': 'Implement unique user identification'
            },
            {
                'control_id': '164.312(a)(2)(iv)',
                'category': 'Technical Safeguards',
                'description': 'Encryption',
                'requirement': 'Encrypt ePHI at rest and in transit'
            },
            {
                'control_id': '164.312(b)',
                'category': 'Technical Safeguards',
                'description': 'Audit controls',
                'requirement': 'Implement audit logging mechanisms'
            },
            {
                'control_id': '164.308(a)(6)',
                'category': 'Administrative Safeguards',
                'description': 'Incident response',
                'requirement': 'Implement security incident procedures'
            }
        ]

        for ctrl in hipaa_controls:
            self.controls.append(Control(
                control_id=ctrl['control_id'],
                framework=self.framework,
                category=ctrl['category'],
                description=ctrl['description'],
                requirement=ctrl['requirement'],
                status=ControlStatus.NOT_APPLICABLE
            ))

    def assess_control(self, control_id: str, status: ControlStatus,
                      evidence: List[str] = None, findings: List[str] = None,
                      remediation: str = "", owner: str = "", due_date: str = ""):
        """Assess a specific control"""
        for control in self.controls:
            if control.control_id == control_id:
                control.status = status
                control.evidence = evidence or []
                control.findings = findings or []
                control.remediation = remediation
                control.owner = owner
                control.due_date = due_date
                break

    def generate_report(self) -> Dict:
        """Generate compliance audit report"""
        summary = {
            'compliant': 0,
            'non_compliant': 0,
            'partially_compliant': 0,
            'not_applicable': 0
        }

        categories = {}

        for control in self.controls:
            # Update summary
            summary[control.status.value] += 1

            # Group by category
            if control.category not in categories:
                categories[control.category] = {
                    'controls': [],
                    'compliant': 0,
                    'non_compliant': 0
                }

            categories[control.category]['controls'].append({
                'control_id': control.control_id,
                'description': control.description,
                'status': control.status.value,
                'findings': control.findings,
                'remediation': control.remediation
            })

            if control.status == ControlStatus.COMPLIANT:
                categories[control.category]['compliant'] += 1
            elif control.status == ControlStatus.NON_COMPLIANT:
                categories[control.category]['non_compliant'] += 1

        total_assessed = len([c for c in self.controls if c.status != ControlStatus.NOT_APPLICABLE])
        compliance_rate = (summary['compliant'] / total_assessed * 100) if total_assessed > 0 else 0

        return {
            'framework': self.framework.value,
            'timestamp': datetime.now().isoformat(),
            'summary': summary,
            'compliance_rate': f"{compliance_rate:.2f}%",
            'categories': categories,
            'action_items': self.get_action_items()
        }

    def get_action_items(self) -> List[Dict]:
        """Get prioritized action items"""
        action_items = []

        for control in self.controls:
            if control.status in [ControlStatus.NON_COMPLIANT, ControlStatus.PARTIALLY_COMPLIANT]:
                action_items.append({
                    'control_id': control.control_id,
                    'category': control.category,
                    'description': control.description,
                    'status': control.status.value,
                    'findings': control.findings,
                    'remediation': control.remediation,
                    'owner': control.owner,
                    'due_date': control.due_date
                })

        return sorted(action_items, key=lambda x: x['status'] == 'non_compliant', reverse=True)

    def export_report(self, filename: str):
        """Export report to JSON"""
        report = self.generate_report()

        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"Report exported to {filename}")

# Usage
if __name__ == '__main__':
    # SOC 2 Audit
    auditor = ComplianceAuditor(ComplianceFramework.SOC2)

    # Assess controls
    auditor.assess_control(
        'CC6.1',
        ControlStatus.COMPLIANT,
        evidence=['MFA enabled', 'RBAC implemented'],
        findings=[]
    )

    auditor.assess_control(
        'CC6.2',
        ControlStatus.PARTIALLY_COMPLIANT,
        evidence=['TLS enabled'],
        findings=['Data at rest not encrypted'],
        remediation='Implement database encryption',
        owner='Security Team',
        due_date='2024-03-31'
    )

    auditor.assess_control(
        'CC7.2',
        ControlStatus.NON_COMPLIANT,
        findings=['No security monitoring in place'],
        remediation='Implement SIEM solution',
        owner='Infrastructure Team',
        due_date='2024-02-28'
    )

    # Generate report
    report = auditor.generate_report()

    print(f"\n=== {report['framework']} Compliance Audit ===")
    print(f"Compliance Rate: {report['compliance_rate']}")
    print(f"\nSummary:")
    print(f"  Compliant: {report['summary']['compliant']}")
    print(f"  Non-Compliant: {report['summary']['non_compliant']}")
    print(f"  Partially Compliant: {report['summary']['partially_compliant']}")

    print(f"\nAction Items: {len(report['action_items'])}")
    for item in report['action_items'][:5]:
        print(f"  - {item['control_id']}: {item['description']}")

    # Export
    auditor.export_report('compliance-audit-report.json')
```

### 2. **Node.js Compliance Automation**

```javascript
// compliance-automation.js
const axios = require('axios');
const fs = require('fs').promises;

class ComplianceAutomation {
  constructor() {
    this.checks = [];
  }

  // Check encryption at rest
  async checkEncryptionAtRest() {
    console.log('Checking encryption at rest...');

    const findings = [];

    // Check database encryption
    // Implementation would connect to actual database
    const dbEncrypted = false;

    if (!dbEncrypted) {
      findings.push('Database encryption not enabled');
    }

    return {
      control: 'Encryption at Rest',
      compliant: findings.length === 0,
      findings
    };
  }

  // Check encryption in transit
  async checkEncryptionInTransit() {
    console.log('Checking encryption in transit...');

    const findings = [];
    const endpoints = ['https://api.example.com'];

    for (const endpoint of endpoints) {
      try {
        const response = await axios.get(endpoint, {
          httpsAgent: new (require('https')).Agent({
            rejectUnauthorized: true,
            minVersion: 'TLSv1.2'
          })
        });

        // Check TLS version and cipher
        const tls = response.request.socket.getProtocol();
        const cipher = response.request.socket.getCipher();

        if (!tls.includes('TLSv1.2') && !tls.includes('TLSv1.3')) {
          findings.push(`Weak TLS version: ${tls}`);
        }

        if (cipher.name.includes('DES') || cipher.name.includes('RC4')) {
          findings.push(`Weak cipher: ${cipher.name}`);
        }
      } catch (error) {
        findings.push(`TLS check failed: ${error.message}`);
      }
    }

    return {
      control: 'Encryption in Transit',
      compliant: findings.length === 0,
      findings
    };
  }

  // Check access controls
  async checkAccessControls() {
    console.log('Checking access controls...');

    const findings = [];

    // Check MFA
    const mfaEnabled = true; // Check actual MFA status

    if (!mfaEnabled) {
      findings.push('MFA not enabled for all users');
    }

    // Check password policy
    const passwordPolicy = {
      minLength: 12,
      requireUppercase: true,
      requireNumbers: true,
      requireSpecial: true
    };

    if (passwordPolicy.minLength < 12) {
      findings.push('Password minimum length less than 12');
    }

    return {
      control: 'Access Controls',
      compliant: findings.length === 0,
      findings
    };
  }

  // Check audit logging
  async checkAuditLogging() {
    console.log('Checking audit logging...');

    const findings = [];

    // Check log retention
    const logRetentionDays = 90;

    if (logRetentionDays < 90) {
      findings.push('Log retention less than 90 days');
    }

    // Check log events
    const requiredEvents = [
      'authentication',
      'authorization',
      'data_access',
      'configuration_changes'
    ];

    const loggedEvents = ['authentication', 'authorization'];

    const missingEvents = requiredEvents.filter(e => !loggedEvents.includes(e));

    if (missingEvents.length > 0) {
      findings.push(`Missing log events: ${missingEvents.join(', ')}`);
    }

    return {
      control: 'Audit Logging',
      compliant: findings.length === 0,
      findings
    };
  }

  async runAllChecks() {
    this.checks = [
      await this.checkEncryptionAtRest(),
      await this.checkEncryptionInTransit(),
      await this.checkAccessControls(),
      await this.checkAuditLogging()
    ];

    return this.generateReport();
  }

  generateReport() {
    const compliant = this.checks.filter(c => c.compliant).length;
    const nonCompliant = this.checks.length - compliant;
    const complianceRate = (compliant / this.checks.length) * 100;

    return {
      timestamp: new Date().toISOString(),
      summary: {
        total: this.checks.length,
        compliant,
        nonCompliant,
        complianceRate: `${complianceRate.toFixed(2)}%`
      },
      checks: this.checks
    };
  }
}

// Usage
async function main() {
  const automation = new ComplianceAutomation();
  const report = await automation.runAllChecks();

  console.log('\n=== Compliance Report ===');
  console.log(`Compliance Rate: ${report.summary.complianceRate}`);
  console.log(`Compliant: ${report.summary.compliant}/${report.summary.total}`);

  await fs.writeFile('compliance-report.json', JSON.stringify(report, null, 2));
}

main().catch(console.error);
```

## Best Practices

### ✅ DO
- Automate compliance checks
- Document all controls
- Maintain evidence repository
- Conduct regular audits
- Track remediation progress
- Involve stakeholders
- Keep policies updated

### ❌ DON'T
- Skip documentation
- Ignore findings
- Delay remediation
- Cherry-pick controls
- Forget evidence collection

## Compliance Frameworks

- **SOC 2**: Trust Service Criteria
- **GDPR**: Data protection
- **HIPAA**: Healthcare data
- **PCI-DSS**: Payment card data
- **ISO 27001**: Information security
- **NIST**: Cybersecurity framework

## Resources

- [SOC 2 Compliance Guide](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/aicpasoc2report.html)
- [GDPR Official Text](https://gdpr-info.eu/)
- [PCI-DSS Requirements](https://www.pcisecuritystandards.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
