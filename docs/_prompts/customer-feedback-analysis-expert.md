---
category: customer-focused
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for customer-focused optimization and expert consultation
slug: customer-feedback-analysis-expert
tags:
- customer focused
title: Customer Feedback Analysis Expert
use_cases:
- customer-focused optimization
- professional workflow enhancement
version: 3.0.0
---

# Customer Feedback Analysis Expert

## Metadata
- **Category**: Customer-Focused/Analytics
- **Created**: 2025-07-21
- **Version**: 1.0.0
- **Tags**: feedback-analysis, sentiment-analysis, customer-insights, data-analysis
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description
Transform raw customer feedback into actionable insights that drive product and service improvements. This prompt helps analyze feedback from multiple sources to identify patterns, priorities, and opportunities.

## Prompt Template

```
I'll help you analyze customer feedback to uncover actionable insights. Let's start with understanding your data:

FEEDBACK SOURCES:
- What types of feedback do you have? (surveys, reviews, support tickets, social media)
- How much feedback are we analyzing? (volume, time period)
- What format is it in? (structured ratings, open text, mixed)

BUSINESS CONTEXT:
- What specific aspects concern you? (product features, service quality, pricing)
- Any recent changes that might impact feedback?
- What decisions will this analysis inform?

ANALYSIS GOALS:
- Looking for trends, specific issues, or both?
- Need to compare segments or time periods?
- Any hypotheses to validate?

Based on your feedback data, I'll deliver:

## 1. SENTIMENT & THEME ANALYSIS
**Overall Sentiment Distribution**:
- Positive: X% | Neutral: Y% | Negative: Z%
- Trend over time
- Channel comparison

**Top Themes Identified**:
| Theme | Frequency | Sentiment | Example Quotes |
|-------|-----------|-----------|----------------|
| [Categorized themes with supporting evidence] |

## 2. PRIORITY MATRIX
**Impact vs. Frequency Analysis**:
- **Critical Issues** (High frequency + High negative impact)
- **Quick Wins** (Easy fixes with positive impact)
- **Strategic Opportunities** (Lower frequency but high value)
- **Monitor List** (Low impact items to track)

## 3. CUSTOMER SEGMENT INSIGHTS
Feedback patterns by:
- Customer type/tier
- Product/service line
- Geographic region
- Usage patterns
- Journey stage

Key differences and specific needs per segment

## 4. ROOT CAUSE ANALYSIS
For top issues:
- **Surface Complaint** → **Underlying Cause**
- Contributing factors
- Related feedback patterns
- Correlation with operational data

## 5. ACTION PLAN RECOMMENDATIONS
**Immediate Actions** (This week):
- Critical issue responses
- Communication needs

**Short-term** (Next month):
- Process improvements
- Product fixes

**Strategic** (Quarter):
- Systemic changes
- Investment priorities

Plus: Response templates and tracking metrics
```

## Examples

### Example 1: SaaS Product Feedback Analysis
**Input**: "3,000 support tickets and 500 NPS responses over last quarter, seeing churn increase"
**Output**: Identified 3 critical issues causing 60% of negative feedback, root cause linking to recent UI changes, segmented analysis showing enterprise customers 3x more affected, with specific fix prioritization.

### Example 2: Retail Customer Reviews
**Input**: "10,000 product reviews across 50 SKUs, want to improve product development"
**Output**: Theme analysis revealing sizing inconsistency as top issue (23% of negative reviews), quality perception varies by price point, competitive analysis showing gaps, recommended changes to 8 products.

## Usage Instructions
1. Gather all feedback sources and provide context about volume and format
2. Share any specific concerns or hypotheses you have
3. Review the theme analysis and validate against your experience
4. Use the priority matrix to focus resources
5. Implement action plan with measurement framework

## Related Prompts
- Voice of Customer Analysis Expert
- Customer Satisfaction Measurement Expert
- Customer Journey Mapping Expert