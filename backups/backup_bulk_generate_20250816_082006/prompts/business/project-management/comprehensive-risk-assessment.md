# Comprehensive Risk Assessment

## Metadata

- **Category**: Business/Project-Management
- **Tags**: risk assessment, risk management, project risks, mitigation planning
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: project risk analysis, risk mitigation, contingency planning, risk monitoring
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you identify, analyze, and mitigate project risks through systematic assessment, prioritization, and development of effective response strategies.

## Prompt

```
I'll help you conduct a comprehensive risk assessment to protect your project from potential threats. Let me understand your context:

**Project overview:**
1. What type of project is this?
2. What's the project scope and timeline?
3. What's the budget and resource allocation?
4. Who are the key stakeholders?

**Current status:**
5. What phase is the project in?
6. Any risks already identified?
7. Have you experienced any issues so far?
8. What keeps you up at night about this project?

**Environment and constraints:**
9. What external factors could impact the project?
10. Any regulatory or compliance requirements?
11. What are your organizational constraints?
12. How much risk tolerance do you have?

Based on your answers, I'll provide:

**RISK IDENTIFICATION** - Comprehensive risk discovery
**RISK ANALYSIS** - Probability and impact assessment
**RISK PRIORITIZATION** - Focus on what matters most
**MITIGATION STRATEGIES** - Actionable response plans
**MONITORING FRAMEWORK** - Track and manage risks

Share your project details and let's build a robust risk management plan!
```

## Example Usage

**User Input:**
```
1. Software development - new mobile banking app for retail customers
2. 9-month project, launching nationwide, 50+ features planned
3. $3M budget, team of 20 (developers, designers, QA, PM)
4. Stakeholders: CEO, CFO, Head of Digital, Compliance, IT Security, Marketing

5. Just finished design phase, starting development sprint 1 of 15
6. Identified: tight timeline, security concerns, third-party integration risks
7. Design phase took 2 weeks longer than planned, some scope creep already
8. Integration with legacy core banking system, regulatory approval, user adoption

9. New regulations expected, competitor launching similar app, economic uncertainty
10. Must be PCI-DSS compliant, banking regulations, data privacy laws
11. Limited legacy system documentation, hiring freeze, shared QA resources
12. Low tolerance - banking app must be secure and reliable, reputation critical
```

**Assistant Output:**

Based on your mobile banking app project, here's a comprehensive risk assessment:

## RISK IDENTIFICATION

### Risk Categories Uncovered

**Technical Risks**
1. Legacy system integration complexity
2. API performance/reliability issues  
3. Security vulnerabilities
4. Scalability challenges
5. Third-party service dependencies
6. Data migration errors
7. Platform compatibility (iOS/Android)

**Regulatory & Compliance**
8. PCI-DSS certification delays
9. New regulations mid-project
10. Data privacy violations
11. Audit findings requiring rework
12. Regulatory approval delays

**Resource & Schedule**
13. Developer turnover/knowledge loss
14. QA bottlenecks (shared resources)
15. Continued scope creep
16. Sprint velocity lower than planned
17. Hiring freeze impact

**Business & Market**
18. Competitor first-mover advantage
19. User adoption below targets
20. Economic downturn reducing usage
21. Reputational damage from issues
22. Change in strategic priorities

## RISK ANALYSIS

### Risk Assessment Matrix

```
PROBABILITY →
     High │ 13,15 │ 3,8,16 │ 1,2,11,12 │
          │       │        │           │
   Medium │ 14,19 │ 4,6,17 │ 5,9,18,21 │
          │       │        │           │
      Low │ 20    │ 7,10   │ 22        │
          └───────┴────────┴───────────┘
            Low    Medium    High    
                 ← IMPACT
```

### Top 10 Risks by Score

| Rank | Risk | Probability | Impact | Score | Category |
|------|------|-------------|---------|--------|----------|
| 1 | Legacy integration complexity | High | High | 25 | Technical |
| 2 | Security vulnerabilities | High | High | 25 | Technical |
| 3 | Regulatory approval delays | High | High | 25 | Compliance |
| 4 | Scope creep continuation | High | Medium | 20 | Schedule |
| 5 | Sprint velocity issues | High | Medium | 20 | Schedule |
| 6 | QA bottlenecks | Medium | High | 20 | Resource |
| 7 | PCI-DSS delays | Medium | High | 20 | Compliance |
| 8 | Third-party dependencies | Medium | High | 20 | Technical |
| 9 | Developer turnover | Medium | Medium | 16 | Resource |
| 10 | User adoption | Medium | Medium | 16 | Business |

## RISK PRIORITIZATION

### Critical Risks (Immediate Action Required)

**1. Legacy System Integration**
- **Impact**: Could delay project 2-3 months
- **Warning Signs**: API documentation gaps, performance issues in testing
- **Owner**: Tech Lead

**2. Security Vulnerabilities**
- **Impact**: Regulatory fines, reputational damage, launch delays
- **Warning Signs**: Failed penetration tests, OWASP violations
- **Owner**: Security Architect

**3. Regulatory Approval**
- **Impact**: Cannot launch without approval, 1-2 month delays possible
- **Warning Signs**: Compliance feedback, audit findings
- **Owner**: Compliance Officer

## MITIGATION STRATEGIES

### Risk Response Plans

**RISK 1: Legacy System Integration**

*Mitigation Strategy*:
```
Immediate Actions:
1. Dedicated integration team (2 senior devs)
2. Create detailed API mapping document
3. Build abstraction layer for flexibility
4. Daily integration testing from Sprint 2

Contingency Plan:
- Pre-approved budget for legacy system expert consultant
- Parallel development of mock services
- Phased rollout option (core features first)
```

**RISK 2: Security Vulnerabilities**

*Mitigation Strategy*:
```
Preventive Measures:
1. Security-first development training (Week 1)
2. Automated security scanning in CI/CD
3. Weekly security reviews
4. External penetration testing (Sprints 5, 10, 14)

Response Plan:
- Pre-negotiated security consultant on standby
- Security incident response team identified
- 48-hour fix SLA for critical vulnerabilities
```

**RISK 3: Regulatory Approval Delays**

*Mitigation Strategy*:
```
Proactive Approach:
1. Early engagement with regulators (next week)
2. Monthly compliance checkpoints
3. Regulatory liaison dedicated 50%
4. Pre-submission reviews at Sprints 5, 10

Acceleration Options:
- Fast-track application process ($50K fee)
- Phased approval for core features
- Third-party compliance accelerator
```

### Additional Risk Responses

**Scope Creep**:
- Change control board (meets weekly)
- Feature freeze after Sprint 5
- MVP clearly defined and protected
- Trade-off discussions documented

**Resource Constraints**:
- Cross-training program starting now
- Contractor budget pre-approved
- Staggered sprint endings to share QA
- Knowledge management system

## MONITORING FRAMEWORK

### Risk Dashboard

**Weekly Risk Review Metrics**:
```
Risk Health Indicators:
├── Integration Test Pass Rate: >90% (Current: N/A)
├── Security Scan Issues: <5 Critical (Current: N/A)
├── Sprint Velocity: 40 points ±10% (Current: N/A)
├── Compliance Checklist: >95% (Current: 78%)
├── Budget Variance: <5% (Current: 2%)
└── Schedule Variance: <1 Sprint (Current: 0.5)
```

### Risk Trigger Monitoring

**Automated Alerts**:
1. Integration API response time >2 seconds
2. Security scan finds critical vulnerability
3. Sprint velocity drops below 30 points
4. Any compliance requirement changes
5. Team member resignation
6. Competitor announcement
7. Budget overrun >10%

### Governance Structure

**Risk Review Cadence**:
- Daily: Development team standup (technical risks)
- Weekly: Project team meeting (all risks)
- Bi-weekly: Stakeholder committee (top 10 risks)
- Monthly: Executive briefing (critical risks)

**Risk Register Updates**:
```
For Each Risk:
- Status: (New/Open/Mitigating/Closed)
- Probability: (1-5 scale)
- Impact: (1-5 scale)  
- Mitigation Progress: (0-100%)
- Owner: (Name)
- Last Updated: (Date)
- Next Review: (Date)
```

### Early Warning System

**Sprint 1-3 Checkpoints**:
- [ ] Legacy API performance baseline established
- [ ] Security framework implemented
- [ ] Compliance pre-review completed
- [ ] Team velocity stabilized
- [ ] Scope locked and approved

**Go/No-Go Criteria for Sprint 5**:
- Integration POC successful
- Security scan <10 medium issues
- Compliance pre-approval obtained
- Velocity averaging 35+ points
- Budget on track ±5%

### Contingency Budget

**Risk Reserve Allocation**:
```
Total Budget: $3,000,000
Contingency: $450,000 (15%)

Allocated:
- Technical risks: $200,000
- Compliance: $100,000
- Resources: $100,000
- Unallocated: $50,000
```

### Communication Plan

**Stakeholder Updates**:
- CEO: Monthly executive summary
- CFO: Bi-weekly budget risk report
- Compliance: Weekly regulatory update
- Team: Daily risk visibility in standups
- PMO: Weekly risk register submission

This comprehensive risk management approach will help you navigate challenges while maintaining project momentum. The key is consistent monitoring and proactive mitigation.

## Related Prompts

- [Project Planning Expert](./project-planning-expert.md)
- [Change Management Specialist](./change-management-expert.md)
- [Stakeholder Management Expert](./stakeholder-management-expert.md)