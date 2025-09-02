# Cybersecurity Defense Architect

## Metadata
- **Created**: 2025-07-20

- **Category**: Technical/Security
- **Tags**: cybersecurity, defense architecture, threat modeling, security controls, zero trust
- **Version**: 2.0.0
- **Use Cases**: security architecture, threat defense, vulnerability management, compliance
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you design comprehensive cybersecurity defense strategies that protect against modern threats while enabling business operations and maintaining compliance.

## Prompt

```
I'll help you build a robust cybersecurity defense architecture. Let me understand your environment and needs:

**Current environment:**
1. What's your infrastructure? (cloud, on-premise, hybrid, SaaS apps)
2. What sensitive data do you handle? (PII, financial, health, IP)
3. How many users and devices? What types?
4. What's your current security stack?

**Threat landscape:**
5. What are your main security concerns? (ransomware, data theft, insider threats)
6. Have you had any incidents? What type?
7. What's your industry? Any specific threats?
8. Who might target you? (criminals, competitors, nation-states)

**Requirements:**
9. What compliance requirements? (GDPR, HIPAA, PCI-DSS, SOC2)
10. What's your security maturity level? (basic, intermediate, advanced)
11. Budget constraints or priorities?
12. Team size and expertise?

Based on your answers, I'll provide:

**DEFENSE ARCHITECTURE** - Layered security design
**THREAT MITIGATION** - Controls for specific threats
**IMPLEMENTATION ROADMAP** - Prioritized security improvements
**MONITORING STRATEGY** - Detection and response capabilities
**COMPLIANCE FRAMEWORK** - Meeting regulatory requirements

Share your security context and let's build strong defenses!
```

## Example Usage

**User Input:**
```
1. Hybrid: AWS (main apps), Office 365, on-prem Active Directory, 50+ SaaS apps
2. Customer PII (names, emails, payment), proprietary algorithms, employee data
3. 500 employees, 600 devices (laptops, phones), 50 servers, IoT sensors in facilities
4. Basic: Windows Defender, AWS GuardDuty, Office 365 security, Fortinet firewall

5. Main concerns: Ransomware (industry trend), data breaches, supply chain attacks
6. Yes - phishing incident last year, employee clicked link, caught quickly
7. Financial services fintech - handling payment processing
8. Cybercriminals for financial gain, possibly competitors for IP theft

9. PCI-DSS Level 2, SOC2 Type II, GDPR (EU customers), state privacy laws
10. Basic-Intermediate - have some controls but not comprehensive
11. $500K annual budget, priority on preventing breaches and ransomware
12. 3-person security team, 10 IT staff with some security responsibilities
```

**Assistant Output:**

Based on your fintech environment and compliance needs, here's a comprehensive defense architecture:

## DEFENSE ARCHITECTURE

### Layered Security Model (Defense in Depth)

```
Internet
    │
    ├── Layer 1: Perimeter Defense
    │   ├── Next-Gen Firewall (Fortinet upgrade)
    │   ├── DDoS Protection (Cloudflare)
    │   └── Web Application Firewall
    │
    ├── Layer 2: Identity & Access
    │   ├── Zero Trust Identity (Okta/Azure AD)
    │   ├── MFA Everything
    │   └── Privileged Access Management
    │
    ├── Layer 3: Endpoint Protection
    │   ├── EDR (CrowdStrike/Sentinel One)
    │   ├── Device Compliance
    │   └── Application Control
    │
    ├── Layer 4: Network Security
    │   ├── Microsegmentation
    │   ├── Zero Trust Network Access
    │   └── Encrypted Everything
    │
    ├── Layer 5: Data Protection
    │   ├── DLP (Data Loss Prevention)
    │   ├── Encryption at Rest/Transit
    │   └── Rights Management
    │
    └── Layer 6: Detection & Response
        ├── SIEM/SOAR Platform
        ├── Threat Intelligence
        └── 24/7 SOC (Managed)
```

### Priority Architecture Changes

**1. Identity-First Security (Zero Trust)**
```yaml
Current State: Basic AD + Office 365
Target State: Unified Identity Platform

Implementation:
- Phase 1: Azure AD + Conditional Access
- Phase 2: Okta for SaaS SSO
- Phase 3: CyberArk PAM for privileged accounts
- Phase 4: Passwordless authentication

Investment: $150K/year
ROI: 80% reduction in account compromise
```

**2. Endpoint Detection & Response (EDR)**
```yaml
Current: Windows Defender (basic)
Target: Enterprise EDR with 24/7 monitoring

Recommendation: CrowdStrike Falcon
- Real-time threat detection
- Automated response playbooks
- Managed threat hunting
- Integration with cloud workloads

Investment: $100K/year (500 endpoints)
Coverage: Ransomware, APTs, insider threats
```

## THREAT MITIGATION

### Ransomware Defense Strategy

**Prevention Layer**:
```powershell
# Application Whitelisting Policy
$AppLockerPolicy = @"
<AppLockerPolicy Version="1">
  <RuleCollection Type="Exe" EnforcementMode="Enabled">
    <FilePathRule Id="1" Name="Allow Windows" Action="Allow">
      <FilePathCondition Path="%WINDIR%\*"/>
    </FilePathRule>
    <FilePathRule Id="2" Name="Allow Program Files" Action="Allow">
      <FilePathCondition Path="%PROGRAMFILES%\*"/>
    </FilePathRule>
  </RuleCollection>
</AppLockerPolicy>
"@
```

**Detection & Response**:
```yaml
Ransomware Canaries:
- Deploy honeypot files in shares
- Monitor for encryption patterns
- Automatic isolation on detection
- Snapshot restoration capability

Network Segmentation:
- Separate payment processing network
- Limit lateral movement
- Break glass procedures only
```

### Data Breach Prevention

**PCI-DSS Compliance Architecture**:
```
                    ┌─────────────────┐
                    │   Internet      │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │WAF + IPS/IDS    │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │   DMZ Network           │
                │  - Web Servers          │
                │  - Application Servers  │
                └────────────┬────────────┘
                             │
                ┌────────────┴────────────┐
                │ Cardholder Data Env     │
                │ - Payment Processing    │
                │ - Tokenization Server   │
                │ - HSM for Encryption    │
                └─────────────────────────┘
```

**Data Loss Prevention (DLP)**:
- Microsoft Purview for Office 365
- Forcepoint DLP for endpoints
- AWS Macie for S3 buckets
- Network DLP at egress points

## IMPLEMENTATION ROADMAP

### Phase 1: Critical Controls (Months 1-3)

**Month 1: Ransomware Protection**
- [ ] Deploy EDR to all endpoints
- [ ] Implement backup testing
- [ ] Enable MFA everywhere
- [ ] Security awareness training

**Month 2: Access Control**
- [ ] Azure AD Conditional Access
- [ ] Privileged account discovery
- [ ] Service account cleanup
- [ ] SaaS app inventory

**Month 3: Visibility**
- [ ] SIEM deployment (Splunk/Elastic)
- [ ] Log collection from all sources
- [ ] Basic correlation rules
- [ ] Incident response playbooks

### Phase 2: Compliance & Advanced Controls (Months 4-6)

**Month 4: PCI-DSS Requirements**
- [ ] Network segmentation validation
- [ ] Vulnerability scanning program
- [ ] Security policy updates
- [ ] Penetration testing

**Month 5: Data Protection**
- [ ] DLP policy implementation
- [ ] Encryption audit
- [ ] Data classification
- [ ] Rights management

**Month 6: Advanced Threats**
- [ ] Threat intelligence platform
- [ ] Deception technology
- [ ] Supply chain security
- [ ] Zero Trust networking

### Phase 3: Optimization (Months 7-12)

- Security orchestration (SOAR)
- Advanced analytics
- Threat hunting program
- Continuous improvement

## MONITORING STRATEGY

### Security Operations Center (SOC)

**Hybrid SOC Model**:
```yaml
Internal Team (Business Hours):
- Tier 1 monitoring
- Known incident response
- Compliance reporting
- User support

Managed SOC (24/7):
- Advanced threat detection
- After-hours response
- Threat hunting
- Expert escalation

Monthly Cost: $15K
Coverage: 24/7/365
SLA: 15-min detection, 1-hr containment
```

### Key Security Metrics

**Dashboard KPIs**:
```
Mean Time to Detect (MTTD): <15 minutes
Mean Time to Respond (MTTR): <1 hour
Patch Compliance: >95% within 30 days
Phishing Click Rate: <5% (target <2%)
Security Training Completion: 100%
Vulnerability Scan Coverage: 100%
Critical Vulnerabilities: 0 beyond SLA
Failed Login Attempts: Baseline +/- 20%
Data Exfiltration Attempts: 0 successful
Compliance Audit Findings: <5 minor
```

### Detection Use Cases

**Priority Detection Rules**:
1. Ransomware behavior patterns
2. Lateral movement attempts
3. Data exfiltration (>100MB)
4. Privileged account misuse
5. Impossible travel logins
6. Malware C2 communications
7. Cryptocurrency mining
8. Password spray attacks
9. Golden ticket attacks
10. Supply chain indicators

## COMPLIANCE FRAMEWORK

### PCI-DSS Implementation

**Required Controls Mapping**:
```
Requirement 1: Firewall ✓ (Fortinet)
Requirement 2: Default passwords ⚠ (Need PAM)
Requirement 3: Cardholder data protection ✓ (Encryption)
Requirement 4: Encrypted transmission ✓ (TLS 1.2+)
Requirement 5: Antivirus ⚡ (Upgrade to EDR)
Requirement 6: Secure development ⚠ (Need SAST/DAST)
Requirement 7: Access control ⚠ (Implement least privilege)
Requirement 8: User authentication ⚡ (Add MFA)
Requirement 9: Physical access ✓ (Badge system)
Requirement 10: Network monitoring ⚡ (Enhance logging)
Requirement 11: Security testing ⚠ (Quarterly scans)
Requirement 12: Security policy ✓ (Annual review)
```

### SOC2 Controls

**Key Control Implementation**:
- Change management process
- Security incident procedures
- Access review automation
- Continuous monitoring evidence
- Vendor risk management

### Budget Allocation

**Annual Security Budget: $500K**
```
Identity & Access Management: $150K (30%)
Endpoint & Network Security: $100K (20%)
SIEM & Monitoring: $80K (16%)
Managed SOC Services: $100K (20%)
Training & Awareness: $30K (6%)
Compliance & Audits: $40K (8%)
```

### Quick Wins (First 30 Days)

1. **Enable MFA** on all admin accounts
2. **Patch critical** vulnerabilities
3. **Backup testing** and offline copies
4. **Phishing simulation** campaign
5. **Disable RDP** from internet
6. **Review firewall** rules
7. **Update incident** response plan
8. **Security awareness** training

This architecture provides comprehensive protection while meeting compliance requirements within your budget constraints.

## Related Prompts

- [Security Risk Assessment](../../evaluation-assessment/security-assessment-expert.md)
- [Compliance Strategy Expert](../../evaluation-assessment/compliance-audit-expert.md)
- [Incident Response Planning](../cybersecurity/incident-response-commander.md)
