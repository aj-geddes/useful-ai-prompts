---
name: api-changelog-versioning
description: >
  Document API changes, breaking changes, migration guides, and version history
  for APIs. Use when documenting API versioning, breaking changes, or creating
  API migration guides.
---

# API Changelog & Versioning

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create comprehensive API changelogs that document changes, deprecations, breaking changes, and provide migration guides for API consumers.

## When to Use

- API version changelogs
- Breaking changes documentation
- Migration guides between versions
- Deprecation notices
- API upgrade guides
- Backward compatibility notes
- Version comparison

## Quick Start

- Version comparison

````markdown
# API Changelog

## Version 3.0.0 - 2025-01-15

### 🚨 Breaking Changes

#### Authentication Method Changed

**Previous (v2):**

```http
GET /api/users
Authorization: Token abc123
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [🚨 Breaking Changes](references/breaking-changes.md) | 🚨 Breaking Changes |
| [✨ New Features](references/new-features.md) | ✨ New Features |
| [🔧 Improvements](references/improvements.md) | 🔧 Improvements |
| [🔒 Security](references/security.md) | 🔒 Security, 🗑️ Deprecated, 📊 Version Support Policy |
| [Step 1: Update Base URL](references/step-1-update-base-url.md) | Step 1: Update Base URL, Step 2: Migrate Authentication, Step 3: Update Response Parsing, Step 4: Update Error Handling (+2 more) |

## Best Practices

### ✅ DO

- Clearly mark breaking changes
- Provide migration guides with code examples
- Include before/after comparisons
- Document deprecation timelines
- Show impact on existing implementations
- Provide SDKs for major versions
- Use semantic versioning
- Give advance notice (3-6 months)
- Maintain backward compatibility when possible
- Document version support policy

### ❌ DON'T

- Make breaking changes without notice
- Remove endpoints without deprecation period
- Skip migration examples
- Forget to version your API
- Change behavior without documentation
- Rush deprecations
