---
category: planning
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for planning optimization and expert consultation
slug: risk-management-planning-expert
tags:
- planning
title: Risk Management Planning Expert
use_cases:
- planning optimization
- professional workflow enhancement
version: 3.0.0
---

# Risk Management Planning Expert

## Metadata

- **Category**: Planning
- **Tags**: risk management, risk assessment, mitigation planning, contingency planning, enterprise risk
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: enterprise risk management, project risk planning, operational risk assessment, strategic risk mitigation
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical risk management planning assistant that helps you identify, assess, and mitigate risks to protect your organization while enabling strategic objectives. Provide your risk context and I'll develop comprehensive risk frameworks with mitigation strategies, contingency plans, and monitoring systems.

## Prompt

```
I'll help you create a comprehensive risk management plan that protects your organization while enabling strategic growth. Let me gather information about your risk management needs.

About your organization:
1. What type of organization are you? (startup, growing company, enterprise, nonprofit)
2. What industry are you in?
3. What's the scope of risk planning? (project-specific, operational, enterprise-wide)
4. What's your risk tolerance level? (conservative, moderate, aggressive)

Risk context:
5. What are your main business objectives or projects?
6. What risks are you most concerned about? (operational, financial, strategic, compliance)
7. What regulatory requirements do you need to meet?
8. Who are your key stakeholders? (investors, customers, employees, regulators)

Current situation:
9. What risk management processes do you currently have?
10. Have you experienced any significant risks or incidents before?
11. What would be the impact of major disruptions to your business?
12. What resources do you have for risk management?

Based on your answers, I'll create:

**1. RISK ASSESSMENT** - Comprehensive identification and analysis of key risks
**2. MITIGATION STRATEGIES** - Specific actions to reduce risk likelihood and impact
**3. CONTINGENCY PLANS** - Response procedures for when risks materialize
**4. MONITORING FRAMEWORK** - Systems to track and manage risks ongoing
**5. GOVERNANCE STRUCTURE** - Roles, responsibilities, and decision-making processes

Please provide the information above, and I'll design a risk management plan that protects your organization while supporting your strategic objectives.
```

## Example Usage

**User Input:**
```
1. Organization: Growing SaaS company
2. Industry: FinTech - payment processing software
3. Scope: Enterprise-wide risk management
4. Risk tolerance: Moderate - growth-focused but compliance-critical

5. Objectives: Scale to $50M revenue, expand internationally, maintain 99.9% uptime
6. Main concerns: Data breaches, regulatory compliance, operational scaling, competitive pressure
7. Regulatory requirements: PCI DSS, SOC 2, GDPR, various financial regulations
8. Key stakeholders: Investors, enterprise customers, employees, regulators

9. Current processes: Basic security policies, annual audits, incident response plan
10. Past incidents: Minor outage last year (2 hours), failed compliance audit finding resolved
11. Major disruption impact: Customer churn, regulatory penalties, revenue loss, reputation damage
12. Resources: 3-person security team, $500K annual budget, growing compliance team
```

**Assistant Output:**

Based on your FinTech payment processing company, here's your comprehensive risk management plan:

# FINTECH RISK MANAGEMENT PLAN

## 1. RISK ASSESSMENT

### Critical Risk Categories

**Category 1: Data Security & Privacy (Critical Priority)**
- **Data Breach Risk**: Unauthorized access to payment/customer data
- **Impact**: $5-50M in losses, regulatory penalties, customer churn
- **Probability**: Medium (increasing with scale)
- **Current Controls**: Basic security, SOC 2 Type I

**Category 2: Regulatory Compliance (High Priority)**  
- **PCI DSS Non-Compliance**: Payment card industry violations
- **GDPR Violations**: European data privacy breaches
- **Impact**: $1-10M penalties, business operations restrictions
- **Probability**: Medium (complex requirements, changing regulations)
- **Current Controls**: Annual audits, basic compliance tracking

**Category 3: Operational Resilience (High Priority)**
- **Platform Downtime**: Service interruptions affecting customers
- **Scaling Failures**: Cannot handle growth in transaction volume
- **Impact**: $100K per hour downtime, customer SLA violations
- **Probability**: Medium (high growth stress on systems)
- **Current Controls**: Basic monitoring, limited redundancy

**Category 4: Business Continuity (Medium Priority)**
- **Key Person Risk**: Dependence on critical employees
- **Vendor Dependencies**: Third-party service failures
- **Competitive Pressure**: Market share loss to competitors
- **Impact**: Moderate business disruption
- **Probability**: Medium to Low

### Risk Priority Matrix

| Risk | Impact | Probability | Risk Score | Priority |
|------|---------|-------------|------------|----------|
| Major Data Breach | Critical (9) | Medium (6) | 54 | Critical |
| PCI DSS Non-Compliance | High (8) | Medium (5) | 40 | High |
| Platform Downtime | High (7) | Medium (5) | 35 | High |
| GDPR Violations | High (6) | Medium (4) | 24 | Medium |
| Key Person Loss | Medium (5) | Low (3) | 15 | Medium |

## 2. MITIGATION STRATEGIES

### Critical Risk Mitigation

**Data Security Enhancement ($200K investment)**
- **Immediate (0-3 months):**
  - Complete SOC 2 Type II certification
  - Implement multi-factor authentication across all systems
  - Establish Security Operations Center (SOC)
  - Conduct penetration testing quarterly

- **Medium-term (3-12 months):**
  - Deploy advanced threat detection and response
  - Implement zero-trust network architecture
  - Establish data encryption at rest and in transit
  - Create security awareness training program

**Regulatory Compliance Program ($150K investment)**
- **Immediate (0-3 months):**
  - Hire dedicated compliance manager
  - Implement automated compliance monitoring
  - Create compliance dashboard and reporting

- **Medium-term (3-12 months):**
  - Achieve PCI DSS Level 1 certification
  - Implement GDPR compliance program
  - Establish regulatory change monitoring
  - Create compliance training for all employees

**Operational Resilience Building ($250K investment)**
- **Immediate (0-3 months):**
  - Implement comprehensive monitoring and alerting
  - Create redundant infrastructure architecture
  - Establish 24/7 operations center

- **Medium-term (3-12 months):**
  - Build automatic failover capabilities
  - Implement load testing and capacity planning
  - Create detailed runbooks for all critical processes

## 3. CONTINGENCY PLANS

### Data Breach Response Plan
**Phase 1: Immediate Response (0-4 hours)**
- Incident commander activation
- Affected systems isolation
- Initial damage assessment
- Legal and PR team notification

**Phase 2: Investigation & Containment (4-24 hours)**
- Forensic investigation initiation
- Customer and regulatory notification (as required)
- Public communication strategy execution
- Additional security measures deployment

**Phase 3: Recovery & Lessons Learned (1-4 weeks)**
- Systems restoration and monitoring
- Customer support and retention efforts
- Regulatory cooperation and reporting
- Post-incident review and improvement

### Compliance Violation Response
**Immediate Actions:**
- Notify legal counsel and compliance team
- Document violation scope and impact
- Begin remediation efforts
- Prepare regulatory response

**Remediation Process:**
- Root cause analysis and fix implementation
- Process improvements and controls strengthening
- Staff retraining and policy updates
- Regular monitoring and verification

## 4. MONITORING FRAMEWORK

### Key Risk Indicators (KRIs)

**Security Metrics:**
- Security incidents per month (target: <5)
- Mean time to detection (target: <1 hour)
- Phishing test failure rate (target: <5%)
- Vulnerability patching time (target: <48 hours)

**Compliance Metrics:**
- Audit findings (target: 0 critical)
- Compliance training completion (target: 100%)
- Regulatory change implementation time (target: <30 days)
- Customer data requests response time (target: <72 hours)

**Operational Metrics:**
- System uptime (target: 99.9%)
- Transaction processing capacity utilization (alert: >80%)
- Response time for critical transactions (target: <200ms)
- Customer-reported incidents (target: <10/month)

### Monitoring Dashboard
**Daily Monitoring:**
- Security event logs and alerts
- System performance and capacity metrics
- Transaction volume and error rates
- Customer support ticket trends

**Weekly Reviews:**
- Risk indicator trend analysis
- Incident and near-miss review
- Compliance status assessment
- Vendor performance evaluation

**Monthly Reporting:**
- Risk dashboard for executives
- Compliance status report
- Incident summary and trends
- Risk mitigation progress update

## 5. GOVERNANCE STRUCTURE

### Risk Management Team
**Chief Risk Officer**: Overall risk strategy and reporting (hire within 6 months)
**Security Manager**: Cybersecurity and data protection
**Compliance Manager**: Regulatory compliance and auditing
**Operations Manager**: Business continuity and operational resilience

### Risk Committee Structure
**Executive Risk Committee (Monthly):**
- CEO, CTO, COO, Head of Legal
- Strategic risk decisions and resource allocation
- Board reporting and stakeholder communication

**Operational Risk Team (Weekly):**
- Department managers and risk team
- Day-to-day risk monitoring and response
- Incident management and lessons learned

### Decision-Making Framework
**Low Risk Decisions**: Department manager authority
**Medium Risk Decisions**: Risk team approval required
**High Risk Decisions**: Executive committee approval
**Critical Risk Decisions**: Board notification/approval

### Implementation Timeline

**Phase 1 (Months 1-3): Foundation**
- Hire compliance manager
- Complete SOC 2 Type II
- Implement basic monitoring
- Budget: $100K

**Phase 2 (Months 4-6): Enhancement** 
- Establish SOC and advanced security
- Launch compliance program
- Build operational resilience
- Budget: $200K

**Phase 3 (Months 7-12): Optimization**
- Hire Chief Risk Officer
- Advanced threat protection
- International compliance readiness
- Budget: $300K

This risk management plan provides a structured approach to protecting your FinTech business while enabling aggressive growth, with clear priorities, timelines, and success metrics.

## Related Prompts

- [Contingency Planning Expert](./contingency-planning-expert.md)
- [Business Continuity Expert](./business-continuity-expert.md)  
- [Strategic Planning Expert](./strategic-planning-expert.md)

## Usage Instructions

1. Start with comprehensive risk identification across all business areas
2. Conduct quantitative risk assessment with impact and probability analysis
3. Develop targeted mitigation strategies based on risk priority levels
4. Create detailed contingency plans for high-impact scenarios
5. Establish monitoring systems with key risk indicators and dashboards
6. Build governance structure appropriate to organization size and complexity
7. Implement risk management culture through training and awareness
8. Plan for regular reviews and continuous improvement of risk framework

## Examples

### Example 1: Startup Risk Management

**Input**:

```
{{organization_type}}: Early-stage tech startup
{{scope}}: Operational risk management  
{{risk_tolerance}}: Moderate - growth-focused with prudent controls
{{main_concerns}}: Product development delays, funding risks, market competition
{{resources}}: Limited budget, small team, need cost-effective solutions
```

**Output**: [Lean risk management framework focused on critical startup risks with cost-effective mitigation strategies and simple monitoring systems]

### Example 2: Enterprise Risk Management

**Input**:

```
{{organization_type}}: Large corporation  
{{scope}}: Enterprise-wide risk framework
{{risk_tolerance}}: Conservative - heavily regulated industry
{{main_concerns}}: Regulatory compliance, operational disruptions, cybersecurity
{{resources}}: Dedicated risk team, significant budget, complex stakeholder requirements
```

**Output**: [Comprehensive enterprise risk management program with detailed governance, compliance frameworks, and sophisticated monitoring systems]

## Related Prompts

- [Crisis Management Expert](/prompts/problem-solving/crisis-management.md)
- [Business Continuity Expert](/prompts/planning/business-continuity.md)
- [Compliance Management Expert](/prompts/planning/compliance-management.md)

## Research Notes

- Based on ISO 31000, COSO ERM, and NIST risk management frameworks
- Integrates quantitative risk assessment with practical mitigation strategies  
- Emphasizes business-aligned risk management that enables rather than constrains growth
- Focuses on actionable risk controls with clear ownership and accountability
- Balances comprehensive risk coverage with practical implementation considerations
