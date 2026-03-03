---
name: mocking-stubbing
description: >
  Create and manage mocks, stubs, spies, and test doubles for isolating unit
  tests from external dependencies. Use for mock, stub, spy, test double,
  Mockito, Jest mocks, and dependency isolation.
---

# Mocking and Stubbing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Mocking and stubbing are essential techniques for isolating units of code during testing by replacing dependencies with controlled test doubles. This enables fast, reliable, and focused unit tests that don't depend on external systems like databases, APIs, or file systems.

## When to Use

- Isolating unit tests from external dependencies
- Testing code that depends on slow operations (DB, network)
- Simulating error conditions and edge cases
- Verifying interactions between objects
- Testing code with non-deterministic behavior (time, randomness)
- Avoiding expensive operations in tests
- Testing error handling without triggering real failures

## Quick Start

Minimal working example:

```typescript
// services/UserService.ts
import { UserRepository } from "./UserRepository";
import { EmailService } from "./EmailService";

export class UserService {
  constructor(
    private userRepository: UserRepository,
    private emailService: EmailService,
  ) {}

  async createUser(userData: CreateUserDto) {
    const user = await this.userRepository.create(userData);
    await this.emailService.sendWelcomeEmail(user.email, user.name);
    return user;
  }

  async getUserStats(userId: string) {
    const user = await this.userRepository.findById(userId);
    if (!user) throw new Error("User not found");

    const orderCount = await this.userRepository.getOrderCount(userId);
    return { ...user, orderCount };
  }
}

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Jest Mocking (JavaScript/TypeScript)](references/jest-mocking-javascripttypescript.md) | Jest Mocking (JavaScript/TypeScript) |
| [Python Mocking with unittest.mock](references/python-mocking-with-unittestmock.md) | Python Mocking with unittest.mock |
| [Mockito for Java](references/mockito-for-java.md) | Mockito for Java |
| [Advanced Mocking Patterns](references/advanced-mocking-patterns.md) | Advanced Mocking Patterns |

## Best Practices

### ✅ DO

- Mock external dependencies (DB, API, file system)
- Use dependency injection for easier mocking
- Verify important interactions with mocks
- Reset mocks between tests
- Mock at the boundary (repositories, services)
- Use spies for partial mocking when needed
- Create reusable mock factories
- Test both success and failure scenarios

### ❌ DON'T

- Mock everything (don't mock what you own)
- Over-specify mock interactions
- Use mocks in integration tests
- Mock simple utility functions
- Create complex mock hierarchies
- Forget to verify mock calls
- Share mocks between tests
- Mock just to make tests pass
