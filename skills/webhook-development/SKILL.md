---
name: webhook-development
description: >
  Implement webhook systems for event-driven integration with retry logic,
  signature verification, and delivery guarantees. Use when creating event
  notification systems, integrating with external services, or building
  event-driven architectures.
---

# Webhook Development

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build reliable webhook systems with event delivery, signature verification, retry logic, and dead-letter handling for asynchronous integrations.

## When to Use

- Sending real-time notifications to external systems
- Implementing event-driven architectures
- Integrating with third-party platforms
- Building audit trails and logging systems
- Triggering automated workflows
- Delivering payment or order notifications

## Quick Start

Minimal working example:

```json
{
  "id": "evt_1234567890",
  "timestamp": "2025-01-15T10:30:00Z",
  "event": "order.created",
  "version": "1.0",
  "data": {
    "orderId": "ORD-123456",
    "customerId": "CUST-789",
    "amount": 99.99,
    "currency": "USD",
    "items": [
      {
        "productId": "PROD-001",
        "quantity": 2,
        "price": 49.99
      }
    ],
    "status": "pending"
  },
  "attempt": 1,
  "retryable": true
}
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Webhook Event Schema](references/webhook-event-schema.md) | Webhook Event Schema |
| [Node.js Webhook Service](references/nodejs-webhook-service.md) | Node.js Webhook Service |
| [Python Webhook Handler](references/python-webhook-handler.md) | Python Webhook Handler |
| [Best Practices](references/best-practices.md) | Best Practices, Webhook Events |

## Best Practices

### ✅ DO

- Verify webhook signatures (HMAC-SHA256) on every incoming request before processing the payload
- Implement idempotency using the event ID so duplicate deliveries don't cause duplicate side effects
- Respond with a 2xx status quickly and process the payload asynchronously via a queue
- Use exponential backoff with jitter for retry delivery on failed webhook sends
- Log every delivery attempt, response code, and latency for debugging delivery issues
- Route failed deliveries to a dead-letter queue with alerting for manual review

### ❌ DON'T

- Trust webhook payloads without signature verification — treat them as untrusted external input
- Perform long-running work synchronously in the webhook handler (it will cause timeouts and retries)
- Expose internal error details (stack traces, DB errors) in webhook response bodies
- Retry indefinitely without a maximum attempt count or circuit breaker
