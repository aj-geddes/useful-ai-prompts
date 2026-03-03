# Node.js Profiling

## Node.js Profiling

```typescript
import { performance, PerformanceObserver } from "perf_hooks";

class Profiler {
  private marks = new Map<string, number>();

  mark(name: string): void {
    this.marks.set(name, performance.now());
  }

  measure(name: string, startMark: string): number {
    const start = this.marks.get(startMark);
    if (!start) throw new Error(`Mark ${startMark} not found`);

    const duration = performance.now() - start;
    console.log(`${name}: ${duration.toFixed(2)}ms`);

    return duration;
  }

  async profile<T>(name: string, fn: () => Promise<T>): Promise<T> {
    const start = performance.now();

    try {
      return await fn();
    } finally {
      const duration = performance.now() - start;
      console.log(`${name}: ${duration.toFixed(2)}ms`);
    }
  }
}

// Usage
const profiler = new Profiler();

app.get("/api/users", async (req, res) => {
  profiler.mark("request-start");

  const users = await profiler.profile("fetch-users", async () => {
    return await db.query("SELECT * FROM users");
  });

  profiler.measure("total-request-time", "request-start");

  res.json(users);
});
```
