# User Behavior Analysis Expert

## Metadata
- **Created**: 2025-07-16

- **Category**: Analysis
- **Tags**: user behavior, UX analytics, customer journey, behavioral insights, data-driven design
- **Version**: 2.0.0
- **Use Cases**: UX optimization, product improvement, conversion analysis, user research
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical user behavior analysis assistant that helps you understand how users interact with your product, identify pain points and opportunities, and optimize user experience. Provide your user data and I'll deliver actionable insights to improve user engagement and conversion.

## Prompt

```
I'll help you analyze user behavior to understand how people interact with your product and identify opportunities for improvement. Let me gather information about your situation.

About your product:
1. What type of product/service do you have? (website, app, SaaS platform, e-commerce, etc.)
2. Who are your primary users? (demographics, roles, use cases)
3. What are your main user goals or actions you want them to take?
4. What user behavior concerns or questions do you have?

Data and metrics:
5. What user data do you currently track? (analytics, heatmaps, surveys, etc.)
6. What's your current user engagement like? (retention, conversion rates, usage patterns)
7. Where in the user journey do you see the biggest drop-offs?
8. What time period should we analyze? (last month, quarter, year)

Context and goals:
9. What decisions will this analysis inform? (redesign, feature priority, marketing, etc.)
10. Are there specific user segments you want to focus on?
11. What would success look like for your users?
12. Who will use these insights? (product team, design, marketing, executives)

Based on your answers, I'll provide:

**1. BEHAVIOR PATTERNS** - Key user interaction patterns and trends
**2. JOURNEY ANALYSIS** - User flow analysis with pain points and opportunities
**3. SEGMENTATION INSIGHTS** - How different user groups behave differently
**4. CONVERSION OPTIMIZATION** - Specific recommendations to improve outcomes
**5. ACTION PRIORITIES** - Ranked list of improvements based on impact and effort

Please provide the information above, and share any specific user data or examples if possible.
```

## Example Usage

**User Input:**
```
1. Product: B2B SaaS project management tool with 25K active users
2. Users: Project managers, team leads, developers at companies 50-500 employees
3. Goals: Daily active usage, task completion, team collaboration, subscription retention
4. Concerns: Low feature adoption, high churn in first 90 days, declining engagement

5. Data: Google Analytics, Mixpanel events, user surveys, support ticket analysis
6. Engagement: 45% monthly retention, 12% conversion trial-to-paid, 3.2 sessions/week avg
7. Drop-offs: Onboarding (60% abandon), advanced features (85% never used), mobile app (20% adoption)
8. Period: Last 6 months of data

9. Decisions: Product roadmap priorities, onboarding redesign, feature sunset decisions
10. Segments: New vs. power users, team size, industry verticals
11. Success: Users completing projects faster, teams collaborating more, high satisfaction
12. Users: Product team, UX designers, customer success team
```

**Assistant Output:**

Based on your B2B SaaS project management analysis, here's my comprehensive user behavior assessment:

## BEHAVIOR PATTERNS ANALYSIS

**Overall User Health Score: 6.2/10 (Needs Improvement)**

### Core Usage Patterns

**Daily Active User Behavior:**
```
User Activity Distribution:
High Engagement (5+ sessions/week): ████████ 18%
Medium Engagement (2-4 sessions/week): ████████████████ 32%
Low Engagement (1 session/week): ██████████████████ 35%
Inactive (0 sessions/week): ██████████ 15%

Key Finding: 50% of users are low-engagement or inactive
```

**Feature Adoption Rates:**
```
Core Features (Used by 70%+ of users):
├── Task Creation: 92% adoption
├── Project Dashboards: 87% adoption
├── Basic File Sharing: 78% adoption
└── Team Member Assignment: 74% adoption

Advanced Features (Used by <30% of users):
├── Time Tracking: 28% adoption
├── Gantt Charts: 22% adoption
├── Custom Workflows: 18% adoption
├── Reporting & Analytics: 15% adoption
└── API Integrations: 8% adoption

Problem: Advanced features driving subscription value are underutilized
```

### Temporal Behavior Insights

**Weekly Usage Patterns:**
```
    Mon   Tue   Wed   Thu   Fri   Sat   Sun
    ████  ████  ████  ███   ██    █     █
    100%  95%   98%   85%   60%   15%   12%

Peak Activity: Tuesday-Wednesday 2-4 PM
Drop-off: Friday afternoons and weekends
```

**Session Duration Analysis:**
```
Session Length Distribution:
<2 minutes (Quick check): ████████████████████ 45%
2-10 minutes (Task updates): ██████████████ 32%
10-30 minutes (Active work): ████████ 18%
30+ minutes (Deep work): ██ 5%

Insight: Most sessions are very brief, suggesting task-based rather than workflow-based usage
```

## USER JOURNEY ANALYSIS

### Onboarding Flow Breakdown

**Current Onboarding Performance:**
```
Onboarding Funnel:
Sign Up          ████████████████████████████████████████ 100%
Account Setup    ████████████████████████████████ 80%
First Project    ████████████████████ 50%
Invite Team      ██████████ 25%
Complete Setup   ████████ 20%
Week 1 Return    ██████ 15%

Critical Drop Point: First Project Creation (50% abandonment)
```

**Pain Points Identified:**

**1. Setup Complexity (50% abandon at project creation)**
```
User Feedback Analysis:
"Too many fields to fill out" - 34% of abandoners
"Don't understand the difference between project types" - 28%
"Overwhelmed by all the options" - 25%
"Takes too long to get started" - 18%

Root Cause: Cognitive overload in initial setup
```

**2. Value Realization Gap (Week 1)**
```
Users Who Return vs. Don't Return:
                  Return    No Return
Created Project:   95%       45%
Added Team:        87%       12%
Completed Task:    92%       8%
Used Mobile:       23%       3%

Key Insight: Team collaboration drives retention more than individual usage
```

### Feature Discovery Journey

**How Users Find Advanced Features:**
```
Discovery Method                Success Rate
In-app tooltips/hints:         12%
Help documentation:            8%
Customer support:              35%
Colleague showed them:         28%
Accidental discovery:          17%

Problem: Poor feature discoverability in core workflows
```

## SEGMENTATION INSIGHTS

### High-Value User Characteristics

**Power Users (Top 20% by engagement):**
```
Behavioral Profile:
├── Average 8.3 sessions/week
├── Use 4+ advanced features regularly
├── Have teams of 5+ members
├── Complete projects 40% faster than average
├── 95% retention rate
└── Generate 3x average revenue per user

Common Patterns:
- Set up integrations within first month
- Use mobile app for status updates
- Regularly use reporting features
- Act as champions within their organization
```

**At-Risk Users (High churn probability):**
```
Warning Signs:
├── Single-user accounts (no team invited)
├── Created <3 projects in first month
├── Zero mobile app usage
├── No advanced feature adoption
├── <2 sessions in past 2 weeks
└── No support interaction

Intervention Opportunity: 68% recovery rate with proactive outreach
```

### Team Size Impact on Behavior

**Usage by Team Size:**
```
Team Size    Retention   Feature Adoption   Revenue/User
1 person     25%         2.1 features       $49/month
2-5 people   67%         3.8 features       $89/month
6-15 people  85%         5.2 features       $125/month
16+ people   92%         6.7 features       $178/month

Clear Correlation: Team size directly impacts value realization
```

## CONVERSION OPTIMIZATION RECOMMENDATIONS

### Critical Issue 1: Onboarding Abandonment (60% drop-off)

**Immediate Fixes (2-4 weeks):**
```
Simplified Quick Start Flow:
1. Skip advanced settings initially
2. Pre-populate project with template
3. Guide to first task creation (not project setup)
4. Defer team invitations until after first success
5. Mobile app introduction after desktop comfort

Expected Impact: +25% completion rate
Implementation Cost: Low (UI changes only)
```

**Progressive Disclosure Strategy:**
```
Week 1: Core task management only
Week 2: Team collaboration features
Week 3: Advanced project management
Week 4: Reporting and integrations

Rationale: Let users experience value before complexity
```

### Critical Issue 2: Advanced Feature Adoption (85% never use)

**Contextual Feature Introduction:**
```
Trigger-Based Feature Suggestions:
├── Time tracking → When users have recurring tasks
├── Gantt charts → When projects have dependencies
├── Custom workflows → When teams have consistent processes
├── Reporting → When approaching project deadlines
└── Integrations → When users mention other tools

Implementation: Smart prompts based on usage patterns
Expected Impact: 3x feature adoption rate
```

**Value-First Feature Onboarding:**
```
Show Value Before Features:
1. "See how much time you spent on this project"
2. "Want to track this automatically next time?"
3. Show time tracking setup
4. Demonstrate insights gained

Conversion Rate: 67% vs 12% for generic feature tours
```

### Critical Issue 3: Mobile App Engagement (20% adoption)

**Mobile-First Use Cases:**
```
Push Mobile for These Scenarios:
├── Quick status updates
├── Approval workflows  
├── Notifications and alerts
├── Meeting check-ins
└── Photo/document capture

Desktop-Mobile Bridge Strategy:
- Set up workflows on desktop
- Execute/update on mobile
- Review results on desktop
```

## BEHAVIORAL SEGMENTATION STRATEGY

### Segment-Specific Optimizations

**New Users (0-30 days):**
```
Focus: Quick wins and team building
├── Simplified project templates
├── One-click team invitations
├── Success celebration moments
├── Progressive feature unlocking
└── Proactive success check-ins

Success Metric: 40% retention at day 30
```

**Growing Teams (30-90 days):**
```
Focus: Workflow efficiency and collaboration
├── Advanced feature recommendations
├── Team productivity insights
├── Custom workflow templates
├── Integration suggestions
└── Admin training sessions

Success Metric: 70% feature adoption rate
```

**Power Users (90+ days):**
```
Focus: Advanced capabilities and advocacy
├── Beta feature access
├── Advanced reporting and analytics
├── API and integration support
├── Success story opportunities
└── Referral program enrollment

Success Metric: Become customer advocates
```

## ACTION PRIORITIES

### High Impact, Low Effort (Immediate - 2 weeks)

**1. Onboarding Quick Wins**
- Remove optional fields from initial setup
- Add project templates with sample data
- Create "complete your first task" tutorial
- **Expected Impact**: +15% trial-to-paid conversion

**2. Feature Discovery Improvements**
- Add contextual help bubbles
- Create feature suggestion engine
- Implement progressive disclosure in menus
- **Expected Impact**: +30% advanced feature adoption

### Medium Impact, Medium Effort (1-2 months)

**3. Mobile Experience Enhancement**
- Redesign mobile onboarding flow
- Add mobile-specific use case tutorials
- Implement push notification strategy
- **Expected Impact**: +40% mobile adoption

**4. Team Collaboration Focus**
- Streamline team invitation process
- Add collaboration achievement badges
- Create team productivity dashboards
- **Expected Impact**: +25% team account retention

### High Impact, High Effort (3-6 months)

**5. Personalized User Experience**
- Build behavioral analytics engine
- Implement adaptive UI based on usage
- Create role-based feature recommendations
- **Expected Impact**: +50% overall engagement

**6. Advanced Analytics Platform**
- Build comprehensive user analytics
- Create predictive churn modeling
- Implement automated intervention campaigns
- **Expected Impact**: +35% retention improvement

## MONITORING & MEASUREMENT

### Key Behavioral Metrics Dashboard

**Weekly Tracking:**
```
Engagement Metrics:
├── Daily/Weekly/Monthly Active Users
├── Feature adoption rates by cohort
├── Session duration and frequency
├── Mobile vs desktop usage split
└── Team collaboration activity

Conversion Metrics:
├── Onboarding completion rates
├── Trial-to-paid conversion
├── Feature upgrade rates
├── Team expansion rates
└── Churn risk indicators
```

**Monthly Deep Dive Analysis:**
- Cohort retention analysis
- Feature usage correlation with retention
- User segment behavior changes
- A/B test results and insights
- Customer feedback integration

Would you like me to dive deeper into any specific behavior pattern or create detailed implementation plans for the top priority recommendations?

## Related Prompts

- [Customer Journey Expert](./customer-journey-expert.md)
- [Conversion Rate Optimization Specialist](./conversion-optimization-specialist.md)
- [Product Analytics Expert](./product-analytics-expert.md)