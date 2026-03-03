---
name: reactive-programming
description: >
  Implement reactive programming patterns using RxJS, streams, observables, and
  backpressure handling. Use when building event-driven UIs, handling async data
  streams, or managing complex data flows.
---

# Reactive Programming

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build responsive applications using reactive streams and observables for handling asynchronous data flows.

## When to Use

- Complex async data flows
- Real-time data updates
- Event-driven architectures
- UI state management
- WebSocket/SSE handling
- Combining multiple data sources

## Quick Start

Minimal working example:

```typescript
import {
  Observable,
  Subject,
  BehaviorSubject,
  fromEvent,
  interval,
} from "rxjs";
import {
  map,
  filter,
  debounceTime,
  distinctUntilChanged,
  switchMap,
} from "rxjs/operators";

// Create observable from array
const numbers$ = new Observable<number>((subscriber) => {
  subscriber.next(1);
  subscriber.next(2);
  subscriber.next(3);
  subscriber.complete();
});

numbers$.subscribe({
  next: (value) => console.log(value),
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [RxJS Basics](references/rxjs-basics.md) | RxJS Basics |
| [Search with Debounce](references/search-with-debounce.md) | Search with Debounce |
| [State Management](references/state-management.md) | State Management |
| [WebSocket with Reconnection](references/websocket-with-reconnection.md) | WebSocket with Reconnection |
| [Combining Multiple Streams](references/combining-multiple-streams.md) | Combining Multiple Streams |
| [Backpressure Handling](references/backpressure-handling.md) | Backpressure Handling |
| [Custom Operators](references/custom-operators.md) | Custom Operators |

## Best Practices

### ✅ DO

- Unsubscribe to prevent memory leaks
- Use operators to transform data
- Handle errors properly
- Use shareReplay for expensive operations
- Combine streams when needed
- Test reactive code

### ❌ DON'T

- Subscribe multiple times to same observable
- Forget to unsubscribe
- Use nested subscriptions
- Ignore error handling
- Make observables stateful
