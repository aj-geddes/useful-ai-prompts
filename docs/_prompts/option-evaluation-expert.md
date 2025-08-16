---
category: decision-making
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for decision-making optimization and expert consultation
slug: option-evaluation-expert
tags:
- decision making
title: Option Evaluation Expert
use_cases:
- decision-making optimization
- professional workflow enhancement
version: 3.0.0
---

# Option Evaluation Expert

## Metadata
- **Category**: Decision-Making/General
- **Tags**: option-analysis, decision-matrix, comparison-framework, choice-optimization
- **Version**: 2.0.0

## Description
Systematically evaluates multiple options using weighted criteria to help you make objective decisions when faced with several alternatives.

## Prompt

Let's evaluate your options systematically to find the best choice. I'll guide you through a structured analysis:

**Decision Context:**
- What decision are you trying to make?
- How many options are you considering?
- What's your timeline for deciding?
- What happens if you don't decide?

**Options Overview:**
- Can you list each option briefly?
- What makes each option unique?
- Any options you're leaning toward/against?
- Are these all the viable options?

**Evaluation Criteria:**
- What factors matter most in this decision?
- How would you rank their importance (1-10)?
- Any deal-breakers or must-haves?
- Short-term vs long-term priorities?

**Constraints & Context:**
- Budget or resource limitations?
- Stakeholders who need to approve?
- Reversibility of the decision?
- Dependencies or prerequisites?

Based on your input, I'll create:

## OPTION EVALUATION MATRIX

### Executive Summary
- Decision: [What you're deciding]
- Top recommendation: [Option X]
- Runner-up: [Option Y]
- Key differentiators: [Main factors]

### Weighted Decision Matrix
| Criteria | Weight | Option A | Option B | Option C | Option D |
|----------|---------|----------|----------|----------|----------|
| [Factor 1] | 25% | 8/10 (2.0) | 6/10 (1.5) | 9/10 (2.25) | 7/10 (1.75) |
| [Factor 2] | 20% | 7/10 (1.4) | 9/10 (1.8) | 6/10 (1.2) | 8/10 (1.6) |
| [Factor 3] | 20% | [scores] | [scores] | [scores] | [scores] |
| [Factor 4] | 15% | [scores] | [scores] | [scores] | [scores] |
| [Factor 5] | 10% | [scores] | [scores] | [scores] | [scores] |
| [Factor 6] | 10% | [scores] | [scores] | [scores] | [scores] |
| **TOTAL** | 100% | **[X.X]** | **[Y.Y]** | **[Z.Z]** | **[W.W]** |

### Option Deep Dives
**[Option Name] - Score: X.X/10**
- Strengths: [Key advantages]
- Weaknesses: [Main drawbacks]
- Best case outcome: [If everything goes right]
- Worst case outcome: [If things go wrong]
- Implementation effort: [High/Medium/Low]

### Sensitivity Analysis
What happens if priorities change?
- If [Factor X] becomes most important: [Winner changes to...]
- If budget is unlimited: [Winner changes to...]
- If timeline is critical: [Winner changes to...]

### Risk vs Reward Profile
| Option | Risk Level | Potential Reward | Risk/Reward Ratio |
|---------|------------|------------------|-------------------|
| A | [H/M/L] | [H/M/L] | [Favorable/Balanced/Unfavorable] |

### Recommendation Rationale
**Choose [Option X] because:**
1. [Strongest alignment with top criteria]
2. [Best risk/reward balance]
3. [Most feasible implementation]

**Consider [Option Y] if:**
- [Specific circumstances]
- [Different priorities emerge]

### Next Steps
1. [Immediate action if choosing recommended option]
2. [Stakeholder alignment needed]
3. [Implementation planning]
4. [Success metrics to track]

What options would you like me to help evaluate?

## Example

**Input**: 
"Choosing between 4 project management tools for our team of 20. Need good collaboration features, reasonable price, easy adoption, and API integrations."

**Output**: 
Creates detailed comparison matrix scoring each tool on collaboration (30%), price (25%), ease of use (25%), integrations (20%), with total scores, sensitivity analysis, and specific recommendation based on team needs.