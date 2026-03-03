---
name: performance-regression-debugging
description: >
  Identify and debug performance regressions from code changes. Use comparison
  and profiling to locate what degraded performance and restore baseline
  metrics.
---

# Performance Regression Debugging

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Performance regressions occur when code changes degrade application performance. Detection and quick resolution are critical.

## When to Use

- After deployment performance degrades
- Metrics show negative trend
- User complaints about slowness
- A/B testing shows variance
- Regular performance monitoring

## Quick Start

Minimal working example:

```javascript
// Before: 500ms response time
// After: 1000ms response time (2x slower = regression)

// Capture baseline metrics
const baseline = {
  responseTime: 500, // ms
  timeToInteractive: 2000, // ms
  largestContentfulPaint: 1500, // ms
  memoryUsage: 50, // MB
  bundleSize: 150, // KB gzipped
};

// Monitor after change
const current = {
  responseTime: 1000,
  timeToInteractive: 4000,
  largestContentfulPaint: 3000,
  memoryUsage: 150,
  bundleSize: 200,
};

// Calculate regression
const regressions = {};
for (let metric in baseline) {
  const change = (current[metric] - baseline[metric]) / baseline[metric];
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Detection & Measurement](references/detection-measurement.md) | Detection & Measurement |
| [Root Cause Identification](references/root-cause-identification.md) | Root Cause Identification |
| [Fixing & Verification](references/fixing-verification.md) | Fixing & Verification |
| [Prevention Measures](references/prevention-measures.md) | Prevention Measures |

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
