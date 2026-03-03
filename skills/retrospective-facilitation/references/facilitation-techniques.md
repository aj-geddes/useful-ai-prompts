# Facilitation Techniques

## Facilitation Techniques

```python
# Retrospective facilitation framework

class RetrospectiveFacilitator:
    FORMATS = {
        'Start-Stop-Continue': {
            'description': 'What should we start, stop, continue doing?',
            'duration_minutes': 45,
            'best_for': 'Process improvements'
        },
        'Went-Well-Improve': {
            'description': 'What went well? What can we improve?',
            'duration_minutes': 45,
            'best_for': 'General retrospectives'
        },
        'Sailboat': {
            'description': 'Wind (helping), Anchor (hindering), Rocks (risks)',
            'duration_minutes': 60,
            'best_for': 'Identifying blockers and enablers'
        },
        'Timeline': {
            'description': 'Walk through sprint chronologically',
            'duration_minutes': 60,
            'best_for': 'Complex sprints with incidents'
        }
    }

    def __init__(self, team_size, format_type='Went-Well-Improve'):
        self.team_size = team_size
        self.format = format_type
        self.duration = self.FORMATS[format_type]['duration_minutes']
        self.agenda = self.create_agenda()

    def create_agenda(self):
        """Create timed agenda"""
        return {
            'Opening': {
                'duration_minutes': 5,
                'activities': [
                    'Welcome and goals',
                    'Set psychological safety',
                    'Explain format'
                ]
            },
            'Data Gathering': {
                'duration_minutes': 15,
                'activities': [
                    'Individual reflection (5 min)',
                    'Silent brainstorming on board (10 min)'
                ]
            },
            'Discussion': {
                'duration_minutes': 20,
                'activities': [
                    'Group clustering similar items',
                    'Discuss themes and patterns',
                    'Ask clarifying questions'
                ]
            },
            'Improvement Planning': {
                'duration_minutes': 15,
                'activities': [
                    'Vote on priority items',
                    'Create action items',
                    'Assign owners'
                ]
            },
            'Closing': {
                'duration_minutes': 5,
                'activities': [
                    'Summarize decisions',
                    'Commit to improvements',
                    'Appreciate team'
                ]
            }
        }

    def facilitate_discussion(self, feedback_items):
        """Guide productive discussion"""
        return {
            'structure': [
                {
                    'step': 'Clustering',
                    'action': 'Group similar items together',
                    'facilitation_tip': 'Ask "Are these related?"'
                },
                {
                    'step': 'Exploration',
                    'action': 'Understand root causes',
                    'facilitation_tip': 'Ask "Why?" 5 times'
                },
                {
                    'step': 'Solution Generation',
                    'action': 'Brainstorm solutions',
                    'facilitation_tip': 'No criticism, defer judgment'
                },
                {
                    'step': 'Prioritization',
                    'action': 'Vote on what matters most',
                    'facilitation_tip': 'Use dot voting'
                }
            ],
            'facilitation_questions': [
                'Can you help us understand what happened?',
                'Why do you think this happened?',
                'How can we prevent this next time?',
                'What would success look like?'
            ]
        }

    def ensure_psychological_safety(self):
        """Create safe environment for honest feedback"""
        return {
            'opening_statement': '''
            This is a safe space. There's no blame here. We're all
            learning together. Everything shared stays confidential.
            ''',
            'ground_rules': [
                'Assume positive intent',
                'Criticize ideas, not people',
                'Everyone participates',
                'Listen without interrupting',
                'No side conversations'
            ],
            'practices': [
                'Use anonymous input for sensitive topics',
                'Give balanced feedback (positive & improvement)',
                'Acknowledge emotions and concerns',
                'Thank people for vulnerability'
            ]
        }
```
