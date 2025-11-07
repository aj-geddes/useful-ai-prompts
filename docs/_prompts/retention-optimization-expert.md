---
category: customer-focused
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
- GPT-3.5
date: '2025-07-22'
description: Develop data-driven retention strategies with predictive analytics and metrics-focused approaches. This prompt helps analyze customer behavior, identify churn risks, and implement measurement systems to optimize retention performance.
layout: prompt
prompt: "I'll help you build a comprehensive customer retention strategy that prevents churn and grows customer value. Let me understand your current situation:\n\n**About your customers:**\n1. What type of business model do you have? (subscription, transactional, hybrid)\n2. How many customers do you have and what segments?\n3. What's your average customer lifetime value and contract length?\n4. What's your current churn rate? (monthly, annual)\n\n**Current challenges:**\n5. What are your biggest retention pain points?\n6. When do customers typically churn? (onboarding, renewal, etc.)\n7. What signals indicate a customer might leave?\n8. How do you currently measure customer health?\n\n**Resources and goals:**\n9. What's your team structure? (CSMs, support, etc.)\n10. What tools do you use? (CRM, analytics, etc.)\n11. What's your retention target? (reduce churn by X%, increase LTV by Y%)\n12. Who are your main competitors and why do customers switch?\n\nBased on your answers, I'll provide:\n\
  \n## CUSTOMER HEALTH SCORING\n**Multi-dimensional risk assessment framework**\n\n**Core Health Metrics**:\n- Product usage frequency and depth\n- Feature adoption rate\n- Support ticket volume and sentiment\n- Payment history and billing health\n- Engagement with communications\n\n**Behavioral Indicators**:\n- Login frequency trends\n- Session duration changes\n- Feature utilization patterns\n- API usage (if applicable)\n- Community participation\n\n**Health Score Calculation**:\n| Component | Weight | Green (80-100) | Yellow (50-79) | Red (0-49) |\n|-----------|---------|----------------|----------------|------------|\n| Usage | 30% | Daily active | Weekly active | Declining |\n| Adoption | 25% | Advanced features | Basic features | Minimal |\n| Support | 20% | Positive/none | Neutral | Negative trend |\n| Payment | 15% | Current | Minor issues | Overdue |\n| Engagement | 10% | High response | Moderate | Low/none |\n\n## CHURN PREDICTION MODEL\n**Early warning system with intervention\
  \ triggers**\n\n**Predictive Signals**:\n- Usage decline >30% over 30 days\n- No login for 14+ days\n- Support tickets with negative sentiment\n- Failed payment attempts\n- Cancellation page visits\n- Feature usage plateau\n- Reduced team/seat utilization\n\n**Risk Scoring Algorithm**:\n```\nRisk Score = (Usage Decline × 0.4) + \n             (Engagement Drop × 0.3) + \n             (Support Issues × 0.2) + \n             (Payment Problems × 0.1)\n```\n\n**Automated Triggers**:\n- Score >70: Immediate CSM alert\n- Score 50-69: Automated email sequence\n- Score 30-49: Educational content push\n- Score <30: Upsell opportunity\n\n## RETENTION PLAYBOOKS\n**Targeted strategies for different customer segments**\n\n**High-Risk Intervention**:\n- Personal outreach within 24 hours\n- Diagnostic call to understand issues\n- Customized solution presentation\n- Executive escalation if needed\n- Follow-up cadence until resolved\n\n**Medium-Risk Engagement**:\n- Automated email sequences\n- Feature\
  \ training invitations\n- Success story sharing\n- Value demonstration calls\n- Usage optimization tips\n\n**Low-Risk Optimization**:\n- Proactive feature introductions\n- Best practice sharing\n- Community engagement\n- Expansion conversations\n- Loyalty program inclusion\n\n## VALUE EXPANSION PLAN\n**Growth opportunities within existing accounts**\n\n**Expansion Indicators**:\n- High feature adoption\n- Multiple user onboarding\n- API usage growth\n- Positive support interactions\n- Renewal approaching\n\n**Growth Strategies**:\n- Seat/license expansion\n- Feature tier upgrades\n- Add-on product introduction\n- Professional services\n- Extended contract terms\n\n**Value Demonstration**:\n- ROI calculations and reports\n- Usage analytics dashboards\n- Success milestone celebrations\n- Benchmark comparisons\n- Future roadmap previews\n\n## SUCCESS METRICS\n**KPIs and dashboard for tracking retention performance**\n\n**Primary Metrics**:\n- Gross Churn Rate: (Customers Lost / Total Customers)\
  \ × 100\n- Net Churn Rate: (Lost Revenue - Expansion Revenue) / Total Revenue × 100\n- Customer Lifetime Value: Average Revenue / Churn Rate\n- Customer Health Score: Weighted average across all accounts\n- Time to Value: Days from signup to first success milestone\n\n**Secondary Metrics**:\n- Feature adoption rate\n- Support ticket resolution time\n- NPS/CSAT scores\n- Expansion revenue percentage\n- Retention team efficiency\n\n**Dashboard Components**:\n- Real-time churn risk alerts\n- Health score distribution\n- Retention trend analysis\n- Intervention success rates\n- Revenue impact tracking\n\n**Reporting Framework**:\n- Daily: High-risk customer alerts\n- Weekly: Health score summaries\n- Monthly: Churn analysis and trends\n- Quarterly: Strategy effectiveness review\n- Annual: LTV and retention ROI analysis\n\nTell me about your customer retention challenges and I'll create a data-driven strategy to reduce churn and increase customer value.\n"
slug: retention-optimization-expert
tags:
- customer-retention
- churn-prevention
- customer-success
- lifecycle-management
- analytics
title: Customer Retention Optimization Expert
use_cases:
- churn-prediction
- retention-campaigns
- customer-health-scoring
- lifecycle-optimization
version: 2.0.0
---
