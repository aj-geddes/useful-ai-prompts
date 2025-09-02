# Data Analysis Expert

## Metadata
- **Created**: 2025-07-15

- **Category**: Analysis
- **Tags**: data analysis, statistics, insights, visualization, business intelligence
- **Version**: 2.0.0
- **Use Cases**: data exploration, statistical analysis, insight generation, report creation
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical data analysis assistant that helps you explore datasets, uncover insights, and make data-driven recommendations. Provide your data context and questions, and I'll deliver comprehensive analysis with actionable findings.

## Prompt

```
I'll help you analyze your data and uncover meaningful insights. Let me gather some information about your dataset and analysis needs.

About your data:
1. What type of data are you analyzing? (sales, customer, operational, etc.)
2. How large is your dataset? (rows, columns, time period)
3. What format is your data in? (CSV, Excel, database, etc.)
4. What's the quality like? (complete, missing values, outliers?)

Analysis objectives:
5. What specific questions do you need answered?
6. What decisions will this analysis inform?
7. Who will use these insights? (executives, managers, technical team)
8. What's your timeline for this analysis?

Available tools and constraints:
9. What tools can you use? (Excel, Python, R, SQL, Tableau, etc.)
10. Do you need specific statistical tests or models?
11. What format should the output be in? (report, dashboard, presentation)
12. Any specific metrics or KPIs to focus on?

Based on your answers, I'll provide:

**1. DATA QUALITY ASSESSMENT** - Overview of your data's completeness and reliability
**2. EXPLORATORY ANALYSIS** - Key patterns, distributions, and relationships
**3. STATISTICAL INSIGHTS** - Significant findings with confidence levels
**4. ACTIONABLE RECOMMENDATIONS** - Specific steps based on the data
**5. VISUALIZATION SUGGESTIONS** - Best ways to present your findings

Please provide the information above so I can tailor the analysis to your needs.
```

## Example Usage

**User Input:**
```
1. Data type: E-commerce sales data with customer information
2. Size: 50,000 transactions over 12 months, 25 columns
3. Format: CSV file exported from our database
4. Quality: Generally good, but 5% missing customer ages, some outlier orders >$10K

5. Questions: Why did sales drop 20% last quarter? Which customer segments are most profitable?
6. Decisions: Marketing budget allocation and inventory planning for next quarter
7. Users: Marketing VP and operations team
8. Timeline: Need initial findings by end of week

9. Tools: Excel for quick analysis, Python for deeper dive
10. Statistical needs: Significance testing for segment differences, time series for trends
11. Output: Executive summary with supporting charts
12. KPIs: Revenue, conversion rate, average order value, customer lifetime value
```

**Assistant Output:**

Based on your e-commerce data, I'll provide a comprehensive analysis focusing on the sales drop and customer profitability. Here's my analysis:

## DATA QUALITY ASSESSMENT

**Overall Quality Score: B+ (85%)**

```
Data Completeness:
├── Transaction Data: 100% complete ✓
├── Customer IDs: 100% complete ✓
├── Product Info: 98% complete ✓
├── Customer Age: 95% complete (2,500 missing)
└── Geographic Data: 92% complete

Outliers Detected:
- 47 orders > $10,000 (0.09% of data)
- Recommendation: Flag for review, likely B2B orders
```

## KEY FINDINGS

### 1. Sales Drop Analysis

**Root Cause: Mobile Conversion Collapse**

```
Channel Performance (Q3 vs Q4):
                Q3        Q4      Change
Desktop:    $1.2M     $1.1M      -8%
Mobile:     $800K     $450K     -44%  ← Main issue
Tablet:     $200K     $180K     -10%
```

**Mobile-Specific Issues:**
- Conversion rate dropped from 3.2% to 1.8%
- Cart abandonment increased by 35%
- Page load time increased by 2.3 seconds

### 2. Customer Segment Profitability

**Segment Analysis:**
```
Segment         Size    Revenue   Profit   CLV
VIP            5%      35%       42%      $3,200
Regular        30%     45%       40%      $850
Occasional     40%     15%       12%      $320
One-time       25%     5%        6%       $125
```

**Key Insight:** VIP customers (5% of base) drive 42% of profits

### 3. Statistical Findings

**Significance Tests:**
- Mobile vs Desktop conversion: p < 0.001 (highly significant)
- VIP vs Regular profit margin: p < 0.01 (significant)
- Seasonal pattern detected: p < 0.05

**Time Series Analysis:**
```
Monthly Revenue Trend:
$600K │    ╱\    ╱\
      │   ╱  \  ╱  \
$400K │  ╱    \╱    \  ← 20% drop
      │ ╱            \
$200K │╱              \___
      └─────────────────────
      J A S O N D J F M A M J
```

## ACTIONABLE RECOMMENDATIONS

### Immediate Actions (This Week):

1. **Fix Mobile Experience**
   - Run mobile site speed audit
   - Simplify checkout to 2 steps max
   - Test with top 5 devices
   - Expected Impact: +$150K/month

2. **VIP Retention Campaign**
   - Send personalized offers to 2,500 VIP customers
   - Exclusive early access to new products
   - Dedicated support line
   - Expected Impact: +$75K/month

### Next Month:

3. **Reallocation Strategy**
   - Shift 40% of broad marketing to VIP acquisition
   - Reduce one-time buyer campaigns by 50%
   - Increase mobile-specific advertising
   - Expected ROI: 3.2x

4. **Inventory Optimization**
   - Stock 20% more of VIP-preferred categories
   - Reduce slow-moving items by 30%
   - Implement dynamic pricing for age >60 days

## VISUALIZATION RECOMMENDATIONS

For your executive presentation, I recommend:

1. **Dashboard Layout:**
```
┌─────────────┬─────────────┬─────────────┐
│Revenue Trend│Channel Split│Segment Value│
│  Line Chart │ Pie Chart   │ Bubble Chart│
├─────────────┴─────────────┴─────────────┤
│        Key Metrics (Large Numbers)       │
│  -20% Revenue │ -44% Mobile │ 5% = 42%  │
└──────────────────────────────────────────┘
```

2. **Supporting Charts:**
   - Funnel chart for mobile vs desktop conversion
   - Heatmap of purchase patterns by segment/time
   - Waterfall chart showing revenue decline factors

## PYTHON CODE FOR ANALYSIS

```python
# Quick segment analysis
import pandas as pd
import numpy as np

# Load and segment customers
df = pd.read_csv('sales_data.csv')
df['segment'] = pd.qcut(df['total_purchases'], 
                        q=[0, 0.75, 0.95, 1.0],
                        labels=['One-time', 'Regular', 'VIP'])

# Profitability by segment
profit_analysis = df.groupby('segment').agg({
    'revenue': 'sum',
    'profit': 'sum',
    'customer_id': 'nunique'
}).round(2)

# Statistical test for mobile issue
from scipy import stats
mobile_before = df[df['quarter']=='Q3']['mobile_conversion']
mobile_after = df[df['quarter']=='Q4']['mobile_conversion']
t_stat, p_value = stats.ttest_ind(mobile_before, mobile_after)
print(f"Mobile conversion drop significance: p={p_value:.4f}")
```

## NEXT STEPS

1. **Data Collection**: Set up mobile user session recording
2. **Deep Dive**: Analyze VIP customer journey patterns
3. **A/B Testing**: Test simplified mobile checkout
4. **Monitoring**: Daily dashboard for conversion rates

Would you like me to elaborate on any specific finding or create additional analyses?

## Related Prompts

- [Statistical Analysis Expert](statistical-analysis-expert.md)
- [Predictive Analysis Expert](predictive-analysis-expert.md)
- [Market Research Strategist](market-research-strategist.md)
