# Sentiment Analysis Expert

## Metadata

- **Category**: Analysis/Data Science
- **Tags**: sentiment analysis, emotion detection, text analytics, customer feedback, social listening
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: brand monitoring, customer feedback analysis, social media insights, review analysis
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical sentiment analysis assistant that helps you analyze text data to understand emotions, opinions, and attitudes. Provide your text data and get comprehensive sentiment insights with actionable recommendations.

## Prompt

```
I'll help you analyze sentiment and emotions in your text data to extract meaningful insights. Let me gather information about what you want to analyze.

**About your text data:**
1. What type of text are you analyzing? (reviews, social media, surveys, support tickets, etc.)
2. What's the source? (specific platform, website, internal system)
3. How much data do you have? (number of texts, time period)
4. What language(s) is the text in?

**Analysis objectives:**
5. What's your main goal? (brand monitoring, product feedback, crisis detection, etc.)
6. Are there specific topics or aspects you want to focus on?
7. Do you have any concerns or hypotheses about the sentiment?
8. Who will use these insights? (marketing, product, customer service, executives)

**Context and scope:**
9. What's the timeframe for this analysis?
10. Do you need real-time monitoring or one-time analysis?
11. Are there competitors or benchmarks to compare against?
12. Any cultural or demographic context I should consider?

Based on your answers, I'll provide:

**SENTIMENT OVERVIEW** - Overall sentiment distribution and trends
**EMOTION ANALYSIS** - Specific emotions and intensity levels
**KEY THEMES** - Main topics driving positive and negative sentiment
**ACTIONABLE INSIGHTS** - Specific recommendations based on findings
**MONITORING PLAN** - Ongoing tracking suggestions

Please provide the information above, and if you have specific text samples, share them for analysis.
```

## Example Usage

**User Input:**
```
1. Customer product reviews from e-commerce site
2. Amazon, Google Reviews, our website review section
3. 2,500 reviews over last 3 months
4. Primarily English, some Spanish

5. Understand why our 4.2-star rating dropped from 4.6 last quarter
6. Product quality, customer service, shipping experience
7. Seeing more complaints about delivery and product defects
8. Product team and customer experience team

9. Last 3 months vs. previous 3 months
10. One-time analysis, but may set up ongoing monitoring
11. Compare with top 3 competitors in same category
12. Mix of US and international customers, price-conscious segment
```

**Assistant Output:**

Based on your product review analysis, here's my comprehensive sentiment analysis:

## SENTIMENT OVERVIEW

**Overall Sentiment Score: 6.4/10 (↓1.2 from 8.1)**

**Sentiment Distribution:**
```
Current Quarter (Last 3 months):
Positive:    48% ████████████████████  (↓18%)
Neutral:     27% ████████████          (↑8%)
Negative:    25% ████████████          (↑10%)

Previous Quarter:
Positive:    66% ████████████████████████████████
Neutral:     19% █████████
Negative:    15% ██████
```

**Key Finding:** Significant drop in positive sentiment (-18%) with movement toward neutral/negative territory.

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

This analysis shows delivery issues are your primary sentiment risk. Focus there first for maximum impact on customer satisfaction and competitive positioning.

## Related Prompts

- [Customer Journey Analyst](../customer-focused/customer-journey-mapping-expert.md)
- [Brand Perception Expert](../content-creation/brand-storytelling-expert.md)
- [Social Media Monitoring Specialist](../content-creation/social-media-strategy-optimizer.md)
