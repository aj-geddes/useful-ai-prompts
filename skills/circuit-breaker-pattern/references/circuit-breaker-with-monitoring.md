# Circuit Breaker with Monitoring

## Circuit Breaker with Monitoring

```typescript
interface CircuitBreakerMetrics {
  state: CircuitState;
  totalRequests: number;
  successfulRequests: number;
  failedRequests: number;
  rejectedRequests: number;
  averageResponseTime: number;
  lastStateChange: number;
}

class MonitoredCircuitBreaker extends CircuitBreaker {
  private metrics: CircuitBreakerMetrics = {
    state: CircuitState.CLOSED,
    totalRequests: 0,
    successfulRequests: 0,
    failedRequests: 0,
    rejectedRequests: 0,
    averageResponseTime: 0,
    lastStateChange: Date.now(),
  };

  private responseTimes: number[] = [];

  async execute<T>(
    operation: () => Promise<T>,
    fallback?: () => T | Promise<T>,
  ): Promise<T> {
    this.metrics.totalRequests++;

    if (this.getState() === CircuitState.OPEN) {
      this.metrics.rejectedRequests++;
    }

    const startTime = Date.now();

    try {
      const result = await super.execute(operation, fallback);

      this.metrics.successfulRequests++;
      this.recordResponseTime(Date.now() - startTime);

      return result;
    } catch (error) {
      this.metrics.failedRequests++;
      throw error;
    }
  }

  private recordResponseTime(time: number): void {
    this.responseTimes.push(time);

    // Keep only last 100 response times
    if (this.responseTimes.length > 100) {
      this.responseTimes.shift();
    }

    this.metrics.averageResponseTime =
      this.responseTimes.reduce((a, b) => a + b, 0) / this.responseTimes.length;
  }

  getMetrics(): CircuitBreakerMetrics {
    return {
      ...this.metrics,
      state: this.getState(),
    };
  }
}
```
