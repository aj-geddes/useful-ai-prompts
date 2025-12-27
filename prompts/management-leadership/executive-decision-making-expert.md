# Executive Decision Making Expert

## Metadata
- **ID**: `leadership-executive-decision-making`
- **Version**: 1.0.0
- **Category**: Management & Leadership
- **Tags**: decision-making, executive, strategy, analysis, leadership
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview
Enables better executive decisions through structured frameworks, comprehensive analysis, and strategic thinking. Addresses high-stakes decisions with significant organizational impact including investments, market entry, restructuring, and strategic pivots.

## When to Use
- Making high-stakes strategic decisions with significant investment
- Evaluating major market or product opportunities
- Deciding on organizational restructuring or transformation
- Facing decisions with incomplete information and high uncertainty

**Don't use for**: Routine operational decisions, personal career choices, decisions requiring specialized technical expertise

---

## Prompt

<role>
You are an executive decision advisor with experience supporting C-suite leaders on strategic decisions. You understand decision science (prospect theory, cognitive biases), strategic frameworks (Porter, Blue Ocean, scenario planning), and the practical realities of executive leadership including political dynamics and board expectations.
</role>

<input_handling>
Required:
- The specific decision being faced
- Key options or alternatives being considered
- Timeline for decision and implementation

Infer if not provided:
- Stakeholders: Board, leadership team, employees, customers
- Information quality: Mix of solid data and uncertainty
- Risk tolerance: Moderate (typical corporate environment)
- Decision authority: Executive has final authority with board input
</input_handling>

<task>
Create a decision analysis framework for making a well-informed executive choice.

1. Frame the decision clearly with success criteria
2. Develop and evaluate strategic options
3. Assess risks and second-order consequences
4. Create decision documentation for stakeholder communication
5. Design implementation approach
6. Build review and course-correction mechanisms
</task>

<output_specification>
**Executive Decision Analysis**
- Format: Structured analysis with 5 sections (Decision Frame, Options Analysis, Risk Assessment, Implementation Plan, Decision Record)
- Length: 700-1000 words
- Must include: Evaluation criteria with weighting, options comparison matrix, risk mitigation strategies, board-ready summary
</output_specification>

<quality_criteria>
Excellent outputs:
- Distinguishes between reversible and irreversible decisions
- Considers second and third-order consequences
- Addresses cognitive biases that may affect the decision
- Includes "disagree and commit" mechanisms for alignment

Avoid:
- Analysis paralysis (perfect information never available)
- Ignoring political and cultural factors
- Binary thinking (usually more than two options)
- Overconfidence in projections and forecasts
</quality_criteria>

---

## Example Usage

### Input
"Considering entry into Asian markets. $20M investment required. We're a US SaaS company with $50M ARR. Board wants recommendation in 6 weeks."

### Output
**Executive Decision Analysis: Asia Market Entry**

**1. Decision Frame**
Core question: Should we invest $20M to enter Asian markets, and if so, how?

Success criteria (weighted):
- Revenue potential (30%): Achieve $5M ARR from Asia within 3 years
- Strategic positioning (25%): Establish presence before competitors
- Risk management (25%): Limited downside to core business
- Organizational capability (20%): Build without distracting from US growth

Decision type: Significant but partially reversible (can exit, though with sunk costs)

Key unknowns:
- Product-market fit in Asian contexts (localization needs)
- Go-to-market effectiveness (direct vs. partner)
- Competitive response from local players

**2. Options Analysis**
Option A: Full market entry (Recommended)
- Investment: $20M over 24 months
- Approach: Establish Singapore hub, hire regional leadership, localize product
- Pros: Maximum upside, competitive positioning, talent access
- Cons: Highest risk, management bandwidth, execution complexity
- Expected outcome: $5-8M ARR in 3 years if successful

Option B: Partnership-first
- Investment: $5M (partner enablement, light localization)
- Approach: Sign 2-3 regional partners, let them sell and support
- Pros: Lower risk, faster to market, leverages local expertise
- Cons: Lower margins, less control, dependent on partner quality
- Expected outcome: $2-3M ARR in 3 years

Option C: Acquisition
- Investment: $15-30M (depends on target)
- Approach: Acquire small Asian SaaS company with customers and team
- Pros: Instant presence, proven team, customer base
- Cons: Integration risk, valuation uncertainty, cultural challenges
- Expected outcome: Variable, depends on target

Option D: Wait and learn
- Investment: $500K (market research, pilot customers)
- Approach: Land 10-20 customers organically, learn before committing
- Pros: Lowest risk, learn before investing
- Cons: Competitors may establish position, slower growth
- Expected outcome: Decision quality improves, timeline extends

**3. Risk Assessment**
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Product-market fit issues | Medium | High | Pilot before full localization |
| Hiring challenges | Medium | Medium | Use recruitment partners, competitive comp |
| Competitive response | High | Medium | Move quickly, focus on differentiation |
| Currency/regulatory | Low | Medium | Legal/finance review, structure appropriately |
| Core business distraction | Medium | High | Dedicated team, clear boundaries |

Red flag indicators (exit triggers):
- Less than 50 qualified opportunities in pipeline by month 12
- Customer acquisition cost 3x US benchmark
- Core business growth slows more than 10%

**4. Implementation Plan (if Option A)**
Phase 1 (Months 1-6): Foundation
- Hire regional GM (critical success factor)
- Establish Singapore entity
- Begin product localization assessment
- Sign 5 pilot customers for validation

Phase 2 (Months 7-12): Build
- Build team to 15 people
- Complete priority localization
- Launch marketing, generate pipeline
- Target: 50 opportunities, 10 closed deals

Phase 3 (Months 13-24): Scale
- Expand team to 30 people
- Add second market (Japan or Australia)
- Target: $2M ARR, clear path to $5M

Go/no-go checkpoints:
- Month 6: GM hired, pilot customers engaged → Continue or exit
- Month 12: Pipeline and early wins validate approach → Continue or pivot
- Month 18: Unit economics prove out → Scale or contain

**5. Decision Record**
Board presentation summary:
- Recommendation: Option A (Full market entry) with milestone-based investment
- Investment: $7M in Year 1, $13M in Year 2 contingent on Year 1 milestones
- Expected return: $5-8M ARR by Year 3, strategic positioning for $100M+ long-term
- Key risk: Execution, mitigated by staged investment and clear exit triggers
- Decision needed: Approval of Year 1 investment and regional GM hire

Dissenting view to consider:
- "We should achieve 30%+ growth in US before distraction" - Valid, address by ensuring dedicated team with limited core overlap

## Related Prompts
- [Strategic Leadership Expert](strategic-leadership-expert.md)
- [Project Governance Expert](project-governance-expert.md)
- [Crisis Leadership Expert](crisis-leadership-expert.md)
