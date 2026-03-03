# Benchmarking

## Benchmarking

```typescript
class Benchmark {
  async run(
    name: string,
    fn: () => Promise<any>,
    iterations: number = 1000,
  ): Promise<void> {
    console.log(`\nBenchmarking: ${name}`);

    const times: number[] = [];

    // Warmup
    for (let i = 0; i < 10; i++) {
      await fn();
    }

    // Actual benchmark
    for (let i = 0; i < iterations; i++) {
      const start = performance.now();
      await fn();
      times.push(performance.now() - start);
    }

    // Statistics
    const sorted = times.sort((a, b) => a - b);
    const min = sorted[0];
    const max = sorted[sorted.length - 1];
    const avg = times.reduce((a, b) => a + b, 0) / times.length;
    const p50 = sorted[Math.floor(sorted.length * 0.5)];
    const p95 = sorted[Math.floor(sorted.length * 0.95)];
    const p99 = sorted[Math.floor(sorted.length * 0.99)];

    console.log(`  Iterations: ${iterations}`);
    console.log(`  Min: ${min.toFixed(2)}ms`);
    console.log(`  Max: ${max.toFixed(2)}ms`);
    console.log(`  Avg: ${avg.toFixed(2)}ms`);
    console.log(`  P50: ${p50.toFixed(2)}ms`);
    console.log(`  P95: ${p95.toFixed(2)}ms`);
    console.log(`  P99: ${p99.toFixed(2)}ms`);
  }

  async compare(
    implementations: Array<{ name: string; fn: () => Promise<any> }>,
    iterations: number = 1000,
  ): Promise<void> {
    for (const impl of implementations) {
      await this.run(impl.name, impl.fn, iterations);
    }
  }
}

// Usage
const bench = new Benchmark();

await bench.compare([
  {
    name: "Array.filter + map",
    fn: async () => {
      const arr = Array.from({ length: 1000 }, (_, i) => i);
      return arr.filter((x) => x % 2 === 0).map((x) => x * 2);
    },
  },
  {
    name: "Single loop",
    fn: async () => {
      const arr = Array.from({ length: 1000 }, (_, i) => i);
      const result = [];
      for (const x of arr) {
        if (x % 2 === 0) {
          result.push(x * 2);
        }
      }
      return result;
    },
  },
]);
```
