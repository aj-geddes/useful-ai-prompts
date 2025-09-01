# Performance Evaluation Expert

## Metadata
- **Created**: 2025-07-22

- **Category**: Analysis
- **Tags**: performance evaluation, KPIs, metrics analysis, benchmarking, performance optimization
- **Version**: 2.0.0
- **Use Cases**: performance assessment, KPI tracking, team evaluation, productivity analysis
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical performance evaluation assistant that helps you assess performance, identify gaps, and develop improvement plans. Provide your performance context and I'll deliver comprehensive analysis with actionable recommendations.

## Prompt

```
I'll help you evaluate performance and identify improvement opportunities. Let me gather information about what you need to assess.

About the evaluation:
1. What are you evaluating? (individual, team, department, process, etc.)
2. What performance areas? (productivity, quality, financial, customer service, etc.)
3. What time period are you reviewing?
4. What's your role in this evaluation?

Current situation:
5. What are your current performance metrics/KPIs?
6. What are the targets or benchmarks?
7. What concerns triggered this evaluation?
8. What data do you have available?

Goals and context:
9. What are your strategic goals or objectives?
10. How will this evaluation be used? (improvement planning, compensation, etc.)
11. What's your organizational culture around performance?
12. What resources are available for improvements?

Based on your answers, I'll provide:

**1. PERFORMANCE SCORECARD** - Overall assessment with key metrics
**2. GAP ANALYSIS** - Where you stand vs. targets and why
**3. ROOT CAUSE ANALYSIS** - Underlying reasons for performance issues
**4. BENCHMARKING** - How you compare to standards
**5. ACTION PLAN** - Specific steps to improve performance

Please provide the information above to begin the evaluation.
```

## Example Usage

**User Input:**
```
1. Evaluating: Customer service department (25 agents)
2. Areas: Response time, resolution rate, customer satisfaction, productivity
3. Time period: Last quarter (Q4) vs previous quarters and year
4. Role: Department manager responsible for improvement

5. Current metrics:
   - Average response time: 4.5 minutes (increased from 3.2)
   - First-call resolution: 68% (down from 75%)
   - Customer satisfaction: 3.8/5 (down from 4.2)
   - Tickets per agent: 45/day (up from 42)

6. Targets: 3-min response, 80% FCR, 4.5 CSAT, 50 tickets/day
7. Concerns: Customer complaints increasing, agent turnover up 20%
8. Data: CRM system, call recordings, customer surveys, HR records

9. Goals: Improve customer experience, reduce churn, increase efficiency
10. Purpose: Create improvement plan and justify additional resources
11. Culture: Performance-driven but supportive, open to change
12. Resources: $50K budget for training/tools, can hire 2 more agents
```

**Assistant Output:**

Based on your customer service department evaluation, here's my comprehensive analysis:

## PERFORMANCE SCORECARD

**Overall Performance: 72% (C+) - Needs Improvement**

```
Department Performance Dashboard
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Response Time      ██████░░░░ 62% ↓
Resolution Rate    ████████░░ 85% ↓  
Customer Satisfaction ████████░░ 84% ↓
Productivity       █████████░ 90% ↑
Agent Engagement   █████░░░░░ 55% ↓

Overall Trend: Declining (-8% vs last quarter)
```

**Key Findings:**
- Quality metrics declining while volume increases
- Agent burnout driving performance issues
- System inefficiencies creating bottlenecks

## GAP ANALYSIS

### Performance vs. Targets

```
Metric              Current   Target   Gap     Impact
─────────────────────────────────────────────────────
Response Time       4.5 min   3.0 min  -50%    High
First Call Resolve  68%       80%      -12pp   Critical
Customer Satisfaction 3.8     4.5      -0.7    Critical
Productivity        45/day    50/day   -10%    Medium
```

### Why These Gaps Exist:

1. **Response Time Gap (-50%)**
   - New ticketing system causing 30% delays
   - Increased complexity of issues (+25%)
   - Insufficient staffing during peak hours

2. **Resolution Rate Gap (-12pp)**
   - Knowledge base outdated (40% of articles)
   - New agents lack product training
   - Escalation process unclear

3. **CSAT Gap (-0.7 points)**
   - Long wait times frustrating customers
   - Inconsistent service quality
   - Lack of empowerment to resolve issues

## ROOT CAUSE ANALYSIS

### Primary Root Causes Identified:

**1. Agent Turnover & Training Gaps**
```
Turnover Impact Analysis:
- 20% turnover = 5 agents left
- New agents take 3 months to full productivity
- Training backlog creating quality issues
- Experienced agents overloaded (+15% tickets)
```

**2. System & Process Inefficiencies**
```
Process Bottlenecks:
┌─────────────┐  2 min   ┌──────────┐  1.5 min  ┌──────────┐
│ Ticket Intake│ ──────→ │ Diagnosis │ ──────→  │Resolution│
└─────────────┘ (manual) └──────────┘ (no tools)└──────────┘
                   ↑            ↑                      ↑
               [30% delay]  [Knowledge gaps]    [No authority]
```

**3. Leadership & Support Gaps**
- Supervisors managing 12-15 agents (industry standard: 8-10)
- No real-time coaching or quality monitoring
- Limited career development paths

## BENCHMARKING ANALYSIS

### Industry Comparison:

```
Your Performance vs Industry Standards
                    You     Industry   Best-in-Class
                           Average    
Response Time      4.5 min  3.5 min    2.0 min
FCR Rate          68%      75%        85%
CSAT              3.8/5    4.1/5      4.6/5
Agent Utilization 72%      78%        82%
Turnover Rate     20%      15%        8%

Position: Bottom 30th percentile
```

**Competitive Gaps:**
- Technology: 2 years behind industry leaders
- Training: 40 hours vs 80 hours industry standard
- Empowerment: Limited vs. full resolution authority

## ACTION PLAN

### Immediate Actions (Week 1-2)

**1. Stabilize Current Performance**
- Implement emergency schedule coverage
- Pair new agents with mentors
- Create quick-reference guides for top issues
- Expected Impact: +10% efficiency

**2. Quick Technology Fixes**
- Fix ticketing system delays (vendor ticket opened)
- Deploy chat macros for common responses
- Enable screen-sharing for complex issues
- Expected Impact: -20% response time

### Short-term Improvements (Month 1-3)

**3. Enhance Training & Support**
```
Training Overhaul Plan:
Week 1-2: Product knowledge intensive
Week 3-4: Systems and tools mastery
Week 5-6: Soft skills and de-escalation
Week 7-8: Shadowing and certification

Investment: $15K
Expected ROI: 25% productivity gain
```

**4. Implement Quality Program**
- Daily team huddles (15 min)
- Weekly 1-on-1 coaching sessions
- Real-time monitoring dashboard
- Peer recognition system

### Medium-term Initiatives (Month 3-6)

**5. Technology Upgrade**
- AI-powered knowledge base ($20K)
- Automated ticket routing
- Customer self-service portal
- Predictive issue resolution

**6. Organizational Restructure**
- Hire 2 senior agents ($100K annual)
- Promote 2 team leads
- Reduce supervisor span to 8-10 agents
- Create specialist roles for complex issues

### Success Metrics & Monitoring

```
90-Day Targets:
├── Response Time: 3.5 min (-22%)
├── FCR Rate: 75% (+7pp)
├── CSAT: 4.2/5 (+0.4)
├── Turnover: <15% (-5pp)
└── Productivity: 48/day (+7%)

Monitoring Cadence:
- Daily: Real-time dashboard
- Weekly: Team performance review
- Monthly: Full scorecard analysis
```

### Budget Allocation

```
Total Budget: $50K + 2 new hires

Training & Development:     $15K (30%)
Technology Improvements:    $20K (40%)
Quality Program:           $10K (20%)
Recognition & Retention:    $5K (10%)

Annual cost (2 agents):    $100K
Expected annual savings:   $250K (from reduced turnover & efficiency)
ROI: 150% in year 1
```

### Risk Mitigation

**Potential Risks:**
1. **Change resistance** → Involve agents in planning
2. **Technology delays** → Have manual backups
3. **Budget overrun** → Phase implementation
4. **Continued turnover** → Exit interviews & stay bonuses

Would you like me to detail any specific aspect of this plan or create implementation templates?

## Related Prompts

- [Team Performance Analyzer](./team-performance-analyzer.md)
- [Process Optimization Expert](./process-optimization-expert.md)
- [Employee Engagement Analyst](./employee-engagement-analyst.md)
