---
category: decision-making
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
- GPT-3.5
date: '2025-07-21'
description: Master the art of prioritization with proven frameworks like Impact/Effort Matrix, MoSCoW Method, and Eisenhower Matrix. Transform overwhelming task lists into clear action plans that focus energy on what matters most.
layout: prompt
prompt: |
  I'll help you prioritize effectively using proven frameworks. Let's understand your situation:
  
  PRIORITIZATION CONTEXT:
  - What type of items are you prioritizing? (projects, tasks, features, initiatives)
  - How many items are you evaluating? (rough count)
  - What's driving the need to prioritize? (limited resources, deadlines, strategic focus)
  
  CONSTRAINTS & CRITERIA:
  - What resources are limited? (time, budget, people, expertise)
  - What are your key success criteria?
  - Any fixed deadlines or dependencies?
  - Who are the key stakeholders involved?
  
  Based on your context, I'll provide:
  
  ## 1. FRAMEWORK RECOMMENDATION
  
  **Best Framework for Your Situation:**
  - Primary framework selection and rationale
  - Supporting frameworks for additional clarity
  - Customization for your specific needs
  
  ## 2. IMPACT/EFFORT MATRIX
  
  **High Impact ↑**
  ```
              | [Do First]    | [Do Next]
              | Quick Wins    | Major Projects
  ------------|---------------|---------------
              | [Schedule]    | [Question]  
              | Fill-ins      | Time Sinks
  **Low Impact ↓**
              Low Effort →    High Effort
  ```
  
  **Quadrant Actions:**
  - **Do First** (High Impact, Low Effort): Immediate priorities
  - **Do Next** (High Impact, High Effort): Plan and resource properly  
  - **Schedule** (Low Impact, Low Effort): Fill available time slots
  - **Question** (Low Impact, High Effort): Consider elimination
  
  ## 3. EISENHOWER MATRIX
  
  **Urgent ↑**
  ```
              | [Crisis]      | [Prevention]
              | Do Now        | Plan & Schedule  
  ------------|---------------|---------------
              | [Distractions]| [Time Wasters]
              | Delegate      | Eliminate
  **Not Urgent ↓**
              Important →     Not Important
  ```
  
  ## 4. MOSCOW METHOD
  
  **Priority Levels:**
  - **Must Have**: Non-negotiable, critical requirements
  - **Should Have**: Important but can be delayed if necessary
  - **Could Have**: Nice to have, adds value but not essential
  - **Won't Have**: Explicitly excluded for this time period
  
  ## 5. VALUE-BASED PRIORITIZATION
  
  **Scoring Matrix:**
  | Item | Business Value | User Value | Effort | Risk | Priority Score |
  |------|----------------|------------|--------|------|----------------|
  | [Template for your items] |||||| 
  
  **Scoring Guide:**
  - Business Value (1-10): Revenue, cost savings, strategic alignment
  - User Value (1-10): User satisfaction, problem severity, frequency
  - Effort (1-10): Development time, complexity, resources needed
  - Risk (1-10): Technical risk, market risk, execution risk
  - Priority Score: (Business Value + User Value) / (Effort + Risk)
  
  ## 6. KANO MODEL CLASSIFICATION
  
  **Feature Categories:**
  - **Delighters**: Exceed expectations, high satisfaction when present
  - **Performance**: Linear satisfaction relationship with quality
  - **Basic**: Expected features, dissatisfaction when missing
  - **Indifferent**: Little impact on satisfaction
  - **Reverse**: Can actually decrease satisfaction
  
  ## 7. WEIGHTED DECISION MATRIX
  
  **Custom Criteria Weighting:**
  - Define your specific criteria (ROI, strategic fit, feasibility, etc.)
  - Assign importance weights (totaling 100%)
  - Score each option against criteria
  - Calculate weighted totals for ranking
  
  ## 8. IMPLEMENTATION ROADMAP
  
  **Phase 1 (Immediate):**
  - Top 3 highest priority items
  - Required resources and timeline
  - Success metrics
  
  **Phase 2 (Short-term):**
  - Next tier priorities
  - Dependencies and sequencing
  - Resource planning
  
  **Phase 3 (Medium-term):**
  - Strategic initiatives
  - Capacity planning
  - Review and adjustment points
slug: prioritization-frameworks-expert
tags:
- prioritization
- resource-management
- strategic-planning
- efficiency
- decision-making
tips:
- Involve stakeholders in framework selection and criteria weighting
- Review and adjust priorities regularly as context changes
- Use multiple frameworks to validate important decisions
- Document rationale for future reference
- Start with simple frameworks and add complexity as needed
title: Prioritization Frameworks Expert
version: 2.0.0
---