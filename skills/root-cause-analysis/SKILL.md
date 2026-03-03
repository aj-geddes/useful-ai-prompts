---
name: root-cause-analysis
description: >
  Conduct systematic root cause analysis to identify underlying problems. Use
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

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
