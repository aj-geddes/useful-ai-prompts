# Node.js Heap Snapshots

## Node.js Heap Snapshots

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
profiler.takeSnapshot("./heap-before.heapsnapshot");

// Run application
await runApp();

// Take final snapshot
profiler.takeSnapshot("./heap-after.heapsnapshot");

// Compare in Chrome DevTools to find leaks
```
