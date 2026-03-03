---
name: microservices-architecture
description: >
  Design and implement microservices architecture including service boundaries,
  communication patterns, API gateways, service mesh, service discovery, and
  distributed system patterns. Use when building microservices, distributed
  systems, or service-oriented architectures.
---

# Microservices Architecture

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Comprehensive guide to designing, implementing, and maintaining microservices architectures. Covers service decomposition, communication patterns, data management, deployment strategies, and observability for distributed systems.

## When to Use

- Designing new microservices architectures
- Decomposing monolithic applications
- Implementing service-to-service communication
- Setting up API gateways and service mesh
- Implementing service discovery
- Managing distributed transactions
- Designing inter-service data consistency
- Scaling independent services

## Quick Start

Minimal working example:

```
Bounded Contexts:
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Order Service  │  │  User Service   │  │ Payment Service │
│                 │  │                 │  │                 │
│ - Create Order  │  │ - User Profile  │  │ - Process Pay   │
│ - Order Status  │  │ - Auth          │  │ - Refund        │
│ - Order History │  │ - Preferences   │  │ - Transactions  │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Service Boundary Design](references/service-boundary-design.md) | Service Boundary Design |
| [Communication Patterns](references/communication-patterns.md) | Communication Patterns |
| [API Gateway Pattern](references/api-gateway-pattern.md) | API Gateway Pattern |
| [Service Discovery](references/service-discovery.md) | Service Discovery |
| [Data Consistency Patterns](references/data-consistency-patterns.md) | Data Consistency Patterns |
| [Service Mesh (Istio)](references/service-mesh-istio.md) | Service Mesh (Istio) |

## Best Practices

### ✅ DO

- Design services around business capabilities
- Use asynchronous communication where possible
- Implement circuit breakers for resilience
- Use API gateway for cross-cutting concerns
- Implement distributed tracing
- Use service mesh for service-to-service communication
- Design for failure (chaos engineering)
- Implement health checks for all services
- Use correlation IDs for request tracking
- Version your APIs
- Implement proper monitoring and alerting
- Use event-driven architecture for loose coupling
- Implement idempotent operations
- Use database per service pattern

### ❌ DON'T

- Share databases between services
- Create overly granular services (nanoservices)
- Use distributed transactions (two-phase commit)
- Ignore network latency and failures
- Share domain models between services
- Deploy all services as one unit
- Hardcode service URLs
- Forget to implement authentication/authorization
- Use synchronous calls for long-running operations
- Ignore backward compatibility
- Skip monitoring and logging
- Create circular dependencies between services
