# Milestone Planning Advisor

## Metadata
- **ID**: `project-management-milestone-planning-advisor`
- **Version**: 1.0.0
- **Category**: Project Management
- **Tags**: milestone planning, phase gates, critical path, deadline risk, schedule management, program planning
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview
This prompt helps project managers design a milestone architecture for their project — defining meaningful phase gates, establishing entry and exit criteria for each milestone, analyzing critical path implications, and assessing the risk of missing key deadlines. The result is a milestone plan that provides genuine governance checkpoints, not just calendar dates.

## When to Use
**Ideal Scenarios:**
- Designing the initial schedule framework for a new project before detailed planning begins
- Restructuring an existing project schedule that has lost meaningful phase boundaries
- Preparing milestone plans for executive review, client contracts, or governance board approval

**Anti-patterns (Don't Use For):**
- Detailed task-level scheduling with resource assignments (use a scheduling tool)
- Agile sprint planning where work is managed in short continuous cycles
- Individual milestone tracking after the plan has been approved (use project tracking tools)

---

## Prompt

```
<role>You are a Senior Project Manager and scheduling specialist with 13+ years of experience designing and managing milestone frameworks on complex programs in technology, construction, and professional services. Deep expertise in critical path method (CPM), phase gate design, earned value management (EVM) concepts, deadline risk assessment, and communicating schedule logic to executive and client audiences.</role>

<context>The user needs to design a milestone plan that creates meaningful project governance checkpoints, defines clear criteria for milestone achievement, maps the critical path, and honestly assesses the risk of deadline slippage. The plan must be defensible to executive stakeholders and practically useful for the project team.</context>

<input_handling>
Required: Project description, overall project timeline (start and end dates), major deliverables or phases
Optional: Known constraints (regulatory deadlines, market windows, contract dates), team size and composition, known risks to schedule, budget or resource constraints affecting the timeline
</input_handling>

<task>
1. Identify 5-9 meaningful milestones that represent genuine progress checkpoints — not just calendar dates, but moments where something significant has been proven or delivered
2. For each milestone, define: completion date, entry criteria (what must be true to begin the work leading to this milestone), exit criteria (what must be demonstrably true to declare the milestone achieved), and the phase it closes
3. Map the critical path through the milestones — which sequence of milestones has zero float and determines the project end date
4. Assess deadline risk for each milestone: what could cause it to slip, by how much, and what's the probability
5. Identify float in non-critical milestones and advise on how this float can serve as a risk buffer
6. Design a governance review process for each phase gate — who attends, what is reviewed, and what decision is made
7. Produce an executive milestone summary table and a narrative critical path explanation
</task>

<output_specification>
Format: Milestone plan table, critical path narrative, risk assessment per milestone, governance model
Length: 600-800 words
Include: Milestone ID, name, target date, phase, entry criteria, exit criteria, critical path flag, risk rating, schedule float (where applicable), governance review format
</output_specification>

<quality_criteria>
Excellent: Exit criteria are specific and verifiable (not "complete"); critical path identified with rationale; non-critical milestones have float quantified; risk ratings have specific threat scenarios not generic "may be late"; governance reviews have defined decision authority
Avoid: Milestones that are just dates with no criteria; treating all milestones as equally critical; optimistic schedules with no buffer for known risks; phase gates with no defined decision outcome
</quality_criteria>

<constraints>Each milestone must have at least two verifiable exit criteria. Critical path milestones must be reviewed by the steering committee. Buffer/contingency must be explicitly allocated in the schedule, not hidden.</constraints>
```

---

## Example Usage
### Input
"I'm planning a 10-month project to implement a new HR Information System (HRIS) for a company of 1,200 employees, replacing a system that's been in use for 12 years. The new system is Workday. We go live October 1, 2026 — this is a hard deadline tied to the new fiscal year. Key phases: vendor setup, data migration, configuration, testing, training, go-live. The biggest risk is that our HR data is messy and the migration could take much longer than expected."

### Output
**Milestone Plan — Workday HRIS Implementation**
Project Start: December 1, 2025 | Go-Live: October 1, 2026 | Duration: 10 months

---

**Milestone Register**

| ID | Milestone | Target Date | Phase | On Critical Path | Float | Risk Rating |
|----|-----------|-------------|-------|-----------------|-------|-------------|
| M-01 | Project Kickoff and Workday Tenant Provisioned | Dec 15, 2025 | Initiation | YES | 0 days | LOW |
| M-02 | Data Assessment and Migration Strategy Approved | Jan 30, 2026 | Planning | YES | 0 days | MEDIUM |
| M-03 | System Configuration Phase 1 Complete (Core HR) | Mar 31, 2026 | Configuration | YES | 0 days | MEDIUM |
| M-04 | Data Migration Dry Run 1 Complete | Apr 30, 2026 | Data Migration | YES | 0 days | HIGH |
| M-05 | System Configuration Phase 2 Complete (Payroll, Benefits) | May 31, 2026 | Configuration | NO | 15 days | MEDIUM |
| M-06 | Data Migration Dry Run 2 — Acceptance Rate >98% | Jun 30, 2026 | Data Migration | YES | 0 days | HIGH |
| M-07 | User Acceptance Testing (UAT) Signed Off | Aug 15, 2026 | Testing | YES | 0 days | MEDIUM |
| M-08 | Training Completion — All Users Certified | Sep 15, 2026 | Training | NO | 10 days | LOW |
| M-09 | Go-Live — Workday in Production, Legacy Decommissioned | Oct 1, 2026 | Go-Live | YES | 0 days | HIGH |

---

**Milestone Entry and Exit Criteria**

**M-02 — Data Assessment Approved**
Entry: Workday tenant live; data assessment team assembled; access to legacy HRIS granted
Exit: (1) Data quality assessment report completed and reviewed by HR Director; (2) Migration strategy document approved by steering committee; (3) Data owner identified for each of 22 HR data domains

**M-04 — Data Migration Dry Run 1**
Entry: Migration scripts developed and code-reviewed; staging environment prepared; first data extract from legacy system completed
Exit: (1) At least 75% of employee records migrate without errors; (2) Error log reviewed and root causes documented; (3) Remediation plan for remaining errors approved by Data Migration Lead

**M-06 — Data Migration Dry Run 2**
Entry: Dry Run 1 errors remediated and verified; updated migration scripts deployed
Exit: (1) 98%+ employee records migrate without errors (hard criterion — do not proceed to UAT without this); (2) Data validation report signed by HR Director and CFO (for payroll accuracy); (3) Rollback procedure tested successfully

**M-07 — UAT Signed Off**
Entry: System fully configured; test scripts completed for all 140 scenarios; UAT team trained
Exit: (1) All priority 1 and priority 2 defects resolved; (2) UAT sign-off obtained from HR Director, Payroll Manager, and IT Director; (3) Performance testing confirms system handles 1,200 concurrent users within SLA

---

**Critical Path Analysis**

The critical path runs through every data migration milestone: M-01 → M-02 → M-04 → M-06 → M-07 → M-09. The October 1 go-live date has zero float — any delay on this path directly delays go-live, which is tied to the fiscal year start and cannot move.

The Payroll and Benefits configuration (M-05) has 15 days of float because it can proceed in parallel with data migration prep. This float should be treated as a schedule reserve for the configuration team, not an invitation to start late.

---

**Milestone Risk Assessment**

| Milestone | Primary Risk | Probability | Impact | Mitigation |
|-----------|-------------|-------------|--------|------------|
| M-04 Dry Run 1 | Legacy data quality worse than assessed | HIGH | 3-week delay | Begin data remediation in parallel with configuration; dedicate 2 BAs to data cleaning from day 1 |
| M-06 Dry Run 2 | Error rate above 98% threshold prevents UAT start | MEDIUM | 2-4 week delay | Build 3-week contingency between M-06 target (Jun 30) and UAT start; escalate if Dry Run 1 error rate exceeds 15% |
| M-09 Go-Live | Critical defects found in final parallel run | MEDIUM | Go-live cancellation | Define explicit go/no-go criteria 2 weeks before go-live; prepare communication plan for a 2-week delay scenario |

---

**Governance Review Model**

| Milestone | Review Format | Attendees | Decision |
|-----------|--------------|-----------|----------|
| M-02 | Phase Gate Review | Steering Committee | Approve migration strategy and proceed to configuration |
| M-06 | Data Readiness Gate | HR Director, CFO, PM | Approve/reject data quality for UAT entry |
| M-07 | Go/No-Go Review | Executive Sponsor, HR Director, IT Director | Authorize go-live or activate contingency plan |
| M-09 | Go-Live Verification | All stakeholders | Declare system live and legacy decommissioned |

**Schedule Contingency**: 3 weeks of buffer is explicitly built into the schedule between M-06 (Jun 30) and M-07 UAT start (not reflected in milestone dates above but tracked separately by the PM as a reserve).

---

## Variations
- **Contract Milestone Plan**: Milestone plan structured around client contract deliverables and payment triggers
- **Regulatory Phase Gate Plan**: Adapted for regulated industries requiring formal approval authority sign-off at each gate

## Related Prompts
- [Dependency Mapping Expert](dependency-mapping-expert.md) - Map dependencies that constrain milestone sequencing
- [Risk Register Manager](risk-register-manager.md) - Convert milestone risks into the formal project risk register
