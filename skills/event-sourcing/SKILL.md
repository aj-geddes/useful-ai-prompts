---
name: event-sourcing
description: >
  Implement event sourcing and CQRS patterns using event stores, aggregates, and
  projections. Use when building audit trails, temporal queries, or systems
  requiring full history.
---

# Event Sourcing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Store state changes as a sequence of events rather than the current state, enabling temporal queries, audit trails, and event replay.

## When to Use

- Audit trail requirements
- Temporal queries (state at any point in time)
- Event-driven microservices
- CQRS implementations
- Financial systems
- Complex domain models
- Debugging and analysis
- Compliance and regulation

## Quick Start

Minimal working example:

```typescript
interface DomainEvent {
  id: string;
  aggregateId: string;
  aggregateType: string;
  eventType: string;
  data: any;
  metadata: {
    userId?: string;
    timestamp: number;
    version: number;
  };
}

interface Aggregate {
  id: string;
  version: number;
}

class EventStore {
  private events: DomainEvent[] = [];

  async appendEvents(
    aggregateId: string,
    expectedVersion: number,
    events: Omit<DomainEvent, "id" | "metadata">[],
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Event Store (TypeScript)](references/event-store-typescript.md) | Event Store (TypeScript) |
| [Projections (Read Models)](references/projections-read-models.md) | Projections (Read Models) |
| [Event Store with PostgreSQL](references/event-store-with-postgresql.md) | Event Store with PostgreSQL |
| [Snapshots for Performance](references/snapshots-for-performance.md) | Snapshots for Performance |

## Best Practices

### ✅ DO

- Store events immutably
- Version your events
- Use optimistic concurrency
- Create snapshots for performance
- Use projections for queries
- Keep events small and focused
- Include metadata (timestamp, user, etc.)
- Handle event versioning/migration

### ❌ DON'T

- Mutate past events
- Store current state only
- Skip concurrency checks
- Query event store for reads
- Make events too large
- Forget about event schema evolution
