---
category: customer-focused
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
- GPT-3.5
date: '2025-07-21'
description: Design efficient escalation processes that ensure critical customer issues are resolved quickly by the right experts. This prompt helps create clear escalation paths, criteria, and communication protocols.
layout: prompt
prompt: |
  I'll help you design an efficient support escalation process. Let's understand your current setup:
  
  SUPPORT STRUCTURE:
  - How many support tiers do you have currently?
  - What types of issues does each tier handle?
  - What's your current escalation volume and patterns?
  
  ESCALATION CHALLENGES:
  - What triggers most escalations today?
  - Where do escalations get stuck or delayed?
  - Any customer complaints about escalation experience?
  
  BUSINESS CONTEXT:
  - SLA commitments for different issue types?
  - Peak volume times and resource constraints?
  - Key stakeholders involved in escalations?
  
  Here's your comprehensive escalation framework:
  
  ## 1. TIERED ESCALATION MODEL
  
  **Escalation Path**:
  - **Tier 1** → **Tier 2**: Technical complexity or time limit reached
  - **Tier 2** → **Tier 3**: Specialized expertise or development needed
  - **Any Tier** → **Management**: Customer relationship or business risk
  
  **Escalation Criteria**:
  | Trigger | Tier 1 → 2 | Tier 2 → 3 | Any → Management |
  |---------|------------|------------|------------------|
  | Time Limit | 4 hours | 8 hours | VIP customer |
  | Complexity | Can't diagnose | Needs development | Revenue at risk |
  | Customer Request | Asks for manager | Escalates again | Executive contact |
  | Impact Level | Multiple users | System-wide | Brand reputation |
  
  ## 2. ESCALATION DECISION MATRIX
  
  **Automatic Escalation Guidelines**:
  - Customer impact assessment
  - Technical complexity evaluation
  - Business risk factors
  - Time sensitivity analysis
  
  **Manual Escalation Guidelines**:
  - Agent discretion factors
  - Customer relationship status
  - Issue novelty or uniqueness
  - Resource availability
  
  ## 3. COMMUNICATION PROTOCOLS
  
  **Internal Handoff Process**:
  | Step | Action | Information Required | Tool/Template |
  |------|--------|---------------------|---------------|
  | 1 | Document | Issue summary, steps taken | Escalation template |
  | 2 | Assess | Priority, complexity, customer | Triage checklist |
  | 3 | Route | Assign to appropriate specialist | Routing rules |
  | 4 | Brief | Verbal/chat handoff if urgent | Handoff protocol |
  | 5 | Update | Customer notification | Communication template |
  
  **Customer Communication**:
  - Escalation acknowledgment template
  - Expected timeline setting
  - Progress update schedule
  - Resolution confirmation
  
  ## 4. PRIORITY MANAGEMENT
  
  **Severity Levels**:
  | Level | Description | Response Time | Escalation Path |
  |-------|-------------|---------------|----------------|
  | P1 | System down, revenue impact | 1 hour | Direct to Tier 3 |
  | P2 | Major functionality broken | 4 hours | Tier 1 → Tier 2 |
  | P3 | Minor issues, workarounds exist | 8 hours | Standard path |
  | P4 | Enhancement requests | 24 hours | Planning queue |
  
  **Queue Management**:
  - Priority weighting algorithm
  - Resource allocation rules
  - Overflow procedures
  - Weekend/holiday coverage
  
  ## 5. QUALITY & IMPROVEMENT
  
  **Escalation Metrics**:
  - Volume by type and tier
  - Resolution time by level
  - Customer satisfaction post-escalation
  - First-contact resolution impact
  
  **Prevention Analysis**:
  - Root cause tracking
  - Knowledge base gaps
  - Training needs identification
  - Product improvement inputs
  
  **Process Optimization**:
  - Monthly escalation reviews
  - Tier skill gap analysis
  - Automation opportunities
  - Feedback implementation
slug: support-escalation-process-expert
tags:
- escalation-management
- support-tiers
- issue-resolution
- incident-response
tips:
- Map current escalation patterns before redesigning
- Define clear criteria that agents can easily follow
- Build in automatic de-escalation when appropriate
- Train all tiers on the complete process
- Monitor and adjust thresholds based on data
title: Support Escalation Process Expert
version: 1.0.0
---