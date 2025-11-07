---
name: kpi-dashboard-design
description: Design and build dashboards that track key performance indicators. Select relevant metrics, visualize data effectively, and communicate insights to stakeholders.
---

# KPI Dashboard Design

## Overview

Effective KPI dashboards make performance visible, enable data-driven decisions, and help teams align around shared goals.

## When to Use

- Creating performance measurement systems
- Leadership reporting and visibility
- Operational monitoring
- Project progress tracking
- Team performance management
- Customer health monitoring
- Financial reporting

## Instructions

### 1. **KPI Selection Framework**

```python
# Select relevant, measurable KPIs

class KPISelection:
    KPI_CRITERIA = {
        'Relevant': 'Directly aligned with business strategy',
        'Measurable': 'Can be quantified and tracked',
        'Actionable': 'Team can influence the metric',
        'Timely': 'Measured frequently (daily/weekly)',
        'Bounded': 'Has clear target/threshold',
        'Simple': 'Easy to understand'
    }

    def identify_business_goals(self):
        """Map goals to KPIs"""
        return {
            'Revenue Growth': [
                'Monthly Recurring Revenue (MRR)',
                'Annual Recurring Revenue (ARR)',
                'Customer Lifetime Value (CLV)',
                'Average Revenue Per User (ARPU)'
            ],
            'Customer Acquisition': [
                'Customer Acquisition Cost (CAC)',
                'Conversion Rate',
                'Traffic to Lead Rate',
                'Sales Pipeline Value'
            ],
            'Customer Retention': [
                'Churn Rate',
                'Net Promoter Score (NPS)',
                'Customer Satisfaction (CSAT)',
                'Retention Rate'
            ],
            'Operational Efficiency': [
                'Cost per Customer',
                'Time to Value',
                'System Uptime',
                'Support Response Time'
            ],
            'Product Quality': [
                'Defect Rate',
                'Feature Adoption',
                'User Engagement',
                'Performance Score'
            ]
        }

    def validate_kpi(self, kpi):
        """Check KPI against criteria"""
        validation = {}

        for criterion, definition in self.KPI_CRITERIA.items():
            validation[criterion] = {
                'definition': definition,
                'assessment': self.assess_criterion(kpi, criterion),
                'rating': 'Pass' if self.assess_criterion(kpi, criterion) else 'Fail'
            }

        is_valid = all(v['rating'] == 'Pass' for v in validation.values())

        return {
            'kpi': kpi.name,
            'validation': validation,
            'is_valid': is_valid,
            'recommendation': 'Include in dashboard' if is_valid else 'Refine or exclude'
        }

    def define_kpi_target(self, kpi):
        """Set measurable targets"""
        return {
            'kpi': kpi.name,
            'current_value': kpi.current,
            'target_value': kpi.target,
            'time_period': 'Q1 2025',
            'improvement': f"{(kpi.target - kpi.current) / kpi.current * 100:.1f}%",
            'owner': kpi.owner,
            'review_frequency': 'Weekly',
            'threshold_green': kpi.target,
            'threshold_yellow': kpi.target * 0.9,
            'threshold_red': kpi.target * 0.7
        }
```

### 2. **Dashboard Design**

```yaml
Dashboard Design Template:

Name: Sales Performance Dashboard
Audience: Sales Team, Management
Update Frequency: Daily
Users: 15 sales reps, 3 managers

---

## Dashboard Structure

### Top Section: Executive Summary (30% height)
  - Total Revenue (YTD): $2.5M (vs $2.2M target)
  - Pipeline Value: $8.7M (vs $7.5M target)
  - Win Rate: 28% (vs 25% target) - GREEN
  - Average Deal Size: $125K (vs $120K target)

### Left Column: Sales Performance (35% width)

  Sales by Rep (Ranked)
    - John Smith: $850K
    - Jane Doe: $720K
    - Bob Johnson: $630K
    - ...visualization: Horizontal bar chart

  Sales Trend (YTD)
    - Chart type: Line chart
    - X-axis: Months
    - Y-axis: Revenue
    - Target line overlaid
    - Goal: Show trend vs plan

### Right Column: Pipeline Analysis (35% width)

  Pipeline by Stage
    - Prospecting: $1.2M (12 deals)
    - Qualification: $2.1M (18 deals)
    - Proposal: $3.2M (15 deals)
    - Negotiation: $2.2M (8 deals)
    - Visualization: Funnel chart

  Deal Velocity
    - Avg days in stage by stage
    - Bottlenecks identification
    - Conversion rates

### Bottom Section: Detailed Metrics (20% height)

  Key Metrics Row:
    - Deals Closed This Month: 6
    - Average Sales Cycle: 45 days
    - Win Rate vs. Competitors: 28% vs 22%
    - Customer Satisfaction: 4.3/5

---

## Visual Design Principles

Color Coding:
  Green (On Target):  #4CAF50
  Yellow (At Risk):   #FFC107
  Red (Off Track):    #F44336
  Gray (No Data):     #9E9E9E

Data Visualization:
  - Sales Performance: Line or Column chart
  - Pipeline Stage: Funnel or Waterfall chart
  - Geographic: Map with heat zones
  - Trend: Area or Line chart
  - Distribution: Bar or Pie chart
  - Comparison: Grouped bar chart

Interactivity:
  - Click to drill down to details
  - Filter by rep, region, product
  - Time period selector
  - Export to PDF/Excel
  - Alerts for threshold violations

---

## Refresh Strategy

Real-Time (every 5 minutes):
  - Active sales calls
  - Deal status changes

Hourly:
  - Revenue totals
  - Pipeline updates

Daily (overnight):
  - Historical trends
  - Aggregated reports

Manual:
  - Target adjustments
  - Threshold changes
```

### 3. **Dashboard Implementation**

```javascript
// Build dashboard with data integration

class KPIDashboard {
  constructor(config) {
    this.config = config;
    this.widgets = [];
    this.data = {};
    this.alerts = [];
  }

  createWidget(kpi) {
    return {
      id: `widget-${kpi.id}`,
      title: kpi.name,
      metric_value: kpi.current_value,
      target_value: kpi.target_value,
      threshold: this.calculateThreshold(kpi),
      visualization: {
        type: kpi.chart_type, // 'gauge', 'number', 'chart'
        config: this.getVisualizationConfig(kpi)
      },
      drill_down: true,
      refresh_frequency: kpi.refresh_rate || 'hourly'
    };
  }

  calculateThreshold(kpi) {
    const range = kpi.target_value - kpi.minimum_value;

    return {
      green: kpi.target_value,
      yellow: kpi.target_value - (range * 0.2),
      red: kpi.target_value - (range * 0.5),
      status: this.getStatus(kpi),
      trend: this.calculateTrend(kpi)
    };
  }

  getStatus(kpi) {
    const percentOfTarget = kpi.current_value / kpi.target_value;

    if (percentOfTarget >= 1) return 'Green';
    if (percentOfTarget >= 0.8) return 'Yellow';
    return 'Red';
  }

  calculateTrend(kpi) {
    const change = kpi.current_value - kpi.previous_period_value;
    const changePercent = (change / kpi.previous_period_value) * 100;

    return {
      direction: change > 0 ? 'Up' : 'Down',
      value: Math.abs(changePercent).toFixed(1),
      momentum: this.assessMomentum(change, kpi)
    };
  }

  generateAlerts() {
    return this.widgets
      .filter(w => w.threshold.status !== 'Green')
      .map(w => ({
        severity: w.threshold.status,
        message: `${w.title} is ${w.threshold.status} (${w.metric_value} vs ${w.target_value} target)`,
        action: 'Review and investigate',
        timestamp: new Date()
      }));
  }

  exportReport() {
    return {
      format: ['PDF', 'Excel', 'CSV'],
      include: ['Metrics', 'Charts', 'Trends', 'Commentary'],
      schedule: 'Weekly, every Monday morning'
    };
  }
}
```

### 4. **KPI Monitoring & Governance**

```yaml
KPI Governance Framework:

Quarterly KPI Review:
  - Review progress against targets
  - Adjust targets if needed
  - Celebrate achievements
  - Identify improvement areas
  - Update documentation

Annual KPI Assessment:
  - Reassess KPI relevance
  - Align with strategy changes
  - Remove obsolete metrics
  - Add new metrics as needed
  - Update dashboard design

---

KPI Health Check:

Ask these questions monthly:

1. Is this KPI still relevant?
   If No: Mark for retirement

2. Do we have accurate data?
   If No: Fix data source

3. Is it actionable?
   If No: Drill down to driver metrics

4. Is target realistic?
   If No: Adjust based on new data

5. Are we taking action on insights?
   If No: Improve governance/communication

---

Common KPI Mistakes to Avoid:

1. Too Many KPIs (limit to 5-7)
2. Lagging metrics only (include leading too)
3. No ownership assigned
4. Targets not aligned with strategy
5. Dashboard not updated regularly
6. No drill-down capability
7. Metrics not actionable by team
8. Ignoring data quality issues
9. No connection to compensation/goals
10. Dashboard unused by stakeholders
```

## Best Practices

### ✅ DO
- Start with business goals, not data
- Limit dashboards to 5-7 core metrics
- Include both leading and lagging indicators
- Assign clear metric ownership
- Update dashboards regularly
- Make drill-down available
- Use visual hierarchy effectively
- Test with actual users
- Include context and benchmarks
- Document metric definitions

### ❌ DON'T
- Create dashboards without clear purpose
- Include too many metrics (analysis paralysis)
- Forget about data quality
- Build without stakeholder input
- Use confusing visualizations
- Leave dashboards stale
- Ignore mobile viewing experience
- Skip training on dashboard usage
- Create metrics no one can influence
- Change metrics frequently

## KPI Dashboard Tips

- Use traffic light colors (green/yellow/red)
- Include month-to-date and year-to-date views
- Show trend arrows for quick scanning
- Add comparison to previous period
- Enable drill-down to supporting data
