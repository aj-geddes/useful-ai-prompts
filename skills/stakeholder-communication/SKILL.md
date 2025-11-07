---
name: stakeholder-communication
description: Manage stakeholder expectations and engagement through targeted communication, regular updates, and relationship building. Tailor messaging for different stakeholder groups and priorities.
---

# Stakeholder Communication

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

## Instructions

### 1. **Stakeholder Analysis**

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

### 2. **Communication Planning**

```yaml
Stakeholder Communication Plan:

Project: Customer Portal Redesign
Duration: 6 months
Start Date: January 1

---

Stakeholder Group: Executive Leadership
Members: CEO, CFO, CMO
Interests: ROI, Timeline, Brand impact
Engagement: Manage closely

Communication Strategy:
  Frequency: Monthly (30-min executive briefing)
  Format: Presentation + 1-page summary
  Medium: Video conference
  Owner: Project Manager

Key Messages:
  - Project progress vs. milestone targets
  - Budget status and variance
  - Business value realized/projected
  - Any critical issues requiring decision

Sample Agenda:
  5 min: Status summary (Green/Yellow/Red)
  10 min: Key achievements & milestones
  5 min: Budget & resource update
  10 min: Risks & critical decisions needed

---

Stakeholder Group: Technical Governance
Members: Solutions Architect, Security Lead, Infrastructure Lead
Interests: Architecture, Security, Performance
Engagement: Manage closely

Communication Strategy:
  Frequency: Bi-weekly (60-min technical sync)
  Format: Technical review, design discussions
  Medium: In-person / Video conference
  Owner: Technical Lead

Key Messages:
  - Architecture decisions & trade-offs
  - Security review status
  - Performance benchmarks
  - Technical debt & mitigation

---

Stakeholder Group: End Users
Members: 500+ portal users
Interests: Functionality, Usability, Support
Engagement: Keep informed

Communication Strategy:
  Frequency: Quarterly (user sessions), ongoing feedback
  Format: Demos, surveys, support channels
  Medium: In-app notifications, email, forums
  Owner: Product Manager

Key Messages:
  - New features and capabilities
  - Timeline for improvements
  - How feedback is being used
  - Support & training resources
```

### 3. **Status Communication Templates**

```javascript
// Status report generation and distribution

class StatusReporting {
  constructor(project) {
    this.project = project;
    this.reportDate = new Date();
  }

  generateExecutiveStatus() {
    return {
      projectName: this.project.name,
      reportDate: this.reportDate,
      status: 'Green', // Green/Yellow/Red
      summary: `Project is on track. Completed Phase 1 milestones with 95%
                budget adherence. Minor delay in vendor integration (handled).`,

      keyMetrics: {
        schedulePercentComplete: 45,
        budgetUtilization: 42,
        scope: 'On track',
        quality: 'All tests passing'
      },

      achievements: [
        'Completed user research and documented requirements',
        'Finalized system architecture and technology stack',
        'Established development pipeline and CI/CD',
        'Delivered Phase 1 prototype to stakeholders'
      ],

      risks: [
        {
          risk: 'Third-party API delay',
          impact: 'Medium',
          mitigation: 'Using mock service, 80% contingency time built in'
        }
      ],

      nextSteps: [
        'Begin Phase 2 development (Week 5)',
        'User acceptance testing planning',
        'Production environment setup'
      ],

      decisionsNeeded: [
        'Approval for enhanced security requirements (+1 week)',
        'Budget for additional load testing tools'
      ]
    };
  }

  generateDetailedStatus() {
    return {
      ...this.generateExecutiveStatus(),

      detailedMetrics: {
        scheduleVariance: '+0.5 weeks (ahead)',
        costVariance: '-$5,000 (under)',
        qualityMetrics: {
          testCoverage: 85,
          defectDensity: '0.2 per 1000 lines',
          codeReviewCompliance: 100
        }
      },

      phaseBreakdown: [
        {
          phase: 'Phase 1: Planning & Design',
          status: 'Complete',
          percentComplete: 100,
          owner: 'John Smith'
        },
        {
          phase: 'Phase 2: Development',
          status: 'In Progress',
          percentComplete: 45,
          owner: 'Sarah Johnson'
        }
      ],

      issueLog: [
        {
          id: 'ISS-001',
          description: 'Vendor API documentation incomplete',
          severity: 'Medium',
          owner: 'Tech Lead',
          targetResolution: '2025-01-15'
        }
      ]
    };
  }

  sendStatusReport(recipients, format = 'email') {
    const report = this.generateExecutiveStatus();

    return {
      to: recipients,
      subject: `[${report.status}] ${report.projectName} Status - Week of ${this.reportDate}`,
      body: this.formatReportBody(report),
      attachments: ['detailed_status.pdf'],
      scheduledSend: false
    };
  }

  formatReportBody(report) {
    return `
Project Status: ${report.status}
Report Date: ${this.reportDate.toISOString().split('T')[0]}

EXECUTIVE SUMMARY
${report.summary}

KEY METRICS
- Schedule: ${report.keyMetrics.schedulePercentComplete}% Complete
- Budget: ${report.keyMetrics.budgetUtilization}% Utilized
- Quality: ${report.keyMetrics.quality}

ACHIEVEMENTS THIS PERIOD
${report.achievements.map(a => `• ${a}`).join('\n')}

UPCOMING MILESTONES
${report.nextSteps.map(s => `• ${s}`).join('\n')}

RISKS & ISSUES
${report.risks.map(r => `• ${r.risk} (${r.impact} Impact): ${r.mitigation}`).join('\n')}

DECISIONS NEEDED
${report.decisionsNeeded.map(d => `• ${d}`).join('\n')}
    `;
  }
}
```

### 4. **Difficult Conversations**

```markdown
## Handling Difficult Stakeholder Conversations

### Preparing for Difficult Conversations

1. **Gather Facts**
   - Be clear about the issue/change
   - Have data to support your position
   - Understand implications for stakeholder

2. **Anticipate Reactions**
   - What concerns might arise?
   - What are valid pain points?
   - What mitigations can you offer?

3. **Plan the Conversation**
   - One-on-one preferred for sensitive topics
   - Choose appropriate timing and location
   - Prepare talking points
   - Identify decision-maker authority

### Delivering Bad News

Bad News Template:

1. **Context** (30 seconds)
   - What is the situation?
   - Why are we discussing this?

2. **The News** (Direct & Clear)
   - State clearly what's changed
   - Provide specific impact
   - Avoid softening language

3. **Root Cause** (if applicable)
   - Explain what happened
   - Take responsibility if appropriate
   - Avoid blame

4. **Impact Assessment**
   - Timeline impact
   - Budget impact
   - Scope impact

5. **Mitigation Plan**
   - What will you do about it?
   - Specific actions & timeline
   - How will you prevent recurrence?

6. **Next Steps**
   - What decisions are needed?
   - When will you follow up?
   - How can stakeholder help?

### Example Conversation

**Issue:** Timeline extension needed (2 weeks)

"Thank you for your time. I need to share an important update about
our timeline.

We've discovered that the integration with the payment system requires
more extensive security hardening than initially estimated. We've run
performance tests and determined we need an additional 2 weeks to meet
our security and compliance requirements.

This impacts our delivery date from March 15 to March 29. Budget impact
is minimal ($8K for additional testing).

Here's what we're doing to manage this: We're running security tests
in parallel with development, we've engaged the security team early,
and we've built in validation checkpoints to catch issues early.

The alternative is to launch with reduced security, which we cannot
recommend given our risk profile.

I need your approval to proceed with the extended timeline. Can we
schedule a 30-minute call with you and the executive team tomorrow
to discuss?"
```

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

## Communication Tips

- Schedule communication at consistent times
- Use visual dashboards for metrics
- Record important conversations
- Share why, not just what changed
