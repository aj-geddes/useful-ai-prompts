# Gap Identification Framework

## Gap Identification Framework

```python
# Systematic gap identification

class GapAnalysis:
    GAP_CATEGORIES = {
        'Business Capability': 'Functions organization can perform',
        'Process': 'How work gets done',
        'Technology': 'Tools and systems available',
        'Skills': 'Knowledge and expertise',
        'Data': 'Information available',
        'People/Culture': 'Team composition and mindset',
        'Organization': 'Structure and roles',
        'Metrics': 'Ability to measure performance'
    }

    def identify_gaps(self, current_state, future_state):
        """Compare current vs desired and find gaps"""
        gaps = []

        for capability in future_state['capabilities']:
            current_capability = self.find_capability(
                capability['name'],
                current_state['capabilities']
            )

            if current_capability is None:
                gaps.append({
                    'capability': capability['name'],
                    'gap_type': 'Missing',
                    'description': f"Organization lacks {capability['name']}",
                    'importance': capability['importance'],
                    'impact': 'High' if capability['importance'] == 'Critical' else 'Medium'
                })
            elif current_capability['maturity'] < capability['target_maturity']:
                gaps.append({
                    'capability': capability['name'],
                    'gap_type': 'Maturity',
                    'current_maturity': current_capability['maturity'],
                    'target_maturity': capability['target_maturity'],
                    'gap_size': capability['target_maturity'] - current_capability['maturity'],
                    'importance': capability['importance'],
                    'impact': 'Medium'
                })

        return gaps

    def prioritize_gaps(self, gaps):
        """Rank gaps by importance and effort"""
        scored_gaps = []

        for gap in gaps:
            importance = self.score_importance(gap)
            effort = self.estimate_effort(gap)
            value = importance / effort if effort > 0 else 0

            scored_gaps.append({
                **gap,
                'importance_score': importance,
                'effort_score': effort,
                'value_score': value,
                'priority': self.assign_priority(value)
            })

        return sorted(scored_gaps, key=lambda x: x['value_score'], reverse=True)

    def score_importance(self, gap):
        """Score how important gap is"""
        if gap['importance'] == 'Critical':
            return 10
        elif gap['importance'] == 'High':
            return 7
        else:
            return 4

    def estimate_effort(self, gap):
        """Estimate effort to close gap"""
        # Returns 1-10 scale
        return gap.get('effort_estimate', 5)

    def assign_priority(self, value_score):
        """Assign priority based on value"""
        if value_score > 2:
            return 'High'
        elif value_score > 1:
            return 'Medium'
        else:
            return 'Low'
```
