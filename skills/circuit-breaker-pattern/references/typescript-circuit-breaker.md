# TypeScript Circuit Breaker

## TypeScript Circuit Breaker

```typescript
enum CircuitState {
  CLOSED = "CLOSED",
  OPEN = "OPEN",
  HALF_OPEN = "HALF_OPEN",
}

interface CircuitBreakerConfig {
  failureThreshold: number;
  successThreshold: number;
  timeout: number;
  resetTimeout: number;
}

interface CircuitBreakerStats {
  failures: number;
  successes: number;
  consecutiveFailures: number;
  consecutiveSuccesses: number;
  lastFailureTime?: number;
}

class CircuitBreaker {
  private state: CircuitState = CircuitState.CLOSED;
  private stats: CircuitBreakerStats = {
    failures: 0,
    successes: 0,
    consecutiveFailures: 0,
    consecutiveSuccesses: 0,
  };
  private nextAttempt: number = Date.now();

  constructor(private config: CircuitBreakerConfig) {}

  async execute<T>(
    operation: () => Promise<T>,
    fallback?: () => T | Promise<T>,
  ): Promise<T> {
    if (this.state === CircuitState.OPEN) {
      if (Date.now() < this.nextAttempt) {
        console.log("Circuit breaker OPEN, using fallback");

        if (fallback) {
          return await fallback();
        }

        throw new Error("Circuit breaker is OPEN");
      }

      // Try to recover
      this.state = CircuitState.HALF_OPEN;
      console.log("Circuit breaker entering HALF_OPEN state");
    }

    try {
      const result = await this.executeWithTimeout(operation);
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();

      if (fallback) {
        return await fallback();
      }

      throw error;
    }
  }

  private async executeWithTimeout<T>(operation: () => Promise<T>): Promise<T> {
    return Promise.race([
      operation(),
      new Promise<T>((_, reject) =>
        setTimeout(
          () => reject(new Error("Operation timeout")),
          this.config.timeout,
        ),
      ),
    ]);
  }

  private onSuccess(): void {
    this.stats.successes++;
    this.stats.consecutiveSuccesses++;
    this.stats.consecutiveFailures = 0;

    if (this.state === CircuitState.HALF_OPEN) {
      if (this.stats.consecutiveSuccesses >= this.config.successThreshold) {
        console.log("Circuit breaker CLOSED after recovery");
        this.state = CircuitState.CLOSED;
        this.resetStats();
      }
    }
  }

  private onFailure(): void {
    this.stats.failures++;
    this.stats.consecutiveFailures++;
    this.stats.consecutiveSuccesses = 0;
    this.stats.lastFailureTime = Date.now();

    if (this.state === CircuitState.HALF_OPEN) {
      console.log("Circuit breaker OPEN after failed recovery");
      this.trip();
      return;
    }

    if (
      this.state === CircuitState.CLOSED &&
      this.stats.consecutiveFailures >= this.config.failureThreshold
    ) {
      console.log("Circuit breaker OPEN after threshold reached");
      this.trip();
    }
  }

  private trip(): void {
    this.state = CircuitState.OPEN;
    this.nextAttempt = Date.now() + this.config.resetTimeout;
  }

  private resetStats(): void {
    this.stats = {
      failures: 0,
      successes: 0,
      consecutiveFailures: 0,
      consecutiveSuccesses: 0,
    };
  }

  getState(): CircuitState {
    return this.state;
  }

  getStats(): CircuitBreakerStats {
    return { ...this.stats };
  }

  reset(): void {
    this.state = CircuitState.CLOSED;
    this.resetStats();
  }
}

// Usage
const breaker = new CircuitBreaker({
  failureThreshold: 5,
  successThreshold: 2,
  timeout: 3000,
  resetTimeout: 60000,
});

async function callExternalAPI() {
  return breaker.execute(
    async () => {
      const response = await fetch("https://api.example.com/data");
      if (!response.ok) throw new Error("API error");
      return response.json();
    },
    () => {
      // Fallback: return cached data
      return { data: "cached" };
    },
  );
}
```
