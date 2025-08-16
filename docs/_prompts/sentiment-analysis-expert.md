---
category: analysis
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for analysis optimization and expert consultation
slug: sentiment-analysis-expert
tags:
- analysis
title: Sentiment Analysis Expert
use_cases:
- analysis optimization
- professional workflow enhancement
version: 3.0.0
---

# Sentiment Analysis Expert

## Metadata

- **Category**: Analysis
- **Tags**: sentiment analysis, emotion detection, text analytics, customer feedback, social listening
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: brand monitoring, customer feedback analysis, social media insights, review analysis
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical sentiment analysis assistant that helps you analyze text data to understand emotions, opinions, and attitudes. Provide your text data and I'll deliver comprehensive sentiment insights with actionable recommendations.

## Prompt

```
I'll help you analyze sentiment and emotions in your text data to extract meaningful insights. Let me gather information about what you want to analyze.

About your text data:
1. What type of text are you analyzing? (reviews, social media, surveys, support tickets, etc.)
2. What's the source? (specific platform, website, internal system)
3. How much data do you have? (number of texts, time period)
4. What language(s) is the text in?

Analysis objectives:
5. What's your main goal? (brand monitoring, product feedback, crisis detection, etc.)
6. Are there specific topics or aspects you want to focus on?
7. Do you have any concerns or hypotheses about the sentiment?
8. Who will use these insights? (marketing, product, customer service, executives)

Context and scope:
9. What's the timeframe for this analysis?
10. Do you need real-time monitoring or one-time analysis?
11. Are there competitors or benchmarks to compare against?
12. Any cultural or demographic context I should consider?

Based on your answers, I'll provide:

**1. SENTIMENT OVERVIEW** - Overall sentiment distribution and trends
**2. EMOTION ANALYSIS** - Specific emotions and intensity levels
**3. KEY THEMES** - Main topics driving positive and negative sentiment
**4. ACTIONABLE INSIGHTS** - Specific recommendations based on findings
**5. MONITORING PLAN** - Ongoing tracking suggestions

Please provide the information above, and if you have specific text samples, share them for analysis.
```

## Example Usage

**User Input:**
```
1. Type: Customer product reviews from e-commerce site
2. Source: Amazon, Google Reviews, our website review section
3. Volume: 2,500 reviews over last 3 months
4. Language: Primarily English, some Spanish

5. Goal: Understand why our 4.2-star rating dropped from 4.6 last quarter
6. Focus: Product quality, customer service, shipping experience
7. Concerns: Seeing more complaints about delivery and product defects
8. Users: Product team and customer experience team

9. Timeframe: Last 3 months vs. previous 3 months
10. Need: One-time analysis, but may set up ongoing monitoring
11. Competitors: Compare with top 3 competitors in same category
12. Context: Mix of US and international customers, price-conscious segment
```

**Assistant Output:**

Based on your product review analysis, here's my comprehensive sentiment analysis:

## SENTIMENT OVERVIEW

**Overall Sentiment Score: 6.4/10 (↓1.2 from 8.1)**

**Sentiment Distribution:**
```
Current Quarter (Last 3 months):
Positive:    48% ██████████████████████  (↓18%)
Neutral:     27% ████████████            (↑8%)
Negative:    25% ████████████            (↓10%)

Previous Quarter:
Positive:    66% ████████████████████████████████
Neutral:     19% ████████████
Negative:    15% ██████████
```

**Key Finding:** Significant drop in positive sentiment (-18%) with sentiment moving toward neutral/negative territory.

## EMOTION ANALYSIS

### Primary Emotions Detected

**Negative Emotions (Increasing):**
- **Frustration**: 32% (↑15%) - Mainly delivery delays
- **Disappointment**: 28% (↑12%) - Product quality issues  
- **Anger**: 18% (↑8%) - Customer service problems
- **Anxiety**: 12% (↑5%) - Uncertainty about orders

**Positive Emotions (Decreasing):**
- **Satisfaction**: 45% (↓20%) - Still majority but declining
- **Excitement**: 22% (↓10%) - New features appreciated
- **Trust**: 18% (↓15%) - Brand confidence shaken
- **Gratitude**: 15% (↓8%) - Good experiences

### Emotion Intensity Heatmap
```
High Intensity    Medium Intensity    Low Intensity
────────────────  ─────────────────   ──────────────
Frustration ████  Satisfaction ████   Excitement ██
Disappoint. ███   Trust ████████      Gratitude ███
Anger ████████    Anxiety ██████      
```

## KEY THEMES & SENTIMENT DRIVERS

### Top Negative Drivers

**1. Delivery Problems (35% of negative mentions)**
```
Sample Quotes:
"Package was supposed to arrive Tuesday, came Friday damaged"
"Third time my order was delayed with no communication"
"Delivery guy left expensive item on doorstep in rain"

Sentiment Impact: -0.8 points
Emotion: Frustration (high intensity)
Frequency: 875 mentions
```

**2. Product Quality Issues (28% of negative mentions)**
```
Sample Quotes:
"Product broke after 2 weeks, feels cheap compared to before"
"Color was completely different from photos"
"Missing parts, had to contact support multiple times"

Sentiment Impact: -0.6 points
Emotion: Disappointment (medium-high intensity)
Frequency: 700 mentions
```

**3. Customer Service Problems (22% of negative mentions)**
```
Sample Quotes:
"Waited 2 hours on chat, then got disconnected"
"Support agent was rude and unhelpful"
"Still waiting for response to my email from last week"

Sentiment Impact: -0.7 points
Emotion: Anger (high intensity)
Frequency: 550 mentions
```

### Top Positive Drivers

**1. Product Features (52% of positive mentions)**
```
Sample Quotes:
"Love the new design, much easier to use"
"Exactly what I needed, works perfectly"
"Great value for the price point"

Sentiment Impact: +0.5 points
Emotion: Satisfaction (medium intensity)
Frequency: 1,248 mentions
```

**2. Fast Shipping (When It Works) (31% of positive mentions)**
```
Sample Quotes:
"Arrived next day as promised, great packaging"
"Faster than expected delivery"

Sentiment Impact: +0.4 points
Emotion: Pleasant surprise (medium intensity)
Frequency: 744 mentions
```

## COMPARATIVE ANALYSIS

### Competitor Sentiment Comparison

**Your Brand vs. Top 3 Competitors:**
```
Brand           Overall Score    Delivery    Quality    Service
─────────────   ─────────────    ────────    ───────    ───────
Your Brand      6.4/10 ↓         5.2/10      6.8/10     5.9/10
Competitor A    7.8/10 →         8.1/10      7.5/10     7.9/10
Competitor B    7.2/10 ↑         7.5/10      6.9/10     7.0/10
Competitor C    6.9/10 →         6.8/10      7.2/10     6.5/10
```

**Gap Analysis:**
- **Delivery**: 1.6-2.9 point gap (your biggest weakness)
- **Service**: 1.1-2.0 point gap (second priority)
- **Quality**: 0.1-0.7 point gap (relatively competitive)

## ACTIONABLE INSIGHTS

### Immediate Actions (Next 30 Days)

**1. Emergency Delivery Improvement**
- Partner with more reliable shipping carriers
- Implement real-time tracking notifications
- Create proactive delay communication system
- Expected impact: +0.4 sentiment points

**2. Customer Service Triage**
- Increase chat/phone support capacity
- Create escalation process for frustrated customers
- Implement response time guarantees
- Expected impact: +0.3 sentiment points

**3. Quality Control Review**
- Audit current supplier quality standards
- Implement random product testing
- Review product photos for accuracy
- Expected impact: +0.2 sentiment points

### Strategic Actions (Next 90 Days)

**4. Delivery Experience Overhaul**
```
Improvements Needed:
├── Carrier Diversification: Add 2 regional carriers
├── Packaging Quality: Upgrade to damage-resistant materials
├── Delivery Options: Add evening/weekend delivery
├── Communication: SMS/email updates at each stage
└── Recovery Process: Instant replacement for damaged items
```

**5. Customer Service Excellence Program**
```
Service Improvements:
├── Training: Advanced de-escalation techniques
├── Tools: Faster access to order/product information  
├── Empowerment: Ability to offer instant solutions
├── Metrics: Response time <5min, resolution rate >90%
└── Follow-up: Satisfaction check 24 hours later
```

### Recovery Timeline & Targets

**30-Day Goal:** Sentiment score 7.0 (+0.6)
- Stop delivery issues bleeding
- Improve service responsiveness
- Address quality control gaps

**60-Day Goal:** Sentiment score 7.5 (+1.1)
- New delivery partnerships active
- Service training completed
- Quality improvements visible

**90-Day Goal:** Sentiment score 8.0 (+1.6)
- Match competitor performance
- Exceed customer expectations
- Rebuild brand trust

## MONITORING RECOMMENDATIONS

### Real-Time Alerts Setup
```
Critical Alerts (Immediate notification):
├── Sentiment drops below 6.0 in any 24-hour period
├── Delivery complaints spike >50% above normal
├── Service satisfaction drops below 70%
└── Any review mentions competitor switching

Warning Alerts (Daily digest):
├── Negative sentiment increases >5% week-over-week
├── New product quality issues emerge
├── Response time exceeds targets
└── Competitor sentiment improvements detected
```

### Weekly Tracking Dashboard
- Overall sentiment trend
- Issue category breakdown
- Competitor gap monitoring
- Action plan progress
- Customer effort scores

### Monthly Deep Dive
- Emerging themes analysis
- Customer journey sentiment mapping
- Competitive positioning review
- ROI of improvement initiatives

Would you like me to analyze specific review samples you have, or dive deeper into any particular aspect of the sentiment analysis?

## Related Prompts

- [Customer Journey Analyst](./customer-journey-analyst.md)
- [Brand Perception Expert](./brand-perception-expert.md)
- [Social Media Monitoring Specialist](./social-media-monitoring-specialist.md)
- **Total Volume**: 48,392 mentions
- **Engagement Rate**: 4.7% (above average)
│ Virality Score: 6.8/10                      │
└─────────────────────────────────────────────┘

Trend Over Time:
  50%│     ╱─╲    ╱╲
     │    ╱   ╲  ╱  ╲   Positive
  40%│   ╱     ╲╱    ╲ ╱
     │  ╱              ╲
  30%│ ─────────────────── Neutral
     │╲        ╱╲      ╱
  20%│ ╲      ╱  ╲    ╱  Negative
     │  ╲____╱    ╲__╱
     └────────────────────────
      Jan  Feb  Mar  Apr  May

Key Inflection Points:
Feb 15: Product launch (+18% positive)
Mar 22: Service issue (-15% spike negative)
Apr 30: Recovery campaign (+12% positive)
```

#### Emotional Spectrum Analysis

```
Emotion Detection Results (Plutchik Model):
                    Joy
                 ████████ 28%
                    ↑
    Anticipation ←─────→ Trust
        ██████ 22%     ████████ 31%
           ↖         ↗
    Fear      ╳     Surprise
   ████ 12%         ███ 8%
           ↙         ↘
    Anger  ←─────→  Disgust
   █████ 15%        ██ 6%
                    ↓
                 Sadness
                ████ 11%

Primary Emotional Clusters:
• Trust + Joy = Love (Brand affinity: High)
• Anticipation + Joy = Optimism (Future outlook: Positive)
• Fear + Surprise = Awe (Product impact: Moderate)
• Anger + Disgust = Contempt (Service issues: Concerning)
```

### DETAILED SENTIMENT ANALYSIS

#### Aspect-Based Sentiment Breakdown

```
Product/Service Aspect Sentiment:
┌────────────────┬─────────┬─────────┬─────────┐
│ Aspect         │ Positive│ Neutral │ Negative│
├────────────────┼─────────┼─────────┼─────────┤
│ Product Quality│   72%   │   18%   │   10%   │
│ ████████████   │ ██████████████   │ ██      │
├────────────────┼─────────┼─────────┼─────────┤
│ Customer Service│  38%   │   27%   │   35%   │
│ ██████         │ ████████│ █████   │ ██████  │
├────────────────┼─────────┼─────────┼─────────┤
│ Pricing/Value  │   45%   │   30%   │   25%   │
│ ███████        │ █████████│ ██████ │ █████   │
├────────────────┼─────────┼─────────┼─────────┤
│ User Experience│   61%   │   24%   │   15%   │
│ ██████████     │ ████████████   │ ███      │
├────────────────┼─────────┼─────────┼─────────┤
│ Brand Image    │   68%   │   22%   │   10%   │
│ ███████████    │ █████████████  │ ██       │
└────────────────┴─────────┴─────────┴─────────┘

Key Insights:
✓ Product quality drives positive sentiment
⚠ Customer service is polarizing issue
✓ Brand perception remains strong
```

#### Sentiment Drivers Analysis

```python
# Top Positive Drivers
positive_themes = {
    'product_innovation': {
        'frequency': 3847,
        'sentiment_score': 8.9,
        'example': "The new features are game-changing!",
        'keywords': ['innovative', 'revolutionary', 'amazing'],
        'impact': 'High brand differentiation'
    },
    'ease_of_use': {
        'frequency': 2932,
        'sentiment_score': 8.4,
        'example': "So intuitive, my grandma could use it",
        'keywords': ['simple', 'easy', 'intuitive'],
        'impact': 'Broad market appeal'
    },
    'value_for_money': {
        'frequency': 2156,
        'sentiment_score': 7.8,
        'example': "Worth every penny and more",
        'keywords': ['value', 'worth', 'affordable'],
        'impact': 'Purchase justification'
    }
}

# Top Negative Drivers
negative_themes = {
    'support_response_time': {
        'frequency': 1823,
        'sentiment_score': 2.3,
        'example': "Waiting 3 days for a response is unacceptable",
        'keywords': ['slow', 'waiting', 'ignored'],
        'impact': 'Churn risk increase'
    },
    'bug_issues': {
        'frequency': 1245,
        'sentiment_score': 3.1,
        'example': "App crashes every time I try to save",
        'keywords': ['crash', 'bug', 'broken'],
        'impact': 'Usage friction'
    }
}
```

### EMOTIONAL JOURNEY MAPPING

#### Customer Emotional Timeline

```
Typical Customer Emotional Journey:
         Excitement
             ↑
    Discovery │ Purchase  Usage   Issue    Resolution
        ●────┼─────●──────●──────●─────────●
        │    │     │      │      │         │
   Hope │    │ Joy │      │ Frustration   │ Satisfaction
        │    │     │      ↓              ↗ │
        │    │     │   Anxiety      Relief │
        │    │     │                       │
────────┴────┴─────┴───────────────────────┴────
Pre-purchase  Day 0   Week 1   Week 4    Week 6

Emotional Volatility Index: 6.8/10 (Moderate)
Recovery Rate: 73% return to positive
Critical Intervention Points: Week 1, Week 4
```

#### Sentiment Contagion Analysis

```
Social Influence Patterns:
┌─────────────────────────────────────────────┐
│ Influencer Sentiment → Follower Sentiment   │
├─────────────────────────────────────────────┤
│ Positive Influencer Post:                   │
│ • Reach: 45,000                            │
│ • Engagement: 12%                          │
│ • Sentiment Lift: +15% in replies          │
│ • Cascade Effect: 3.2x amplification       │
├─────────────────────────────────────────────┤
│ Negative Influencer Post:                   │
│ • Reach: 38,000                            │
│ • Engagement: 18% (higher!)                │
│ • Sentiment Drop: -22% in replies          │
│ • Cascade Effect: 4.7x amplification       │
└─────────────────────────────────────────────┘

Key Finding: Negative sentiment spreads
47% faster than positive sentiment

Mitigation Strategy Required
```

### COMPETITIVE SENTIMENT ANALYSIS

#### Brand Sentiment Comparison

```
Market Sentiment Landscape:
                 Positive Sentiment %
    70%│      ● Competitor A
       │     ╱ ╲
    60%│    ╱   ● Us (Rising)
       │   ╱   ╱ ╲
    50%│  ●   ╱   ╲ ● Competitor B
       │ ╱   ╱     ╲
    40%│╱   ●       ╲
       │  Competitor C ╲
    30%│              ● Competitor D
       └──────────────────────────
        Low          High
           Mention Volume →

Share of Voice: 28% (2nd place)
Sentiment Gap vs Leader: -8%
Momentum: +2.3% monthly (Fastest growing)
```

#### Topic-Based Competitive Analysis

```
Sentiment by Key Topics:
                    Us    Comp A  Comp B  Industry
Innovation         85%     78%     62%      71%
Quality            78%     82%     71%      74%
Service            62%     89%     68%      73%
Price/Value        71%     65%     84%      72%
Overall            74%     79%     71%      73%

Competitive Advantages:
• Innovation perception (+14% vs industry)
• Price/value balance (+6% vs Comp A)

Competitive Weaknesses:
• Service sentiment (-27% vs Comp A)
• Quality perception (-4% vs leader)
```

### REAL-TIME ALERTS & EMERGING ISSUES

#### Sentiment Anomaly Detection

```
Active Sentiment Alerts:
┌─────────────────────────────────────────────┐
│ 🔴 CRITICAL: Negative Spike Detected        │
├─────────────────────────────────────────────┤
│ Time: Last 4 hours                          │
│ Volume: 342 mentions (5x normal)            │
│ Sentiment: -73% negative                    │
│ Primary Issue: Payment processing errors    │
│ Geographic: US East Coast                   │
│ Virality Risk: High (R₀ = 3.2)            │
├─────────────────────────────────────────────┤
│ Recommended Actions:                        │
│ 1. Immediate response team activation       │
│ 2. Public acknowledgment within 1 hour      │
│ 3. Executive escalation triggered           │
└─────────────────────────────────────────────┘

Historical Context: Similar to March incident
Expected Duration: 24-48 hours if handled well
```

#### Emerging Theme Detection

```python
# Emerging Topics (Last 7 Days)
emerging_themes = {
    'sustainability_concerns': {
        'growth_rate': '+340%',
        'current_volume': 892,
        'sentiment': 'Mixed (45% positive)',
        'example': "Love the product but what about packaging?",
        'opportunity': 'ESG communication gap'
    },
    'feature_request_ai': {
        'growth_rate': '+280%',
        'current_volume': 567,
        'sentiment': 'Positive (78%)',
        'example': "When will you add AI features like [competitor]?",
        'opportunity': 'Innovation roadmap reveal'
    },
    'community_building': {
        'growth_rate': '+125%',
        'current_volume': 423,
        'sentiment': 'Very Positive (87%)',
        'example': "The user community is amazing!",
        'opportunity': 'Amplify community voice'
    }
}

# Predictive Theme Modeling
next_30_days_forecast = {
    'sustainability': 'Will reach 5,000 mentions',
    'ai_features': 'Plateau at 1,000 mentions',
    'pricing_pressure': 'Emerge if competitors move'
}
```

### LINGUISTIC & CULTURAL ANALYSIS

#### Language Pattern Insights

```
Communication Style Analysis:
┌─────────────────────────────────────────────┐
│ Linguistic Markers          │ Frequency     │
├─────────────────────────────┼───────────────┤
│ First-person pronouns       │ 68% of posts  │
│ Emotional intensifiers      │ 45% of posts  │
│ Comparative language        │ 32% of posts  │
│ Recommendation phrases      │ 28% of posts  │
│ Sarcasm indicators         │ 8% of posts   │
└─────────────────────────────┴───────────────┘

Engagement Correlation:
• Personal stories: 3.2x more engagement
• Emotional language: 2.8x more shares
• Questions: 4.1x more responses
• Humor/Sarcasm: 2.3x more reactions

Writing Style Impact on Sentiment:
Formal/Professional: 65% positive
Casual/Conversational: 71% positive
Emotional/Passionate: 58% positive (volatile)
Technical/Detailed: 74% positive
```

#### Cross-Cultural Sentiment Variations

```
Regional Sentiment Differences:
                    US    UK    DE    JP    BR
Overall Positive   68%   72%   61%   58%   75%
Service Mentions   45%   38%   52%   31%   41%
Quality Focus      32%   41%   58%   67%   28%
Price Sensitivity  High  Med   Low   Med   High
Feature Requests   38%   31%   44%   52%   29%

Cultural Insights:
• German market: Quality-obsessed, detailed feedback
• Japanese market: Indirect criticism, high standards
• Brazilian market: Enthusiastic, social sharing
• UK market: Dry humor in complaints
• US market: Direct, solution-oriented
```

### PREDICTIVE SENTIMENT MODELING

#### Sentiment Trajectory Forecast

```
30-Day Sentiment Prediction:
  55%│         ╱─── Optimistic (30%)
     │        ╱
  50%│      ╱───── Base Case (50%)
     │    ●───
  45%│  ╱      ╲─── Conservative (20%)
     │╱Current   ╲
  40%│ (48%)      ╲
     └──────────────────────
      Now    +1W   +2W   +1M

Prediction Confidence: 78%
Key Assumptions:
• No major product issues
• Competitor activity normal
• Seasonal patterns considered

Risk Factors:
• Unresolved service issues (-5%)
• Competitor campaign (-3%)
• Economic downturn (-4%)
```

### ACTIONABLE RECOMMENDATIONS

#### Strategic Response Framework

```
Priority Action Matrix:
                    High Impact
                         │
    Quick Wins          │    Strategic Moves
    • Respond to        │    • Service overhaul
      viral negative    │    • AI feature launch
    • Amplify positive  │    • Community program
                        │
    Low ────────────────┼──────────────── High
    Effort              │              Effort
                        │
    Maintenance         │    Consider Later
    • Regular monitoring│    • Packaging redesign
    • FAQ updates       │    • Premium tier
    • Template responses│    • Global expansion
                        │
                    Low Impact

Immediate Actions (This Week):
1. Address payment processing issue publicly
2. Launch "We heard you" service improvement campaign
3. Engage top positive advocates as amplifiers
4. Create sustainability roadmap communication

Strategic Initiatives (This Quarter):
1. Implement AI-powered features per demand
2. Redesign customer service experience
3. Build brand ambassador program
4. Develop crisis response playbook
```

#### Communication Strategy

```
Sentiment-Driven Messaging:
┌─────────────────────────────────────────────┐
│ Audience Segment   │ Tone      │ Channel   │
├────────────────────┼───────────┼───────────┤
│ Happy Customers    │ Grateful  │ Email/SM  │
│ Message: "Thank you for believing in us"    │
├────────────────────┼───────────┼───────────┤
│ Frustrated Users   │ Empathetic│ Direct    │
│ Message: "We hear you and we're fixing it"  │
├────────────────────┼───────────┼───────────┤
│ Neutral Observers  │ Informative│ Blog/PR  │
│ Message: "Here's what makes us different"   │
├────────────────────┼───────────┼───────────┤
│ Potential Churners │ Urgent    │ Personal  │
│ Message: "Let us make this right for you"   │
└─────────────────────────────────────────────┘

Channel Effectiveness:
Twitter: Real-time response (< 1 hour)
Email: Detailed explanations (< 24 hours)
Community: Peer support amplification
CEO Communication: Crisis/major positive only
```

### MEASUREMENT & MONITORING

#### Sentiment KPI Dashboard

```
Real-Time Sentiment Metrics:
┌─────────────────────────────────────────────┐
│ SENTIMENT HEALTH SCORE: ████████░░ 76/100  │
├─────────────────────────────────────────────┤
│ 24-Hour Metrics:                            │
│ • Volume: 1,247 mentions (↑12%)             │
│ • Positive Ratio: 51% (↑3%)                │
│ • Response Rate: 78% < 2hrs                │
│ • Escalations: 23 (↓5)                     │
├─────────────────────────────────────────────┤
│ Weekly Trends:                              │
│ • NPS Correlation: +0.73                    │
│ • Churn Prediction: -2.1%                  │
│ • Revenue Impact: +$147K                   │
└─────────────────────────────────────────────┘

Alert Thresholds:
• Negative spike > 40%: Immediate alert
• Volume surge > 3x: Trend analysis
• Influencer negative: Executive escalation
• Sentiment < 40%: Crisis mode activation
```

### APPENDICES

#### A. Methodology & Algorithms

[NLP models used, accuracy metrics, validation approach]

#### B. Detailed Linguistic Analysis

[Part-of-speech patterns, semantic networks, emotion lexicons]

#### C. Historical Sentiment Patterns

[Long-term trends, seasonal variations, event impacts]

#### D. Response Templates

[Pre-approved messages for common sentiment scenarios]

```

## Usage Instructions
1. Define clear objectives for sentiment analysis
2. Ensure representative data sampling across channels
3. Consider cultural and linguistic context
4. Look beyond polarity to emotional nuance
5. Track sentiment drivers, not just scores
6. Connect sentiment to business outcomes
7. Develop response playbooks for different scenarios
8. Monitor competitor sentiment for context

## Examples
### Example 1: Product Launch Sentiment Analysis
**Input**:
```

{{data_source}}: Twitter, Reddit, product reviews
{{volume}}: 15,000 mentions over 2 weeks
{{domain}}: Consumer electronics - smartphone launch
{{analysis_objective}}: Assess launch success and identify issues
{{specific_focus}}: Camera features, battery life, price perception

```

**Output**: [Comprehensive analysis showing 73% positive sentiment with camera innovation driving enthusiasm, but 31% negative sentiment on battery concerns, with specific recommendations for marketing messages and product improvements]

## Related Prompts
- [Social Media Analyst](/prompts/analysis/social-media-analyst.md)
- [Brand Reputation Manager](/prompts/communication/brand-reputation-manager.md)
- [Customer Feedback Analyzer](/prompts/analysis/customer-feedback-analyzer.md)

## Research Notes
- Combines NLP techniques with psychological frameworks
- Goes beyond simple positive/negative to emotional nuance
- Includes predictive modeling and trend detection
- Emphasizes actionable insights over metrics
- Integrates competitive context and cultural factors
```
