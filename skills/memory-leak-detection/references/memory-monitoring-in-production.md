# Memory Monitoring in Production

## Memory Monitoring in Production

```typescript
class MemoryMonitor {
  private alerts: Array<(usage: NodeJS.MemoryUsage) => void> = [];

  startMonitoring(
    options: {
      interval?: number;
      heapThreshold?: number;
      rssThreshold?: number;
    } = {},
  ): void {
    const {
      interval = 60000,
      heapThreshold = 0.9,
      rssThreshold = 0.95,
    } = options;

    setInterval(() => {
      const usage = process.memoryUsage();
      const heapUsedPercent = usage.heapUsed / usage.heapTotal;

      if (heapUsedPercent > heapThreshold) {
        console.warn(
          `⚠️  High heap usage: ${(heapUsedPercent * 100).toFixed(2)}%`,
        );

        this.alerts.forEach((fn) => fn(usage));

        // Force GC if available
        if (global.gc) {
          console.log("Forcing garbage collection...");
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
  console.error("Memory alert triggered:", usage);
});

monitor.startMonitoring({
  interval: 30000,
  heapThreshold: 0.85,
});
```
