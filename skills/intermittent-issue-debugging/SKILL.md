---
name: intermittent-issue-debugging
description: >
  Debug issues that occur sporadically and are hard to reproduce. Use monitoring
  and systematic investigation to identify root causes of flaky behavior.
---

# Intermittent Issue Debugging

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Intermittent issues are the most difficult to debug because they don't occur consistently. Systematic approach and comprehensive monitoring are essential.

## When to Use

- Sporadic errors in logs
- Users report occasional issues
- Flaky tests
- Race conditions suspected
- Timing-dependent bugs
- Resource exhaustion issues

## Quick Start

Minimal working example:

```javascript
// Strategy 1: Comprehensive Logging
// Add detailed logging around suspected code

function processPayment(orderId) {
  const startTime = Date.now();
  console.log(`[${startTime}] Payment start: order=${orderId}`);

  try {
    const result = chargeCard(orderId);
    console.log(`[${Date.now()}] Payment success: ${orderId}`);
    return result;
  } catch (error) {
    const duration = Date.now() - startTime;
    console.error(`[${Date.now()}] Payment FAILED:`, {
      order: orderId,
      error: error.message,
      duration_ms: duration,
      error_type: error.constructor.name,
      stack: error.stack,
    });
    throw error;
  }
}

// Strategy 2: Correlation IDs
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Capturing Intermittent Issues](references/capturing-intermittent-issues.md) | Capturing Intermittent Issues |
| [Common Intermittent Issues](references/common-intermittent-issues.md) | Common Intermittent Issues |
| [Systematic Investigation Process](references/systematic-investigation-process.md) | Systematic Investigation Process |
| [Monitoring & Prevention](references/monitoring-prevention.md) | Monitoring & Prevention |

## Best Practices

### ✅ DO

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
