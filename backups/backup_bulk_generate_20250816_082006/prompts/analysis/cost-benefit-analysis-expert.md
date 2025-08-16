# Cost-Benefit Analysis Expert

## Metadata

- **Category**: Analysis
- **Tags**: cost-benefit analysis, ROI calculation, investment evaluation, financial modeling, decision analysis
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: project evaluation, investment decisions, resource allocation, business case development
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical cost-benefit analysis assistant that helps you evaluate projects, investments, and strategic decisions. Provide your project details and I'll deliver a comprehensive financial analysis with clear recommendations.

## Prompt

```
I'll help you conduct a thorough cost-benefit analysis for your project or investment decision. Let me gather some information to provide accurate financial insights.

About your project:
1. What project or investment are you evaluating?
2. What's the total estimated investment amount?
3. What's your implementation timeline?
4. What are the main expected benefits?

Financial context:
5. What's your organization's hurdle rate or required return?
6. Over what time period should we analyze (e.g., 5 years, 10 years)?
7. What's your cost of capital or discount rate?
8. Are there any budget constraints or limits?

Risk factors:
9. What are the main risks that could impact costs or benefits?
10. How confident are you in your estimates? (High/Medium/Low)
11. Are there any regulatory or compliance considerations?
12. What alternatives are you considering (including "do nothing")?

Based on your answers, I'll provide:

**1. FINANCIAL SUMMARY** - NPV, IRR, payback period, and ROI
**2. COST BREAKDOWN** - Direct, indirect, and hidden costs
**3. BENEFIT ANALYSIS** - Quantified benefits and value drivers  
**4. RISK ASSESSMENT** - Sensitivity analysis and scenarios
**5. RECOMMENDATION** - Clear go/no-go decision with rationale

I'll present the analysis in clear tables and visualizations to support your decision-making.

Please provide the information above for your cost-benefit analysis.
```

## Example Usage

**User Input:**
```
1. Project: Implementing a new CRM system for our sales team
2. Investment: $250,000 total (software, implementation, training)
3. Timeline: 6 months to implement, expecting benefits starting month 7
4. Benefits: Increase sales efficiency, better customer insights, reduced admin time

5. Hurdle rate: 15% annual return minimum
6. Analysis period: 5 years
7. Discount rate: 10% (our WACC)
8. Budget constraint: Must stay under $300K total

9. Main risks: User adoption might be slow, integration complexity, data migration issues
10. Confidence: Medium - based on vendor quotes and industry benchmarks
11. Regulatory: Need to ensure GDPR compliance for customer data
12. Alternatives: Keep current system (no cost but losing opportunities), or basic upgrade for $50K
```

**Assistant Output:**

Based on your CRM implementation project, here's my comprehensive cost-benefit analysis:

## FINANCIAL SUMMARY

**Key Investment Metrics:**
```
NPV (5 years):        $287,450
IRR:                  38%
Payback Period:       2.1 years  
ROI:                  215%
Benefit-Cost Ratio:   2.15
```

✅ **All metrics exceed your requirements** - Strong financial case

## COST BREAKDOWN

**Total 5-Year Costs: $398,000**

```
Initial Investment (Year 0):
├── Software Licenses:         $80,000
├── Implementation:           $120,000
├── Training:                 $30,000
├── Data Migration:           $20,000
└── Subtotal:                $250,000

Ongoing Annual Costs:
├── Maintenance (15%):        $12,000
├── Support:                  $6,000
├── Additional Training:      $5,000
└── Annual Total:            $23,000

Hidden Costs Identified:
├── Productivity Dip (3 mo):  $45,000
├── IT Resources:             $15,000
├── Change Management:        $18,000
└── Hidden Total:            $78,000
```

## BENEFIT ANALYSIS

**Total 5-Year Benefits: $856,000**

```
Annual Benefit Breakdown:
                          Year 1   Year 2   Year 3   Year 4   Year 5
Sales Efficiency Gains    $65,000  $95,000  $110,000 $120,000 $125,000
├── 20% time savings
└── 15 more deals/year

Customer Retention        $25,000  $40,000  $45,000  $50,000  $55,000  
├── 5% better retention
└── Higher lifetime value

Admin Cost Reduction      $20,000  $24,000  $24,000  $24,000  $24,000
├── 2 hours/day saved
└── Automated reporting

Total Annual Benefits     $110,000 $159,000 $179,000 $194,000 $204,000
```

**Note:** Year 1 benefits start in month 7 (post-implementation)

## RISK-ADJUSTED SCENARIOS

**Sensitivity Analysis:**

```
Scenario              NPV        IRR    Payback   Probability
Best Case (+20%)      $412,000   52%    1.7 yrs   20%
Base Case            $287,450   38%    2.1 yrs   50%
Worst Case (-30%)    $124,000   21%    3.2 yrs   25%
Failure Case         -$178,000  -15%   Never      5%

Expected Value: $278,325 (probability-weighted)
```

**Critical Success Factors:**
1. User adoption rate must exceed 70% by month 9
2. Data migration must be 95%+ accurate
3. Integration downtime must be under 48 hours

## COMPARATIVE ANALYSIS

```
Option              NPV        Initial Cost   Risk    Strategic Fit
CRM Implementation  $287,450   $250,000      Medium  High
Basic Upgrade      $45,000    $50,000       Low     Low  
Status Quo         -$156,000  $0            High    Poor

Opportunity Cost of Inaction: $443,450 over 5 years
```

## RECOMMENDATION

**DECISION: PROCEED WITH CRM IMPLEMENTATION**

**Rationale:**
- 38% IRR significantly exceeds 15% hurdle rate
- Payback in 2.1 years provides quick value
- Even worst-case scenario (21% IRR) exceeds requirements
- Strategic benefits beyond financials

**Implementation Approach:**
1. **Phase 1** (Months 1-2): Core CRM setup, pilot with top performers
2. **Phase 2** (Months 3-4): Full rollout with intensive training  
3. **Phase 3** (Months 5-6): Advanced features and optimization

**Risk Mitigation Plan:**
- Appoint dedicated change champion
- Create super-user program for peer support
- Set aside $25K contingency for additional training
- Establish weekly adoption metrics tracking

**Key Milestones:**
- Month 2: Successful pilot (10 users, 90% satisfaction)
- Month 4: 50% team actively using system
- Month 6: 85% adoption, first ROI evidence
- Month 9: Full benefits realization begins

Would you like me to detail any specific aspect further, such as the implementation timeline or create a presentation-ready executive summary?

## Related Prompts

- [ROI Calculator](./roi-calculator.md)
- [Risk Assessment Expert](./risk-assessment-specialist.md)
- [Financial Modeling Expert](./financial-modeling-expert.md)
