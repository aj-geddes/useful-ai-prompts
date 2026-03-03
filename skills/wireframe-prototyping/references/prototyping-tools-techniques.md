# Prototyping Tools & Techniques

## Prototyping Tools & Techniques

```python
# Create interactive prototypes

class PrototypeFramework:
    TOOLS = {
        'Figma': {
            'fidelity': 'Medium-High',
            'interactivity': 'Full',
            'collaboration': 'Real-time',
            'cost': 'Free-$30/month'
        },
        'Framer': {
            'fidelity': 'High',
            'interactivity': 'Advanced',
            'collaboration': 'Limited',
            'cost': '$12+/month'
        },
        'Adobe XD': {
            'fidelity': 'High',
            'interactivity': 'Full',
            'collaboration': 'Good',
            'cost': '$20/month'
        }
    }

    def create_prototype_flow(self):
        """Define user interaction flows"""
        return {
            'screens': [
                {'name': 'Login', 'interactions': ['Email input', 'Password input', 'Submit button']},
                {'name': 'Dashboard', 'interactions': ['View projects', 'Create new', 'Search']},
                {'name': 'Project Detail', 'interactions': ['View tasks', 'Edit project', 'Share']}
            ],
            'flows': [
                {'from': 'Login', 'to': 'Dashboard', 'trigger': 'Valid credentials'},
                {'from': 'Dashboard', 'to': 'Project Detail', 'trigger': 'Click project'},
                {'from': 'Project Detail', 'to': 'Dashboard', 'trigger': 'Back button'}
            ]
        }

    def define_interactions(self, screen):
        """Map user interactions"""
        return {
            'screen': screen,
            'interactions': [
                {
                    'element': 'Submit button',
                    'trigger': 'Click',
                    'action': 'Validate form and submit'
                },
                {
                    'element': 'Email field',
                    'trigger': 'Focus',
                    'action': 'Show placeholder, hint text'
                }
            ]
        }

    def test_prototype(self, prototype):
        """Gather feedback on prototype"""
        return {
            'testing_method': 'Unmoderated user testing',
            'participants': 5,
            'duration': '30 minutes each',
            'tasks': [
                'Complete user registration',
                'Create first project',
                'Invite team member'
            ],
            'metrics': [
                'Task completion rate',
                'Time to complete',
                'Error rate',
                'User satisfaction'
            ]
        }
```
