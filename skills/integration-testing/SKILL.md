---
name: integration-testing
description: >
  Design and implement integration tests that verify component interactions, API
  endpoints, database operations, and external service communication. Use for
  integration test, API test, end-to-end component testing, and service layer
  validation.
---

# Integration Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Integration testing validates that different components, modules, or services work correctly together. Unlike unit tests that isolate single functions, integration tests verify the interactions between multiple parts of your system including databases, APIs, external services, and infrastructure.

## When to Use

- Testing API endpoints with real database connections
- Verifying service-to-service communication
- Validating data flow across multiple layers
- Testing repository/DAO layer with actual databases
- Checking authentication and authorization flows
- Verifying message queue consumers and producers
- Testing third-party service integrations

## Quick Start

Minimal working example:

```javascript
// test/api/users.integration.test.js
const request = require("supertest");
const app = require("../../src/app");
const { setupTestDB, teardownTestDB } = require("../helpers/db");

describe("User API Integration Tests", () => {
  beforeAll(async () => {
    await setupTestDB();
  });

  afterAll(async () => {
    await teardownTestDB();
  });

  beforeEach(async () => {
    await clearUsers();
  });

  describe("POST /api/users", () => {
    it("should create a new user with valid data", async () => {
      const userData = {
        email: "test@example.com",
        name: "Test User",
        password: "SecurePass123!",
      };
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [API Integration Testing](references/api-integration-testing.md) | API Integration Testing |
| [Database Integration Testing](references/database-integration-testing.md) | Database Integration Testing |
| [External Service Integration](references/external-service-integration.md) | External Service Integration |
| [Message Queue Integration](references/message-queue-integration.md) | Message Queue Integration |

## Best Practices

### ✅ DO

- Use real databases in integration tests (in-memory or containers)
- Test actual HTTP requests, not mocked responses
- Verify database state after operations
- Test transaction boundaries and rollbacks
- Include authentication/authorization in tests
- Test error scenarios and edge cases
- Use test containers for isolated environments
- Clean up data between tests

### ❌ DON'T

- Mock database connections in integration tests
- Skip testing error paths
- Leave test data in databases
- Use production databases for testing
- Ignore transaction management
- Test only happy paths
- Share state between tests
- Hardcode URLs or credentials
