---
category: customer-focused
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
- GPT-3.5
date: '2025-07-21'
description: Transform raw customer feedback into actionable insights that drive product and service improvements. This prompt helps analyze feedback from multiple sources to identify patterns, priorities, and opportunities.
layout: prompt
prompt: |
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
slug: customer-feedback-analysis-expert
tags:
- feedback-analysis
- sentiment-analysis
- customer-insights
- data-analysis
tips:
- Gather all feedback sources and provide context about volume and format
- Share any specific concerns or hypotheses you have
- Review the theme analysis and validate against your experience
- Use the priority matrix to focus resources
- Implement action plan with measurement framework
title: Customer Feedback Analysis Expert
version: 1.0.0
---
