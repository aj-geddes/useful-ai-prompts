---
name: cpu-profiling
description: >
  Profile CPU usage to identify hot spots and bottlenecks. Optimize code paths.
  Use when high cpu usage, slow execution, performance regression, or before optimization.
  consuming most CPU time for better performance and resource efficiency.
---

# CPU Profiling

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

CPU profiling identifies which functions consume most CPU time, enabling targeted optimization of expensive code paths.

## When to Use

- High CPU usage
- Slow execution
- Performance regression
- Before optimization
- Production monitoring

## Quick Start

Minimal working example:

```yaml
Browser Profiling:

Chrome DevTools:
  Steps:
    1. DevTools → Performance
    2. Click record
    3. Perform action
    4. Stop recording
    5. Analyze flame chart
  Metrics:
    - Function call duration
    - Call frequency
    - Total time vs self time

Firefox Profiler:
  - Built-in performance profiler
  - Flame graphs
  - Timeline view
  - Export and share

React Profiler:
  - DevTools → Profiler
  - Component render times
  - Phase: render vs commit
  - Why component re-rendered
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Profiling Tools](references/profiling-tools.md) | Profiling Tools |
| [Analysis & Interpretation](references/analysis-interpretation.md) | Analysis & Interpretation |
| [Optimization Process](references/optimization-process.md) | Optimization Process |
| [Monitoring & Best Practices](references/monitoring-best-practices.md) | Monitoring & Best Practices |

## Best Practices

### ✅ DO

- Profile under realistic workloads — synthetic micro-benchmarks hide real-world hot paths
- Distinguish between "self time" and "total time" in flame charts to find the actual bottleneck
- Take multiple profile samples and compare to rule out noise from GC pauses or OS scheduling
- Establish a performance baseline before optimizing so you can measure the actual improvement
- Profile in production-like environments; dev-mode overhead (source maps, HMR) skews results

### ❌ DON'T

- Optimize functions that account for less than 1% of total CPU time — focus on the hot path
- Profile with browser DevTools extensions enabled; they add overhead and distort measurements
- Assume a slow function is CPU-bound without checking for I/O waits, lock contention, or GC pressure
- Commit performance changes without before/after profiling data to validate the improvement
