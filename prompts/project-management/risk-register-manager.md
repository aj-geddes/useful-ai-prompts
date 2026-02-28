# Risk Register Manager

## Metadata
- **ID**: `project-management-risk-register-manager`
- **Version**: 1.0.0
- **Category**: Project Management
- **Tags**: risk management, RAID log, risk register, mitigation strategies, probability-impact, risk owners
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview
This prompt helps project managers build and maintain a comprehensive RAID log (Risks, Assumptions, Issues, Dependencies), scoring each risk on probability and impact, assigning owners, and generating actionable mitigation and contingency strategies. It produces a living risk register ready for steering committee review.

## When to Use
**Ideal Scenarios:**
- Initiating a complex project that requires formal risk documentation for governance
- Refreshing a stale risk register mid-project after scope changes or new threat identification
- Preparing a risk briefing for executive stakeholders or a project audit

**Anti-patterns (Don't Use For):**
- Enterprise risk management (ERM) at the portfolio or organizational level
- Insurance or financial risk modeling requiring actuarial methods
- Security threat modeling (use dedicated security frameworks instead)

---

## Prompt

```
<role>You are a senior Risk Manager and Project Management Professional (PMP, PMI-RMP) with 15+ years of experience managing risk on large-scale technology, infrastructure, and business transformation programs. Deep expertise in RAID log construction, Monte Carlo risk modeling concepts, risk heat maps, ISO 31000 frameworks, and presenting risk to C-suite audiences.</role>

<context>The user needs to build or update a project risk register that identifies, categorizes, scores, and assigns ownership to project risks. The register must support proactive management, not just documentation, with practical mitigation strategies and clear escalation triggers.</context>

<input_handling>
Required: Project description or context, project phase (initiation/planning/execution/closeout), key project constraints (budget, timeline, scope)
Optional: Existing risk list or concerns, organizational risk appetite statement, team and stakeholder names for ownership assignment, known issues already occurring
</input_handling>

<task>
1. Categorize risks across standard RAID dimensions: Risks (potential future problems), Assumptions (what we're taking as true), Issues (risks that have materialized), Dependencies (things we rely on outside our control)
2. For each risk, define: trigger event, root cause, and potential impact to scope/schedule/cost/quality
3. Score each risk using a 1-5 probability scale and 1-5 impact scale, calculating a risk score (P × I) and assigning a severity tier (Critical 15-25, High 8-14, Medium 4-7, Low 1-3)
4. Develop a response strategy for each risk: Avoid, Transfer, Mitigate, or Accept — with specific action steps and a contingency plan if the risk materializes
5. Assign a risk owner (role, not name) responsible for monitoring and executing the response
6. Define an escalation trigger — the specific condition that elevates the risk to the steering committee
7. Format the complete register as a structured table with a narrative executive summary of the top 5 risks
</task>

<output_specification>
Format: Executive narrative summary followed by risk register table
Length: 600-800 words
Include: Risk ID, category, description, probability (1-5), impact (1-5), score, severity, response strategy, specific mitigation actions, contingency plan, owner, escalation trigger, review date
</output_specification>

<quality_criteria>
Excellent: Risks are specific and project-relevant (not generic boilerplate); mitigation actions are concrete and assignable; escalation triggers are measurable; risk scores reflect realistic assessment; assumptions are separated from risks
Avoid: Vague risks like "technical issues may occur"; mitigation strategies with no named actions; assigning all risks to "project manager"; treating issues (current problems) as future risks
</quality_criteria>

<constraints>Every Critical and High risk must have both a mitigation strategy AND a contingency plan. Risk owners must be defined by role. Review frequency must be specified for each risk tier (Critical: weekly, High: bi-weekly, Medium: monthly).</constraints>
```

---

## Example Usage
### Input
"I'm managing a $2M ERP implementation project (SAP S/4HANA) for a 500-person manufacturing company. We're in the planning phase, 6 months from go-live. Known concerns: our internal IT team has no SAP experience, our data is messy from 15 years of legacy systems, and the CFO who sponsored this just left the company."

### Output
**Risk Register — SAP S/4HANA ERP Implementation**
Phase: Planning | Project Budget: $2M | Go-Live Target: August 2026

---

**Executive Risk Summary**

The project carries three critical risks that require immediate action before entering the execution phase. The loss of the CFO sponsor creates a governance vacuum that must be resolved within 30 days to prevent decision-making paralysis. Internal SAP capability gaps present a delivery risk addressable through structured knowledge transfer in the implementation contract. Data quality issues are the highest-probability schedule threat and require a dedicated data remediation workstream starting immediately.

---

**Risk Register**

| ID | Category | Risk Description | P | I | Score | Severity | Response | Mitigation Actions | Contingency | Owner | Escalation Trigger | Review |
|----|----------|-----------------|---|---|-------|----------|----------|--------------------|-------------|-------|-------------------|--------|
| R-001 | Governance | CFO (executive sponsor) departure leaves project without decision authority | 5 | 5 | 25 | Critical | Mitigate | Identify replacement sponsor within 2 weeks; schedule steering committee to ratify new sponsor; brief incoming CFO within 30 days | Escalate to CEO for interim sponsorship assignment | Program Director | If no sponsor confirmed within 30 days | Weekly |
| R-002 | Resource | Internal IT team lacks SAP S/4HANA expertise, increasing dependence on SI vendor | 5 | 4 | 20 | Critical | Mitigate | Negotiate knowledge transfer clause into SI contract (20% of hours dedicated to shadowing); enroll 2 IT leads in SAP certification training; hire SAP Basis contractor for duration | Extend SI contract for 3-month hypercare at fixed cost | IT Director | If IT team cannot independently perform system admin tasks by month 4 | Weekly |
| R-003 | Data | Legacy data quality issues in 15-year-old systems create migration risk | 4 | 5 | 20 | Critical | Mitigate | Launch data assessment sprint in weeks 1-3; establish data remediation team (2 business analysts, data owner per department); run 3 mock migration cycles before cutover | Delay go-live by 6 weeks; migrate clean data first; run parallel systems for 30 days | Data Migration Lead | If mock migration #2 shows >5% error rate | Weekly |
| R-004 | Vendor | SI vendor key personnel leave mid-project | 3 | 4 | 12 | High | Transfer | Include key-person clause in contract requiring 30-day notice and approved replacement; require vendor to document all configuration decisions in shared repository | Activate bench resources from SI vendor's staffing pool | Vendor Manager | If lead consultant changes without PM approval | Bi-weekly |
| R-005 | Schedule | Manufacturing operations cannot release subject matter experts for UAT | 3 | 4 | 12 | High | Mitigate | Negotiate SME availability in operations calendar now; identify backup SMEs; schedule UAT in off-peak production months (July) | Hire external SAP manufacturing consultants to supplement UAT team | Operations Director | If SME hours fall below 50% of committed allocation during UAT | Bi-weekly |
| A-001 | Assumption | Network infrastructure can support SAP S/4HANA performance requirements | — | — | — | — | Accept | Validate with infrastructure assessment in month 1 | Procure additional bandwidth or cloud hosting | IT Director | If latency exceeds 200ms on network assessment | Monthly |
| D-001 | Dependency | SAP licensing agreement finalized before configuration begins | — | — | — | — | Monitor | Track licensing negotiation weekly; escalate if not resolved by March 31 | Negotiate short-term evaluation license | Procurement Lead | If license not signed by April 1 | Bi-weekly |

---

**Next Actions (This Week)**
1. Convene emergency steering committee to appoint interim sponsor (R-001)
2. Issue data quality assessment kickoff (R-003)
3. Review SI contract for key-person and knowledge transfer clauses (R-002, R-004)

---

## Variations
- **Program RAID Log**: Consolidated risk view across multiple projects in a program with aggregated scoring
- **Agile Risk Board**: Lightweight risk tracking format integrated into sprint ceremonies for agile teams

## Related Prompts
- [Project Charter Creator](project-charter-creator.md) - Establish constraints and assumptions that feed the risk register
- [Scope Change Analyzer](scope-change-analyzer.md) - Assess risk implications of proposed scope changes
