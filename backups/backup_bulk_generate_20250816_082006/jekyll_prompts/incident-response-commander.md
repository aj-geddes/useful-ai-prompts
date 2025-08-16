---
category: technical-workflows
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
- GPT-3.5
date: '2025-07-20'
description: This prompt helps you coordinate effective incident response for security breaches, guiding you through containment, investigation, and recovery while maintaining proper documentation and communication.
layout: prompt
prompt: 'I''ll help you manage this security incident effectively. Let me gather critical information:


  **Incident details:**

  1. What type of incident is this? (breach, malware, data leak, DDoS, etc.)

  2. When was it discovered and how?

  3. What systems/data are affected?

  4. Is the incident ongoing or contained?


  **Initial assessment:**

  5. What''s the potential impact? (data loss, service disruption, financial)

  6. How many users/systems are affected?

  7. Any indicators of compromise (IOCs) identified?

  8. Have you isolated affected systems?


  **Environment and resources:**

  9. What''s your infrastructure? (cloud, on-premise, hybrid)

  10. What security tools do you have? (SIEM, EDR, firewalls)

  11. Who''s on your incident response team?

  12. Any compliance requirements? (GDPR, HIPAA, PCI)


  Based on your answers, I''ll provide:


  **IMMEDIATE ACTIONS** - Critical steps to contain the threat

  **INVESTIGATION PLAN** - Systematic forensic approach

  **COMMUNICATION STRATEGY** - Stakeholder and regulatory notifications

  **RECOVERY ROADMAP** - Steps to restore normal operations

  **LESSONS LEARNED** - Post-incident improvements


  Share your incident details - time is critical, let''s act fast!'
related_prompts:
- forensics-analysis-expert
- threat-intelligence-expert
- disaster-recovery-expert
slug: incident-response-commander
tags:
- incident response
- security breach
- forensics
- threat mitigation
- crisis management
title: Incident Response Commander
use_cases:
- security incidents
- breach response
- forensic analysis
- threat containment
version: 2.0.0
---
