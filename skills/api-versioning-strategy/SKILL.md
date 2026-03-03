---
name: api-versioning-strategy
description: >
  Implement API versioning strategies including URL versioning, header
  versioning, backward compatibility, deprecation strategies, and migration
  guides. Use when dealing with API versions, deprecating endpoints, or managing
  breaking changes.
---

# API Versioning Strategy

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Comprehensive guide to API versioning approaches, deprecation strategies, backward compatibility techniques, and migration planning for REST APIs, GraphQL, and gRPC services.

## When to Use

- Designing new APIs with versioning from the start
- Adding breaking changes to existing APIs
- Deprecating old API versions
- Planning API migrations
- Ensuring backward compatibility
- Managing multiple API versions simultaneously
- Creating API documentation for different versions
- Implementing API version routing

## Quick Start

Minimal working example:

```typescript
// express-router.ts
import express from "express";

const app = express();

// Version 1
app.get("/api/v1/users", (req, res) => {
  res.json({
    users: [{ id: 1, name: "John Doe" }],
  });
});

// Version 2 - Added email field
app.get("/api/v2/users", (req, res) => {
  res.json({
    users: [{ id: 1, name: "John Doe", email: "john@example.com" }],
  });
});

// Shared logic with version-specific transformations
app.get("/api/:version/users/:id", async (req, res) => {
  const user = await userService.findById(req.params.id);

  if (req.params.version === "v1") {
    res.json({ id: user.id, name: user.name });
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Versioning Approaches](references/versioning-approaches.md) | Versioning Approaches |
| [Backward Compatibility Patterns](references/backward-compatibility-patterns.md) | Backward Compatibility Patterns |
| [Deprecation Strategy](references/deprecation-strategy.md) | Deprecation Strategy |
| [Migration Guide Example](references/migration-guide-example.md) | Migration Guide Example |
| [Response Structure](references/response-structure.md) | Response Structure |
| [Date Format](references/date-format.md) | Date Format, Error Format |
| [JavaScript/TypeScript](references/javascripttypescript.md) | JavaScript/TypeScript, Python |
| [GraphQL Versioning](references/graphql-versioning.md) | GraphQL Versioning |
| [gRPC Versioning](references/grpc-versioning.md) | gRPC Versioning |
| [Version Detection & Routing](references/version-detection-routing.md) | Version Detection & Routing |
| [Testing Multiple Versions](references/testing-multiple-versions.md) | Testing Multiple Versions |
| [Pattern 1: Version-Agnostic Core](references/pattern-1-version-agnostic-core.md) | Pattern 1: Version-Agnostic Core, Pattern 2: Feature Flags for Gradual Rollout, Pattern 3: API Version Metrics |

## Best Practices

### ✅ DO

- Version from day one (even if v1)
- Document breaking vs non-breaking changes
- Provide clear migration guides with code examples
- Use semantic versioning principles
- Give 6-12 months deprecation notice
- Monitor usage of deprecated APIs
- Send deprecation warnings to API consumers
- Support at least 2 versions simultaneously
- Use adapters/transformers for version logic
- Test all supported versions
- Log which API version is being used
- Provide migration tooling when possible
- Be consistent with versioning approach

### ❌ DON'T

- Change API behavior without versioning
- Remove versions without notice
- Support too many versions (>3)
- Use different versioning strategies in same API
- Break APIs without incrementing version
- Forget to update documentation
- Deprecate too quickly (<6 months)
- Ignore feedback from API consumers
- Make every change a new version
- Use version numbers inconsistently
