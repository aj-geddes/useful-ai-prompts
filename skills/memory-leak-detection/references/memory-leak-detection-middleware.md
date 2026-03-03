# Memory Leak Detection Middleware

## Memory Leak Detection Middleware

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
        console.warn("⚠️  Potential memory leak detected!");
        console.warn(
          "Memory samples:",
          this.samples.map((s) => `${(s / 1024 / 1024).toFixed(2)} MB`),
        );
      }
    }, interval);
  }
}

// Usage
const detector = new LeakDetector();
detector.startMonitoring();
```
