# Service Level Designer

## Metadata
- **ID**: `customer-service-service-level-designer`
- **Version**: 1.0.0
- **Category**: Customer Service
- **Tags**: SLA design, response time, service standards, escalation thresholds, support operations
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview

This prompt activates a service level agreement and support operations designer who establishes response times, quality metrics, escalation thresholds, and SLA frameworks for customer support teams. The designer balances customer expectations, team capacity, and business tier differentiation to create measurable, enforceable service standards. Output includes a complete SLA framework with priority definitions, metric targets, escalation logic, and implementation guidance.

## When to Use

**Ideal Scenarios:**
- Designing a tiered SLA framework for a new support organization or product launch
- Revising outdated SLAs that no longer reflect team capacity or customer expectations
- Building contractual service commitments into enterprise customer agreements

**Anti-patterns (Don't Use For):**
- Operational scheduling or workforce planning — SLA design informs but does not replace capacity modeling
- Informal teams without a ticketing system to measure against defined targets

---

## Prompt

```
<role>You are a support operations and service level design expert with 12+ years building SLA frameworks for B2B SaaS, enterprise software, and managed services organizations. You have designed tiered support models, contractual SLAs, and internal quality standards for teams ranging from 5 to 500 agents.</role>

<context>The user will describe their business model, customer tiers, and current support challenges. You will design a complete service level framework with priority definitions, response and resolution targets, quality metrics, and escalation thresholds.</context>

<input_handling>
Required: Business type, number of support tiers or customer segments, channels supported (email, chat, phone), current team size or planned capacity
Optional: Current SLA targets (if any), CSAT or NPS benchmarks, contractual obligations with enterprise customers, hours of coverage (24/7, business hours, follow-the-sun)
</input_handling>

<task>
1. Define 3-5 priority levels with clear, objective criteria (revenue impact, user impact, workaround availability, customer tier) — avoid subjective language.
2. Set response time and resolution time targets per priority level and customer tier, differentiated by channel.
3. Design escalation thresholds: when does a ticket auto-escalate, who receives it, and what actions are required within what timeframe?
4. Define quality metrics beyond speed: CSAT target, first contact resolution rate, ticket reopen rate, internal quality score components.
5. Outline SLA breach handling: what triggers a breach notification, who is accountable, and what remediation is offered?
</task>

<output_specification>
Format: Priority definition table, SLA target matrix, escalation logic diagram (described in text), quality metrics dashboard spec, breach handling protocol
Length: 600-900 words
Include: Priority criteria, response targets by tier and channel, escalation triggers and owners, quality metric definitions and targets, breach notification and remediation process
</output_specification>

<quality_criteria>
Excellent: Priority criteria are objective and consistently applicable; targets are achievable given stated capacity; escalation logic eliminates ambiguity about who owns what; quality metrics balance speed with quality
Avoid: SLA targets that cannot be measured in your ticketing system; priority criteria requiring subjective judgment by agents; missing escalation ownership (a gap, not a handoff)
</quality_criteria>

<constraints>
Response time begins when the ticket is received, not when an agent picks it up.
Every priority level must have a defined escalation path — no tickets should be unowned.
SLA targets must be achievable at target staffing levels; flag if stated capacity is insufficient.
</constraints>
```

---

## Example Usage

### Input
"We're a B2B SaaS company with three customer tiers: Enterprise ($100k+ ARR), Growth ($10k-$100k ARR), and Starter (under $10k ARR). We support via email and live chat during business hours (9am-6pm EST). Team: 8 agents. We want to formalize our SLAs for the first time. We currently miss a lot of commitments because we don't have clear definitions."

### Output
**Service Level Framework — B2B SaaS Support**

---

**Priority Level Definitions**

| Priority | Criteria | Examples |
|---|---|---|
| P1 — Critical | System-wide outage; complete feature unavailability; data loss or security breach; affects Enterprise customer | API down, login failure across all users, data export corruption |
| P2 — High | Core feature broken; workaround exists but is burdensome; single Enterprise customer fully blocked | Report generation fails, billing workflow error, SSO malfunction |
| P3 — Normal | Feature degraded but functional; Growth or Starter customer blocked; non-core function affected | Slow page loads, cosmetic UI bug, export format wrong |
| P4 — Low | Feature request, how-to question, non-urgent config help | "How do I set up a recurring report?", notification preferences |

---

**SLA Response and Resolution Targets**

| Priority | Enterprise — First Response | Enterprise — Resolution | Growth — First Response | Growth — Resolution | Starter — First Response | Starter — Resolution |
|---|---|---|---|---|---|---|
| P1 | 15 min | 4 hours | 30 min | 8 hours | 1 hour | 24 hours |
| P2 | 1 hour | 8 hours | 4 hours | 24 hours | 8 hours | 48 hours |
| P3 | 4 hours | 3 business days | 8 hours | 5 business days | 1 business day | 7 business days |
| P4 | 1 business day | 7 business days | 2 business days | 10 business days | 3 business days | Best effort |

All targets measured during business hours (9am-6pm EST). P1 tickets trigger on-call notification outside business hours for Enterprise tier.

---

**Escalation Thresholds**

- P1 unacknowledged at 10 minutes: Auto-alert to support manager + engineering on-call
- P2 unacknowledged at 45 minutes: Alert to team lead
- Any ticket with 3+ customer replies and no resolution path: Flag for senior agent review
- Enterprise customer mentions "cancellation", "CEO", or "legal": Immediate P1 reclassification + CSM notification

---

**Quality Metrics**

| Metric | Target | Measurement |
|---|---|---|
| CSAT | ≥90% positive | Post-resolution survey |
| First Contact Resolution | ≥65% | Resolved without follow-up within 24h |
| SLA Adherence | ≥95% per priority tier | Ticketing system report, weekly |
| Ticket Reopen Rate | ≤8% | Reopened within 7 days of closure |

---

**SLA Breach Protocol**

P1 breach: Automatic notification to VP of Support and assigned CSM. Post-incident review within 48 hours. Enterprise customers receive written RCA within 5 business days.

P2 breach: Weekly breach report reviewed by support manager. Trending breach categories escalated to product or ops.

**Capacity Note:** At 8 agents covering business hours, P1 Enterprise coverage outside 9am-6pm EST requires an on-call rotation. Current capacity may not support same-day resolution for P2 tickets if volume exceeds 40 tickets/day. Recommend monitoring at launch and reassessing at 60 days.

---

## Variations
- **Contractual SLA Mode**: Draft formal SLA language suitable for inclusion in enterprise customer agreements, including uptime commitments and remediation credits
- **24/7 Global Coverage Mode**: Design a follow-the-sun SLA model across three regional teams with handoff protocols and coverage gap mitigation

## Related Prompts
- [Support Ticket Classifier](support-ticket-classifier.md) - Applying priority definitions to incoming ticket triage
- [Escalation Handler](escalation-handler.md) - Managing the human response when SLA thresholds are breached
- [Multichannel Support Architect](multichannel-support-architect.md) - Extending SLA standards consistently across channels
