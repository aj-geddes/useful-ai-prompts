---
category: research
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for research optimization and expert consultation
slug: temperature-0-research-framework-for-architectural-decision-records
tags:
- research
title: Temperature 0 Research Framework for Architectural Decision Records
use_cases:
- research optimization
- professional workflow enhancement
version: 3.0.0
---

# Temperature 0 Research Framework for Architectural Decision Records

## Purpose

This framework defines a structured, evidence-oriented methodology for conducting technical due diligence in preparation for drafting an Architectural Decision Record (ADR) at Temperature 0. It enables comprehensive evaluation of technology choices, risk postures, and strategic fit within a target architectural domain.

---

## Solicit User Input: Research Initialization Parameters

To begin a rigorous research process, provide complete and unambiguous input for the following fields:

- **Architectural Decision Topic**: Clearly define the decision or tradeoff being evaluated.
- **Target Domain and Scope**: Specify the domain in which the decision applies (e.g., identity federation, service mesh routing, observability pipeline).
- **Evaluation Criteria**: Enumerate the dimensions on which alternatives will be assessed (e.g., operational cost, latency guarantees, security controls, extensibility).
- **Candidate Technologies**: Provide a comprehensive list of tools, frameworks, protocols, or platforms under consideration.
- **Governance Requirements**: Include regulatory, policy, or internal compliance mandates relevant to the decision (e.g., FedRAMP, SOC 2, internal architecture council standards).
- **Lifecycle Expectation**: Define the expected duration of the decision's validity and its operational horizon (e.g., stopgap vs. strategic platform commitment).

---

## Research Execution Principles

- **Technology Landscape Survey**: Identify all viable solutions in the problem space, including those emerging, mature, or nearing deprecation.
- **Multi-Dimensional Tradeoff Analysis**: Evaluate each candidate against the user-defined criteria using a normalized comparison matrix.
- **Ecosystem and Standards Maturity**: Examine each option’s alignment with open standards, interoperability guarantees, and community activity.
- **Precedent and Institutional History**: Reference internal ADRs, industry case studies, and relevant RFCs where applicable.
- **Reversibility and Risk Posture**: Explicitly document the lock-in risk, escape strategies, and resiliency considerations of each option.

---

## Temperature 0 LLM-Compatible Research Prompt

```text
Conduct a formal architectural decision analysis using the following parameters:

- Topic: [INSERT DECISION TOPIC]
- Domain: [INSERT DOMAIN CONTEXT]
- Evaluation Criteria: [E.G., COST, LATENCY, SECURITY, MAINTAINABILITY]
- Candidate Technologies: [LIST ALL OPTIONS]
- Governance Requirements: [LIST RELEVANT POLICIES OR STANDARDS]
- Timeline Expectation: [SHORT-TERM, MULTI-YEAR, ETC.]

Instructions:
1. Identify and describe all relevant technologies or architecture patterns.
2. For each candidate, provide:
   - Core capabilities and known constraints
   - Adoption profile and support ecosystem
   - Release cadence and maintenance health
   - Integration complexity and interoperability barriers
   - Security architecture and compliance posture
3. Build a structured comparison matrix against the defined criteria.
4. Reference any similar ADRs, RFCs, or vendor-neutral benchmarks.
5. Summarize with neutral, fact-based observations suitable for direct use in a Temperature 0 ADR.

Response Format Requirements:
- Maintain strict objectivity with no speculative or subjective statements
- Ground all conclusions in standards-compliant references or benchmark data
- Use declarative language aligned with ADR conventions
- Ensure output is immediately reusable in an enterprise ADR record
```

---

## Deliverables

- `research-summary.md`: Consolidated analysis of all candidate technologies with tradeoff matrix
- `rationale-notes.md`: Structured justifications and constraints for the decision, with source-backed commentary
- `references.md`: Annotated citations of all supporting material, including access metadata and versioning

---

## Success Criteria

- ✅ All alternatives are analyzed with equivalent rigor
- ✅ Comparison matrix transparently reflects user-defined evaluation criteria
- ✅ Risks, constraints, and reversibility are articulated
- ✅ All findings are verifiable and free from editorial bias
- ✅ Final content is ADR-ready without additional formatting or interpretation

---

## Quality Assurance Standards

- **Objectivity**: No subjective language or implicit recommendations without supporting evidence
- **Completeness**: Each dimension of evaluation must be addressed for all candidates
- **Verifiability**: Every assertion must be backed by documentation, empirical data, or primary-source references
- **ADR Alignment**: Structure and language must conform to Temperature 0 ADR expectations
- **Metadata Discipline**: All cited materials must include access method, date retrieved, and version or commit hash where relevant
