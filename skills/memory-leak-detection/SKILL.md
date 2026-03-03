---
name: memory-leak-detection
description: >
  Detect and fix memory leaks using heap snapshots, memory profiling, and leak
  detection tools. Use when investigating memory growth, OOM errors, or
  optimizing memory usage.
---

# Memory Leak Detection

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Identify and fix memory leaks to prevent out-of-memory crashes and optimize application performance.

## When to Use

- Memory usage growing over time
- Out of memory (OOM) errors
- Performance degradation
- Container restarts
- High memory consumption

## Quick Start

Minimal working example:

```typescript
import v8 from "v8";
import fs from "fs";

class MemoryProfiler {
  takeSnapshot(filename: string): void {
    const snapshot = v8.writeHeapSnapshot(filename);
    console.log(`Heap snapshot saved to ${snapshot}`);
  }

  getMemoryUsage(): NodeJS.MemoryUsage {
    return process.memoryUsage();
  }

  formatMemory(bytes: number): string {
    return `${(bytes / 1024 / 1024).toFixed(2)} MB`;
  }

  printMemoryUsage(): void {
    const usage = this.getMemoryUsage();

    console.log("Memory Usage:");
    console.log(`  RSS: ${this.formatMemory(usage.rss)}`);
    console.log(`  Heap Total: ${this.formatMemory(usage.heapTotal)}`);
    console.log(`  Heap Used: ${this.formatMemory(usage.heapUsed)}`);
    console.log(`  External: ${this.formatMemory(usage.external)}`);
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js Heap Snapshots](references/nodejs-heap-snapshots.md) | Node.js Heap Snapshots |
| [Memory Leak Detection Middleware](references/memory-leak-detection-middleware.md) | Memory Leak Detection Middleware |
| [Common Memory Leak Patterns](references/common-memory-leak-patterns.md) | Common Memory Leak Patterns |
| [Python Memory Profiling](references/python-memory-profiling.md) | Python Memory Profiling |
| [WeakMap/WeakRef for Cache](references/weakmapweakref-for-cache.md) | WeakMap/WeakRef for Cache |
| [Memory Monitoring in Production](references/memory-monitoring-in-production.md) | Memory Monitoring in Production |

## Best Practices

### ✅ DO

- Remove event listeners when done
- Clear timers and intervals
- Use WeakMap/WeakRef for caches
- Limit cache sizes
- Monitor memory in production
- Profile regularly
- Clean up after tests

### ❌ DON'T

- Create circular references
- Hold references to large objects unnecessarily
- Forget to clean up resources
- Ignore memory growth
- Skip WeakMap for object caches
