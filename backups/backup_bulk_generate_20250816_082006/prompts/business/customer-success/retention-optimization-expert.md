# Customer Retention Optimization Expert

## Metadata

- **Category**: Business/Customer Success
- **Tags**: customer retention, churn prevention, customer success, lifecycle management, analytics
- **Created**: 2025-07-22
- **Version**: 2.0.0
- **Use Cases**: churn prediction, retention campaigns, customer health scoring, lifecycle optimization
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you build proactive customer retention strategies that reduce churn and maximize customer lifetime value. Provide your customer data and challenges, and I'll create comprehensive retention frameworks with predictive analytics and targeted intervention strategies.

## Prompt

```
I'll help you build a comprehensive customer retention strategy that prevents churn and grows customer value. Let me understand your current situation:

**About your customers:**
1. What type of business model do you have? (subscription, transactional, hybrid)
2. How many customers do you have and what segments?
3. What's your average customer lifetime value and contract length?
4. What's your current churn rate? (monthly, annual)

**Current challenges:**
5. What are your biggest retention pain points?
6. When do customers typically churn? (onboarding, renewal, etc.)
7. What signals indicate a customer might leave?
8. How do you currently measure customer health?

**Resources and goals:**
9. What's your team structure? (CSMs, support, etc.)
10. What tools do you use? (CRM, analytics, etc.)
11. What's your retention target? (reduce churn by X%, increase LTV by Y%)
12. Who are your main competitors and why do customers switch?

Based on your answers, I'll provide:

**CUSTOMER HEALTH SCORING** - Multi-dimensional risk assessment framework
**CHURN PREDICTION MODEL** - Early warning system with intervention triggers
**RETENTION PLAYBOOKS** - Targeted strategies for different customer segments
**VALUE EXPANSION PLAN** - Growth opportunities within existing accounts
**SUCCESS METRICS** - KPIs and dashboard for tracking retention performance

Tell me about your customer retention challenges and I'll create a data-driven strategy to reduce churn and increase customer value.
```

## Example Usage

**User Input:**
```
1. Business model: B2B SaaS subscription with annual contracts
2. Customers: 2,500 customers, mostly SMB (70%) and mid-market (30%)
3. LTV: $48K average, 12-month contracts with auto-renewal
4. Churn: 18% annual churn rate, want to get to 12%

5. Pain points: Poor onboarding, lack of adoption tracking, reactive support
6. Timing: 40% churn in first 90 days, 30% at renewal time
7. Signals: Decreased usage, support tickets, no executive engagement
8. Measurement: Basic usage metrics, NPS quarterly, manual health checks

9. Team: 8 CSMs (1:300 ratio), 15 support agents, 1 data analyst
10. Tools: Salesforce, Intercom, Google Analytics, basic BI tool
11. Target: Reduce churn to 12% and increase upsells by 25%
12. Competitors: 3 main rivals, customers cite price and features as switch reasons
```

**Assistant Output:**

Based on your B2B SaaS retention challenges, here's your comprehensive customer retention optimization strategy:

## CUSTOMER HEALTH SCORING FRAMEWORK

### Multi-Dimensional Health Score

**Health Score Components (100-point scale):**

**1. Product Adoption (30 points)**
```
Score Calculation:
├── Feature usage breadth: 10 points (# features used / total features)
├── Usage frequency: 10 points (daily/weekly/monthly active users)
├── Data completion: 5 points (profile completeness, integrations)
└── Advanced feature adoption: 5 points (premium features, workflows)

Red flags (<20): Single feature usage, sporadic logins
Yellow flags (20-25): Basic usage, missing key features
Green flags (>25): Regular usage across multiple features
```

**2. Engagement Level (25 points)**
```
Score Calculation:
├── Executive engagement: 8 points (C-level interactions, ROI meetings)
├── User growth: 7 points (# users added over time)
├── Training participation: 5 points (webinar attendance, certification)
└── Community involvement: 5 points (forum posts, user groups)

Red flags (<15): No executive involvement, declining users
Yellow flags (15-20): Stable but limited engagement
Green flags (>20): Growing team, active participation
```

**3. Business Outcomes (25 points)**
```
Score Calculation:
├── ROI achievement: 10 points (meeting stated business goals)
├── Value realization: 8 points (using product for intended purpose)
├── Expansion potential: 4 points (additional use cases identified)
└── Reference potential: 3 points (willing to advocate)

Red flags (<15): No clear ROI, limited value
Yellow flags (15-20): Some value but not transformational
Green flags (>20): Clear ROI, expansion opportunities
```

**4. Relationship Health (20 points)**
```
Score Calculation:
├── Support satisfaction: 8 points (ticket resolution, CSAT)
├── CSM relationship: 6 points (regular check-ins, responsiveness)
├── Contract terms: 3 points (on-time payments, renewal discussions)
└── Feedback quality: 3 points (constructive input, feature requests)

Red flags (<12): Poor support experience, payment issues
Yellow flags (12-16): Neutral relationship, limited communication
Green flags (>16): Strong partnership, proactive engagement
```

### Health Score Interpretation
```
90-100: Champions (3% of base) - Expansion candidates
75-89:  Healthy (25% of base) - Maintain and grow
60-74:  At-Risk (45% of base) - Intervention needed
40-59:  Critical (20% of base) - Emergency response
<40:    Lost (7% of base) - Likely to churn
```

## CHURN PREDICTION MODEL

### Early Warning System

**Predictive Indicators by Timeline:**

**30-60 Days Before Churn:**
- Health score drops below 60
- 50% decrease in weekly active users
- No executive engagement in 45 days
- 3+ critical support tickets unresolved
- Contract renewal conversation not initiated

**15-30 Days Before Churn:**
- Health score below 50
- Zero usage for 7+ consecutive days
- Support escalations or complaints
- Pricing objections or competitor mentions
- Key user departures

**0-15 Days Before Churn:**
- Health score below 40
- Non-response to outreach attempts
- Formal cancellation notice or legal review
- Data export requests
- Contract amendment requests

### Intervention Triggers

**Automated Alert System:**
```
CRITICAL ALERT (24-hour response):
├── Health score drops 20+ points in 30 days
├── Zero usage for 5+ consecutive days
├── Support escalation with sentiment analysis negative
└── Executive contact becomes unresponsive

HIGH PRIORITY (48-hour response):
├── Health score 60-40 range
├── 30% usage decrease month-over-month
├── Missed 2+ scheduled check-ins
└── Payment delays or invoice disputes

MEDIUM PRIORITY (1-week response):
├── Health score 75-60 range
├── Declining engagement metrics
├── Feature adoption plateau
└── Competitive activity detected
```

## RETENTION PLAYBOOKS

### Playbook 1: New Customer Onboarding (Days 1-90)

**Goal: Reduce early churn from 40% to 20%**

**Week 1-2: Foundation**
```
Day 1:
├── Welcome email sequence (CEO video + success guide)
├── CSM introduction call
├── Technical setup and integration
└── Success criteria definition

Day 3-5:
├── First value demonstration
├── Key user training session
├── Success metrics baseline
└── 30-60-90 day plan review

Week 2:
├── Feature walkthrough based on use case
├── Executive check-in (ROI timeline)
├── User adoption tracking begins
└── Integration verification
```

**Week 3-8: Adoption**
```
Week 3-4:
├── Advanced feature introduction
├── Best practice training
├── Power user identification
└── Success milestone #1 (basic value)

Week 5-6:
├── Workflow optimization
├── Additional user training
├── Integration expansion
└── Success milestone #2 (process improvement)

Week 7-8:
├── ROI measurement and reporting
├── Executive business review
├── Expansion opportunity identification
└── Success milestone #3 (business impact)
```

**Week 9-12: Optimization**
```
Week 9-10:
├── Advanced workflow implementation
├── Team expansion planning
├── Competitive differentiation review
└── Success milestone #4 (transformation)

Week 11-12:
├── 90-day success review
├── Annual planning integration
├── Reference opportunity discussion
└── Health score assessment (target: 80+)
```

### Playbook 2: At-Risk Customer Recovery (Health Score 40-60)

**Goal: Recover 60% of at-risk customers to healthy status**

**Immediate Response (Week 1):**
```
Day 1: Emergency Assessment
├── Health score deep dive analysis
├── Usage pattern analysis (last 90 days)
├── Support ticket review
└── Stakeholder mapping update

Day 2-3: Rapid Diagnosis
├── Executive outreach call
├── User interview (3-5 key users)
├── Technical audit
└── Competitive threat assessment

Day 4-5: Recovery Plan
├── Custom success plan development
├── Resource allocation (CSM, tech, exec)
├── Quick win identification
└── Timeline and milestone setting
```

**Intervention Execution (Week 2-4):**
```
Week 2: Quick Wins
├── Immediate technical fixes
├── Process optimization
├── Additional training or support
└── Early success demonstration

Week 3: Value Reinforcement
├── ROI recalculation and presentation
├── Business case refresh
├── Success story sharing
└── Executive sponsor engagement

Week 4: Future Planning
├── Renewal strategy discussion
├── Expansion opportunity exploration
├── Long-term partnership vision
└── Health score reassessment
```

### Playbook 3: Renewal Excellence (60-90 days before renewal)

**Goal: Achieve 95% renewal rate with 20% upsell attachment**

**90 Days Before Renewal:**
```
├── Renewal timeline and strategy creation
├── Business value assessment
├── Stakeholder influence mapping
└── Competitive landscape review
```

**60 Days Before Renewal:**
```
├── Executive business review
├── ROI presentation and documentation
├── Expansion opportunity presentation
└── Renewal proposal preparation
```

**30 Days Before Renewal:**
```
├── Formal renewal negotiation
├── Contract terms optimization
├── Upsell finalization
└── Future roadmap alignment
```

## VALUE EXPANSION STRATEGY

### Expansion Opportunity Framework

**Expansion Categories:**

**1. User Expansion (Land and Expand)**
```
Current State: 50 users average
Target: 75 users (+50% expansion)

Expansion Triggers:
├── Department rollout completion
├── New team onboarding
├── Seasonal business growth
└── Merger/acquisition activity

Expansion Process:
├── Usage capacity analysis
├── Department success story development
├── Expansion ROI calculation
└── Implementation timeline planning
```

**2. Feature Expansion (Upsell)**
```
Current State: Basic plan average
Target: 40% of customers on premium plans

Upsell Triggers:
├── Advanced workflow needs
├── Reporting and analytics requirements
├── Integration complexity
└── Compliance or security needs

Upsell Process:
├── Feature gap analysis
├── Business case development
├── Pilot program offering
└── Success measurement and expansion
```

**3. Multi-Product Expansion (Cross-sell)**
```
Current State: Single product adoption
Target: 25% multi-product customers

Cross-sell Triggers:
├── Adjacent use case identification
├── Workflow integration opportunities
├── Vendor consolidation initiatives
└── Strategic partnership expansion

Cross-sell Process:
├── Ecosystem mapping
├── Integration value demonstration
├── Pilot program implementation
└── Full deployment and optimization
```

## SUCCESS METRICS DASHBOARD

### Key Retention Metrics

**Primary KPIs:**
```
CHURN METRICS:
├── Monthly churn rate: Current 1.5% → Target 1.0%
├── Annual churn rate: Current 18% → Target 12%
├── Revenue churn rate: Current 20% → Target 10%
└── Time to churn: Average 8 months → Target 18+ months

GROWTH METRICS:
├── Net revenue retention: Current 95% → Target 110%
├── Customer lifetime value: Current $48K → Target $65K
├── Expansion revenue %: Current 15% → Target 25%
└── Upsell success rate: Current 20% → Target 35%
```

**Leading Indicators:**
```
HEALTH METRICS:
├── Average health score: Current 68 → Target 75+
├── Customers in green zone: Current 28% → Target 40%
├── Customers in red zone: Current 27% → Target 15%
└── Health score improvement rate: Track monthly trends

ENGAGEMENT METRICS:
├── Daily active users: Current 35% → Target 50%
├── Feature adoption rate: Current 40% → Target 60%
├── Support satisfaction: Current 4.2/5 → Target 4.5/5
└── NPS score: Current 32 → Target 50+
```

**Operational Metrics:**
```
TEAM PERFORMANCE:
├── CSM productivity: Accounts per CSM
├── Response time: Current 4 hours → Target 2 hours
├── Resolution time: Current 24 hours → Target 12 hours
└── Proactive outreach rate: Current 30% → Target 60%

PROCESS EFFICIENCY:
├── Onboarding completion rate: Current 75% → Target 95%
├── Time to first value: Current 45 days → Target 30 days
├── Renewal preparation time: Current 30 days → Target 60 days
└── Intervention success rate: Current 40% → Target 60%
```

### Real-Time Monitoring Dashboard

**Executive Summary View:**
```
┌─────────────────────────────────────────────┐
│ RETENTION HEALTH OVERVIEW                   │
├─────────────────────────────────────────────┤
│ Monthly Churn Rate: 1.2% ▼ (Target: 1.0%)  │
│ Health Score Avg: 71 ▲ (Target: 75+)       │
│ At-Risk Customers: 487 ▼ (Target: <375)    │
│ Intervention Success: 65% ▲ (Target: 60%)   │
└─────────────────────────────────────────────┘

SEGMENT PERFORMANCE:
├── SMB Segment: 1.8% churn, 68 health score
├── Mid-Market: 0.8% churn, 76 health score
├── Enterprise: 0.4% churn, 82 health score
└── New Customers: 2.5% churn, 62 health score
```

This comprehensive retention strategy provides the framework to reduce your churn from 18% to 12% while increasing customer value through systematic health monitoring, predictive intervention, and value expansion.

## Related Prompts

- [Customer Success Manager](./customer-success-manager.md)
- [Churn Prevention Specialist](./churn-prevention-specialist.md)
- [Customer Analytics Expert](./customer-analytics-expert.md)
