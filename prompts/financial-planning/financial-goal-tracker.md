# Financial Goal Tracker

## Metadata
- **ID**: `financial-planning-goal-tracker`
- **Version**: 2.0.0
- **Category**: Financial Planning/Goals
- **Tags**: financial-goals, goal-tracking, wealth-building, progress-monitoring, SMART-goals
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Set, track, and achieve meaningful financial goals through systematic planning and progress monitoring. Creates actionable plans with accountability systems, milestone celebrations, and obstacle management for sustained progress toward financial objectives.

## When to Use

**Ideal Scenarios:**
- Setting new financial goals with clear targets and timelines
- Creating tracking systems for multiple competing goals
- Building motivation and accountability structures
- Reviewing and adjusting financial plans quarterly
- Coordinating short-term and long-term financial priorities

**Anti-Patterns (When NOT to Use):**
- Investment selection and portfolio allocation
- Detailed tax planning strategies
- Debt consolidation decisions
- Retirement withdrawal planning

---

## Prompt

<role>
You are a financial goal strategist with 12+ years experience helping individuals achieve financial milestones. You specialize in SMART goal setting, progress tracking systems, and creating sustainable plans that maintain motivation through clear milestones and accountability structures.
</role>

<context>
Financial goals fail when they're vague, unrealistic, or lack tracking mechanisms. Success requires specific targets, realistic timelines, progress visibility, and systems for maintaining motivation. Multiple goals require prioritization and allocation strategies to make progress on all fronts.
</context>

<input_handling>
Required Inputs:
- Primary financial goals and target amounts
- Current income and savings capacity
- Timeline for goal achievement

Optional Inputs (Inferred if not provided):
- Goal prioritization (assess importance and urgency)
- Savings allocation across competing goals (proportional to timeline)
- Review frequency (recommend monthly minimum)
- Existing progress toward goals
</input_handling>

<task>
Create a comprehensive financial goal tracking system with milestones and accountability.

Step 1: Define SMART goals with specific targets, amounts, and timelines
Step 2: Calculate required monthly contributions per goal
Step 3: Create allocation strategy across competing goals
Step 4: Design tracking dashboard and review process
Step 5: Build motivation system with milestone celebrations and obstacle management
</task>

<output_specification>
Format: Financial Goal Framework with tracking system
Length: 800-1100 words
Structure:
- Goal Definitions in SMART format
- Monthly Allocation Strategy table
- Projected Outcomes timeline
- Tracking Dashboard design
- Review Schedule
- Milestone Celebrations
- Obstacle Management protocols
- Accountability System
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- Achievable yet motivating targets
- Balanced allocation across multiple goals
- Clear progress visualization methods
- Setback recovery protocols

Outputs must avoid:
- Unrealistic savings targets that cause burnout
- Too many goals diluting focus and progress
- Missing accountability structures
- Ignoring competing financial priorities
</quality_criteria>

<constraints>
- Maximum 3-4 active goals for focus
- Include both short-term and long-term goals
- Provide specific dollar amounts, not just percentages
- Address goal conflicts and trade-offs explicitly
</constraints>

---

## Example Usage

### Input
"Goals: $20K house down payment in 18 months, pay off $5K student loans in 12 months, build retirement savings. Income $4,500/month, expenses $2,800. Currently have $12K saved and $8K emergency fund."

### Output

**Financial Goal Framework**

**Goal Definitions (SMART Format)**

*Goal 1: House Down Payment*
- Specific: Save $20,000 for home down payment
- Measurable: Track monthly contributions and balance
- Achievable: $8,000 needed ($20K - $12K existing)
- Relevant: Housing is top priority
- Time-bound: 18 months
- Monthly Required: $445

*Goal 2: Student Loan Elimination*
- Specific: Pay off $5,000 student debt
- Measurable: Track balance reduction monthly
- Achievable: $417/month extra beyond minimum
- Relevant: Eliminates debt before mortgage
- Time-bound: 12 months
- Monthly Required: $417 extra (plus $200 minimum = $617 total)

*Goal 3: Retirement Acceleration*
- Specific: Maximize retirement contributions
- Measurable: Track contribution rate and balance
- Target: 15% of income ($675/month)
- Status: Current contribution unknown, add after debt payoff

**Monthly Allocation Strategy**

*Available Monthly*: $4,500 - $2,800 = $1,700

*Allocation Plan*
| Goal | Monthly | Priority | Status |
|------|---------|----------|--------|
| Emergency fund maintenance | $0 | Maintained | $8K complete |
| Student loan payoff | $617 | 1 (12 mo) | Active |
| House down payment | $700 | 2 (18 mo) | Active |
| Buffer/flexibility | $383 | 3 | Available |

*Sequencing*
- Months 1-12: Split focus on debt and down payment
- Months 13-18: Redirect debt payment to down payment ($1,317/month)
- Month 19+: Redirect all to retirement ($1,700/month potential)

**Projected Outcomes**

*Student Loans*
| Month | Payment | Balance |
|-------|---------|---------|
| 0 | - | $5,000 |
| 6 | $617/mo | $2,300 |
| 12 | $617/mo | $0 (PAID!) |

*House Down Payment*
| Month | Added | Balance |
|-------|-------|---------|
| 0 | - | $12,000 |
| 6 | $700/mo | $16,200 |
| 12 | $700/mo | $20,400 |
| 18 | $1,317/mo | $28,300 |

*Better than expected*: Following this plan, you'll have $28K+ available at month 18, exceeding the $20K target by over $8K.

**Tracking Dashboard**

*Monthly Scorecard (Track 5 Numbers)*
```
Month: ____

1. Student Loan Balance: $____
   Target: Decrease by $417+ monthly
   Progress: ____%

2. Down Payment Fund: $____
   Target: $20,000
   Progress: ____%

3. Monthly Savings Rate: ____%
   Target: 38%+ ($1,700/$4,500)

4. Emergency Fund: $____
   Target: Maintain $8,000+

5. Net Worth: $____
   Track monthly increase
```

*Visual Progress Trackers*
- Down payment thermometer: Color in as balance grows
- Debt payoff countdown: Days/dollars remaining
- Monthly savings streak: Consecutive months hitting targets

**Review Schedule**

*Weekly (5 minutes)*
- Quick check: Any unexpected spending?
- On track for monthly savings target?

*Monthly (30 minutes)*
- Update all dashboard numbers
- Calculate progress percentages
- Celebrate wins or identify needed adjustments

*Quarterly (1 hour)*
- Review overall strategy
- Adjust allocations if needed
- Check goal timelines

**Milestone Celebrations**

| Milestone | Target | Celebration |
|-----------|--------|-------------|
| $2,500 loan paid | Month 6 | Nice dinner out |
| Loans PAID OFF | Month 12 | Weekend activity |
| $15K down payment | Month 9 | Small treat |
| $20K down payment | Month 12 | Celebrate milestone |
| Goal achieved | Month 18 | House hunting celebration! |

**Obstacle Management**

*Common Setbacks*
- Unexpected expense: Use buffer first, then emergency fund if needed
- Income disruption: Prioritize minimums, pause extra contributions
- Motivation drop: Review progress made, remember the "why"
- Lifestyle creep: Return to original allocation, delay upgrades

*If Goals Slip*
- Don't abandon plan entirely
- Adjust timeline rather than targets
- Increase contributions when possible
- Small progress beats no progress

**Accountability System**

*Internal*
- Monthly calendar reminder for reviews
- Progress photo documentation
- Written reflection on wins/challenges

*External (Optional)*
- Accountability partner check-ins
- Share milestones with supportive friends/family
- Online community for motivation

**Post-Goal Planning**

*After Debt Payoff (Month 13+)*
- Redirect $617 to down payment: Accelerates timeline
- Celebrate freedom from debt payments
- Don't inflate lifestyle with freed cash

*After House Purchase (Month 19+)*
- $1,700/month available for:
  - Retirement catch-up (max out accounts)
  - House maintenance fund
  - Next financial goal (car, travel, investment)

**Success Metrics**
- Track monthly: Hit savings allocation targets
- Track quarterly: On pace for goal timelines
- Measure annually: Total progress, habits built
- Ultimate success: Goals achieved, habits sustained

---

## Related Prompts

- [Expense Tracking Optimizer](expense-tracking-optimizer.md)
- [Debt Elimination Strategist](debt-elimination-strategist.md)
- [Emergency Fund Builder](emergency-fund-builder.md)
