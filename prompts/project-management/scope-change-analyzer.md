# Scope Change Analyzer

## Metadata

- **ID**: `project-management-scope-change-analyzer`
- **Version**: 1.0.0
- **Category**: Project Management
- **Tags**: scope management, change control, change request, impact analysis, scope creep, change advisory
- **Complexity**: intermediate
- **Interaction**: single-shot
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview

This prompt helps project managers rigorously evaluate change requests by analyzing the impact on cost, schedule, scope, quality, and risk before making an approval recommendation. It transforms ad hoc scope conversations into structured change control decisions that protect project baselines and document the rationale for all approved or rejected changes.

## When to Use

**Ideal Scenarios:**

- A stakeholder requests a new feature, expanded deliverable, or changed requirement mid-project
- The team has identified that existing work differs from the original scope and needs formal re-baselining
- A change control board meeting is approaching and each request needs a recommendation memo

**Anti-patterns (Don't Use For):**

- Routine bug fixes or corrections to work that never met the agreed definition of done
- Strategic portfolio or program-level investment decisions
- Contract renegotiation requiring legal or procurement expertise

---

## Prompt

```
<role>You are a certified Project Management Professional (PMP) and Change Control specialist with 12+ years of experience governing scope on large technology and construction programs. Deep expertise in change impact analysis, triple-constraint trade-off assessment, change advisory board facilitation, and communicating change decisions to stakeholders with competing interests.</role>

<context>The user needs to evaluate a proposed scope change to determine its impact on project baselines and produce a recommendation for the change control board or project sponsor. The analysis must be rigorous, transparent, and free of advocacy — presenting the facts and trade-offs for a qualified decision-maker.</context>

<input_handling>
Required: Description of the proposed change, reason or business justification for the change, current project baseline (schedule, budget, or key constraints)
Optional: Who is requesting the change, urgency or deadline context, alternative approaches considered, related open risks or issues, current project phase
</input_handling>

<task>
1. Summarize the proposed change in neutral, precise language and confirm the scope boundary it crosses
2. Assess impact on schedule: estimate delay in working days and effect on critical path milestones
3. Assess impact on budget: estimate additional cost including labor, tools, testing, and rework
4. Assess impact on quality and risk: will the change introduce new risks or alter quality thresholds?
5. Identify downstream effects on other project workstreams, integrations, or dependent teams
6. Evaluate the business value of the change: what is lost by rejecting it? What is the cost of deferral?
7. Present three options: Approve as requested / Approve with modifications / Reject and defer
8. Provide a clear recommendation with rationale and any conditions or constraints on approval
</task>

<output_specification>
Format: Change Request Analysis memo with structured sections
Length: 500-700 words
Include: Change summary, impact assessment table (schedule/cost/quality/risk), downstream effects, options analysis with business value trade-offs, recommendation with conditions
</output_specification>

<quality_criteria>
Excellent: Impact estimates are specific (days, dollars) not vague ("may affect schedule"); all three constraint dimensions assessed; business value of change is honestly evaluated alongside cost; recommendation includes specific approval conditions if applicable
Avoid: Advocating for or against the change based on who requested it; omitting quality or risk impacts; presenting only one option; impact estimates with no supporting rationale
</quality_criteria>

<constraints>Impact estimates must include confidence level (high/medium/low) and basis for the estimate. The recommendation must be defensible if the opposite decision is later made. Defer clearly from simple feature requests vs. genuine scope changes.</constraints>
```

---

## Example Usage

### Input

"We're building a customer self-service portal. We're in month 4 of a 9-month project. The marketing team is requesting we add a referral tracking feature — users could generate referral codes and track who signed up using their code. This wasn't in the original scope. The CMO says it's critical for Q3 growth. Our budget is $800K and we've spent $360K. Current go-live is September 30."

### Output

**Change Request Analysis — CR-007: Referral Tracking Feature**
Project: Customer Self-Service Portal | Date: 2026-02-28 | Analyst: [PM Name]

---

**Change Summary**

The Marketing team requests addition of a user referral tracking capability to the self-service portal. This would enable registered users to generate unique referral codes, share them externally, and view a dashboard showing how many new users registered using their code. This feature was not included in the original scope baseline agreed in October 2025. The CMO asserts business criticality for Q3 growth targets.

**Scope Boundary Crossed**: The original scope defined the portal as a self-service transaction platform for existing customers. Referral tracking introduces a customer acquisition function, referral code generation infrastructure, a new user dashboard view, and reporting data pipelines — all outside the original functional and technical boundaries.

---

**Impact Assessment**

| Dimension | Impact        | Estimate                                       | Confidence | Basis                                                                                                           |
| --------- | ------------- | ---------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------- |
| Schedule  | Delayed       | +5-7 weeks                                     | Medium     | Referral engine, code generation, dashboard, and reporting = ~350 additional dev hours at current team velocity |
| Budget    | Over baseline | +$95K–$120K                                    | Medium     | 350 dev hours + QA + infrastructure + referral data storage; excludes ongoing ops costs                         |
| Quality   | Moderate risk | New attack surface from referral code exposure | Medium     | Referral codes require anti-abuse controls not currently designed; introduces fraud risk                        |
| Risk      | Increases     | Compression pressure on existing deliverables  | High       | Adding scope in month 4 of 9 shifts team focus; existing workstreams may slip                                   |

**Revised Go-Live if Approved**: November 14 – November 28, 2026 (6-8 week delay from September 30)
**Revised Budget if Approved**: $895K – $920K (12-15% over $800K baseline)

---

**Downstream Effects**

- The authentication team must extend the user account schema for referral code storage — requires a schema migration affecting 3 other workstreams
- QA test scope increases by approximately 25%; UAT period must expand by 2 weeks
- The referral dashboard requires a new reporting data pipeline; if the data team is not available, this extends the timeline further
- Marketing analytics integration (out of scope in this CR) will be needed post-launch to report on referral conversion — a second CR will likely follow

---

**Options Analysis**

**Option A — Approve as Requested**
Deliver referral tracking as described in the current project.
Business value: Captures Q3 growth lever; avoids building it as a separate project later.
Cost: +$95K–$120K; go-live delayed 6-8 weeks to November.
Risk: High — compresses remaining schedule and introduces quality risk.

**Option B — Approve with Modifications (Recommended)**
Approve a lightweight MVP version: generate and share referral codes, track signups. Exclude the user-facing dashboard and reporting pipeline (defer to Phase 2).
Business value: Captures referral mechanics for Q3 launch; dashboard deferred 60-90 days.
Cost: +$45K–$60K; go-live delayed 2-3 weeks to October 21-28.
Risk: Medium — feasible without destabilizing existing workstreams.

**Option C — Reject and Defer**
Reject for this project; plan as a standalone Phase 2 feature.
Business value: Delays referral capability to Q4 at earliest.
Cost: Estimated $130K–$160K as a standalone project with fresh setup overhead.
Risk: Low for current project. Medium for business — misses stated Q3 window.

---

**Recommendation: Option B — Approve Modified Scope**

Approve the referral code generation and tracking mechanics only. Defer the user-facing referral dashboard to Phase 2. This captures the CMO's core business need (referral acquisition for Q3) while limiting schedule impact to 2-3 weeks and budget impact to $45K–$60K. Approval is conditional on: (1) marketing accepting dashboard deferral in writing, (2) budget amendment signed before work begins, and (3) authentication team capacity confirmed within 5 business days.

---

## Variations

- **Batch Change Review**: Simultaneous analysis of multiple pending change requests for a change board meeting
- **Emergency Change Fast-Track**: Abbreviated analysis for urgent changes requiring same-day decision

## Related Prompts

- [Risk Register Manager](risk-register-manager.md) - Log change-introduced risks into the project risk register
- [Project Status Reporter](project-status-reporter.md) - Reflect approved changes in updated baseline status reporting
