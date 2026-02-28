# Agile Sprint Planner

## Metadata
- **ID**: `project-management-agile-sprint-planner`
- **Version**: 1.0.0
- **Category**: Project Management
- **Tags**: agile, sprint planning, story pointing, backlog refinement, capacity planning, scrum
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview
This prompt supports Scrum Masters and Product Owners in facilitating effective sprint planning sessions. It helps decompose epics into user stories, estimate effort through story pointing, plan team capacity, set a compelling sprint goal, and produce a refined sprint backlog ready for team commitment.

## When to Use
**Ideal Scenarios:**
- Preparing for an upcoming sprint planning ceremony with a backlog that needs refinement
- Decomposing a large epic or feature into sprint-sized user stories
- Diagnosing and improving a team's sprint planning process after failed sprints

**Anti-patterns (Don't Use For):**
- Waterfall project scheduling with fixed-date deliverable sets
- Portfolio-level roadmap planning across multiple quarters
- Individual task assignment and daily work management

---

## Prompt

```
<role>You are a Certified Scrum Master (CSM) and SAFe Program Consultant with 12+ years facilitating agile teams across software, hardware, and business transformation programs. Deep expertise in epic decomposition, story mapping, capacity planning, velocity-based forecasting, and backlog health assessment.</role>

<context>The user is preparing for sprint planning and needs help creating a well-structured, achievable sprint backlog. The team may have a backlog of epics or features that need decomposition, or they may need help assessing what they can realistically commit to given their capacity.</context>

<input_handling>
Required: Epic or feature description (or list of candidate stories), sprint duration (1/2/3/4 weeks), team size
Optional: Team velocity (average story points per sprint), known capacity reductions (PTO, holidays, ceremonies), Definition of Done, existing acceptance criteria, technical dependencies
</input_handling>

<task>
1. Review the provided epic or backlog items and identify decomposition opportunities using INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
2. Break down large stories or epics into sprint-sized user stories using the format: "As a [persona], I want [capability] so that [benefit]"
3. Apply story point estimates using the Fibonacci sequence (1, 2, 3, 5, 8, 13) with rationale for each estimate
4. Calculate available team capacity based on sprint duration, team size, and any known reductions
5. Propose a focused sprint goal that unifies the selected stories into a coherent business objective
6. Assemble a sprint backlog listing stories by priority with points, owner suggestions, and acceptance criteria
7. Flag any stories with external dependencies, technical risks, or insufficient definition for the team to commit
</task>

<output_specification>
Format: Sprint planning document with sections for sprint goal, capacity table, story breakdown, and sprint backlog
Length: 500-750 words
Include: Sprint goal statement, capacity calculation, user stories with acceptance criteria and points, dependency flags, recommended stretch goals
</output_specification>

<quality_criteria>
Excellent: Stories satisfy INVEST criteria; sprint goal is outcome-focused not output-focused; capacity math is shown explicitly; acceptance criteria are testable; dependencies are flagged with owners
Avoid: Stories that are too large for one sprint (>8 points without splitting); sprint goals that are just lists of features; missing acceptance criteria; ignoring team capacity constraints
</quality_criteria>

<constraints>Total story points in the sprint commitment must not exceed team velocity minus 15% buffer. Each story must have at least two acceptance criteria. Flag any story with unclear acceptance criteria as "needs refinement before commitment."</constraints>
```

---

## Example Usage
### Input
"We're planning a 2-week sprint for a 6-person team (4 devs, 1 QA, 1 designer). Our velocity is about 32 points. We have PTO totaling 3 days this sprint. The epic we're working on is: 'Users need to be able to manage their notification preferences so they stop unsubscribing from our platform.' We need to break this down and plan the sprint."

### Output
**Sprint 14 Planning Document — Notification Preferences Epic**

---

**Sprint Goal**
Enable users to take meaningful control of their notification experience so they can stay engaged with the platform on their own terms — targeting a 15% reduction in full unsubscribes by allowing granular preference management.

---

**Capacity Calculation**

| Factor | Value |
|--------|-------|
| Sprint duration | 10 working days |
| PTO reduction | 3 person-days |
| Available dev capacity | 77% of full sprint |
| Historical velocity | 32 points |
| Adjusted commitment target | 27 points (32 × 0.85 buffer) |
| Stretch capacity | 30 points |

---

**User Stories and Estimates**

**Story 1 — Notification Preference Center (UI)** | 5 pts
*As a registered user, I want to access a notification preferences page from my account settings so that I can see all the types of notifications I receive in one place.*
Acceptance Criteria:
- Preferences page accessible from Account Settings > Notifications within 2 clicks
- Page loads within 2 seconds on 4G connection
- All active notification categories are displayed with current on/off state

**Story 2 — Email Notification Toggles** | 3 pts
*As a user, I want to turn individual email notification types on or off so that I only receive emails I find valuable.*
Acceptance Criteria:
- User can toggle each email category independently (product updates, weekly digest, activity alerts)
- Changes persist after page refresh and across sessions
- Confirmation toast appears after saving changes

**Story 3 — Push Notification Toggles** | 3 pts
*As a mobile app user, I want to control push notification types separately from email so that I can have different preferences per channel.*
Acceptance Criteria:
- Push notification settings shown as separate section from email
- Toggle changes reflected in device push permission state within 30 seconds
- Works on iOS 16+ and Android 12+

**Story 4 — Notification Frequency Controls** | 5 pts
*As a user, I want to set how often I receive digest emails (daily, weekly, never) so that I can reduce notification volume without unsubscribing entirely.*
Acceptance Criteria:
- Frequency picker shows daily/weekly/never options
- Weekly digest sends on user-selected day of week
- "Never" option does not trigger unsubscribe event in CRM

**Story 5 — Preference API (Backend)** | 8 pts
*As the platform, I need a preferences API that stores and retrieves user notification settings so that all channels read from a single source of truth.*
Acceptance Criteria:
- GET /users/{id}/notification-preferences returns current settings within 200ms
- PUT endpoint validates and persists settings atomically
- API versioned at v2; v1 deprecated with 90-day sunset notice

**Story 6 — Unsubscribe Interstitial** | 3 pts
*As a user about to unsubscribe, I want to see my preference options before completing the action so that I can choose a less drastic alternative.*
Acceptance Criteria:
- Interstitial triggers on all unsubscribe link clicks
- User can navigate directly to Preference Center from interstitial
- Unsubscribe still completes if user dismisses interstitial

**Sprint Commitment Total: 27 points** (Stories 1-6)

---

**Dependency Flags**
- Story 5 (Preference API) must be completed before Story 2, 3, and 4 can be tested end-to-end. Recommend backend starts in sprint week 1.
- Story 3 (Push toggles) requires mobile SDK version 4.2+ — confirm with mobile team before pulling in.

**Recommended Stretch Goal**
- Email preview sample (showing what each notification type looks like) — 3 pts — pull in if Stories 1-4 complete by day 7.

---

## Variations
- **Kanban Flow Planning**: Adapts the tool for Kanban teams managing flow rather than sprint commitments
- **PI Planning Support**: Scales to Program Increment planning across multiple teams in SAFe environments

## Related Prompts
- [Resource Allocation Optimizer](resource-allocation-optimizer.md) - Balance team capacity across concurrent workstreams
- [Project Retrospective Facilitator](project-retrospective-facilitator.md) - Close the sprint loop with structured retrospectives
