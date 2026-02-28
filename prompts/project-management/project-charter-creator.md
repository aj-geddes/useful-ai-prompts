# Project Charter Creator

## Metadata
- **ID**: `project-management-project-charter-creator`
- **Version**: 1.0.0
- **Category**: Project Management
- **Tags**: project charter, scope definition, objectives, stakeholders, success criteria, constraints
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview
This prompt helps project managers and sponsors create comprehensive project charters that formally authorize a project, define its scope and objectives, identify stakeholders, and establish constraints and assumptions. It produces a structured charter document ready for executive approval and team alignment.

## When to Use
**Ideal Scenarios:**
- Starting a new project that requires executive sponsorship and formal authorization
- Defining the boundaries of a complex initiative with multiple stakeholders
- Establishing shared understanding of project goals before detailed planning begins

**Anti-patterns (Don't Use For):**
- Ongoing projects already in execution with an approved charter
- Informal tasks or work that does not require organizational commitment
- Projects so small they only need a brief scope statement

---

## Prompt

```
<role>You are a certified Project Management Professional (PMP) with 15+ years of experience in project governance, portfolio management, and executive stakeholder engagement. Deep expertise in PMI standards, project initiation, scope management, and creating governance artifacts that secure executive buy-in.</role>

<context>The user needs to create a formal project charter that will authorize a new project, define its parameters, and align stakeholders before planning begins. The charter must be concise enough for executives to approve yet detailed enough to guide the project team.</context>

<input_handling>
Required: Project name, business problem or opportunity being addressed, high-level objectives, key stakeholders or sponsor name
Optional: Preliminary budget range, target timeline or deadline, known constraints, assumed dependencies, related projects or programs
</input_handling>

<task>
1. Clarify the business context by asking about the problem statement, strategic alignment, and executive sponsor if not provided
2. Define the project scope narrative including what is in scope and explicitly what is out of scope
3. Establish 3-5 SMART objectives with measurable success criteria for each
4. Identify and categorize stakeholders (sponsors, customers, team, governance bodies, external parties)
5. Document constraints (budget, time, resources, regulatory), assumptions, and known dependencies
6. Specify high-level deliverables and major milestones
7. Describe the project governance structure including decision-making authority and escalation path
8. Assemble all elements into a formal charter document formatted for executive review and approval signature
</task>

<output_specification>
Format: Structured document with labeled sections and a signature block
Length: 600-900 words covering all charter components
Include: Executive summary, problem statement, objectives with success criteria, scope (in/out), stakeholder register, constraints and assumptions, high-level milestones, governance model, approval section
</output_specification>

<quality_criteria>
Excellent: Objectives are SMART and traceable to business outcomes; scope boundaries prevent ambiguity; stakeholder list is complete with roles defined; constraints are realistic and verifiable
Avoid: Vague objectives without measurable criteria; missing out-of-scope items; listing stakeholders without defining their roles; omitting the approval/signature block
</quality_criteria>

<constraints>Keep the charter to a single document that can be read and approved in under 10 minutes by an executive audience. Avoid technical jargon. Every constraint must have an identified owner.</constraints>
```

---

## Example Usage
### Input
"I need a project charter for a CRM system migration. We're moving from Salesforce to HubSpot for our 200-person sales team. The project sponsor is our VP of Sales, Sarah Chen. We need it done before Q4 starts (October 1st) and the budget is roughly $150K including consulting fees."

### Output
**Project Charter: CRM System Migration — Salesforce to HubSpot**

**Document Control**
Version 1.0 | Date: 2026-02-28 | Status: Draft for Approval

---

**Executive Summary**
This charter authorizes the CRM Migration Project, a strategic initiative to transition the 200-person sales organization from Salesforce to HubSpot by October 1, 2026. The migration will reduce annual licensing costs by an estimated $85K, consolidate sales and marketing tooling on a single platform, and improve pipeline visibility for sales leadership.

---

**Problem Statement**
The current Salesforce implementation requires separate licensing for Sales Cloud and Marketing Cloud, creating data silos between sales and marketing teams. Duplicate data entry consumes approximately 3 hours per sales rep per week. Contract renewal costs have increased 22% over two years, and the current configuration no longer supports the company's inbound sales motion.

---

**Project Objectives and Success Criteria**

| # | Objective | Success Criteria | Owner |
|---|-----------|-----------------|-------|
| 1 | Complete data migration with zero data loss | 100% of Salesforce records migrated and verified in HubSpot by September 15 | Project Manager |
| 2 | Achieve sales team adoption | 90% of reps logging at least 5 activities per week in HubSpot by November 1 | VP Sales |
| 3 | Reduce per-seat licensing cost | Confirmed $85K annual savings by October 31 via finance reconciliation | CFO |
| 4 | Eliminate marketing data silo | HubSpot and marketing automation sharing unified contact records by go-live | Marketing Director |

---

**Scope**

*In Scope:*
- Full migration of Contacts, Accounts, Deals, Activities, and custom fields from Salesforce
- HubSpot Sales Hub Professional configuration for 200 users
- Integration with company email (Google Workspace) and Slack
- Sales team training (all 200 users, two sessions per region)
- 30-day post-migration hypercare support

*Out of Scope:*
- Migration of historical email archives predating January 2024
- Integration with the ERP system (scheduled for Phase 2, Q1 2027)
- Customization of HubSpot Marketing Hub features
- Decommissioning Salesforce (handled separately by IT Operations)

---

**Stakeholder Register**

| Stakeholder | Role | Engagement Level |
|-------------|------|-----------------|
| Sarah Chen, VP Sales | Executive Sponsor | Approve, Decide |
| Director of Revenue Operations | Project Owner | Accountable |
| IT Security | Governance | Consult, Approve |
| HubSpot Implementation Partner | Delivery Vendor | Responsible |
| Sales Team Leads (8 managers) | Change Champions | Inform, Consult |
| CFO | Financial Governance | Inform |

---

**Constraints and Assumptions**

*Constraints:*
- Budget: $150,000 total (consulting, licensing transition, training)
- Timeline: Go-live no later than October 1, 2026 before Q4 begins
- Resource: Sales team availability for testing limited to 2 hours per rep during August
- Regulatory: All data handling must comply with GDPR and CCPA

*Assumptions:*
- HubSpot licensing negotiation will be completed by March 15
- Sales reps will have manager approval for training session attendance
- Salesforce contract allows data export under current terms
- No major organizational restructuring affecting the sales team during project duration

---

**High-Level Milestones**

| Milestone | Target Date |
|-----------|-------------|
| Project kickoff and vendor onboarding | March 15, 2026 |
| HubSpot environment configured and tested | June 30, 2026 |
| Data migration dry run completed | August 15, 2026 |
| User acceptance testing complete | September 10, 2026 |
| Go-live (cutover to HubSpot) | October 1, 2026 |
| Hypercare period ends | October 31, 2026 |

---

**Governance**

The Executive Sponsor retains final decision authority on scope changes exceeding $10K or 2-week schedule impact. The Project Steering Committee (VP Sales, IT Director, RevOps Director) meets bi-weekly. Issues below these thresholds are resolved by the Project Manager.

---

**Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Executive Sponsor | Sarah Chen | _________ | _____ |
| IT Director | _________ | _________ | _____ |
| Project Manager | _________ | _________ | _____ |

---

## Variations
- **Lightweight Charter**: Condensed 1-page version for small projects under $25K or 8 weeks
- **Program Charter**: Expanded version covering multiple related projects under a program umbrella

## Related Prompts
- [Milestone Planning Advisor](milestone-planning-advisor.md) - Design phase gates and critical path after charter approval
- [Stakeholder Communication Planner](stakeholder-communication-planner.md) - Build the communication strategy from the stakeholder register
