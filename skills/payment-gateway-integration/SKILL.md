---
name: payment-gateway-integration
description: >
  Integrate payment gateways like Stripe, PayPal, and Square with backends for
  payment processing, subscription management, and webhook handling. Use when
  building e-commerce platforms, implementing billing systems, and handling
  payments securely.
---

# Payment Gateway Integration

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build secure payment processing systems with major payment providers (Stripe, PayPal, Square), handling transactions, subscriptions, webhooks, PCI compliance, and error scenarios across different backend frameworks.

## When to Use

- Processing customer payments
- Implementing subscription billing
- Building e-commerce platforms
- Handling refunds and disputes
- Managing recurring charges
- Integrating payment webhooks

## Quick Start

Minimal working example:

```python
# config.py
import os

class StripeConfig:
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
    STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')

# stripe_service.py
import stripe
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

class StripePaymentService:
    @staticmethod
    def create_payment_intent(amount, currency='usd', description=None, metadata=None):
        """Create a payment intent"""
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert to cents
                currency=currency,
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Stripe Integration with Python/Flask](references/stripe-integration-with-pythonflask.md) | Stripe Integration with Python/Flask |
| [Node.js/Express Stripe Integration](references/nodejsexpress-stripe-integration.md) | Node.js/Express Stripe Integration |
| [PayPal Integration](references/paypal-integration.md) | PayPal Integration |
| [Subscription Management](references/subscription-management.md) | Subscription Management |

## Best Practices

### ✅ DO

- Use official payment SDK libraries
- Verify webhook signatures
- Store minimal payment information
- Never store full credit card numbers
- Use HTTPS for all payment routes
- Implement proper error handling
- Test with sandbox environments
- Handle payment failures gracefully
- Implement PCI compliance
- Log all payment transactions
- Use idempotency keys
- Implement retry logic

### ❌ DON'T

- Handle raw card data
- Store sensitive payment information
- Log sensitive details
- Trust client-side validation only
- Ignore webhook events
- Hardcode API keys
- Use test keys in production
- Skip SSL/TLS verification
- Forget to validate amounts
- Store payment tokens without encryption
