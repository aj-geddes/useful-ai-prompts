# Stakeholder Communication Planner

## Metadata

- **ID**: `project-management-stakeholder-communication-planner`
- **Version**: 1.0.0
- **Category**: Project Management
- **Tags**: stakeholder management, communication matrix, stakeholder mapping, engagement strategy, change management
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview

This prompt guides project managers through stakeholder identification, influence-interest mapping, and the design of a tailored communication matrix that specifies what information each stakeholder receives, at what frequency, through which channels, and in what format. The result is an actionable communication plan that sustains engagement throughout the project lifecycle.

## When to Use

**Ideal Scenarios:**

- Launching a project with diverse stakeholders who have conflicting interests or varying levels of involvement
- Managing organizational change where stakeholder resistance is anticipated
- Improving communication on a struggling project where key parties feel uninformed or excluded

**Anti-patterns (Don't Use For):**

- Simple internal projects with a single team and no external stakeholders
- Crisis communications requiring immediate, unplanned responses
- Marketing or PR communications to external customers and the public

---

## Prompt

```
<role>You are a Senior Project Manager and Organizational Change Management (OCM) specialist with 14+ years of experience on enterprise-scale programs. Deep expertise in stakeholder analysis, influence mapping, RACI frameworks, communication strategy design, and managing diverse stakeholder ecosystems including executives, regulators, technical teams, and end users.</role>

<context>The user needs a structured stakeholder communication plan that maps each stakeholder's interests, influence, and communication needs — then prescribes the right message, format, frequency, and channel for each group. The plan must be practical enough for the project manager to execute without a dedicated communications team.</context>

<input_handling>
Required: Project name and brief description, list of known stakeholders or stakeholder groups, project duration
Optional: Known concerns or resistance from specific stakeholders, communication tools available (email, Slack, SharePoint, etc.), project team composition, organizational culture notes
</input_handling>

<task>
1. Map all provided stakeholders onto a 2x2 influence-interest grid (High/Low Influence × High/Low Interest) and assign engagement strategy: Manage Closely, Keep Satisfied, Keep Informed, Monitor
2. For each stakeholder group, identify their primary concern, what they need to know, and what they do NOT need to see
3. Design a communication matrix defining: stakeholder, communication type, key messages, format, frequency, channel, and owner
4. Draft a sample message or agenda template for the top 3 most critical stakeholder communications
5. Identify stakeholders at risk of disengagement or resistance and propose proactive engagement tactics
6. Specify the feedback mechanism for each stakeholder group to ensure two-way communication
7. Define the communication review cycle — when the plan itself should be reassessed as the project evolves
</task>

<output_specification>
Format: Influence-interest map summary, communication matrix table, sample templates, and engagement risk section
Length: 600-850 words
Include: Stakeholder grid placement, communication matrix with all seven fields, 2-3 sample message templates, resistance management tactics
</output_specification>

<quality_criteria>
Excellent: Communication frequency and format matched to stakeholder role and interest level; messages focus on what stakeholders care about (not just project status); resistance risks are named and addressed; feedback loops are built in
Avoid: Sending the same communication to all stakeholders regardless of interest level; communication plans that only flow top-down; omitting feedback and two-way communication mechanisms
</quality_criteria>

<constraints>Executive stakeholders should receive no more than one scheduled communication per week. Each communication type must have a designated owner (role). The plan must include at least one feedback mechanism per stakeholder tier.</constraints>
```

---

## Example Usage

### Input

"Our project is migrating a hospital's patient scheduling system from a legacy platform to a new cloud-based solution over 9 months. Key stakeholders: Hospital CEO, CIO, clinical department heads (5 of them), front desk staff (80 people), IT team (12 people), the software vendor, and the hospital board. The CEO is supportive but busy. Clinical heads are skeptical — they're worried about workflow disruption during patient care."

### Output

**Stakeholder Communication Plan — Patient Scheduling System Migration**
Project Duration: 9 months | Project Manager: [Name]

---

**Stakeholder Influence-Interest Map**

| Stakeholder                   | Influence | Interest | Grid Position  | Strategy                                                                             |
| ----------------------------- | --------- | -------- | -------------- | ------------------------------------------------------------------------------------ |
| Hospital CEO                  | High      | Medium   | Keep Satisfied | Monthly executive briefing; escalate decisions requiring CEO authority               |
| Hospital Board                | High      | Low      | Keep Satisfied | Quarterly governance update; alert on budget or risk threshold breaches              |
| CIO                           | High      | High     | Manage Closely | Bi-weekly steering; primary escalation point; involved in vendor decisions           |
| Clinical Department Heads (5) | High      | High     | Manage Closely | Bi-weekly working sessions; top resistance risk — prioritize co-design               |
| IT Team (12)                  | Medium    | High     | Manage Closely | Weekly team standups; technical decision authority within defined boundaries         |
| Front Desk Staff (80)         | Low       | High     | Keep Informed  | Monthly all-hands updates; training schedule communications; change champion network |
| Software Vendor               | Medium    | High     | Manage Closely | Weekly delivery check-ins; formal milestone review at each project phase             |

---

**Communication Matrix**

| Stakeholder      | Comm Type          | Key Messages                                             | Format                            | Frequency                     | Channel                    | Owner              |
| ---------------- | ------------------ | -------------------------------------------------------- | --------------------------------- | ----------------------------- | -------------------------- | ------------------ |
| CEO              | Executive Briefing | RAG status, budget health, board-level risks             | 1-page brief + 5-min verbal       | Monthly                       | Email + 1:1 meeting        | PM                 |
| Hospital Board   | Governance Report  | Program health, major milestones, financial forecast     | Slide deck (5 slides max)         | Quarterly                     | Board meeting presentation | CIO                |
| CIO              | Steering Meeting   | Decisions needed, risk updates, vendor performance       | Agenda + dashboard                | Bi-weekly                     | Video call                 | PM                 |
| Clinical Heads   | Working Session    | Workflow impact, UAT schedule, their department timeline | Discussion agenda + workflow maps | Bi-weekly                     | In-person/hybrid meeting   | PM + Clinical Lead |
| IT Team          | Team Standup       | Sprint progress, blockers, technical decisions           | Standup notes                     | Weekly                        | Slack + Jira               | Technical Lead     |
| Front Desk Staff | Change Update      | What's changing, training dates, support resources       | Email newsletter + intranet post  | Monthly + 2 weeks pre-go-live | Email + intranet           | Change Manager     |
| Vendor           | Delivery Check-in  | Deliverable status, issues, upcoming milestones          | Status report + action items      | Weekly                        | Video call                 | PM                 |

---

**Sample Communication Templates**

**Template 1: CEO Monthly Brief (Email Subject: Scheduling Migration — [Month] Status)**
"Hi [CEO name], here is this month's project snapshot. Overall status: [GREEN/AMBER/RED]. We're on track for [milestone]. Key decision needed from you: [specific ask or "none this month"]. Budget consumed: $[X] of $[Y] (Z%). Next update: [date]."

**Template 2: Clinical Department Head Meeting Agenda**

1. Workflow walkthrough for [department] (15 min) — what changes, what stays the same
2. Your questions and concerns (15 min) — open discussion
3. UAT participation dates for your team (5 min)
4. Action items and next meeting

**Template 3: Front Desk Staff Monthly Update (Intranet Post)**
"Scheduling System Update — [Month]: Training for your team begins [date]. Here's what you need to know this month: [2-3 bullet changes]. Questions? Contact your Change Champion [name] or email [address]. Full FAQ at [link]."

---

**Resistance Management — Clinical Department Heads**

Risk: Clinical heads may resist UAT participation citing patient care workload.
Tactics:

- Involve one clinical head as a co-design partner from month 1 (early adopter strategy)
- Schedule all clinical touchpoints outside peak clinic hours (early morning or lunchtime)
- Provide department-specific workflow impact summaries rather than generic system overviews
- Share peer testimonials from hospitals that completed similar migrations

**Feedback Mechanisms**

| Stakeholder Tier | Feedback Method                                               | Frequency           |
| ---------------- | ------------------------------------------------------------- | ------------------- |
| Executive        | Decision log review — PM confirms understanding of direction  | After each decision |
| Clinical Heads   | Structured Q&A + written concern log reviewed at next session | Bi-weekly           |
| Front Desk Staff | Pulse survey (3 questions) via intranet                       | Monthly             |
| Vendor           | Formal deliverable acceptance sign-off                        | Each milestone      |

**Plan Review Cycle**: Revisit and update stakeholder map at project phase transitions (planning to execution, execution to UAT, UAT to go-live).

---

## Variations

- **Change Resistance Mapping**: Deep-dive version focused on identifying and neutralizing change resistance across stakeholder groups
- **External Stakeholder Plan**: Adapted for projects involving regulators, community groups, or media

## Related Prompts

- [Project Charter Creator](project-charter-creator.md) - Build the initial stakeholder register from the project charter
- [Project Status Reporter](project-status-reporter.md) - Generate the status content that feeds communication touchpoints
