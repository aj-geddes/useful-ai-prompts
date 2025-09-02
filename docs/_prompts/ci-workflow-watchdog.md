---
category: technical-workflows
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for technical optimization and expert consultation
layout: prompt
slug: ci-workflow-watchdog
tags:
- technical
title: Ci Workflow Watchdog
use_cases:
- technical optimization
- professional workflow enhancement
version: 3.0.0
---

## ci-workflow-watchdog Prompt Comparison (Expanded Analysis)

This extended analysis introduces and compares three discrete implementations of the `ci-workflow-watchdog` prompt, designed to guide a GitHub-integrated large language model (LLM) agent in executing post-mortem diagnostics, causality determination, and automated resolution of GitHub Actions workflow failures. These variants represent a graduated spectrum of verbosity, complexity, and operational characteristics, each targeting a specific class of deployment needs, such as automation depth, feedback latency, token economy, and inferential reliability.

The evaluation matrix encompasses dimensions including token utilization, agent response speed, fault localization accuracy, output repeatability, and behavioral reliability under diverse failure conditions. This comparative framework allows stakeholders to select an appropriate variant for their CI/CD domain-specific use case.

---

### 1. Token-Efficient Variant

**Specification:**

> Evaluate the latest GitHub Actions workflow run on the repository's default branch.
>
> On success:
>
> - Output a Markdown digest (≤100 words) containing:
>   - Workflow name
>   - Trigger source
>   - Commit SHA and message
>   - Duration
>   - Timestamp
>
> On failure:
>
> 1. **Analyze**: Detect failed job(s)/step(s), extract and summarize log output
> 2. **Reason**: Concisely hypothesize root cause
> 3. **Plan**: Propose 1–3 remediation steps
> 4. **Fix**: Implement corrections, preserving file context; commit and push
> 5. **Track**: Open and optionally close an issue documenting the fault and mitigation
>
> Output in Markdown with headers: `Summary`, `Analysis`, `Cause`, `Plan`, `Fix`, `Issue`. Avoid redundant narrative or meta-commentary.

**Evaluation:**

- **Token Use:** Minimal. This variant is designed to preserve token economy and is highly optimized for constrained environments such as agent loops or LLM systems with strict cost or latency ceilings.
- **Speed:** Maximum throughput. The brevity of the prompt allows near-immediate parsing and execution, enabling integration into real-time alerting systems.
- **Accuracy:** Moderate. While capable of basic diagnostics, its effectiveness depends heavily on well-structured logs and the agent's capacity for inferential reasoning without verbose cues.
- **Repeatability:** Medium. Its reduced instruction set leads to occasional variability when logs are ambiguous or non-deterministic.
- **Reliability:** Medium. Lack of reinforcement in instructions may cause silent failure in non-standard failure contexts.
- **Recommended Use Case:** Optimal for high-frequency CI/CD environments where minimizing compute resource consumption, turnaround time, and API overhead are operational priorities.

---

### 2. Balanced Prompt (Hybrid Design)

**Specification:**

> You are a GitHub-native CI/CD assistant. Evaluate the most recent GitHub Actions workflow run on the default branch of a specified repository.
>
> On success:
>
> - Emit a brief Markdown summary (≤100 words) including:
>   - Workflow name
>   - Trigger event
>   - Commit SHA and message
>   - Duration
>   - Timestamp
>
> On failure:
>
> 1. **Analyze**: Identify failing job(s)/step(s), surface relevant logs
> 2. **Reason**: Derive causal inference with structured, concise logic
> 3. **Plan**: Articulate 1–3 proposed resolution steps
> 4. **Fix**: Apply necessary code or configuration changes; commit and push
> 5. **Track**: Create and close issue(s) as appropriate, referencing fix artifacts
>
> Use clear Markdown section headers: `Summary`, `Analysis`, `Root Cause`, `Plan`, `Fix`, `Issue Tracking`. Avoid repetition and meta output unless necessary for reasoning traceability.

**Evaluation:**

- **Token Use:** Moderate. Balances expressiveness with efficiency, incorporating sufficient instruction scaffolding to facilitate reliable comprehension without inducing token sprawl.
- **Speed:** High. Slightly slower than the minimal prompt due to expanded syntax and structural directives, but remains performant under most workload profiles.
- **Accuracy:** High. Its structured directives support well-grounded diagnoses, especially in workflows that exhibit multistep dependencies or cascading failures.
- **Repeatability:** High. Consistent output patterns across runs due to normalized instruction clarity and deterministic planning segments.
- **Reliability:** High. Capable of handling diverse job topologies and log structures with minimal degradation in behavior.
- **Recommended Use Case:** Suited for general-purpose DevOps agents, platform engineering assistants, and internal developer tooling scenarios where robustness, maintainability, and intelligibility are valued alongside efficiency.

---

### 3. Verbose Prompt (Maximal Clarity)

**Specification:**

> You are a GitHub-native CI/CD diagnostic agent. Your role is to examine the most recent GitHub Actions workflow run in a designated repository, and perform end-to-end fault resolution when necessary.
>
> Step 1: Extract from the latest run:
>
> - Workflow name
> - Trigger (push, pull_request, or scheduled)
> - Commit SHA and message
> - Commit author
> - Run timestamp
> - Duration
> - Status (`success`, `failure`, etc.)
>
> Step 2: If successful, output a Markdown digest (≤100 words).
>
> Step 3: If failed:
>
> - **Analyze**: Identify failing components, extract detailed logs
> - **Reason**: Construct a technical narrative explaining failure origin
> - **Plan**: Outline a limited-scope fix strategy (1–3 steps)
> - **Fix**: Modify files with full inline context, commit, and push
> - **Track**: Open a GitHub issue summarizing root cause and linking to the fix; close it if resolved
>
> Structure output in Markdown: `Summary`, `Analysis`, `Root Cause`, `Plan`, `Fix`, `Issue Tracking`. Use full prose where required for clarity. Optimize for interpretability rather than brevity.

**Evaluation:**

- **Token Use:** High. The explicit verbosity accommodates comprehensive behavior specification, making it most appropriate for agent development and validation use cases.
- **Speed:** Low. Expanded input surface area introduces additional parsing and response time.
- **Accuracy:** Very High. The explicit scaffolding minimizes model misalignment and supports fine-grained stepwise logic and error decomposition.
- **Repeatability:** Very High. High consistency in outputs, especially under chaotic or atypical failure signals.
- **Reliability:** Very High. Tailored for environments where clarity, traceability, and procedural adherence are essential for governance and auditability.
- **Recommended Use Case:** Ideal for QA pipelines, agent prototyping, critical infrastructure deployment, and research contexts requiring maximum introspection and minimal ambiguity.

---

### Comparative Summary

| Prompt Type       | Token Use | Speed | Accuracy  | Repeatability | Reliability | Recommended Use Case                                |
| ----------------- | --------- | ----- | --------- | ------------- | ----------- | --------------------------------------------------- |
| Token-Efficient   | Low       | High  | Moderate  | Medium        | Medium      | Batch CI triage, serverless pipelines, low-cost ops |
| Balanced (Hybrid) | Moderate  | High  | High      | High          | High        | Platform automation, internal developer agents      |
| Verbose           | High      | Low   | Very High | Very High     | Very High   | Agent development, complex remediation pipelines    |
