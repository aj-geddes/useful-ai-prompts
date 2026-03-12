---
name: performance-regression-debugging
description: >
  Identify and debug performance regressions from code changes. Use comparison
  and profiling to locate what degraded performance and restore baseline.
  Use when after deployment performance degrades, metrics show negative trend, user complaints about slowness, or a/b testing shows variance.
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

- Maintain recorded baseline metrics (response time, TTFB, LCP, memory, bundle size) and compare against them after every deployment
- Use `git bisect` with an automated performance test to pinpoint the exact commit that introduced the regression
- Profile the hot path with flame graphs or CPU profilers rather than guessing which function is slower
- Run performance tests in a stable, isolated environment to avoid noisy-neighbor variance skewing results
- Set CI gates that fail the build when key metrics regress beyond a defined threshold (e.g., p95 latency +10%)

### ❌ DON'T

- Rely on a single metric — a regression in response time might actually be caused by increased memory pressure or GC pauses
- Compare production metrics across different traffic volumes without normalizing for load
- Apply a fix without verifying the improvement with the same benchmark that detected the regression
- Ignore regressions in bundle size or asset count — they compound over time and directly impact load performance
