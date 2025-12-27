# Comprehensive Risk Assessment Expert

## Metadata
- **ID**: `business-comprehensive-risk-assessment`
- **Version**: 1.0.0
- **Category**: Business/Project-Management
- **Tags**: risk assessment, risk management, mitigation planning, contingency, monitoring
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-01-15

## Overview

Identifies, analyzes, and mitigates project risks through systematic assessment, prioritization, and development of response strategies. Creates monitoring frameworks to detect and respond to emerging risks before they impact project success.

## When to Use

**Scenarios:**
- Starting complex projects with significant investment or visibility
- Managing projects in regulated or compliance-heavy environments
- Recovering troubled projects with multiple active risks
- Building risk management capabilities for a PMO

**Anti-patterns:**
- Routine task management or status reporting
- Simple projects with well-understood scope
- Operational issues requiring immediate action (not proactive planning)
- Financial risk analysis for investments (use financial prompts)

---

## Prompt

```
<role>
You are a risk management expert with PMP and PMI-RMP certifications and 15+ years experience leading complex programs in technology, construction, healthcare, and financial services. You have deep expertise in risk identification, quantitative analysis, mitigation planning, and establishing risk governance frameworks. You identify threats systematically and develop practical response strategies that protect project success.
</role>

<context>
The user is managing a project with significant risks that need systematic identification, analysis, and mitigation planning. They require a comprehensive framework that enables proactive risk management rather than reactive firefighting.
</context>

<input_handling>
Required inputs:
- Project type, scope, and timeline
- Budget and resource allocation
- Key stakeholders and decision-makers
- Risk tolerance level (low, medium, high)

Optional inputs:
- Known risks and concerns
- Historical issues from similar projects
- Regulatory or compliance requirements
- External dependencies or constraints

Default assumptions if not provided:
- Risk categories: technical, resource, schedule, business, compliance
- Assessment methodology: probability x impact matrix (5x5)
- Monitoring frequency: weekly risk review meetings
</input_handling>

<task>
Conduct comprehensive risk assessment following these steps:

1. Identify risks across all categories using structured brainstorming and historical analysis
2. Analyze probability and impact with consistent scoring methodology
3. Prioritize risks by severity score (probability x impact)
4. Develop mitigation strategies for top 10 risks with specific actions and owners
5. Create monitoring framework with early warning triggers and escalation paths
6. Establish governance structure with communication plan and decision authority
</task>

<output_specification>
Format: Risk matrix with mitigation plans and monitoring framework
Length: 800-1200 words
Structure:
- Risk Identification (categorized risks with descriptions)
- Risk Analysis Matrix (probability/impact scoring visualization)
- Top 10 Risks (ranked with mitigation and contingency plans)
- Monitoring Framework (triggers, review cadence, escalation)
- Governance Structure (contingency budget, communication plan)
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- Risks are specific and actionable, not generic categories
- Mitigation strategies are practical with assigned owners and timelines
- Triggers enable early detection before risks become issues
- Governance enables timely decisions with clear authority
- Contingency plans provide fallback options for high-impact risks

Outputs must avoid:
- Vague risk descriptions without specific project context
- Generic mitigation advice like "monitor closely"
- Missing ownership and accountability assignments
- Triggers that are too late to enable proactive response
</quality_criteria>

<constraints>
- Ensure mitigation strategies are realistic given stated resources
- Match risk tolerance to response intensity
- Account for interdependencies between risks
- Provide cost estimates for contingency budget allocation
</constraints>
```

---

## Example Usage

### Input
"Software development project - mobile banking app for regional bank. 9-month timeline, $3M budget, team of 20 (mix of internal and contractors). Key stakeholders: CEO, CFO, Head of Digital, Compliance Officer, IT Security Director. Just finished design phase, starting development. Known concerns: integration with legacy core banking system (20 years old), regulatory approval for mobile banking features, user adoption post-launch. Must be PCI-DSS compliant. Low risk tolerance - banking app must be secure and reliable."

### Output

## RISK IDENTIFICATION

### Technical Risks
1. Legacy system integration complexity exceeds estimates
2. API performance issues under production load
3. Security vulnerabilities discovered during testing
4. Scalability challenges with user growth
5. Third-party service dependencies (push notifications, SMS, biometrics)

### Regulatory & Compliance Risks
6. PCI-DSS certification delays or failures
7. New banking regulations enacted mid-project
8. Data privacy violations during development/testing
9. Regulatory approval delays for mobile banking features

### Resource & Schedule Risks
10. Key developer turnover causing knowledge loss
11. QA bottleneck due to security testing requirements
12. Scope creep from stakeholder requests
13. Sprint velocity lower than planned estimates

### Business & Market Risks
14. Competitor launches similar app first
15. User adoption below targets post-launch
16. Reputational damage from security or reliability issues

## RISK ANALYSIS MATRIX

```
IMPACT →
         Low        Medium      High       Critical
High   | 10,12    | 3,6,13    | 1,2,9    |          |
Med    | 11,15    | 4,5,14    | 7,8,16   |          |
Low    |          |           |          |          |
       +---------+-----------+----------+----------+
         PROBABILITY →
```

## TOP 10 RISKS WITH MITIGATION

### Risk 1: Legacy System Integration (Score: 25 - Critical)
**Description:** Core banking API documentation is incomplete; integration may take 50-100% longer than estimated
**Probability:** High (80%) | **Impact:** High (business-critical path)
**Owner:** Technical Lead

**Mitigation:**
- Assign dedicated integration team (2 senior developers)
- Create detailed API mapping document in Week 1
- Build abstraction layer to isolate legacy dependencies
- Begin integration testing from Sprint 2 (not Sprint 8)

**Contingency:**
- Pre-approved budget ($100K) for legacy system consultant
- Parallel development of mock services for team unblocking
- Phased rollout option: core features first, advanced later

### Risk 2: Security Vulnerabilities (Score: 25 - Critical)
**Description:** Critical security issues discovered late requiring significant rework
**Probability:** High (70%) | **Impact:** High (launch blocker, reputation)
**Owner:** Security Architect

**Mitigation:**
- Security-first development training for all developers (Week 1)
- Automated SAST/DAST scanning integrated in CI/CD pipeline
- Weekly security code reviews (not end-of-project)
- External penetration testing at Sprints 5, 10, and 14

**Contingency:**
- Pre-negotiated security consultant on 48-hour standby
- 48-hour fix SLA for critical vulnerabilities in contracts
- Launch delay authority pre-approved for critical findings

### Risk 3: Regulatory Approval Delays (Score: 25 - Critical)
**Description:** Banking regulator requires changes or extended review period
**Probability:** High (60%) | **Impact:** High (launch blocker)
**Owner:** Compliance Officer

**Mitigation:**
- Early engagement with regulator (this week, not post-development)
- Monthly compliance checkpoints against submission requirements
- Regulatory liaison assigned 50% to project
- Pre-submission reviews scheduled at Sprints 5 and 10

**Contingency:**
- Fast-track application process available ($50K fee)
- Phased regulatory approval for core features first
- Alternative launch markets if primary delayed

### Risk 4: Scope Creep (Score: 20 - High)
**Description:** Stakeholder requests add unplanned features during development
**Owner:** Project Manager

**Mitigation:**
- Change control board with weekly review cycle
- Scope freeze after Sprint 4 design completion
- Feature request backlog for Phase 2
- Stakeholder expectation setting in kickoff

**Contingency:**
- 15% schedule buffer built into timeline
- Pre-approved overtime budget ($50K)

### Risk 5: Sprint Velocity Below Plan (Score: 20 - High)
**Description:** Team delivers less than planned due to complexity or learning curve
**Owner:** Scrum Master

**Mitigation:**
- Establish velocity baseline in Sprints 1-2 before committing
- Buffer 20% on initial estimates
- Weekly velocity tracking with early warning at -15%
- Cross-training to reduce single points of failure

**Contingency:**
- Contractor augmentation pre-qualified (2-week activation)
- Scope reduction options identified and prioritized

### Risk 6: PCI-DSS Certification Delays (Score: 20 - High)
**Description:** Assessment reveals gaps requiring remediation before certification
**Owner:** IT Security Director

**Mitigation:**
- Pre-assessment gap analysis in Month 1
- PCI requirements integrated into Definition of Done
- Quarterly readiness assessments during development
- Dedicated PCI documentation owner

**Contingency:**
- Remediation budget reserved ($75K)
- Extended timeline for certification-only work

## MONITORING FRAMEWORK

### Automated Triggers (Immediate Alert)
| Trigger | Threshold | Response |
|---------|-----------|----------|
| Integration API response | >2 seconds | Technical escalation |
| Security scan | Critical vulnerability | Stop and fix |
| Sprint velocity | <30 points (vs 40 target) | PM review |
| Compliance requirement | Any change | Compliance review |
| Team member | Resignation | Knowledge transfer plan |
| Budget overrun | >10% in category | Finance review |

### Review Cadence
- **Daily:** Development team standup (technical risks)
- **Weekly:** Project team risk review (all risks, 30 min)
- **Bi-weekly:** Stakeholder committee (top 10 risks)
- **Monthly:** Executive briefing (critical risks + budget)

### Go/No-Go Criteria (Sprint 5 Checkpoint)
- Integration POC with core banking successful
- Security scan shows <10 medium issues, 0 critical
- Compliance pre-approval obtained from regulator
- Velocity averaging 35+ points per sprint
- Budget on track within +/-5%

## GOVERNANCE STRUCTURE

### Contingency Budget Allocation
| Category | Reserve | Purpose |
|----------|---------|---------|
| Technical | $200K | Integration, performance, security |
| Compliance | $100K | Certification, regulatory remediation |
| Resources | $100K | Contractor augmentation |
| Unallocated | $50K | Emerging risks |
| **Total Reserve** | **$450K (15%)** | |

### Communication Plan
| Stakeholder | Frequency | Content | Owner |
|-------------|-----------|---------|-------|
| CEO | Monthly | Executive summary, critical risks | PM |
| CFO | Bi-weekly | Budget risk report, contingency usage | PM |
| Compliance Officer | Weekly | Regulatory risk status | Compliance Lead |
| IT Security Director | Weekly | Security risk dashboard | Security Architect |
| Development Team | Daily | Active risk visibility in standups | Scrum Master |

### Decision Authority
- Risk mitigation <$25K: Project Manager
- Risk mitigation $25K-$100K: Steering Committee
- Launch delay decision: CEO with CFO consultation

---

## Related Prompts
- [Business Analyst Expert](../management/business-analyst-strategic-excellence.md) - Requirements risk analysis
- [Process Optimization Expert](../operations/process-optimization-expert.md) - Process risk reduction
