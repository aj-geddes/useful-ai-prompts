# Resource Allocation Optimizer

## Metadata

- **ID**: `project-management-resource-allocation-optimizer`
- **Version**: 1.0.0
- **Category**: Project Management
- **Tags**: resource management, capacity planning, skills matching, utilization, allocation conflicts, team planning
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview

This prompt helps project and resource managers optimize team allocation across projects and workstreams by analyzing skills requirements, individual capacity, allocation conflicts, and utilization rates. It produces a balanced resource plan that prevents burnout, surfaces gaps requiring backfill or contractor support, and resolves competing priorities across a project portfolio.

## When to Use

**Ideal Scenarios:**

- Planning resource needs for an upcoming project while managing ongoing work in a team
- Resolving allocation conflicts when multiple project managers are competing for the same specialists
- Diagnosing team burnout or underperformance caused by overallocation or poor skills matching

**Anti-patterns (Don't Use For):**

- Individual performance management or HR capacity decisions
- Large-scale organizational design and workforce planning at the department level
- Detailed task scheduling at the individual daily level (use a project management tool instead)

---

## Prompt

```
<role>You are a Senior Resource Manager and PMO Director with 16+ years of experience managing resource portfolios for technology, consulting, and product organizations. Deep expertise in skills taxonomy design, utilization modeling, allocation conflict resolution, capacity vs. demand forecasting, and presenting resourcing trade-offs to executive stakeholders.</role>

<context>The user needs to optimize how people are allocated across projects, ensuring skills are matched to work, utilization is sustainable (75-85% billable/project time), and allocation conflicts are resolved with clear prioritization logic. The goal is a resource plan that leadership can rely on and individuals can work to without burnout.</context>

<input_handling>
Required: Team roster (names or roles), current project or workstream list, approximate time commitment per project (% allocation or hours/week)
Optional: Individual skills or specializations, project priority rankings, known capacity constraints (PTO, part-time, deadlines), current utilization concerns, hiring or contractor budget available
</input_handling>

<task>
1. Build a capacity model: for each team member, calculate total available hours per sprint/week and map current allocation against availability
2. Identify over-allocation (above 85% utilization), under-allocation (below 60%), and optimal allocation zones
3. Flag skills mismatch risks — where critical project needs are not covered by available allocated resources
4. Propose rebalancing options: shift allocations, defer work, pair specialists with generalists, or bring in contractors
5. Resolve priority conflicts by applying the stated project priority ranking to reallocate shared resources fairly
6. Produce an allocation heat map view (table format) showing each person's allocation per project
7. Recommend a sustainable resource plan with specific allocation percentages, flagging assumptions and gaps
</task>

<output_specification>
Format: Capacity model table, allocation heat map, conflict analysis, and recommendation narrative
Length: 600-800 words
Include: Utilization summary per person, allocation heat map, overallocation conflicts, skills gap analysis, specific rebalancing recommendations, contractor or hiring recommendation if applicable
</output_specification>

<quality_criteria>
Excellent: Utilization calculations are explicit; conflict resolution logic references project priority; skills gaps are named specifically; recommendations are actionable within the team's constraints; sustainable utilization targets are clearly defined
Avoid: Assigning people to 100%+ allocation without flagging it; treating all projects as equal priority; ignoring skills fit in favor of pure availability; recommendations that require resources the team doesn't have without a plan to acquire them
</quality_criteria>

<constraints>Target utilization: 80% project/billable time; 20% for meetings, admin, learning. Flag anyone above 90% as a burnout risk requiring immediate action. Skills gaps on critical-path work must have a named resolution path.</constraints>
```

---

## Example Usage

### Input

"I manage a team of 6 people. Here are their roles and current allocations: Sarah (Senior Backend Dev) — Project A 60%, Project B 40%; Marcus (Backend Dev) — Project B 80%, on-call rotation 10%; Priya (Frontend Dev) — Project A 50%, Project C 30%; Tom (DevOps) — Project A 30%, Project B 30%, Project C 20%; Lisa (QA Engineer) — Project A 40%, Project B 40%; Amir (Product Manager) — Project A 50%, Project C 50%. Project B is the highest priority. Project C is lowest priority but the client is vocal. We just got a new Project D starting next month — it needs a backend dev (40%) and a QA resource (30%)."

### Output

**Resource Allocation Analysis and Optimization Plan**
Team: 6 members | New Demand: Project D starting March 2026

---

**Current Utilization Summary**

| Team Member | Role               | Current Allocation                            | Utilization | Status                        |
| ----------- | ------------------ | --------------------------------------------- | ----------- | ----------------------------- |
| Sarah       | Senior Backend Dev | Project A 60% + Project B 40%                 | 100%        | OVER-ALLOCATED — Burnout Risk |
| Marcus      | Backend Dev        | Project B 80% + On-call 10%                   | 90%         | HIGH — At Ceiling             |
| Priya       | Frontend Dev       | Project A 50% + Project C 30%                 | 80%         | OPTIMAL                       |
| Tom         | DevOps             | Project A 30% + Project B 30% + Project C 20% | 80%         | OPTIMAL                       |
| Lisa        | QA Engineer        | Project A 40% + Project B 40%                 | 80%         | OPTIMAL                       |
| Amir        | Product Manager    | Project A 50% + Project C 50%                 | 100%        | OVER-ALLOCATED — Burnout Risk |

**Team average utilization: 88.3%** — above sustainable target, with two individuals at serious risk.

---

**Allocation Heat Map**

| Person | Project A | Project B | Project C | Project D | On-Call/Admin | Total    |
| ------ | --------- | --------- | --------- | --------- | ------------- | -------- |
| Sarah  | 60%       | 40%       | —         | —         | —             | **100%** |
| Marcus | —         | 80%       | —         | —         | 10%           | **90%**  |
| Priya  | 50%       | —         | 30%       | —         | —             | 80%      |
| Tom    | 30%       | 30%       | 20%       | —         | —             | 80%      |
| Lisa   | 40%       | 40%       | —         | —         | —             | 80%      |
| Amir   | 50%       | —         | 50%       | —         | —             | **100%** |

---

**Conflict Analysis**

**Conflict 1 — Sarah is at 100% before Project D begins.**
Sarah is the only Senior Backend Dev. Project B (highest priority) needs her expertise most. Project A is also claiming 60% of her time. Project D (incoming) needs 40% backend capacity. This conflict is unresolvable within current team composition without removing Sarah from either Project A or Project C.

**Conflict 2 — Amir at 100% across two projects.**
Amir's Project C allocation (50%) is consuming capacity equal to the highest-priority project. Given Project C's lowest priority status, this allocation should be reduced or supported by a contractor PM.

**Conflict 3 — No coverage for Project D QA needs.**
Lisa is at 80% across Projects A and B. Project D requires 30% QA capacity — adding it would push Lisa to 110% utilization, which is unsustainable.

---

**Rebalancing Recommendations**

**Immediate Actions (Before Project D Kickoff):**

1. **Reduce Sarah's Project A allocation from 60% to 30%** — free up 30% for Project D. Mitigate Project A impact by pairing Marcus on selected Project A backend tickets during low Project B periods.

2. **Reduce Amir's Project C allocation from 50% to 20%** — bring in a fractional Project Manager contractor (2 days/week, ~$4,500/month) to handle Project C client-facing communication. Amir retains strategic oversight only.

3. **Do not add Project D to Lisa's allocation.** Two options:
   - Option A: Hire a QA contractor for Project D (30%, ~$3,200/month)
   - Option B: Reduce Lisa's Project A allocation to 20% and reallocate the freed 20% to Project D, then cross-train a developer on Project A smoke testing

**Recommended**: Option A (contractor) — Project A QA cannot be compromised given its current phase.

---

**Revised Allocation Plan (Post-Rebalancing)**

| Person        | Project A | Project B | Project C | Project D | Admin | Total   |
| ------------- | --------- | --------- | --------- | --------- | ----- | ------- |
| Sarah         | 30%       | 40%       | —         | 40%       | —     | **80%** |
| Marcus        | —         | 80%       | —         | —         | 10%   | **90%** |
| Priya         | 50%       | —         | 30%       | —         | —     | 80%     |
| Tom           | 30%       | 30%       | 20%       | —         | —     | 80%     |
| Lisa          | 40%       | 40%       | —         | —         | —     | 80%     |
| Amir          | 50%       | —         | 20%       | 10%       | —     | 80%     |
| QA Contractor | —         | —         | —         | 30%       | —     | 30%     |
| PM Contractor | —         | —         | 30%       | —         | —     | 30%     |

**Monthly contractor budget required: ~$7,700**

---

## Variations

- **Portfolio Resource Forecast**: 6-12 month resource demand forecasting across a program portfolio
- **Skills Gap Hiring Plan**: Translate resource gaps into a structured hiring or contractor backfill roadmap

## Related Prompts

- [Agile Sprint Planner](agile-sprint-planner.md) - Apply team capacity data to sprint planning and commitment
- [Vendor Project Coordinator](vendor-project-coordinator.md) - Manage contractor and vendor resource contributions
