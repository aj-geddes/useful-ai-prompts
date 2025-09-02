# Status Reporting Expert

## Metadata
- **Created**: 2025-01-15

- **Category**: Communication
- **Tags**: status updates, progress reporting, project communication, dashboards, executive reporting
- **Use Cases**: project reporting, progress updates, status communication, metrics presentation
- **Version**: 2.0.0
- **Use Cases**: project status updates, executive dashboards, team progress reports, stakeholder communication
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you create clear, informative status reports that keep stakeholders aligned, surface issues early, and drive action - all while minimizing reporting overhead.

## Prompt

```
I'll help you create status reports that actually get read and drive action. Let me understand your reporting needs:

**About your project:**
1. What project/initiative are you reporting on?
2. What's the current phase and timeline?
3. What are the key deliverables or milestones?
4. What's the overall complexity level?

**About your audience:**
5. Who reads these reports? (executives, team, clients)
6. What do they care about most? (budget, timeline, quality, risks)
7. How much detail do they want?
8. How often do they need updates?

**Current challenges:**
9. What problems do you have with current reporting?
10. What questions come up repeatedly?
11. How much time are you spending on reports?
12. What format do stakeholders prefer?

Based on your answers, I'll create:

**STATUS REPORT TEMPLATE** - Customized format with the right level of detail
**VISUAL DASHBOARD** - Key metrics and progress indicators at a glance
**REPORTING EFFICIENCY PLAN** - How to gather data and create reports faster
**COMMUNICATION STRATEGY** - When and how to deliver different types of updates
**ESCALATION FRAMEWORK** - How to surface issues appropriately

Share your reporting context and I'll design a system that informs without overwhelming.
```

## Example Usage

**User Input:**
```
1. Software development project - new mobile app for customers
2. Month 3 of 9, in development phase after completing design
3. Key milestones: MVP in month 5, beta in month 7, launch month 9
4. Medium complexity - 5 developers, 3 platforms, external API integrations

5. Reports go to: Product VP (weekly), CEO (monthly), Board (quarterly)
6. VP cares about features/timeline, CEO about budget/ROI, Board about strategic impact
7. VP wants moderate detail, CEO wants summary + exceptions, Board wants highlights only
8. Weekly for VP, monthly for CEO, quarterly for Board

9. Takes too long to compile, different people want different formats, lots of redundancy
10. "Are we on track?", "What's blocking progress?", "When will X feature be ready?"
11. About 4-5 hours per week on various status updates
12. VP likes dashboards, CEO prefers email, Board wants slides
```

**Assistant Output:**

Based on your mobile app development project needs, here's a comprehensive status reporting system:

## STATUS REPORT TEMPLATES

### 1. Weekly VP Dashboard (Product VP)

**One-Page Visual Dashboard Format:**

```
PROJECT: Customer Mobile App | Week 12 Status | Updated: [Date]

OVERALL STATUS: 🟡 YELLOW (Minor delays, recoverable)

PROGRESS OVERVIEW:
Development Sprint: 6 of 15  ▓▓▓▓▓▓░░░░░░░░░ 40%
Features Complete: 18 of 45  ▓▓▓▓▓▓▓▓░░░░░░░ 40%
Budget Utilized: $180K of $500K  ▓▓▓▓▓▓▓░░░░░░░░ 36%

KEY ACCOMPLISHMENTS THIS WEEK:
✓ User authentication module completed
✓ iOS payment integration tested successfully  
✓ Android UI framework finalized

BLOCKERS & RISKS:
🔴 API vendor delay - impacting checkout feature (2-week delay)
🟡 Android developer out sick - coverage plan in place
🟡 Performance issues on older devices - optimization needed

NEXT WEEK FOCUS:
• Complete payment processing for Android
• Begin user profile features
• API vendor escalation meeting
• Performance optimization sprint

FEATURE STATUS:
                    Status   Dev%   Test%   Notes
Authentication      ✅      100%   100%    Deployed to staging
Payment - iOS       ✅      100%   90%     Final testing
Payment - Android   🟡      70%    0%      Behind 1 week
User Profiles       🔵      15%    0%      Starting this week
Search              ⚪      0%     0%      Week 14 start
```

### 2. Monthly CEO Email (Executive Summary)

**Subject: Mobile App Development - Month 3 Status Update**

**EXECUTIVE SUMMARY**
Project Status: **YELLOW** - Recoverable delays, mitigation in progress
Budget Status: **GREEN** - Tracking 4% under budget
ROI Timeline: **ON TRACK** - Q4 launch supports $2M revenue target

**KEY METRICS**
- 40% feature complete (target was 45%)
- $180K spent of $500K budget (36%)
- 12 of 15 planned features in development
- 0 critical defects in production code

**EXCEPTIONS REQUIRING ATTENTION**
1. **Third-party API delays** (2 weeks) - Escalated to vendor management
   - Impact: Checkout feature delayed
   - Mitigation: Parallel development of other features
   - Resolution: Vendor committed to 3/15 delivery

2. **Performance on legacy devices** - Affects 15% of target user base
   - Impact: May limit initial market
   - Mitigation: Optimization sprint planned
   - Resolution: Technical solution identified

**FINANCIAL SUMMARY**
- Current burn rate: $60K/month (vs. $65K planned)
- Projected total cost: $480K (vs. $500K budget)
- Cost savings → Development efficiency improvements
- ROI impact → None - launch date unchanged

**DECISIONS NEEDED**
None this period. Will need approval next month for beta testing budget ($25K).

**NEXT MONTH PREVIEW**
- Complete core features (80% target)
- Begin integration testing
- Finalize beta test plan
- No budget or timeline changes expected

### 3. Quarterly Board Presentation (Strategic Overview)

**Slide Format - 3 slides max:**

**Slide 1: Strategic Initiative Update**
```
Mobile App Development: Transforming Customer Experience

Status: ON TRACK for Q4 Launch
- 40% complete, meeting adjusted milestones
- $2M revenue opportunity intact
- Competitive advantage maintained

Strategic Impact:
• 50% of customers requesting mobile access
• First-mover advantage in our segment  
• Foundation for digital transformation
```

**Slide 2: Key Metrics & Milestones**
```
Progress Against Plan:
              Q1    Q2    Q3    Q4
Design        ████  
Development         ████  ████
Testing                   ████  
Launch                          ████

Investment: $180K of $500K (on budget)
Team: 5 developers, 2 designers (fully staffed)
Quality: 0 critical issues, 95% code coverage
```

**Slide 3: Risks & Opportunities**
```
Managed Risks:
• Vendor dependency - Mitigation in place
• Technical complexity - Team upskilled
• Market timing - Accelerated where possible

Emerging Opportunities:
• Partnership interest from 2 major retailers
• Additional features requested by enterprise clients
• Platform expansion potential (tablet, web)

Next Quarter: MVP delivery, beta testing, go-to-market preparation
```

## VISUAL DASHBOARD COMPONENTS

### Real-Time Project Dashboard
```javascript
// Key Metrics to Track
const dashboardMetrics = {
  // Progress Indicators
  overallProgress: {
    planned: calculatePlannedProgress(),
    actual: calculateActualProgress(),
    variance: calculateVariance()
  },
  
  // Health Indicators
  schedule: { status: 'yellow', daysAhead: -5 },
  budget: { status: 'green', variance: +4 },
  quality: { status: 'green', defectRate: 0.02 },
  team: { status: 'green', utilization: 0.85 },
  
  // Milestone Tracking
  milestones: [
    { name: 'Design Complete', status: 'done', date: '2024-01-15' },
    { name: 'MVP Ready', status: 'in-progress', date: '2024-03-15' },
    { name: 'Beta Launch', status: 'planned', date: '2024-05-01' }
  ]
};
```

### Visual Elements Design
- **Traffic light system**: Green/Yellow/Red for instant status
- **Progress bars**: Visual representation of completion
- **Trend arrows**: Show direction vs. last period
- **Burn charts**: Budget and timeline consumption
- **Risk heat map**: 3x3 grid of probability vs. impact

## REPORTING EFFICIENCY PLAN

### Data Collection Automation
1. **Source Integration**
   - Pull from Jira: Sprint progress, feature status
   - Pull from Git: Code commits, PR stats
   - Pull from Time tracking: Hours logged
   - Pull from Budget tool: Spend data

2. **Weekly Automation Schedule**
   ```
   Thursday 3pm: Automated data pull
   Thursday 4pm: Dashboard refresh
   Friday 9am: Review and annotate
   Friday 10am: Distribute reports
   ```

3. **Templates and Reusable Components**
   - Standard status categories
   - Pre-written risk descriptions
   - Milestone update formulas
   - Exception highlighting rules

### Time-Saving Process (5 hours → 1.5 hours)
- **Hour 0**: Automated data collection
- **30 min**: Review and validate data
- **30 min**: Update commentary and exceptions  
- **30 min**: Customize for each audience
- **Save 3.5 hours per week!**

## COMMUNICATION STRATEGY

### Reporting Cadence
```
Daily: Team standups (not reported up)
Weekly: VP dashboard (every Friday)
Bi-weekly: Stakeholder newsletter
Monthly: CEO email (first Monday)
Quarterly: Board deck (quarter end + 5 days)
Ad-hoc: Exception alerts (as needed)
```

### Channel Strategy
- **VP**: Interactive dashboard (Tableau/PowerBI)
- **CEO**: Email with PDF attachment
- **Board**: PowerPoint slides
- **Team**: Slack updates
- **Stakeholders**: Newsletter format

### Message Customization
- **Technical audience**: Include architecture decisions, tech debt
- **Business audience**: Focus on features, timeline, ROI
- **Executive audience**: Strategic impact, exceptions only
- **External audience**: High-level progress, no sensitive data

## ESCALATION FRAMEWORK

### Issue Escalation Matrix
```
SEVERITY LEVELS:
Level 1 (Low): Team handles, mention in weekly report
Level 2 (Medium): Escalate to VP within 48 hours
Level 3 (High): Escalate to CEO within 24 hours  
Level 4 (Critical): Immediate CEO/Board notification

ESCALATION TRIGGERS:
Timeline: >2 week delay = Level 2, >4 weeks = Level 3
Budget: >10% variance = Level 2, >20% = Level 3
Quality: Major defect = Level 2, Security issue = Level 4
Team: Key person loss = Level 3
External: Vendor failure = Level 2, Legal issue = Level 4
```

### Escalation Templates

**Level 2 Email Template:**
```
Subject: [PROJECT] Issue Escalation - [Issue Name]

Issue: [Brief description]
Impact: [Timeline/Budget/Quality impact]
Cause: [Root cause if known]
Options: 
1. [Option 1 with tradeoffs]
2. [Option 2 with tradeoffs]
Recommendation: [Your recommended path]
Decision needed by: [Date]
```

This comprehensive system will transform your status reporting from a time-consuming chore into a strategic communication tool that drives decisions and keeps everyone aligned.

## Related Prompts

- [Executive Communication Expert](../management-leadership/executive-decision-making-expert.md)
- [Project Dashboard Designer](../management-leadership/project-governance-expert.md)
- [Meeting Facilitation Expert](meeting-facilitation-expert.md)
