---
name: api-contract-testing
description: >
  Verify API contracts between services to ensure compatibility and prevent
  breaking changes. Use for contract testing, Pact, API contract validation,
  schema validation, and consumer-driven contracts.
---

# API Contract Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Contract testing verifies that APIs honor their contracts between consumers and providers. It ensures that service changes don't break dependent consumers without requiring full integration tests. Contract tests validate request/response formats, data types, and API behavior independently.

## When to Use

- Testing microservices communication
- Preventing breaking API changes
- Validating API versioning
- Testing consumer-provider contracts
- Ensuring backward compatibility
- Validating OpenAPI/Swagger specifications
- Testing third-party API integrations
- Catching contract violations in CI

## Quick Start

Minimal working example:

```typescript
// tests/pact/user-service.pact.test.ts
import { PactV3, MatchersV3 } from "@pact-foundation/pact";
import { UserService } from "../../src/services/UserService";

const { like, eachLike, iso8601DateTimeWithMillis } = MatchersV3;

const provider = new PactV3({
  consumer: "OrderService",
  provider: "UserService",
  port: 1234,
  dir: "./pacts",
});

describe("User Service Contract", () => {
  const userService = new UserService("http://localhost:1234");

  describe("GET /users/:id", () => {
    test("returns user when found", async () => {
      await provider
        .given("user with ID 123 exists")
        .uponReceiving("a request for user 123")
        .withRequest({
          method: "GET",
          path: "/users/123",
          headers: {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Pact for Consumer-Driven Contracts](references/pact-for-consumer-driven-contracts.md) | Pact for Consumer-Driven Contracts |
| [OpenAPI Schema Validation](references/openapi-schema-validation.md) | OpenAPI Schema Validation |
| [JSON Schema Validation](references/json-schema-validation.md) | JSON Schema Validation |
| [REST Assured for Java](references/rest-assured-for-java.md) | REST Assured for Java |
| [Contract Testing with Postman](references/contract-testing-with-postman.md) | Contract Testing with Postman |
| [Pact Broker Integration](references/pact-broker-integration.md) | Pact Broker Integration |

## Best Practices

### ✅ DO

- Test contracts from consumer perspective
- Use matchers for flexible matching
- Validate schema structure, not specific values
- Version your contracts
- Test error responses
- Use Pact broker for contract sharing
- Run contract tests in CI
- Test backward compatibility

### ❌ DON'T

- Test business logic in contract tests
- Hard-code specific values in contracts
- Skip error scenarios
- Test UI in contract tests
- Ignore contract versioning
- Deploy without contract verification
- Test implementation details
- Mock contract tests
