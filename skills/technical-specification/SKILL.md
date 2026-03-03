---
name: technical-specification
description: >
  Create detailed technical specifications, requirements documents, design
  documents, and system architecture specs. Use when writing technical specs,
  requirements docs, or design documents.
---

# Technical Specification

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create comprehensive technical specifications that define system requirements, architecture, implementation details, and acceptance criteria for software projects.

## When to Use

- Feature specifications
- System design documents
- Requirements documentation (PRD)
- Architecture decision records (ADR)
- Technical proposals
- RFC (Request for Comments)
- API design specs
- Database schema designs

## Quick Start

Minimal working example:

```markdown
# Technical Specification: [Feature Name]

**Document Status:** Draft | Review | Approved | Implemented
**Version:** 1.0
**Author:** John Doe
**Date:** 2025-01-15
**Reviewers:** Jane Smith, Bob Johnson
**Last Updated:** 2025-01-15

## Executive Summary

Brief 2-3 sentence overview of what this spec covers and why it's being built.

**Problem:** What problem are we solving?
**Solution:** High-level description of the solution
**Impact:** Expected business/user impact

---

## 1. Background

### Context

Provide background on why this feature is needed:

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Functional Requirements](references/functional-requirements.md) | Functional Requirements |
| [Non-Functional Requirements](references/non-functional-requirements.md) | Non-Functional Requirements |
| [Database Schema](references/database-schema.md) | Database Schema |
| [API Data Models](references/api-data-models.md) | API Data Models |
| [Authentication Endpoints](references/authentication-endpoints.md) | Authentication Endpoints |
| [Rate Limiting](references/rate-limiting.md) | Rate Limiting |
| [Phase 1: Core Authentication](references/phase-1-core-authentication.md) | Phase 1: Core Authentication (Week 1-2), Phase 2: Email Verification (Week 3), Phase 3: Social Login (Week 4), Phase 4: Security Features (Week 5) (+1 more) |

## Best Practices

### ✅ DO

- Include acceptance criteria for each requirement
- Provide architecture diagrams
- Document API contracts
- Specify performance requirements
- List risks and mitigations
- Include implementation timeline
- Add success metrics
- Document security considerations
- Version your specs
- Get stakeholder review

### ❌ DON'T

- Be vague about requirements
- Skip non-functional requirements
- Forget about security
- Ignore alternatives
- Skip testing strategy
- Forget monitoring/observability
- Leave questions unanswered
