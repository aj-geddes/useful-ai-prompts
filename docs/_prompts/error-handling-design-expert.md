---
category: problem-solving
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
- GPT-3.5
date: '2025-07-20'
description: A comprehensive error handling design assistant that helps you build resilient systems. Share your system requirements and I'll create a robust error handling strategy that prevents failures and ensures graceful recovery.
layout: prompt
prompt: 'I''ll help you design robust error handling for your system. Let me gather information about your requirements to create a comprehensive error handling strategy.


  About your system:

  1. What type of system are you building? (web app, API, microservice, etc.)

  2. What programming language/framework are you using?

  3. What are the critical operations that must not fail?

  4. What are the main external dependencies? (databases, APIs, services)


  Error scenarios:

  5. What types of errors do you expect? (network, validation, auth, etc.)

  6. What is the impact of different failure types?

  7. Are there any compliance or audit requirements?

  8. What is your uptime/reliability target?


  Current approach:

  9. How are errors currently handled (if applicable)?

  10. What pain points have you experienced?

  11. What recovery mechanisms exist?

  12. How are errors logged and monitored?


  Based on your answers, I''ll provide:


  **1. ERROR TAXONOMY** - Classification of error types and severity levels

  **2. HANDLING STRATEGY** - Comprehensive approach for each error category

  **3. RECOVERY PATTERNS** - Retry logic, circuit breakers, fallbacks

  **4. USER EXPERIENCE** - Error messages and graceful degradation

  **5. MONITORING SETUP** - Logging, alerting, and observability

  **6. IMPLEMENTATION GUIDE** - Code patterns and best practices


  Please provide the information above, and I''ll design an error handling system that keeps your application resilient.'
related_prompts:
- system-design-expert
slug: error-handling-design-expert
tags:
- error handling
- resilience
- fault tolerance
- system design
- exception handling
tips:
- '**Identify Critical Paths**: Focus on operations that affect users most'
- '**Consider All Layers**: Think about errors at every system level'
- '**Plan for Recovery**: Don''t just catch errors, plan how to recover'
- '**Think About Users**: Consider how errors affect user experience'
- '**Include Monitoring**: Error handling without observability is incomplete'
title: Error Handling Design Expert
use_cases:
- error strategy design
- exception handling
- fault tolerance
- recovery mechanisms
- resilient systems
version: 2.0.0
---
