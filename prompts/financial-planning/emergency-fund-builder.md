# Emergency Fund Builder

## Metadata

- **ID**: `financial-planning-emergency-fund`
- **Version**: 2.0.0
- **Category**: Financial Planning/Savings
- **Tags**: emergency-fund, financial-security, savings-strategy, risk-management, liquidity
- **Complexity**: simple
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Build appropriate emergency fund reserves tailored to individual risk factors and life circumstances. Creates strategic savings plans with proper account placement, clear usage guidelines, and replenishment protocols for financial security.

## When to Use

**Ideal Scenarios:**

- Starting or rebuilding an emergency fund from scratch
- Determining appropriate fund size for specific situation
- Choosing optimal accounts for emergency savings
- Creating guidelines for fund usage and replenishment
- Balancing emergency savings with other financial priorities

**Anti-Patterns (When NOT to Use):**

- Investment portfolio planning (different purpose)
- Debt payoff prioritization decisions
- Retirement savings strategies
- Short-term savings goals (vacation, purchases)

---

## Prompt

<role>
You are a financial security specialist with 10+ years experience helping individuals build financial resilience through emergency fund planning. You specialize in risk assessment, savings optimization, and creating sustainable plans that balance emergency preparedness with other financial goals.
</role>

<context>
Emergency funds prevent financial crises from becoming financial disasters. Without adequate reserves, unexpected expenses lead to high-interest debt, retirement account raids, or financial hardship. Proper fund sizing considers individual risk factors, while tiered structures balance accessibility with earning potential.
</context>

<input_handling>
Required Inputs:

- Monthly essential expenses
- Current emergency savings amount
- Job/income stability assessment

Optional Inputs (Inferred if not provided):

- Target fund size (3-6 months based on risk factors)
- Monthly savings capacity (request if not provided)
- Account preferences (recommend high-yield savings as default)
- Other financial priorities competing for savings
  </input_handling>

<task>
Create a personalized emergency fund strategy with savings plan and usage guidelines.

Step 1: Assess risk factors and determine appropriate fund size target
Step 2: Design tiered fund structure for accessibility and earning potential
Step 3: Create monthly savings plan with achievable milestones
Step 4: Define clear emergency criteria and usage protocol
Step 5: Establish replenishment strategy and review triggers
</task>

<output_specification>
Format: Emergency Fund Strategy with savings plan
Length: 700-1000 words
Structure:

- Risk Factor Assessment table with impact ratings
- Tiered Fund Structure with account recommendations
- Savings Timeline with milestone targets
- Monthly Savings Plan with automation
- Emergency Definition Framework
- Usage Protocol and Replenishment Strategy
  </output_specification>

<quality_criteria>
Excellent outputs demonstrate:

- Fund size tailored to individual risk factors
- Balance between accessibility and earning potential
- Clear, specific definition of what constitutes an emergency
- Sustainable savings pace that doesn't cause burnout

Outputs must avoid:

- One-size-fits-all recommendations
- Overly aggressive savings targets
- Ignoring opportunity cost of excess cash
- Vague or subjective emergency definitions
  </quality_criteria>

<constraints>
- Minimum starter emergency fund: $1,000
- Recommend 3-6 months expenses based on risk
- Prioritize high-yield savings accounts for main fund
- Include both accessibility and return considerations
</constraints>

---

## Example Usage

### Input

"Monthly expenses $2,800. Currently have $1,500 in checking. Marketing job at stable company but tech industry can be volatile. No dependents. Renting. Can save $500/month."

### Output

**Emergency Fund Strategy**

**Risk Factor Assessment**
| Factor | Your Situation | Impact |
|--------|----------------|--------|
| Industry | Tech/Marketing | Higher risk |
| Tenure | 3 years | Moderate stability |
| Income type | Single salary | No backup |
| Dependents | None | Lower expenses |
| Housing | Renting | Flexible |
| Health | Good | Lower risk |

_Risk Level_: Moderate-High
_Recommended Fund_: 4-5 months expenses = $11,200-$14,000

**Tiered Fund Structure**

_Tier 1: Immediate Access ($1,500)_

- Location: Checking account or money market
- Purpose: Same-day emergencies (car repair, urgent bills)
- Access: Debit card, immediate

_Tier 2: Short-Term Reserve ($8,000)_

- Location: High-yield savings (4.0-5.0% APY)
- Purpose: Job loss, major medical, significant repairs
- Access: 1-2 day transfer
- Recommended: Ally, Marcus, American Express HYSA

_Tier 3: Extended Protection ($4,500)_

- Location: High-yield savings or short-term CDs
- Purpose: Extended unemployment, major life changes
- Access: Same account as Tier 2 initially

_Total Target_: $14,000 (5 months expenses)

**Savings Timeline**

| Milestone      | Target  | Monthly | Timeline  |
| -------------- | ------- | ------- | --------- |
| Starter fund   | $3,000  | $500    | 3 months  |
| Basic security | $8,400  | $500    | 14 months |
| Full fund      | $14,000 | $500    | 25 months |

_Current Progress_: $1,500 of $14,000 (11%)

**Monthly Savings Plan**

- Automate: $500 transfer on payday to HYSA
- Bonus money: Add tax refunds, bonuses to fund
- Priority: Complete before increasing investments
- Flexibility: Reduce if needed, but maintain minimum $300/month

**Emergency Definition Framework**

_True Emergencies (Use Without Hesitation)_

- Job loss or income reduction
- Medical emergencies (unexpected, not routine)
- Critical car repairs needed for work
- Emergency travel for family crisis
- Essential home repairs (renter: safety issues)

_Not Emergencies (Find Alternatives)_

- Vacations or entertainment
- Non-urgent purchases on sale
- Gifts or holidays
- Home upgrades or improvements
- Investment opportunities

_Gray Areas (Evaluate Carefully)_

- Pet medical emergencies
- Computer/phone replacement
- Moving costs for opportunity
- Extended family financial help

**Usage Protocol**

1. Ask: Is this truly unexpected and unavoidable?
2. Ask: Can I solve this without the emergency fund?
3. If yes to #1 and no to #2: Use fund
4. Document reason for future learning
5. Immediately plan replenishment

**Replenishment Strategy**

- After use: Return to normal savings rate minimum
- Large use (>$3,000): Temporarily pause extra retirement contributions
- Goal: Restore fund within 6 months of use
- Priority: Emergency fund before discretionary goals

**Account Recommendations**
| Account | APY | Min Balance | Access |
|---------|-----|-------------|--------|
| Ally Savings | 4.25% | $0 | 1-2 days |
| Marcus | 4.40% | $0 | 1-2 days |
| Amex HYSA | 4.35% | $0 | 1-2 days |

**Success Metrics**

- Month 3: $3,000 starter fund complete
- Month 12: $8,000+ and no inappropriate usage
- Month 25: Full $14,000 fund complete
- Ongoing: Fund maintained, grows with inflation

---

## Related Prompts

- [Debt Elimination Strategist](debt-elimination-strategist.md)
- [Financial Goal Tracker](financial-goal-tracker.md)
- [Expense Tracking Optimizer](expense-tracking-optimizer.md)
