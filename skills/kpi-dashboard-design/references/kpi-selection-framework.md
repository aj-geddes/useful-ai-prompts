# KPI Selection Framework

## KPI Selection Framework

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
