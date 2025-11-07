---
name: retrospective-facilitation
description: Facilitate effective retrospectives to capture lessons learned, celebrate successes, and identify actionable improvements for future iterations.
---

# Retrospective Facilitation

## Overview

Retrospectives are critical ceremonies for team learning and continuous improvement. Effective facilitation creates psychological safety, encourages honest feedback, and drives tangible improvements.

## When to Use

- End of sprint (regular cadence)
- Major milestone completion
- Project closure
- After significant events or incidents
- Team transitions or staff changes
- Technology implementations
- Process evaluations

## Instructions

### 1. **Retrospective Planning**

```yaml
Retrospective Planning:

Event: Sprint 23 Retrospective
Date: Friday, Jan 17, 2025
Duration: 60 minutes
Location: Conference Room B / Zoom

Facilitator: Sarah (Scrum Master)
Participants: 8 team members
Invite: Product Owner (optional)

---

Retrospective Goals:
  1. Celebrate sprint successes
  2. Identify what went well
  3. Identify what could improve
  4. Commit to specific improvements
  5. Build team cohesion

Format: "Went Well / Didn't Go Well / Ideas"
Tool: Miro board for virtual collaboration

Pre-Retrospective Preparation:
  - Send survey: anonymous feedback (24hrs before)
  - Gather sprint metrics (velocity, bugs, etc.)
  - Review sprint goals and outcomes
  - Prepare starter questions
  - Set up physical/virtual space

Success Criteria:
  - 100% team attendance
  - Minimum 3 actionable improvements identified
  - Team feels heard and valued
  - Action items assigned with owners
```

### 2. **Facilitation Techniques**

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

### 3. **Action Item Tracking**

```javascript
// Converting retrospective insights to action items

class ActionItemManagement {
  createActionItem(feedback, team) {
    return {
      id: `ACTION-${Date.now()}`,
      title: feedback.title,
      description: feedback.description,
      priority: feedback.priority || 'Medium',
      owner: feedback.owner,
      dueDate: this.calculateDueDate(feedback),
      successCriteria: [
        `${feedback.title} completed`,
        'Results verified in next sprint',
        'Team confirms improvement'
      ],
      resources: feedback.estimatedHours || 4,
      dependencies: feedback.dependencies || [],
      status: 'New',
      createdDate: new Date()
    };
  }

  calculateDueDate(item) {
    // High priority: before next sprint starts
    // Medium: during next sprint
    // Low: next 2 sprints
    const daysFromNow = {
      'High': 7,
      'Medium': 14,
      'Low': 21
    };

    const dueDate = new Date();
    dueDate.setDate(dueDate.getDate() + (daysFromNow[item.priority] || 14));
    return dueDate;
  }

  trackActionItems(items) {
    return {
      total: items.length,
      byStatus: {
        new: items.filter(i => i.status === 'New').length,
        inProgress: items.filter(i => i.status === 'In Progress').length,
        completed: items.filter(i => i.status === 'Completed').length,
        blockedPercent: (items.filter(i => i.status === 'Blocked').length / items.length * 100).toFixed(1)
      },
      summary: items.map(item => ({
        id: item.id,
        title: item.title,
        owner: item.owner,
        dueDate: item.dueDate,
        status: item.status,
        completion: item.completion || 0
      }))
    };
  }

  reviewCompletedItems(previousRetro) {
    return {
      totalCommitted: previousRetro.actionItems.length,
      completed: previousRetro.actionItems.filter(i => i.status === 'Completed').length,
      completionRate: `${(previousRetro.actionItems.filter(i => i.status === 'Completed').length / previousRetro.actionItems.length * 100).toFixed(1)}%`,
      celebration: 'Celebrate completed items!',
      carryOver: previousRetro.actionItems.filter(i => i.status !== 'Completed').map(i => ({
        ...i,
        reason: 'Not completed',
        recommendation: 'Revisit in next retrospective'
      }))
    };
  }
}
```

### 4. **Retrospective Templates**

```yaml
Retrospective Report:

Sprint: Sprint 23 (Jan 7 - Jan 17, 2025)
Facilitator: Sarah
Attendees: 8 engineers, 1 PM
Duration: 60 minutes

---

What Went Well:
  - Shipped feature 3 days early
  - Zero critical bugs in production
  - Great collaboration between frontend/backend
  - Mentoring of new team member
  - Faster code review cycle (2 → 1 day avg)

Celebrated:
  - Front-end team for UI excellence
  - DevOps for infrastructure stability
  - QA for thorough testing

---

What Could Be Improved:
  1. Unclear requirements caused rework (2 developers, 8 hours)
     Root Cause: PO wasn't available early in sprint
     Severity: Medium

  2. Testing infrastructure flaky (3 instances)
     Root Cause: Increased test load, needs optimization
     Severity: High

  3. Documentation gaps in API changes
     Root Cause: Developers focused on feature delivery
     Severity: Low

  4. Long standup meetings (averaging 20 mins)
     Root Cause: Too many status details
     Severity: Medium

---

Action Items Committed:

1. Daily PO availability window (9-10am)
   Owner: Product Manager
   Due: Sprint 24 Start (Jan 21)
   Priority: High

2. Optimize test infrastructure
   Owner: DevOps Lead
   Due: Sprint 24 Mid-point (Jan 28)
   Priority: High
   Estimated Effort: 16 hours

3. Standup time-boxing
   Owner: Scrum Master
   Due: Next Sprint (Jan 21)
   Priority: Medium
   Method: 5-minute timebox, detailed issues in follow-up

4. API documentation template
   Owner: Tech Lead
   Due: Sprint 24 Start (Jan 21)
   Priority: Low

---

Metrics:
  Velocity: 85 story points (vs 80 planned)
  Bugs Found: 2 (both fixed in sprint)
  Code Review Cycle: 23 hours avg (target: 24)
  Team Morale (1-5): 4.2/5

---

Team Feedback:
  "Best sprint in a while!"
  "Would like more focus on code quality"
  "Great support from the team"
```

## Best Practices

### ✅ DO
- Hold retrospectives regularly (every sprint)
- Create psychological safety upfront
- Use varied formats to maintain engagement
- Include the whole team
- Focus on systems, not individuals
- Convert insights to specific action items
- Assign clear owners and due dates
- Track and celebrate completed actions
- Review previous actions at start
- Thank people for participation and honesty

### ❌ DON'T
- Blame individuals or teams
- Let dominant voices control discussion
- Create action items without owners
- Have retrospectives without follow-up
- Ignore difficult feedback
- Focus only on what went wrong
- Hold retrospectives when people are tired/stressed
- Skip closing/celebration
- Mix retrospectives with status meetings
- Ignore patterns across multiple retrospectives

## Retrospective Tips

- Rotate formats every 3-4 sprints to maintain engagement
- Use anonymous input for sensitive feedback
- Time-box discussion to stay focused
- Focus on 3-5 improvements, not 20 action items
- Review and celebrate progress on previous actions
