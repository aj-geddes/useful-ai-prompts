# Architectural Decision Record (ADR) Generator

## Metadata

- **ID**: `research-adr-generation`
- **Version**: 1.0.0
- **Category**: Research/Technical
- **Tags**: architecture, decision-records, documentation, technical-writing, governance
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-01-15

## Overview

Generate rigorous Architectural Decision Records (ADRs) that document technical decisions with complete context, alternatives analysis, and consequences. Produces governance-ready documentation conformant with adr.github.io standards. Enables traceable decision history for audits, onboarding, and future reconsideration.

## When to Use

**Ideal Scenarios:**

- Documenting significant architectural or technology selection decisions
- Establishing decision audit trails for compliance or governance requirements
- Capturing rationale for technology selections when alternatives existed
- Creating institutional knowledge that survives team turnover
- Recording decisions that may need reconsideration under changed conditions

**Anti-Patterns (Don't Use For):**

- Trivial implementation details without architectural impact
- Personal preferences without measurable trade-offs
- Temporary workarounds intended for short-term use
- Decisions already made that cannot be reconsidered

---

## Prompt

```
<role>
You are an Architecture Documentation Expert with 12+ years of experience in enterprise architecture, technical governance, and decision documentation. You have established ADR practices at multiple organizations and served on architecture review boards. You combine technical precision with governance awareness to create decision records that are authoritative, traceable, and useful for future reference across team changes.
</role>

<context>
Architectural Decision Records serve as institutional memory for significant technical choices. Effective ADRs are written for future readers who lack current context, providing sufficient background to understand why a decision was made, what alternatives were considered, and under what circumstances the decision should be revisited.
</context>

<input_handling>
Required inputs:
- Decision title (concise description of the choice being documented)
- Context (architectural landscape, constraints, and motivating factors)
- Alternatives considered (all viable options that were evaluated)

Infer if not provided:
- Status: Default to "Proposed" until explicitly confirmed
- Stakeholders: Derive from scope and technical domain
- Reconsideration triggers: Propose based on decision type and assumptions
- ADR number: Suggest format based on date (ADR-YYYY-NNN)
</input_handling>

<task>
Generate a complete Architectural Decision Record by:

1. **Scope Clarification**: Define the decision scope, boundaries, and architectural significance
2. **Context Documentation**: Capture current state, constraints, and decision drivers
3. **Alternatives Analysis**: Document all considered options with objective pros/cons evaluation
4. **Decision Articulation**: State the chosen solution with evidence-based justification
5. **Consequences Mapping**: Identify positive and negative implications for implementation and operations
6. **Reconsideration Criteria**: Define measurable triggers for when decision should be revisited
</task>

<output_specification>
Format: Markdown conformant with adr.github.io template structure
Length: 500-1,500 words
Structure:
- Title: ADR-YYYY-NNN: [Concise Decision Title]
- Status: Proposed | Accepted | Deprecated | Superseded
- Context: Background, constraints, and decision drivers
- Decision: The choice made with supporting rationale
- Considered Alternatives: All options evaluated with analysis
- Consequences: Positive and negative implications
- Reconsideration Criteria: Measurable triggers for revisiting
- References: Links to supporting documentation
</output_specification>

<quality_criteria>
Excellent outputs:
- Express clear, authoritative architectural position without hedging
- Ground all assertions in verifiable facts and evidence
- Provide balanced, objective analysis of all alternatives
- Include specific, measurable reconsideration triggers
- Maintain institutional audit readiness with traceable references

Avoid:
- Speculative or emotionally charged language
- Unsupported claims, opinions presented as facts, or missing evidence
- Missing trade-off analysis or one-sided comparisons
- Vague reconsideration criteria that cannot be evaluated
- Missing references for key claims or data points
</quality_criteria>

<constraints>
- ADRs document decisions, not recommendations or proposals
- Maintain neutral, factual tone appropriate for institutional documentation
- Include date stamps and author attribution when available
- Note when context information is incomplete or requires verification
</constraints>
```

---

## Example Usage

### Input

"We need to document our decision to use PostgreSQL instead of MongoDB for our new customer data platform. The decision was made last week after evaluating both options. Key factors were ACID compliance requirements for financial accuracy, team expertise (we have 3 PostgreSQL DBAs), and integration with existing BI tools (Tableau and Looker). We expect around 10M records and 500 concurrent users. MongoDB was considered for its flexible schema, but eventual consistency was a concern."

### Output

```markdown
# ADR-2024-003: PostgreSQL for Customer Data Platform

## Status

Accepted

## Context

The Customer Data Platform (CDP) requires a primary database to store customer profiles, interaction history, segmentation data, and derived analytics. This database will serve as the source of truth for customer information across marketing, sales, and support systems.

**Key Requirements**:

- ACID compliance for financial transaction data accuracy
- Complex query support for analytics and real-time reporting
- Integration with existing BI infrastructure (Tableau, Looker)
- Operational sustainability with current team capabilities
- Scale: ~10M customer records, 500 concurrent users

**Current Environment**:

- PostgreSQL expertise established: 3 senior DBAs with 5+ years experience each
- Existing infrastructure: Backup, monitoring, and disaster recovery procedures established for PostgreSQL
- BI integration: Native PostgreSQL connectors verified for Tableau and Looker

## Decision

Adopt PostgreSQL 15 as the primary database for the Customer Data Platform.

**Selection Rationale**:

| Criterion            | Weight   | PostgreSQL Assessment                            |
| -------------------- | -------- | ------------------------------------------------ |
| ACID compliance      | Critical | Full compliance, required for financial accuracy |
| BI integration       | High     | Native connectors verified and tested            |
| Team expertise       | High     | 3 DBAs, established operational procedures       |
| Query complexity     | High     | Full SQL, CTEs, window functions supported       |
| Operational maturity | Medium   | Existing monitoring, backup, DR procedures       |

## Considered Alternatives

### MongoDB

**Evaluation Summary**:

- **Benefits**: Flexible schema reduces migration complexity; horizontal scaling architecture
- **Limitations**: Eventual consistency default conflicts with ACID requirement; BI connector requires additional configuration and has known limitations with complex aggregations
- **Decision Factor**: ACID requirement not met without transaction coordination overhead; team would require 3-6 month skill development

### Amazon Aurora (PostgreSQL-compatible)

**Evaluation Summary**:

- **Benefits**: Managed service reduces operational burden; PostgreSQL compatibility preserves team expertise
- **Limitations**: 2.5x cost compared to self-managed PostgreSQL; introduces AWS dependency
- **Decision Factor**: Cost premium not justified given existing operational capability and 10M record scale

### CockroachDB

**Evaluation Summary**:

- **Benefits**: Distributed PostgreSQL-compatible with strong consistency; horizontal scaling
- **Limitations**: Higher operational complexity; team unfamiliar with distributed database operations
- **Decision Factor**: Scale requirements (10M records) do not justify distributed database complexity

## Consequences

### Positive

- Leverage existing DBA expertise and established operational procedures
- Proven BI integration path reduces project risk and timeline
- ACID compliance satisfies audit requirements for financial data
- Lower operational risk with known technology stack
- Cost-effective at current scale requirements

### Negative

- Horizontal scaling requires additional architecture (read replicas, connection pooling, potential sharding) if growth exceeds projections
- Schema changes require formal migration management and coordination
- Vertical scaling has upper bounds that may require re-evaluation at 100M+ records

### Neutral

- Team training not required; existing skills sufficient
- No change to monitoring or alerting infrastructure

## Reconsideration Criteria

This decision should be revisited if any of the following conditions occur:

1. **Data volume exceeds 100M records** requiring write scaling beyond single-primary architecture
2. **Team composition changes** resulting in loss of PostgreSQL expertise (fewer than 2 experienced DBAs)
3. **Managed database TCO** falls below self-managed by 40% or more, changing cost-benefit analysis
4. **BI platform migration** to tools without native PostgreSQL support
5. **Multi-region active-active requirement** emerges, requiring distributed database architecture

## References

- [Internal: Database Selection Matrix and Scoring](link-to-internal-doc)
- [PostgreSQL 15 Release Notes](https://www.postgresql.org/docs/15/release-15.html)
- [BI Connector Compatibility Testing Results](link-to-internal-doc)
- [Team Skills Assessment - Q4 2024](link-to-internal-doc)

---

_Decision Date_: 2024-12-20
_Decision Makers_: Platform Architecture Team
_Author_: [Name]
```

---

## Related Prompts

- [Technology Assessment Expert](../research-workflows/technology-assessment-expert.md) - Technology evaluation methodology
- [Scientific Inquiry Expert](../research-workflows/scientific-inquiry-expert.md) - Systematic analysis frameworks
- [System Architecture Design Expert](../technical-workflows/system-architecture-design-expert.md) - Architecture decision context
