---
name: kpi-dashboard-design
description: >
  Design and build dashboards that track key performance indicators. Select
  relevant metrics, visualize data effectively, and communicate insights to
  stakeholders.
---

# KPI Dashboard Design

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [KPI Selection Framework](references/kpi-selection-framework.md) | KPI Selection Framework |
| [Dashboard Design](references/dashboard-design.md) | Dashboard Design |
| [Dashboard Implementation](references/dashboard-implementation.md) | Dashboard Implementation |
| [KPI Monitoring & Governance](references/kpi-monitoring-governance.md) | KPI Monitoring & Governance |

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
