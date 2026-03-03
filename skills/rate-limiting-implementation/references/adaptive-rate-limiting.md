# Adaptive Rate Limiting

## Adaptive Rate Limiting

```typescript
class AdaptiveRateLimiter {
  private successRate: number = 1.0;
  private errorRate: number = 0.0;
  private currentLimit: number;

  constructor(
    private baseLimit: number,
    private minLimit: number,
    private maxLimit: number,
  ) {
    this.currentLimit = baseLimit;
  }

  recordSuccess(): void {
    this.successRate = this.successRate * 0.95 + 0.05;
    this.errorRate = this.errorRate * 0.95;
    this.adjustLimit();
  }

  recordError(): void {
    this.successRate = this.successRate * 0.95;
    this.errorRate = this.errorRate * 0.95 + 0.05;
    this.adjustLimit();
  }

  private adjustLimit(): void {
    // Increase limit if success rate is high
    if (this.successRate > 0.95 && this.errorRate < 0.01) {
      this.currentLimit = Math.min(this.currentLimit * 1.1, this.maxLimit);
    }

    // Decrease limit if error rate is high
    if (this.errorRate > 0.1 || this.successRate < 0.8) {
      this.currentLimit = Math.max(this.currentLimit * 0.9, this.minLimit);
    }
  }

  getCurrentLimit(): number {
    return Math.floor(this.currentLimit);
  }
}
```
