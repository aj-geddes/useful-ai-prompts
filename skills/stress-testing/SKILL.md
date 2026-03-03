---
name: stress-testing
description: >
  Test system behavior under extreme load conditions to identify breaking
  points, capacity limits, and failure modes. Use for stress test, capacity
  testing, breaking point analysis, spike test, and system limits validation.
---

# Stress Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Stress testing pushes systems beyond normal operating capacity to identify breaking points, failure modes, and recovery behavior. It validates system stability under extreme conditions and helps determine maximum capacity before degradation or failure.

## When to Use

- Finding system capacity limits
- Identifying breaking points
- Testing auto-scaling behavior
- Validating error handling under load
- Testing recovery after failures
- Planning capacity requirements
- Verifying graceful degradation
- Testing spike traffic handling

## Quick Start

Minimal working example:

```javascript
// stress-test.js
import http from "k6/http";
import { check, sleep } from "k6";
import { Rate } from "k6/metrics";

const errorRate = new Rate("errors");

export const options = {
  stages: [
    // Stress testing: Progressive load increase
    { duration: "2m", target: 100 }, // Normal load
    { duration: "5m", target: 100 }, // Sustain normal
    { duration: "2m", target: 200 }, // Above normal
    { duration: "5m", target: 200 }, // Sustain above normal
    { duration: "2m", target: 300 }, // Breaking point approaching
    { duration: "5m", target: 300 }, // Sustain high load
    { duration: "2m", target: 400 }, // Beyond capacity
    { duration: "5m", target: 400 }, // System under stress
    { duration: "5m", target: 0 }, // Gradual recovery
  ],
  thresholds: {
    http_req_duration: ["p(99)<1000"], // 99% under 1s during stress
    http_req_failed: ["rate<0.05"], // Allow 5% error rate under stress
    errors: ["rate<0.1"],
  },
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [k6 Stress Testing](references/k6-stress-testing.md) | k6 Stress Testing |
| [Spike Testing](references/spike-testing.md) | Spike Testing |
| [Soak/Endurance Testing](references/soakendurance-testing.md) | Soak/Endurance Testing |
| [JMeter Stress Test](references/jmeter-stress-test.md) | JMeter Stress Test |
| [Auto-Scaling Validation](references/auto-scaling-validation.md) | Auto-Scaling Validation |
| [Breaking Point Analysis](references/breaking-point-analysis.md) | Breaking Point Analysis |

## Best Practices

### ✅ DO

- Test in production-like environment
- Monitor all system resources
- Gradually increase load to find limits
- Test recovery after stress
- Document breaking points
- Test auto-scaling behavior
- Plan for graceful degradation
- Monitor for memory leaks

### ❌ DON'T

- Test in production without safeguards
- Skip recovery testing
- Ignore warning signs (CPU, memory)
- Test only success scenarios
- Assume linear scalability
- Forget database capacity
- Skip monitoring third-party dependencies
- Test without proper cleanup
