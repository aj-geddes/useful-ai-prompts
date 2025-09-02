# Financial Modeling Expert

## Metadata
- **Created**: 2025-07-28

- **Category**: Analysis
- **Tags**: financial modeling, valuation, DCF analysis, financial forecasting, investment analysis
- **Use Cases**: financial modeling, forecasting, valuation analysis, investment planning
- **Version**: 2.0.0
- **Use Cases**: company valuation, investment decisions, M&A analysis, financial planning
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical financial modeling and valuation assistant that helps you build models, value companies, and make investment decisions. Provide your company details and I'll create comprehensive financial analysis with multiple valuation approaches.

## Prompt

```
I'll help you build a financial model and valuation analysis. Let me gather information about the company and your modeling needs.

About the company:
1. What company/asset are you valuing? (name, industry, size)
2. What's the purpose? (investment decision, M&A, planning, fundraising)
3. What stage is the company? (startup, growth, mature, turnaround)
4. What's the business model? (subscription, transaction, product sales, etc.)

Financial information:
5. What historical financials do you have? (years, quality, audited?)
6. Current revenue and growth rate?
7. Current margins (gross, EBITDA, net)?
8. Capital structure (debt, equity, cash)?

Assumptions and market:
9. What are your growth assumptions for the next 5 years?
10. Who are the main competitors or comparable companies?
11. What are the key risks and opportunities?
12. What's your target return or hurdle rate?

Based on your answers, I'll provide:

**1. THREE-STATEMENT MODEL** - Income statement, balance sheet, cash flow projections
**2. DCF VALUATION** - Intrinsic value based on cash flows
**3. COMPARABLE ANALYSIS** - Trading and transaction multiples
**4. SCENARIO ANALYSIS** - Bull, base, and bear cases
**5. INVESTMENT RECOMMENDATION** - Clear decision with supporting rationale

Please provide the information above for your financial model and valuation.
```

## Example Usage

**User Input:**
```
1. Company: TechFlow Inc., B2B SaaS for workflow automation, $50M revenue
2. Purpose: Considering acquisition, need to determine fair offer price
3. Stage: Growth stage, 7 years old, profitable
4. Business model: Annual subscriptions, 90% recurring revenue

5. Historical: 3 years audited financials, clean books
6. Current: $50M ARR, growing 35% annually
7. Margins: 80% gross, 15% EBITDA, 8% net (reinvesting heavily)
8. Capital: No debt, $20M cash, 10M shares outstanding

9. Growth: Expect 30% yr1-2, 25% yr3, 20% yr4-5, then 10% terminal
10. Comparables: Asana, Monday.com, Smartsheet (but we're smaller)
11. Risks: Competition, customer concentration (top 10 = 30% revenue)
    Opportunities: New AI features, international expansion
12. Target return: 20% IRR minimum for acquisition
```

**Assistant Output:**

Based on TechFlow's profile, here's my comprehensive valuation analysis:

## VALUATION SUMMARY

**Enterprise Value Range: $425M - $525M**
**Recommended Offer: $475M ($47.50/share)**

Key Metrics:
- Current trading: 8.5x-10.5x revenue (vs peers at 6x-12x)
- Implied EBITDA multiple: 57x-70x (high due to growth)
- 5-year IRR at $475M: 22% (exceeds 20% hurdle)

## THREE-STATEMENT MODEL

**Revenue Build:**
```
Year        2024    2025    2026    2027    2028    2029
Revenue     $50M    $65M    $84M    $105M   $126M   $139M
Growth      35%     30%     30%     25%     20%     10%
```

**P&L Projection ($M):**
```
                2024E   2025E   2026E   2027E   2028E
Revenue         50.0    65.0    84.5    105.6   126.7
Gross Profit    40.0    52.0    67.6    84.5    101.4
 (80% margin)
Operating Exp   32.5    39.0    47.2    54.9    60.8
EBITDA          7.5     13.0    20.4    29.6    40.6
 (% margin)     15%     20%     24%     28%     32%
D&A             2.0     2.6     3.4     4.2     5.1
EBIT            5.5     10.4    17.0    25.4    35.5
Tax (25%)       1.4     2.6     4.3     6.4     8.9
Net Income      4.1     7.8     12.8    19.1    26.6
```

**Key Assumptions:**
- Margin expansion: 15% → 32% EBITDA (scale benefits)
- Sales efficiency improves → CAC payback 14 → 10 months
- Churn remains low: 5% annually
- No debt needed (self-funding growth)

## DCF VALUATION

**WACC Calculation:**
```
Risk-free rate:        4.0%
Equity premium:        7.0%
Beta (SaaS):          1.4
Cost of equity:       13.8%
WACC (no debt):       13.8%
```

**Free Cash Flow ($M):**
```
                2024E   2025E   2026E   2027E   2028E   Terminal
EBIT            5.5     10.4    17.0    25.4    35.5    
Tax             (1.4)   (2.6)   (4.3)   (6.4)   (8.9)
NOPAT           4.1     7.8     12.8    19.1    26.6
+ D&A           2.0     2.6     3.4     4.2     5.1
- CapEx         (1.0)   (1.3)   (1.7)   (2.1)   (2.5)
- Δ NWC         (2.0)   (3.0)   (3.9)   (4.2)   (4.2)
FCF             3.1     6.1     10.6    17.0    25.0    275.0*

*Terminal value at 3% growth

PV of FCF:      $51M
PV of Terminal: $385M
Enterprise Value: $436M
```

## COMPARABLE COMPANY ANALYSIS

**Public SaaS Comparables:**
```
Company         EV/Rev  EV/Rev   Rev      Rule
                (NTM)   (2yr)    Growth   of 40
Asana           6.2x    4.8x     25%      30
Monday.com      9.5x    6.9x     38%      45
Smartsheet      5.8x    4.5x     22%      28
ServiceNow      12.1x   9.2x     23%      42

Average         8.4x    6.4x     27%      36
TechFlow        8.5x    6.5x     35%      50 ✓

Implied EV: $425M (at peer average)
```

**Recent M&A Transactions:**
```
Target          Buyer       EV/Rev  Premium  Strategic
WorkflowCo      Oracle      11.2x   45%      High
ProcessAI       Salesforce  9.8x    38%      High  
AutomateHub     Microsoft   10.5x   42%      Medium

Average M&A multiple: 10.5x
Implied value with 40% premium: $525M
```

## SCENARIO ANALYSIS

```
Scenario        Probability  Value    IRR     Key Assumptions
Bull Case       20%         $625M    28%     40% growth, AI success
Base Case       60%         $475M    22%     Plan case execution
Bear Case       20%         $325M    14%     20% growth, competition

Expected Value: $485M
```

**Sensitivity Analysis (EV):**
```
                Terminal Growth
WACC        2%      3%      4%      5%
11%         $520M   $545M   $575M   $615M
12%         $470M   $490M   $515M   $545M
13%         $425M   $445M   $465M   $490M
14%         $390M   $405M   $425M   $445M
15%         $360M   $375M   $390M   $410M
```

## INVESTMENT RECOMMENDATION

**RECOMMENDATION: PROCEED WITH ACQUISITION AT $475M**

**Rationale:**
1. **Attractive Growth**: 35% growth vs peer average 27%
2. **Margin Expansion**: Clear path from 15% to 30%+ EBITDA
3. **Strategic Fit**: Complementary to your enterprise suite
4. **Reasonable Valuation**: 9.5x forward revenue in-line with quality SaaS

**Deal Structure Suggestion:**
- Base price: $425M (8.5x)
- Performance earnout → Up to $50M based on 2025 targets
- Management retention: 3-year vesting for key personnel
- Escrow: 10% for 18 months (reps & warranties)

**Key Risks to Monitor:**
1. Customer concentration (implement expansion strategy)
2. Competition from majors (leverage your distribution)
3. Technology risk (invest in R&D post-close)

**Integration Value Drivers:**
- Cross-sell to your 5,000 enterprise customers
- Reduce TechFlow's S&M spend by 30%
- Accelerate international expansion
- Bundle with existing products

**Expected Returns:**
- Standalone IRR: 22%
- With synergies IRR: 28-32%
- Payback period: 4.5 years

Would you like me to detail any specific aspect further, such as the integration plan or financing structure?

## Related Prompts

- [M&A Deal Analyzer](../career-development/skill-gap-analyzer.md)
- [Investment Decision Analyst](../financial-planning/real-estate-investment-analyst.md)
- [Financial Due Diligence Expert](financial-modeling-expert.md)
