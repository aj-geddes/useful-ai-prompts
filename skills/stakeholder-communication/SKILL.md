---
name: stakeholder-communication
description: >
  Manage stakeholder expectations and engagement through targeted communication,
  regular updates, and relationship building. Tailor messaging for different
  stakeholder groups and priorities.
---

# Stakeholder Communication

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Effective stakeholder communication ensures alignment, manages expectations, builds trust, and keeps projects on track by addressing concerns proactively.

## When to Use

- Project kickoff and initiation
- Weekly/monthly status updates
- Major milestone achievements
- Changes to scope, timeline, or budget
- Risks or issues requiring escalation
- Stakeholder onboarding
- Handling difficult conversations

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Stakeholder Analysis](references/stakeholder-analysis.md) | Stakeholder Analysis |
| [Communication Planning](references/communication-planning.md) | Communication Planning |
| [Status Communication Templates](references/status-communication-templates.md) | Status Communication Templates |
| [Difficult Conversations](references/difficult-conversations.md) | Difficult Conversations |

## Best Practices

### ✅ DO

- Tailor messages to stakeholder interests and influence
- Communicate proactively, not reactively
- Be transparent about issues and risks
- Provide regular scheduled updates
- Document decisions and communication
- Acknowledge stakeholder concerns
- Follow up on action items
- Build relationships outside crisis mode
- Use multiple communication channels
- Celebrate wins together

### ❌ DON'T

- Overcommunicate or undercommunicate
- Use jargon stakeholders don't understand
- Surprise stakeholders with bad news
- Promise what you can't deliver
- Make excuses without solutions
- Communicate through intermediaries for critical issues
- Ignore feedback or concerns
- Change communication style inconsistently
- Share inappropriate confidential details
- Communicate budget/timeline bad news via email
