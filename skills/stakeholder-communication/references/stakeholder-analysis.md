# Stakeholder Analysis

## Stakeholder Analysis

```python
# Stakeholder identification and engagement planning

class StakeholderAnalysis:
    ENGAGEMENT_LEVELS = {
        'Unaware': 'Provide basic information',
        'Resistant': 'Address concerns, build trust',
        'Neutral': 'Keep informed, demonstrate value',
        'Supportive': 'Engage as advocates',
        'Champion': 'Leverage for change leadership'
    }

    def __init__(self, project_name):
        self.project_name = project_name
        self.stakeholders = []

    def identify_stakeholders(self):
        """Common stakeholder categories"""
        return {
            'Executive Sponsors': {
                'interests': ['ROI', 'Strategic alignment', 'Timeline'],
                'communication': 'Monthly executive summary',
                'influence': 'High',
                'impact': 'High'
            },
            'Project Team': {
                'interests': ['Task clarity', 'Resources', 'Support'],
                'communication': 'Daily standup, weekly planning',
                'influence': 'High',
                'impact': 'High'
            },
            'End Users': {
                'interests': ['Usability', 'Value delivery', 'Support'],
                'communication': 'Beta testing, training, feedback sessions',
                'influence': 'Medium',
                'impact': 'High'
            },
            'Technical Governance': {
                'interests': ['Architecture', 'Security', 'Compliance'],
                'communication': 'Technical reviews, design docs',
                'influence': 'High',
                'impact': 'Medium'
            },
            'Department Heads': {
                'interests': ['Resource impact', 'Timeline', 'Business impact'],
                'communication': 'Bi-weekly updates, resource requests',
                'influence': 'Medium',
                'impact': 'Medium'
            }
        }

    def create_engagement_plan(self, stakeholder):
        """Design communication strategy for each stakeholder"""
        return {
            'name': stakeholder.name,
            'role': stakeholder.role,
            'power': stakeholder.influence_level,  # High/Medium/Low
            'interest': stakeholder.interest_level,  # High/Medium/Low
            'strategy': self.determine_strategy(
                stakeholder.influence_level,
                stakeholder.interest_level
            ),
            'communication_frequency': self.frequency_mapping(stakeholder),
            'key_messages': self.tailor_messages(stakeholder),
            'escalation_threshold': self.set_escalation_rules(stakeholder)
        }

    def determine_strategy(self, power, interest):
        """Stakeholder power/interest matrix"""
        if power == 'High' and interest == 'High':
            return 'Manage closely (key stakeholders)'
        elif power == 'High' and interest == 'Low':
            return 'Keep satisfied'
        elif power == 'Low' and interest == 'High':
            return 'Keep informed'
        else:
            return 'Monitor'

    def frequency_mapping(self, stakeholder):
        strategies = {
            'Manage closely': 'Weekly',
            'Keep satisfied': 'Bi-weekly',
            'Keep informed': 'Monthly',
            'Monitor': 'Quarterly'
        }
        return strategies.get(stakeholder.strategy, 'Monthly')
```
