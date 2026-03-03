---
name: code-review-analysis
description: >
  Perform comprehensive code reviews with best practices, security checks, and
  constructive feedback. Use when reviewing pull requests, analyzing code
  quality, checking for security vulnerabilities, or providing code improvement
  suggestions.
---

# Code Review Analysis

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Systematic code review process covering code quality, security, performance, maintainability, and best practices following industry standards.

## When to Use

- Reviewing pull requests and merge requests
- Analyzing code quality before merging
- Identifying security vulnerabilities
- Providing constructive feedback to developers
- Ensuring coding standards compliance
- Mentoring through code review

## Quick Start

Minimal working example:

```bash
# Check the changes
git diff main...feature-branch

# Review file changes
git diff --stat main...feature-branch

# Check commit history
git log main...feature-branch --oneline
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Initial Assessment](references/initial-assessment.md) | Initial Assessment |
| [Code Quality Analysis](references/code-quality-analysis.md) | Code Quality Analysis |
| [Security Review](references/security-review.md) | Security Review |
| [Performance Review](references/performance-review.md) | Performance Review |
| [Testing Review](references/testing-review.md) | Testing Review |
| [Best Practices](references/best-practices.md) | Best Practices |

## Best Practices

### ✅ DO

- Be constructive and respectful
- Explain the "why" behind suggestions
- Provide code examples
- Ask questions if unclear
- Acknowledge good practices
- Focus on important issues
- Consider the context
- Offer to pair program on complex issues

### ❌ DON'T

- Be overly critical or personal
- Nitpick minor style issues (use automated tools)
- Block on subjective preferences
- Review too many changes at once (>400 lines)
- Forget to check tests
- Ignore security implications
- Rush the review
