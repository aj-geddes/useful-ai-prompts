---
category: business
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for business optimization and expert consultation
slug: financial-model-builder
tags:
- business
title: Financial Model Builder
use_cases:
- business optimization
- professional workflow enhancement
version: 3.0.0
---

# Financial Model Builder

## Metadata

- **Category**: Business/Finance
- **Tags**: financial modeling, financial analysis, forecasting, valuation, scenario planning
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: financial planning, investment analysis, budgeting, valuation models
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you build comprehensive financial models for business planning, investment analysis, and decision-making with proper structure, assumptions, and scenario analysis.

## Prompt

```
I'll help you build a robust financial model tailored to your needs. Let me understand your requirements:

**Model purpose:**
1. What type of financial model do you need? (DCF, LBO, budget, forecast, etc.)
2. What key decisions will this model support?
3. Who's the audience? (investors, management, lenders)
4. What time horizon? (3 years, 5 years, etc.)

**Business context:**
5. What industry/business are you modeling?
6. What's the revenue model?
7. What are the key cost drivers?
8. Any unique business characteristics?

**Data and assumptions:**
9. What historical data do you have?
10. What are your growth assumptions?
11. Any market benchmarks to consider?
12. What scenarios need to be modeled?

Based on your answers, I'll provide:

**MODEL ARCHITECTURE** - Structure and components
**KEY ASSUMPTIONS** - Driver-based inputs and rationale
**FINANCIAL PROJECTIONS** - P&L, cash flow, balance sheet
**SCENARIO ANALYSIS** - Sensitivity and what-if analysis
**VALUATION OUTPUT** - Metrics and investment returns

Share your modeling needs and let's build something powerful!
```

## Example Usage

**User Input:**
```
1. 5-year DCF model for SaaS company acquisition
2. Support buy/hold/pass decision, determine fair valuation and IRR potential
3. Investment committee presentation - PE firm considering majority stake
4. 5-year projection plus terminal value

5. B2B SaaS - project management software for enterprises
6. Subscription model: $50-200/user/month, annual contracts, 500 customers, 50K total users
7. Main costs: Cloud hosting (20% of revenue), Sales (30%), R&D (25%), G&A (15%)
8. High growth, 90% gross margins, 110% net revenue retention, 18-month payback

9. 3 years historicals: Growing 60% YoY, $15M current ARR, EBITDA breakeven
10. Expect 45% growth Y1-2, 35% Y3, 25% Y4-5, then 15% terminal
11. Public SaaS comps trade at 8-12x revenue, 25-35x EBITDA
12. Need base, upside, and downside cases, plus sensitivity analysis
```

**Assistant Output:**

Here's a comprehensive DCF model structure for your SaaS acquisition:

## MODEL ARCHITECTURE

### Workbook Structure

```
Tab Structure:
1. Executive Summary - Key outputs and investment thesis
2. Assumptions - All inputs and drivers
3. Revenue Build - Detailed revenue model
4. Operating Model - P&L projections
5. Cash Flow - FCF and working capital
6. Balance Sheet - Pro forma statements
7. Valuation - DCF, comps, returns
8. Scenarios - Sensitivity analysis
9. Data Room - Historical financials
```

### Model Flow Diagram

```
Assumptions → Revenue Model → Operating Model → Free Cash Flow
                    ↓              ↓                ↓
                Cohort Analysis  EBITDA          Terminal Value
                                   ↓                ↓
                              Valuation → IRR & Returns
```

## KEY ASSUMPTIONS

### Revenue Drivers

**Customer & User Growth**:
```
Base Case Assumptions:
                    Y0      Y1      Y2      Y3      Y4      Y5
Customers          500     700     950    1,235   1,544   1,853
Growth %            -      40%     36%     30%     25%     20%
Users/Customer     100     105     110     115     120     125
Total Users      50,000  73,500  104,500 142,025 185,280 231,625
```

**Pricing & Retention**:
```
ARPU (Annual)     $3,600  $3,780  $3,969  $4,127  $4,292  $4,464
Price Increase      -      5%      5%      4%      4%      4%
Gross Retention    90%     91%     92%     92%     93%     93%
Net Retention     110%    112%    113%    113%    112%    110%
```

**Revenue Build**:
```
ARR Calculation:
Starting ARR                $15.0M
+ New ARR                   $11.3M
+ Expansion ARR              $3.0M
- Churn                    ($2.3M)
= Ending ARR                $27.0M

Y1 Revenue (GAAP)           $21.0M (avg of starting/ending)
```

### Cost Structure

**Operating Expenses**:
```
% of Revenue:        Y1     Y2     Y3     Y4     Y5
Cloud/Hosting       20%    19%    18%    17%    16%
Sales & Marketing   35%    33%    31%    29%    28%
R&D                 25%    24%    23%    22%    21%
G&A                 15%    14%    13%    12%    11%
Total OpEx          95%    90%    85%    80%    76%
EBITDA Margin        5%    10%    15%    20%    24%
```

## FINANCIAL PROJECTIONS

### Income Statement (Base Case)

```
($M)                Y0     Y1     Y2     Y3     Y4     Y5
Revenue           15.0   21.0   30.5   41.9   53.8   66.0
Growth %            -    40%    45%    37%    28%    23%

Gross Profit      13.5   18.9   27.4   37.7   48.4   59.4
Gross Margin      90%    90%    90%    90%    90%    90%

Operating Expenses:
S&M                4.5    7.4    10.1   13.0   15.6   18.5
R&D                3.8    5.3    7.3    9.6    11.8   13.9
G&A                2.3    3.2    4.3    5.4    6.5    7.3
Total OpEx        10.5   15.8   21.7   28.0   33.9   39.6

EBITDA             3.0    3.2    5.8    9.7   14.5   19.8
EBITDA Margin      20%    15%    19%    23%    27%    30%
```

### Free Cash Flow

```
($M)                Y1     Y2     Y3     Y4     Y5
EBITDA             3.2    5.8    9.7   14.5   19.8
- Taxes (25%)     (0.8)  (1.4)  (2.4)  (3.6)  (4.9)
NOPAT              2.4    4.3    7.3   10.9   14.8

- CapEx           (0.4)  (0.6)  (0.8)  (1.1)  (1.3)
- NWC Change      (1.2)  (1.5)  (1.7)  (1.8)  (1.9)
FCF                0.8    2.2    4.7    8.0   11.6

FCF Margin         3.7%   7.1%  11.3%  14.9%  17.6%
```

### Terminal Value

```
Terminal Year (Y5) Metrics:
Revenue: $66.0M
EBITDA: $19.8M
FCF: $11.6M

Terminal Growth: 15% (conservative vs 20%+ market growth)
Terminal Multiple: 10x EBITDA (mid-range of comps)
Terminal Value: $198M

Alternative - Gordon Growth:
Terminal FCF: $11.6M × 1.15 = $13.3M
WACC - Terminal Growth: 20% - 15% = 5%
Terminal Value: $13.3M / 5% = $267M
```

## SCENARIO ANALYSIS

### Three Cases

**Base Case** (50% probability):
- Revenue CAGR: 33%
- Exit EBITDA Margin: 30%
- Enterprise Value: $140M
- IRR: 28%

**Upside Case** (25% probability):
- Revenue CAGR: 40%
- Exit EBITDA Margin: 35%
- Enterprise Value: $185M
- IRR: 38%

**Downside Case** (25% probability):
- Revenue CAGR: 25%
- Exit EBITDA Margin: 22%
- Enterprise Value: $95M
- IRR: 15%

**Probability-Weighted Return**: 27%

### Sensitivity Analysis

**Impact on Enterprise Value**:
```
                   Revenue Growth Rate
                25%    30%    35%    40%    45%
Terminal     8x  $95   $115   $135   $155   $175
Multiple    10x  $110  $135   $160   $185   $210
           12x  $125  $155   $185   $215   $245

Most Sensitive Variables:
1. Net Revenue Retention (±10% = ±$40M EV)
2. CAC Payback (±6mo = ±$25M EV)
3. Terminal Multiple (±2x = ±$35M EV)
```

## VALUATION OUTPUT

### DCF Valuation

```
Enterprise Value Calculation:
                         ($M)
PV of FCF (Y1-5)        $18.5
PV of Terminal Value   $121.5
Enterprise Value       $140.0

Less: Net Debt         ($5.0)
Equity Value          $135.0
```

### Returns Analysis

**Investment Metrics**:
```
Purchase Price: $100M (7.5x current revenue)
Exit Value: $140M (projected)
Hold Period: 5 years

IRR: 28%
Money Multiple: 2.8x
Annual FCF Yield: Growing from 1% to 12%
```

### Comparable Company Analysis

```
Public SaaS Comparables:
               Revenue  Revenue  EBITDA
Company        Growth   Multiple Multiple
Atlassian      35%      15.2x    45.3x
Monday.com     40%      12.5x    N/M
Asana          28%       8.7x    N/M
Smartsheet     32%      10.1x    38.2x

Average        34%      11.6x    41.8x
Target Co.     33%       9.3x    35.0x
```

### Investment Recommendation

**Bull Case**:
- Strong unit economics (110% NRR, 18mo payback)
- Proven product-market fit
- Attractive entry multiple vs comps
- Clear path to 30%+ EBITDA margins

**Bear Case**:
- Competitive market
- Platform risk (relies on integrations)
- Key person dependency
- Limited pricing power

**Recommendation**: **BUY** at up to $110M
- Target 25%+ IRR achievable
- Multiple expansion opportunity
- Strong FCF generation by Y3
- Strategic value to portfolio

### Model Assumptions Requiring Diligence

1. Customer concentration and churn
2. Competitive differentiation sustainability
3. Sales efficiency metrics/magic number
4. Technical debt and platform scalability
5. Management team depth

This model provides a solid framework for your investment decision with appropriate sensitivity to key value drivers.

## Related Prompts

- [Investment Analysis Expert](./investment-analysis-expert.md)
- [Valuation Specialist](./valuation-expert.md)
- [Financial Due Diligence Expert](./due-diligence-expert.md)