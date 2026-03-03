# Token Bucket Algorithm (TypeScript)

## Token Bucket Algorithm (TypeScript)

```typescript
interface TokenBucketConfig {
  capacity: number;
  refillRate: number; // tokens per second
  refillInterval: number; // milliseconds
}

class TokenBucket {
  private tokens: number;
  private lastRefill: number;
  private readonly capacity: number;
  private readonly refillRate: number;
  private readonly refillInterval: number;
  private refillTimer?: NodeJS.Timeout;

  constructor(config: TokenBucketConfig) {
    this.capacity = config.capacity;
    this.tokens = config.capacity;
    this.refillRate = config.refillRate;
    this.refillInterval = config.refillInterval;
    this.lastRefill = Date.now();

    this.startRefill();
  }

  private startRefill(): void {
    this.refillTimer = setInterval(() => {
      this.refill();
    }, this.refillInterval);
  }

  private refill(): void {
    const now = Date.now();
    const timePassed = now - this.lastRefill;
    const tokensToAdd = (timePassed / 1000) * this.refillRate;

    this.tokens = Math.min(this.capacity, this.tokens + tokensToAdd);
    this.lastRefill = now;
  }

  tryConsume(tokens: number = 1): boolean {
    this.refill(); // Refill before checking

    if (this.tokens >= tokens) {
      this.tokens -= tokens;
      return true;
    }

    return false;
  }

  getAvailableTokens(): number {
    this.refill();
    return Math.floor(this.tokens);
  }

  getWaitTime(tokens: number = 1): number {
    this.refill();

    if (this.tokens >= tokens) {
      return 0;
    }

    const tokensNeeded = tokens - this.tokens;
    return (tokensNeeded / this.refillRate) * 1000;
  }

  reset(): void {
    this.tokens = this.capacity;
    this.lastRefill = Date.now();
  }

  destroy(): void {
    if (this.refillTimer) {
      clearInterval(this.refillTimer);
    }
  }
}

// Usage
const rateLimiter = new TokenBucket({
  capacity: 100,
  refillRate: 10, // 10 tokens per second
  refillInterval: 100, // Check every 100ms
});

if (rateLimiter.tryConsume(1)) {
  // Process request
  console.log("Request allowed");
} else {
  const waitTime = rateLimiter.getWaitTime(1);
  console.log(`Rate limited. Retry after ${waitTime}ms`);
}
```
