---
name: intermittent-issue-debugging
description: >
  Debug issues that occur sporadically and are hard to reproduce. Use monitoring.
  Use when sporadic errors in logs, users report occasional issues, flaky tests, or race conditions suspected.
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

- Attach correlation IDs to every request so you can trace a single occurrence across services and logs
- Increase logging verbosity temporarily around the suspected area and capture timestamps, thread IDs, and resource state
- Reproduce timing-dependent bugs with stress tests, chaos engineering, or artificially injected delays
- Use statistical analysis on occurrence patterns (time of day, load level, specific inputs) to narrow the search space
- Write a deterministic regression test that reliably triggers the root cause before declaring the fix complete

### ❌ DON'T

- Dismiss a sporadic failure as a "fluke" without investigating — intermittent issues tend to worsen under load
- Change multiple variables at once when testing a hypothesis; isolate one factor at a time
- Remove enhanced logging immediately after a fix — keep it long enough to confirm the issue is truly resolved in production
- Assume the issue is environment-specific without checking for shared dependencies like DNS, NTP, or connection pool limits
