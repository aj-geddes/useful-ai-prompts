# Real-Time Monitoring

## Real-Time Monitoring

```javascript
// performance-monitor.js
class PerformanceMonitor {
  constructor() {
    this.metrics = [];
  }

  async measureEndpoint(name, fn) {
    const start = performance.now();
    const startMemory = process.memoryUsage();

    try {
      const result = await fn();
      const duration = performance.now() - start;
      const endMemory = process.memoryUsage();

      this.metrics.push({
        name,
        duration,
        memoryDelta: {
          heapUsed: endMemory.heapUsed - startMemory.heapUsed,
          external: endMemory.external - startMemory.external,
        },
        timestamp: new Date(),
      });

      return result;
    } catch (error) {
      throw error;
    }
  }

  getStats(name) {
    const measurements = this.metrics.filter((m) => m.name === name);
    const durations = measurements.map((m) => m.duration);

    return {
      count: measurements.length,
      mean: durations.reduce((a, b) => a + b, 0) / durations.length,
      min: Math.min(...durations),
      max: Math.max(...durations),
      p50: this.percentile(durations, 50),
      p95: this.percentile(durations, 95),
      p99: this.percentile(durations, 99),
    };
  }

  percentile(values, p) {
    const sorted = values.sort((a, b) => a - b);
    const index = Math.ceil((p / 100) * sorted.length) - 1;
    return sorted[index];
  }
}

// Usage in tests
const monitor = new PerformanceMonitor();

test("API endpoint performance", async () => {
  for (let i = 0; i < 100; i++) {
    await monitor.measureEndpoint("getUsers", async () => {
      return await fetch("/api/users").then((r) => r.json());
    });
  }

  const stats = monitor.getStats("getUsers");

  expect(stats.p95).toBeLessThan(500); // 95th percentile under 500ms
  expect(stats.mean).toBeLessThan(200); // Average under 200ms
});
```
