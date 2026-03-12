---
name: memory-optimization
description: >
  Profile and optimize application memory usage. Identify memory leaks, reduce
  memory footprint, and improve efficiency for better performance and.
  Use when high memory usage, memory leaks suspected, slow performance, or out of memory crashes.
  reliability.
---

# Memory Optimization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Memory optimization improves application performance, stability, and reduces infrastructure costs. Efficient memory usage is critical for scalability.

## When to Use

- High memory usage
- Memory leaks suspected
- Slow performance
- Out of memory crashes
- Scaling challenges

## Quick Start

Minimal working example:

```javascript
// Browser memory profiling

// Check memory usage
performance.memory: {
  jsHeapSizeLimit: 2190000000,    // Max available
  totalJSHeapSize: 1300000000,    // Total allocated
  usedJSHeapSize: 950000000       // Currently used
}

// React DevTools Profiler
- Open React DevTools → Profiler
- Record interaction
- See component renders and time
- Identify unnecessary renders

// Chrome DevTools
1. Open DevTools → Memory
2. Take heap snapshot
3. Compare before/after
4. Look for retained objects
5. Check retained sizes

// Node.js profiling
node --inspect app.js
// Open chrome://inspect
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Memory Profiling](references/memory-profiling.md) | Memory Profiling |
| [Memory Leak Detection](references/memory-leak-detection.md) | Memory Leak Detection |
| [Optimization Techniques](references/optimization-techniques.md) | Optimization Techniques |
| [Monitoring & Targets](references/monitoring-targets.md) | Monitoring & Targets |

## Best Practices

### ✅ DO

- Profile with heap snapshots before and after suspected operations to measure actual retained memory, not just allocations
- Use WeakRef and WeakMap for caches and observers that should not prevent garbage collection
- Pool and reuse expensive objects (buffers, database connections) instead of allocating and discarding per request
- Set memory budgets in CI (e.g., `--max-old-space-size` assertions) to catch regressions before they reach production
- Clean up event listeners, timers, and subscriptions in component teardown or `finally` blocks

### ❌ DON'T

- Load entire datasets into memory when streaming or pagination would keep the working set bounded
- Hold references to detached DOM nodes — this is the most common source of browser memory leaks
- Rely on the garbage collector to compensate for unbounded growth in caches or queues — set explicit eviction policies
- Optimize memory in micro-benchmarks without verifying the improvement under realistic, sustained load
