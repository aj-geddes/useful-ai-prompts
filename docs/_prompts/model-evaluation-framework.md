---
category: technical-workflows
compatible_models:
- GPT-4
- Claude 3
- Gemini Pro
- GPT-3.5
date: '2025-07-20'
description: This prompt helps you comprehensively evaluate machine learning models using appropriate metrics, validation strategies, and real-world performance considerations.
layout: prompt
prompt: 'I''ll help you evaluate your machine learning model thoroughly to ensure it meets your business needs. Let me understand your model and context:


  **About your model:**

  1. What type of problem? (classification, regression, clustering, etc.)

  2. What''s your model architecture? (random forest, neural network, etc.)

  3. What''s the business use case?

  4. What are the consequences of false positives vs false negatives?


  **Data context:**

  5. How much data do you have? (training/validation/test split)

  6. Is your data balanced? Any class imbalance issues?

  7. Any data quality concerns? (missing values, outliers, drift)

  8. Is this time series data or cross-sectional?


  **Current performance:**

  9. What metrics have you calculated so far?

  10. Do you have baseline model performance to compare against?

  11. Any specific performance thresholds required?

  12. Have you tested on production-like data?


  Based on your answers, I''ll provide:


  **EVALUATION STRATEGY** - Comprehensive testing approach

  **METRIC ANALYSIS** - Which metrics matter most and why

  **VALIDATION FRAMEWORK** - Proper validation techniques

  **PERFORMANCE INSIGHTS** - Deep dive into model behavior

  **PRODUCTION READINESS** - Deployment considerations


  Share your model details and let''s ensure it''s truly ready for deployment!'
related_prompts:
- ml-experimentation-expert
- feature-engineering-expert
- ml-deployment-expert
slug: model-evaluation-framework
tags:
- model evaluation
- machine learning
- performance metrics
- validation
- model selection
title: Model Evaluation Framework
use_cases:
- model comparison
- performance validation
- production readiness
- ML optimization
version: 2.0.0
---
