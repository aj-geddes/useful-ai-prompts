# Story Refinement Process

## Story Refinement Process

```python
# Story refinement and quality gates

class UserStoryRefinement:
    QUALITY_GATES = {
        'Independent': 'Story can be implemented independently',
        'Negotiable': 'Details can be discussed and refined',
        'Valuable': 'Delivers clear business value',
        'Estimable': 'Team can estimate effort',
        'Small': 'Can be completed in one sprint',
        'Testable': 'Clear acceptance criteria'
    }

    def evaluate_story(self, story):
        """Assess story quality using INVEST criteria"""
        assessment = {}

        for criterion, description in self.QUALITY_GATES.items():
            assessment[criterion] = self.check_criterion(story, criterion)

        return {
            'story_id': story.id,
            'assessment': assessment,
            'ready_for_development': all(assessment.values()),
            'issues': self.identify_issues(story),
            'recommendations': self.provide_recommendations(story)
        }

    def check_criterion(self, story, criterion):
        """Evaluate against specific INVEST criterion"""
        checks = {
            'Independent': lambda s: len(s.dependencies) == 0,
            'Negotiable': lambda s: len(s.acceptance_criteria) > 0,
            'Valuable': lambda s: len(s.business_value) > 0,
            'Estimable': lambda s: s.story_points is not None,
            'Small': lambda s: s.story_points <= 8,
            'Testable': lambda s: len(s.acceptance_criteria) > 0 and all(
                ac.get('test_case') for ac in s.acceptance_criteria
            )
        }
        return checks[criterion](story)

    def refine_story(self, story):
        """Guide refinement discussion"""
        return {
            'story_id': story.id,
            'refinement_agenda': [
                {
                    'topic': 'Clarify scope',
                    'questions': [
                        'What exactly does the user need?',
                        'What's NOT included?',
                        'Are there edge cases?'
                    ]
                },
                {
                    'topic': 'Define acceptance criteria',
                    'questions': [
                        'How do we know when it's done?',
                        'What are success criteria?',
                        'What should fail gracefully?'
                    ]
                },
                {
                    'topic': 'Technical approach',
                    'questions': [
                        'How will we implement this?',
                        'Are there dependencies?',
                        'What are the risks?'
                    ]
                },
                {
                    'topic': 'Estimation',
                    'questions': [
                        'How much effort?',
                        'Any unknowns?',
                        'Buffer needed?'
                    ]
                }
            ],
            'outputs': [
                'Refined story description',
                'Detailed acceptance criteria',
                'Technical approach identified',
                'Story points estimate',
                'Dependencies listed',
                'Team agreement on scope'
            ]
        }
```
