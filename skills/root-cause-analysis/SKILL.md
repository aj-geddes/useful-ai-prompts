---
name: root-cause-analysis
description: >
  Conduct systematic root cause analysis to identify underlying problems. Use.
  Use when production incidents, customer-impacting issues, repeated problems, or unexpected failures.
  structured methodologies to prevent recurring issues and drive improvements.
---

# Root Cause Analysis

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Root cause analysis (RCA) identifies underlying reasons for failures, enabling permanent solutions rather than temporary fixes.

## When to Use

- Production incidents
- Customer-impacting issues
- Repeated problems
- Unexpected failures
- Performance degradation

## Quick Start

Minimal working example:

```yaml
Example: Website Down

Symptom: Website returned 503 Service Unavailable

Why 1: Why was website down?
  Answer: Database connection pool exhausted

Why 2: Why was connection pool exhausted?
  Answer: Queries taking too long, connections not released

Why 3: Why were queries slow?
  Answer: Missing index on frequently queried column

Why 4: Why was index missing?
  Answer: Performance testing didn't use production-like data volume

Why 5: Why wasn't production-like data used?
  Answer: Load testing environment doesn't mirror production

Root Cause: Load testing environment under-provisioned

Solution: Update load testing environment with production-like data

Prevention: Establish environment parity requirements
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [The 5 Whys Technique](references/the-5-whys-technique.md) | The 5 Whys Technique |
| [Systematic RCA Process](references/systematic-rca-process.md) | Systematic RCA Process |
| [RCA Report Template](references/rca-report-template.md) | RCA Report Template |
| [Root Cause Analysis Techniques](references/root-cause-analysis-techniques.md) | Root Cause Analysis Techniques |
| [Follow-Up & Prevention](references/follow-up-prevention.md) | Follow-Up & Prevention |

## Best Practices

### ✅ DO

- Ask "why" at least five times before settling on a root cause — stop only when you reach a systemic factor
- Gather timeline data, logs, and metrics before forming hypotheses to avoid confirmation bias
- Distinguish between contributing factors and the actual root cause in your final report
- Assign concrete, measurable corrective actions with owners and deadlines
- Conduct the analysis blameless — focus on process and system failures, not individuals
- Validate the proposed root cause by confirming it explains all observed symptoms

### ❌ DON'T

- Stop at the first plausible explanation without verifying it against all evidence
- Conflate symptoms (e.g., "server crashed") with root causes (e.g., "no memory limits configured")
- Skip documenting the RCA — undocumented findings get lost and the same issue recurs
- Propose only detective controls; always include at least one preventive action
