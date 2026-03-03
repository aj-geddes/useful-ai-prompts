# Log Sampling (High-Volume Services)

## Log Sampling (High-Volume Services)

```typescript
// log-sampler.ts
class SamplingLogger {
  constructor(
    private logger: Logger,
    private sampleRate: number = 0.1, // 10% sampling
  ) {}

  info(message: string, meta?: object) {
    if (this.shouldSample()) {
      this.logger.info(message, meta);
    }
  }

  // Always log warnings and errors
  warn(message: string, meta?: object) {
    this.logger.warn(message, meta);
  }

  error(message: string, error: Error, meta?: object) {
    this.logger.error(message, error, meta);
  }

  private shouldSample(): boolean {
    return Math.random() < this.sampleRate;
  }

  // Sample based on user ID (consistent sampling)
  infoSampled(userId: string, message: string, meta?: object) {
    const hash = this.hashUserId(userId);
    if (hash % 100 < this.sampleRate * 100) {
      this.logger.info(message, { ...meta, sampled: true });
    }
  }

  private hashUserId(userId: string): number {
    let hash = 0;
    for (let i = 0; i < userId.length; i++) {
      hash = (hash << 5) - hash + userId.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }
}
```
