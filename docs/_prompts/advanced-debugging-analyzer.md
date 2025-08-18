---
category: technical-workflows
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
- GPT-3.5
date: '2025-07-20'
description: This prompt helps you systematically debug complex software issues through structured analysis, hypothesis testing, and root cause identification.
layout: prompt
prompt: 'I''ll help you debug this issue systematically. Let me gather information to understand the problem:


  **About the issue:**

  1. What''s the specific problem or error you''re experiencing?

  2. When did it start happening? (after a deployment, randomly, specific time)

  3. How frequently does it occur? (always, intermittently, under load)

  4. What''s the impact? (crashes, wrong output, performance degradation)


  **Environment details:**

  5. What''s your tech stack? (languages, frameworks, databases)

  6. What environment? (production, staging, local)

  7. Has anything changed recently? (code, config, infrastructure)

  8. Can you reproduce it consistently?


  **Diagnostic data:**

  9. What error messages or logs do you have?

  10. Any metrics or monitoring data available?

  11. What have you already tried?

  12. Any patterns you''ve noticed?


  Based on your answers, I''ll provide:


  **ROOT CAUSE ANALYSIS** - Systematic investigation approach

  **DEBUGGING STRATEGY** - Step-by-step troubleshooting plan

  **DIAGNOSTIC TOOLS** - Specific tools and commands to use

  **SOLUTION OPTIONS** - Potential fixes with trade-offs

  **PREVENTION PLAN** - How to avoid similar issues


  Share your debugging challenge and let''s solve it together!'
related_prompts:
- performance-optimization-expert
- database-optimization-expert
- architecture-review-expert
slug: advanced-debugging-analyzer
tags:
- debugging
- troubleshooting
- root cause analysis
- performance debugging
- diagnostics
title: Advanced Debugging Analyzer
use_cases:
- bug diagnosis
- performance issues
- memory leaks
- system debugging
version: 2.0.0
---
