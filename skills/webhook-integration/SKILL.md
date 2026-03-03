---
name: webhook-integration
description: >
  Implement secure webhook systems for event-driven integrations, including
  signature verification, retry logic, and delivery guarantees. Use when
  building third-party integrations, event notifications, or real-time data
  synchronization.
---

# Webhook Integration

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement robust webhook systems for event-driven architectures, enabling real-time communication between services and third-party integrations.

## When to Use

- Third-party service integrations (Stripe, GitHub, Shopify)
- Event notification systems
- Real-time data synchronization
- Automated workflow triggers
- Payment processing callbacks
- CI/CD pipeline notifications
- User activity tracking
- Microservices communication

## Quick Start

Minimal working example:

```typescript
import crypto from "crypto";
import axios from "axios";

interface WebhookEvent {
  id: string;
  type: string;
  timestamp: number;
  data: any;
}

interface WebhookEndpoint {
  url: string;
  secret: string;
  events: string[];
  active: boolean;
}

interface DeliveryAttempt {
  attemptNumber: number;
  timestamp: number;
  statusCode?: number;
  error?: string;
  duration: number;
}

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Webhook Sender (TypeScript)](references/webhook-sender-typescript.md) | Webhook Sender (TypeScript) |
| [Webhook Receiver (Express)](references/webhook-receiver-express.md) | Webhook Receiver (Express) |
| [Webhook Queue with Bull](references/webhook-queue-with-bull.md) | Webhook Queue with Bull |
| [Webhook Testing Utilities](references/webhook-testing-utilities.md) | Webhook Testing Utilities |

## Best Practices

### ✅ DO

- Use HMAC signatures for verification
- Implement idempotency with event IDs
- Return 200 OK quickly, process asynchronously
- Implement exponential backoff for retries
- Include timestamp to prevent replay attacks
- Use queue systems for reliable delivery
- Log all delivery attempts
- Provide webhook testing tools
- Document webhook payload schemas
- Implement webhook management UI
- Allow filtering by event types
- Support webhook versioning

### ❌ DON'T

- Send sensitive data in webhooks
- Skip signature verification
- Block responses with heavy processing
- Retry indefinitely
- Expose internal error details
- Send webhooks to localhost (in production)
- Forget timeout handling
- Skip rate limiting
