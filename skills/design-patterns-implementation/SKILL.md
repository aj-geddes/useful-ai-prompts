---
name: design-patterns-implementation
description: >
  Apply appropriate design patterns (Singleton, Factory, Observer, Strategy,
  etc.) to solve architectural problems. Use when refactoring code architecture,
  implementing extensible systems, or following SOLID principles.
---

# Design Patterns Implementation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Apply proven design patterns to create maintainable, extensible, and testable code architectures.

## When to Use

- Solving common architectural problems
- Making code more maintainable and testable
- Implementing extensible plugin systems
- Decoupling components
- Following SOLID principles
- Code reviews identifying architectural issues

## Quick Start

Minimal working example:

```typescript
class DatabaseConnection {
  private static instance: DatabaseConnection;
  private connection: any;

  private constructor() {
    this.connection = this.createConnection();
  }

  public static getInstance(): DatabaseConnection {
    if (!DatabaseConnection.instance) {
      DatabaseConnection.instance = new DatabaseConnection();
    }
    return DatabaseConnection.instance;
  }

  private createConnection() {
    return {
      /* connection logic */
    };
  }
}

// Usage
const db1 = DatabaseConnection.getInstance();
const db2 = DatabaseConnection.getInstance();
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Singleton Pattern](references/singleton-pattern.md) | Singleton Pattern |
| [Factory Pattern](references/factory-pattern.md) | Factory Pattern |
| [Observer Pattern](references/observer-pattern.md) | Observer Pattern |
| [Strategy Pattern](references/strategy-pattern.md) | Strategy Pattern |
| [Decorator Pattern](references/decorator-pattern.md) | Decorator Pattern |
| [Repository Pattern](references/repository-pattern.md) | Repository Pattern |
| [Dependency Injection](references/dependency-injection.md) | Dependency Injection |

## Best Practices

### ✅ DO

- Choose patterns that solve actual problems
- Keep patterns simple and understandable
- Document why patterns were chosen
- Consider testability
- Follow SOLID principles
- Use dependency injection
- Prefer composition over inheritance

### ❌ DON'T

- Apply patterns without understanding them
- Over-engineer simple solutions
- Force patterns where they don't fit
- Create unnecessary abstraction layers
- Ignore team familiarity with patterns
