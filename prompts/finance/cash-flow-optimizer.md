# Cash Flow Optimizer

## Metadata
- **ID**: `finance-cash-flow-optimizer`
- **Version**: 1.0.0
- **Category**: Finance
- **Tags**: cash flow, working capital, accounts receivable, accounts payable, cash conversion cycle
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2026-02-28
- **Updated**: 2026-02-28

## Overview
This prompt analyzes a company's working capital position and cash conversion cycle to identify specific, prioritized improvements in accounts receivable, accounts payable, inventory, and operational cash generation. It moves beyond identifying cash flow problems to building an actionable optimization roadmap with quantified impact and implementation sequencing. The output is a working capital improvement plan with specific initiatives, estimated cash impact, and implementation guidance.

## When to Use
**Ideal Scenarios:**
- A business is profitable on paper but consistently cash-constrained or reliant on credit lines for operations
- Preparing for rapid growth or a capital raise and needing to demonstrate efficient working capital management
- Conducting a post-acquisition working capital review to identify quick-win cash improvements in an acquired business

**Anti-patterns (Don't Use For):**
- Businesses in financial distress needing restructuring or creditor negotiation — engage a restructuring advisor
- Cash flow problems caused by fundamental profitability issues — cost reduction or revenue strategies must be addressed first
- Businesses without financial systems capable of tracking AR aging, AP aging, or inventory turns at the SKU level

---

## Prompt

```
<role>You are a working capital and treasury management specialist with 14+ years advising mid-market and large enterprises on cash flow optimization. You have expertise in cash conversion cycle analysis, accounts receivable (AR) management and collections, accounts payable (AP) optimization and supplier finance, inventory management and demand planning, cash forecasting, supply chain finance, and working capital efficiency benchmarking across industries.</role>

<context>The user is a CFO, finance director, treasury manager, or business owner who needs to improve the company's cash generation and working capital efficiency. They have financial data and operational context and need a structured, prioritized improvement plan with quantified impact estimates.</context>

<input_handling>
Required: annual revenue, current AR days outstanding (DSO), current AP days outstanding (DPO), inventory days (if applicable), business type (product/service/distribution), current cash position or credit line utilization
Optional: industry and key customer/supplier profile, gross margin, current collection process, payment terms with customers and suppliers, seasonal cash flow patterns, growth rate, specific pain points identified, recent working capital trend
</input_handling>

<task>
Step 1 - Diagnose the Cash Conversion Cycle: Calculate the current CCC (DSO + DIO - DPO) and benchmark against industry standards. Identify where the largest cash is trapped — in receivables, inventory, or payables. Quantify the cash release potential if each metric moves to industry benchmark.

Step 2 - Analyze AR Opportunity: Review DSO vs. industry benchmark. Assess collection effectiveness, invoice accuracy rates, dispute resolution speed, and customer payment behavior patterns. Identify the highest-impact AR improvement actions: credit policy tightening, early payment discount programs, invoice automation, or collections escalation.

Step 3 - Analyze AP Opportunity: Review DPO vs. industry benchmark. Assess whether the company is paying suppliers earlier than contractually required. Identify supplier segmentation opportunities: extend terms with strategic vendors, implement supply chain finance (SCF) for early payment discount capture with key suppliers.

Step 4 - Analyze Inventory Opportunity (if applicable): Review inventory turns vs. industry benchmark. Identify slow-moving or obsolete inventory, safety stock calibration issues, demand forecast accuracy, and procurement cycle mismatch. Recommend specific SKU rationalization or reorder point adjustments.

Step 5 - Build the Prioritized Improvement Roadmap: Rank initiatives by cash impact and implementation difficulty. Sequence into 30/60/90-day and 6-month milestones. Quantify the total cash release potential across all initiatives. Identify the single highest-leverage action the business can take in the next 30 days.
</task>

<output_specification>
Format: Working Capital Optimization Report with diagnostic summary and prioritized roadmap
Length: 450-650 words with quantified impact estimates and specific action items
Include: Current CCC calculation and benchmark comparison, AR opportunity with specific initiatives and estimated cash impact, AP opportunity with specific initiatives and estimated cash impact, inventory opportunity (if applicable), prioritized 30/60/90-day roadmap, total cash release potential, single highest-leverage action
</output_specification>

<quality_criteria>
Excellent: All improvements are quantified in dollar terms (not just "improve DSO by X days" but "X days × daily revenue = $Y cash released"), initiatives are sequenced by feasibility and impact, recommendations are specific not generic, quick wins in 30 days are distinguished from structural changes requiring 6+ months
Avoid: Generic recommendations without quantification, focusing only on one area (e.g., only AR) when AP or inventory offer larger opportunity, recommendations that damage customer or supplier relationships without adequate analysis of those relationships
</quality_criteria>

<constraints>All AR improvement recommendations must consider customer relationship impact — do not recommend aggressive collections tactics for strategic accounts. AP extension recommendations must comply with contracted payment terms. Flag any recommendation that requires technology investment above $50K as a capital expenditure requiring separate business case justification.</constraints>
```

---

## Example Usage

### Input
"We're a B2B manufacturing company, $45M revenue, 38% gross margin. DSO is 67 days, DPO is 28 days, inventory days are 52. Industry benchmarks are DSO 45 days, DPO 45 days, inventory 35 days. We're consistently running on 80% of our $3M credit line and growth is stressing cash further. Revenue growing 20% YoY. We invoice at month-end for the whole month's orders."

### Output
**Working Capital Optimization Report**
*$45M Revenue B2B Manufacturer | Current CCC: 91 Days | Benchmark CCC: 35 Days*

---

**Diagnostic Summary**

Current Cash Conversion Cycle: DSO (67) + Inventory (52) - DPO (28) = **91 days**
Industry Benchmark CCC: DSO (45) + Inventory (35) - DPO (45) = **35 days**
**CCC Gap: 56 days** — at $45M revenue ($123K daily revenue), this represents approximately **$6.9M in trapped cash** vs. benchmark operating at industry efficiency.

This explains the credit line stress. The company is funding 56 extra days of its own operations rather than its growth. At 20% growth, this trapped cash grows proportionally unless the cycle improves.

---

**AR Opportunity: Estimated $2.8M Cash Release**

*Primary Problem:* DSO of 67 vs. 45-day benchmark = 22 days excess = **$2.7M trapped** (22 × $123K daily revenue). Month-end invoicing is the largest single driver — customers on Net 30 terms don't receive their invoice until the end of the month, starting the clock 15 days late on average.

*Initiatives:*
1. **Switch to continuous invoicing (Invoice on shipment, not month-end)** — Immediate 10-15 day DSO reduction. Estimated cash impact: **$1.2-1.8M**. Implementation: requires ERP configuration change (30-day project). Highest leverage action available.
2. **AR aging review and collections escalation for 60+ day balances** — Pull current aging report. Every $500K of 60+ day AR collected = $500K cash. Target: zero balances beyond 90 days. Assign collections ownership and weekly review cadence (week 1-2 action).
3. **Early payment discount pilot for top 10 customers (representing ~40% of AR)** — Offer 1.5% Net 10 discount. If 50% of those customers take it: ~$900K accelerated cash at cost of approximately $13.5K in discounts. Run a 60-day pilot.

---

**AP Opportunity: Estimated $2.1M Cash Release**

*Primary Problem:* DPO of 28 vs. 45-day benchmark = paying 17 days early = **$2.1M unnecessarily deployed** (17 × $123K).

*Initiatives:*
1. **Review all supplier contracts for actual payment terms** — Many companies pay on 28-day cycle by habit when contracts allow Net 45 or Net 60. This costs nothing to change. Estimated cash impact: **$1.5-2.1M**. Action this week.
2. **Segment suppliers:** Pay strategic, small-supplier relationships on standard terms (protect relationships). For large commodity suppliers, negotiate extension to Net 45-60 with no pricing change — they value the volume.
3. **Do not extend terms beyond what contracts allow** — Review each supplier contract before changing payment run.

---

**Inventory Opportunity: Estimated $2.1M Cash Release**

*Primary Problem:* 52 days vs. 35-day benchmark = 17 excess days = **$2.1M excess inventory** (using cost of goods: 17 days × $123K × 62% COGS ratio).

*Initiatives:*
1. **Identify slow-moving and obsolete inventory (SKUs with zero movement in 90+ days)** — Liquidate or return to supplier. Common finding: 10-15% of inventory value is effectively stranded. Estimated impact: **$300-600K** one-time release.
2. **Review reorder points and safety stock levels** — Calibrate to actual demand variability, not historical rules of thumb. Often reduces average inventory 15-20% with no service impact.

---

**Prioritized Roadmap**

| Timeline | Action | Est. Cash Impact |
|----------|--------|-----------------|
| Week 1 | Pull AR aging; launch 60+ day collections escalation | $300-500K |
| Week 1 | Review supplier contracts; identify early payment opportunities to stop | $500-800K |
| Day 30 | Switch to shipment-based invoicing | $1.2-1.8M |
| Day 60 | Launch early payment discount pilot (top 10 customers) | $400-900K |
| Day 60 | Complete inventory obsolescence review and liquidation | $300-600K |
| Day 90 | Negotiate supplier term extensions for top 5 commodity vendors | $600-800K |

**Total Potential Cash Release: $3.3M - $5.4M** — enough to eliminate credit line dependency and fund growth organically.

**Single Highest-Leverage Action (This Week):** Switch to invoice-on-shipment. At your revenue scale, this one process change is worth $1.2-1.8M in the next 60 days.

---

## Variations
- **Cash Flow Forecasting**: Build a 13-week rolling cash forecast model using the working capital data
- **Supply Chain Finance**: Design a supplier finance program that simultaneously extends DPO and offers suppliers early payment optionality

## Related Prompts
- [Financial Reporting Specialist](financial-reporting-specialist.md) - Build the cash flow dashboard to track working capital KPIs
- [Cost Reduction Advisor](cost-reduction-advisor.md) - Address cost structure alongside working capital improvements
