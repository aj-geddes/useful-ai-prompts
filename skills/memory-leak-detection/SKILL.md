---
name: memory-leak-detection
description: Detect and fix memory leaks using heap snapshots, memory profiling, and leak detection tools. Use when investigating memory growth, OOM errors, or optimizing memory usage.
---

# Memory Leak Detection

## Overview

Identify and fix memory leaks to prevent out-of-memory crashes and optimize application performance.

## When to Use

- Memory usage growing over time
- Out of memory (OOM) errors
- Performance degradation
- Container restarts
- High memory consumption

## Implementation Examples

### 1. **Node.js Heap Snapshots**

```typescript
import v8 from 'v8';
import fs from 'fs';

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

    console.log('Memory Usage:');
    console.log(`  RSS: ${this.formatMemory(usage.rss)}`);
    console.log(`  Heap Total: ${this.formatMemory(usage.heapTotal)}`);
    console.log(`  Heap Used: ${this.formatMemory(usage.heapUsed)}`);
    console.log(`  External: ${this.formatMemory(usage.external)}`);
  }

  monitorMemory(interval: number = 5000): void {
    setInterval(() => {
      this.printMemoryUsage();
    }, interval);
  }
}

// Usage
const profiler = new MemoryProfiler();

// Take initial snapshot
profiler.takeSnapshot('./heap-before.heapsnapshot');

// Run application
await runApp();

// Take final snapshot
profiler.takeSnapshot('./heap-after.heapsnapshot');

// Compare in Chrome DevTools to find leaks
```

### 2. **Memory Leak Detection Middleware**

```typescript
class LeakDetector {
  private samples: number[] = [];
  private maxSamples = 10;
  private threshold = 1.5; // 50% growth

  checkForLeak(): boolean {
    const usage = process.memoryUsage();
    this.samples.push(usage.heapUsed);

    if (this.samples.length > this.maxSamples) {
      this.samples.shift();
    }

    if (this.samples.length < this.maxSamples) {
      return false;
    }

    const first = this.samples[0];
    const last = this.samples[this.samples.length - 1];
    const growth = last / first;

    return growth > this.threshold;
  }

  startMonitoring(interval: number = 10000): void {
    setInterval(() => {
      if (this.checkForLeak()) {
        console.warn('⚠️  Potential memory leak detected!');
        console.warn('Memory samples:', this.samples.map(s =>
          `${(s / 1024 / 1024).toFixed(2)} MB`
        ));
      }
    }, interval);
  }
}

// Usage
const detector = new LeakDetector();
detector.startMonitoring();
```

### 3. **Common Memory Leak Patterns**

```typescript
// BAD: Event listener leak
class BadComponent {
  constructor() {
    window.addEventListener('resize', this.handleResize);
  }

  handleResize = () => {
    // Handler logic
  }

  // Missing cleanup!
}

// GOOD: Proper cleanup
class GoodComponent {
  constructor() {
    window.addEventListener('resize', this.handleResize);
  }

  handleResize = () => {
    // Handler logic
  }

  destroy() {
    window.removeEventListener('resize', this.handleResize);
  }
}

// BAD: Timer leak
function badFunction() {
  setInterval(() => {
    doSomething();
  }, 1000);
  // Interval never cleared!
}

// GOOD: Clear timer
function goodFunction() {
  const intervalId = setInterval(() => {
    doSomething();
  }, 1000);

  return () => clearInterval(intervalId);
}

// BAD: Closure leak
function createClosure() {
  const largeData = new Array(1000000).fill('data');

  return function() {
    // largeData kept in memory even if unused
    console.log('closure');
  };
}

// GOOD: Don't capture unnecessary data
function createClosure() {
  const needed = 'small data';

  return function() {
    console.log(needed);
  };
}

// BAD: Global variable accumulation
let cache = [];

function addToCache(item: any) {
  cache.push(item);
  // Cache grows indefinitely!
}

// GOOD: Bounded cache
class BoundedCache {
  private cache: any[] = [];
  private maxSize = 1000;

  add(item: any) {
    this.cache.push(item);
    if (this.cache.length > this.maxSize) {
      this.cache.shift();
    }
  }
}
```

### 4. **Python Memory Profiling**

```python
import tracemalloc
from typing import List, Tuple

class MemoryProfiler:
    def __init__(self):
        self.snapshots: List = []

    def start(self):
        """Start tracking memory allocations."""
        tracemalloc.start()

    def take_snapshot(self):
        """Take a memory snapshot."""
        snapshot = tracemalloc.take_snapshot()
        self.snapshots.append(snapshot)
        return snapshot

    def compare_snapshots(
        self,
        snapshot1_idx: int,
        snapshot2_idx: int,
        top_n: int = 10
    ):
        """Compare two snapshots."""
        snapshot1 = self.snapshots[snapshot1_idx]
        snapshot2 = self.snapshots[snapshot2_idx]

        stats = snapshot2.compare_to(snapshot1, 'lineno')

        print(f"\nTop {top_n} memory differences:")
        for stat in stats[:top_n]:
            print(f"{stat.size_diff / 1024:.1f} KB: {stat.traceback}")

    def get_top_allocations(self, snapshot_idx: int = -1, top_n: int = 10):
        """Get top memory allocations."""
        snapshot = self.snapshots[snapshot_idx]
        stats = snapshot.statistics('lineno')

        print(f"\nTop {top_n} memory allocations:")
        for stat in stats[:top_n]:
            print(f"{stat.size / 1024:.1f} KB: {stat.traceback}")

    def stop(self):
        """Stop tracking."""
        tracemalloc.stop()


# Usage
profiler = MemoryProfiler()
profiler.start()

# Take initial snapshot
profiler.take_snapshot()

# Run code
data = [i for i in range(1000000)]  # Allocate memory

# Take another snapshot
profiler.take_snapshot()

# Compare
profiler.compare_snapshots(0, 1)

profiler.stop()
```

### 5. **WeakMap/WeakRef for Cache**

```typescript
class WeakCache<K extends object, V> {
  private cache = new WeakMap<K, V>();

  set(key: K, value: V): void {
    this.cache.set(key, value);
  }

  get(key: K): V | undefined {
    return this.cache.get(key);
  }

  has(key: K): boolean {
    return this.cache.has(key);
  }

  delete(key: K): void {
    this.cache.delete(key);
  }
}

// Objects can be garbage collected even if in cache
const cache = new WeakCache<object, string>();
let obj = { id: 1 };

cache.set(obj, 'data');

// When obj is no longer referenced, it can be GC'd
obj = null as any;
```

### 6. **Memory Monitoring in Production**

```typescript
class MemoryMonitor {
  private alerts: Array<(usage: NodeJS.MemoryUsage) => void> = [];

  startMonitoring(options: {
    interval?: number;
    heapThreshold?: number;
    rssThreshold?: number;
  } = {}): void {
    const {
      interval = 60000,
      heapThreshold = 0.9,
      rssThreshold = 0.95
    } = options;

    setInterval(() => {
      const usage = process.memoryUsage();
      const heapUsedPercent = usage.heapUsed / usage.heapTotal;

      if (heapUsedPercent > heapThreshold) {
        console.warn(
          `⚠️  High heap usage: ${(heapUsedPercent * 100).toFixed(2)}%`
        );

        this.alerts.forEach(fn => fn(usage));

        // Force GC if available
        if (global.gc) {
          console.log('Forcing garbage collection...');
          global.gc();
        }
      }
    }, interval);
  }

  onAlert(callback: (usage: NodeJS.MemoryUsage) => void): void {
    this.alerts.push(callback);
  }
}

// Usage
const monitor = new MemoryMonitor();

monitor.onAlert((usage) => {
  // Send alert to monitoring service
  console.error('Memory alert triggered:', usage);
});

monitor.startMonitoring({
  interval: 30000,
  heapThreshold: 0.85
});
```

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

## Tools

- **Node.js**: Chrome DevTools, heapdump, memwatch-next
- **Python**: tracemalloc, memory_profiler, pympler
- **Browsers**: Chrome DevTools Memory Profiler
- **Production**: New Relic, DataDog APM

## Resources

- [Node.js Memory Leaks](https://nodejs.org/en/docs/guides/simple-profiling/)
- [Chrome DevTools Memory](https://developer.chrome.com/docs/devtools/memory-problems/)
- [Python tracemalloc](https://docs.python.org/3/library/tracemalloc.html)
