# Architectural Decision Record (ADR) Generation Prompt

## Solicit User Input for Architectural Decision Parameters

To facilitate the generation of a rigorously composed, Temperature 0 Architectural Decision Record (ADR), please provide detailed and structured responses to the following:

- **Decision Title**: A concise, unambiguous description of the architectural choice under consideration.
- **Contextual Justification**: A thorough exposition of the architectural landscape, including motivating factors such as performance, regulatory compliance, maintainability, interoperability, scalability constraints, and team dynamics.
- **Evaluated Alternatives**: A complete enumeration of all viable technologies, frameworks, or design strategies considered, including incumbent or legacy solutions.
- **Chosen Solution**: Identification of the selected approach with a formal articulation of the selection criteria, supported by empirical or analytical justification.
- **Stakeholder Considerations**: Identification of all involved stakeholders—domain owners, platform teams, governance boards—and the scope of their influence on the decision.
- **Scope of Impact**: A clearly defined boundary of the architectural decision, whether limited to a module, a platform segment, or the system as a whole.
- **Reevaluation Triggers**: Objective metrics or contextual thresholds that would prompt a re-examination of the decision, such as performance degradation, ecosystem shifts, or external policy changes.
- **Supporting Artifacts**: Hyperlinked references to RFCs, benchmarking outputs, comparative analyses, stakeholder discussions, or prior ADRs.

This structured input enables the automatic generation of an ADR conformant with [https://adr.github.io](https://adr.github.io) standards and enterprise architecture governance frameworks.

---

## Structural and Methodological Requirements

- **Definitive Assertion**: Each ADR must express a clear and authoritative architectural position.
- **Temperature 0 Standard**: All prose must be grounded in verifiable facts, avoiding speculative, emotional, or future-contingent language.
- **Comparative Analysis**: All considered alternatives must be evaluated in terms of benefits, tradeoffs, constraints, and alignment with non-functional requirements.
- **Traceability**: Every rationale must reference primary sources such as internal documentation, empirical findings, or authoritative standards.
- **Lifecycle Awareness**: Each decision must delineate its active scope, sunset criteria, and conditions for revision or supersession.

---

## ADR Template for Structured Generation

```md
# [DECISION TITLE]

## Status

Accepted

## Context

[Describe the architectural environment, including motivating constraints, performance drivers, integration dependencies, or compliance considerations.]

## Decision

[State the adopted solution. Provide a factual and context-sensitive justification based on evaluation criteria.]

## Considered Alternatives

- [Option A]: [Concise technical summary of benefits and limitations.]
- [Option B]: [Concise technical summary of benefits and limitations.]
- [Option C]: [Concise technical summary of benefits and limitations.]

## Consequences

[Summarize the architectural, operational, and organizational implications. Include implementation overhead, maintenance burden, or alignment with long-term strategy.]

## Reconsideration Criteria

[Specify measurable indicators or scenarios that would trigger reconsideration of this decision.]

## Supporting References

- [Link to internal documentation, experimental benchmarks, cost models, or external standards.]
```

---

## Validation Benchmarks

- ✅ The decision title is precise and context-specific
- ✅ The context section clearly articulates environmental constraints
- ✅ Alternatives are systematically compared
- ✅ Consequences address both immediate and long-term effects
- ✅ Reconsideration criteria are quantifiable
- ✅ All claims are supported by verifiable references

---

## Quality Assurance Principles

- **Epistemic Rigor**: All assertions must be traceable to measurable outcomes, empirical evaluations, or first-principles reasoning.
- **Linguistic Precision**: Avoid anecdotal or emotionally charged language. Focus exclusively on verifiable factors.
- **Template Consistency**: All ADRs must conform to the standardized format and section ordering.
- **Immutable Versioning**: Include identifiers, timestamps, and relationship markers to prior ADRs.
- **Institutional Auditability**: ADRs must remain reviewable and authoritative within all governance and decision-making forums.
