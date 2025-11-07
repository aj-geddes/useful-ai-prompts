---
name: circuit-breaker-pattern
description: Implement circuit breaker patterns for fault tolerance, automatic failure detection, and fallback mechanisms. Use when calling external services, handling cascading failures, or implementing resilience patterns.
---

# Circuit Breaker Pattern

## Overview

Implement circuit breaker patterns to prevent cascading failures and provide graceful degradation when dependencies fail.

## When to Use

- External API calls
- Microservices communication
- Database connections
- Third-party service integrations
- Preventing cascading failures
- Implementing fallback mechanisms
- Rate limiting protection
- Timeout handling

## Circuit States

```
┌──────────┐
│  CLOSED  │ ◀─── Normal operation
└────┬─────┘
     │ Failures exceed threshold
     ▼
┌──────────┐
│   OPEN   │ ◀─── Reject requests
└────┬─────┘
     │ Timeout expires
     ▼
┌──────────┐
│HALF-OPEN │ ◀─── Test recovery
└────┬─────┘
     │ Success/Failure
     ▼
Back to CLOSED or OPEN
```

## Implementation Examples

### 1. **TypeScript Circuit Breaker**

```typescript
enum CircuitState {
  CLOSED = 'CLOSED',
  OPEN = 'OPEN',
  HALF_OPEN = 'HALF_OPEN'
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
    consecutiveSuccesses: 0
  };
  private nextAttempt: number = Date.now();

  constructor(private config: CircuitBreakerConfig) {}

  async execute<T>(
    operation: () => Promise<T>,
    fallback?: () => T | Promise<T>
  ): Promise<T> {
    if (this.state === CircuitState.OPEN) {
      if (Date.now() < this.nextAttempt) {
        console.log('Circuit breaker OPEN, using fallback');

        if (fallback) {
          return await fallback();
        }

        throw new Error('Circuit breaker is OPEN');
      }

      // Try to recover
      this.state = CircuitState.HALF_OPEN;
      console.log('Circuit breaker entering HALF_OPEN state');
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

  private async executeWithTimeout<T>(
    operation: () => Promise<T>
  ): Promise<T> {
    return Promise.race([
      operation(),
      new Promise<T>((_, reject) =>
        setTimeout(
          () => reject(new Error('Operation timeout')),
          this.config.timeout
        )
      )
    ]);
  }

  private onSuccess(): void {
    this.stats.successes++;
    this.stats.consecutiveSuccesses++;
    this.stats.consecutiveFailures = 0;

    if (this.state === CircuitState.HALF_OPEN) {
      if (
        this.stats.consecutiveSuccesses >= this.config.successThreshold
      ) {
        console.log('Circuit breaker CLOSED after recovery');
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
      console.log('Circuit breaker OPEN after failed recovery');
      this.trip();
      return;
    }

    if (
      this.state === CircuitState.CLOSED &&
      this.stats.consecutiveFailures >= this.config.failureThreshold
    ) {
      console.log('Circuit breaker OPEN after threshold reached');
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
      consecutiveSuccesses: 0
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
  resetTimeout: 60000
});

async function callExternalAPI() {
  return breaker.execute(
    async () => {
      const response = await fetch('https://api.example.com/data');
      if (!response.ok) throw new Error('API error');
      return response.json();
    },
    () => {
      // Fallback: return cached data
      return { data: 'cached' };
    }
  );
}
```

### 2. **Circuit Breaker with Monitoring**

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
    lastStateChange: Date.now()
  };

  private responseTimes: number[] = [];

  async execute<T>(
    operation: () => Promise<T>,
    fallback?: () => T | Promise<T>
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
      this.responseTimes.reduce((a, b) => a + b, 0) /
      this.responseTimes.length;
  }

  getMetrics(): CircuitBreakerMetrics {
    return {
      ...this.metrics,
      state: this.getState()
    };
  }
}
```

### 3. **Opossum-Style Circuit Breaker (Node.js)**

```typescript
import CircuitBreaker from 'opossum';

// Create circuit breaker
const options = {
  timeout: 3000, // 3 seconds
  errorThresholdPercentage: 50,
  resetTimeout: 30000, // 30 seconds
  rollingCountTimeout: 10000,
  rollingCountBuckets: 10,
  name: 'api-breaker'
};

const breaker = new CircuitBreaker(callExternalAPI, options);

// Event handlers
breaker.on('open', () => {
  console.log('Circuit breaker opened');
});

breaker.on('halfOpen', () => {
  console.log('Circuit breaker half-opened');
});

breaker.on('close', () => {
  console.log('Circuit breaker closed');
});

breaker.on('success', (result) => {
  console.log('Request succeeded:', result);
});

breaker.on('failure', (error) => {
  console.error('Request failed:', error);
});

breaker.on('timeout', () => {
  console.error('Request timed out');
});

breaker.on('reject', () => {
  console.warn('Request rejected by circuit breaker');
});

// Fallback
breaker.fallback(() => {
  return { data: 'fallback data' };
});

// Use circuit breaker
async function callExternalAPI() {
  const response = await fetch('https://api.example.com/data');
  if (!response.ok) throw new Error('API error');
  return response.json();
}

// Execute with circuit breaker
breaker.fire()
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

### 4. **Python Circuit Breaker**

```python
from enum import Enum
from typing import Callable, Optional, TypeVar, Generic
import time
import threading

T = TypeVar('T')

class CircuitState(Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

class CircuitBreaker(Generic[T]):
    def __init__(
        self,
        failure_threshold: int = 5,
        success_threshold: int = 2,
        timeout: float = 3.0,
        reset_timeout: float = 60.0
    ):
        self.failure_threshold = failure_threshold
        self.success_threshold = success_threshold
        self.timeout = timeout
        self.reset_timeout = reset_timeout

        self.state = CircuitState.CLOSED
        self.failures = 0
        self.successes = 0
        self.last_failure_time = None
        self.next_attempt = time.time()
        self.lock = threading.Lock()

    def call(
        self,
        func: Callable[[], T],
        fallback: Optional[Callable[[], T]] = None
    ) -> T:
        """Execute function with circuit breaker protection."""
        with self.lock:
            if self.state == CircuitState.OPEN:
                if time.time() < self.next_attempt:
                    print("Circuit breaker OPEN")
                    if fallback:
                        return fallback()
                    raise Exception("Circuit breaker is OPEN")

                # Try to recover
                self.state = CircuitState.HALF_OPEN
                print("Circuit breaker entering HALF_OPEN")

        try:
            result = func()
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            if fallback:
                return fallback()
            raise

    def _on_success(self):
        """Handle successful request."""
        with self.lock:
            self.failures = 0
            self.successes += 1

            if self.state == CircuitState.HALF_OPEN:
                if self.successes >= self.success_threshold:
                    print("Circuit breaker CLOSED")
                    self.state = CircuitState.CLOSED
                    self.successes = 0

    def _on_failure(self):
        """Handle failed request."""
        with self.lock:
            self.failures += 1
            self.successes = 0
            self.last_failure_time = time.time()

            if self.state == CircuitState.HALF_OPEN:
                print("Circuit breaker OPEN after failed recovery")
                self._trip()
            elif self.failures >= self.failure_threshold:
                print(f"Circuit breaker OPEN after {self.failures} failures")
                self._trip()

    def _trip(self):
        """Open the circuit."""
        self.state = CircuitState.OPEN
        self.next_attempt = time.time() + self.reset_timeout

    def get_state(self) -> CircuitState:
        """Get current circuit state."""
        return self.state

    def reset(self):
        """Manually reset the circuit breaker."""
        with self.lock:
            self.state = CircuitState.CLOSED
            self.failures = 0
            self.successes = 0


# Usage
import requests

breaker = CircuitBreaker(
    failure_threshold=5,
    success_threshold=2,
    timeout=3.0,
    reset_timeout=60.0
)

def call_api():
    response = requests.get('https://api.example.com/data', timeout=3)
    response.raise_for_status()
    return response.json()

def fallback():
    return {"data": "cached or default"}

# Execute with circuit breaker
try:
    result = breaker.call(call_api, fallback)
    print(result)
except Exception as e:
    print(f"Error: {e}")
```

### 5. **Resilience4j-Style (Java)**

```java
import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.circuitbreaker.CircuitBreakerConfig;
import io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry;
import io.vavr.control.Try;

import java.time.Duration;
import java.util.function.Supplier;

public class CircuitBreakerExample {

    public static void main(String[] args) {
        // Create circuit breaker config
        CircuitBreakerConfig config = CircuitBreakerConfig.custom()
            .failureRateThreshold(50)
            .waitDurationInOpenState(Duration.ofMillis(30000))
            .permittedNumberOfCallsInHalfOpenState(2)
            .slidingWindowSize(10)
            .recordExceptions(Exception.class)
            .build();

        // Create registry
        CircuitBreakerRegistry registry = CircuitBreakerRegistry.of(config);

        // Get or create circuit breaker
        CircuitBreaker breaker = registry.circuitBreaker("apiBreaker");

        // Event handlers
        breaker.getEventPublisher()
            .onStateTransition(event ->
                System.out.println("State: " + event.getStateTransition())
            )
            .onError(event ->
                System.out.println("Error: " + event.getThrowable())
            )
            .onSuccess(event ->
                System.out.println("Success")
            );

        // Decorate supplier
        Supplier<String> decoratedSupplier = CircuitBreaker
            .decorateSupplier(breaker, this::callExternalService);

        // Execute with circuit breaker
        Try<String> result = Try.of(decoratedSupplier::get)
            .recover(throwable -> "fallback");

        System.out.println(result.get());
    }

    private String callExternalService() {
        // External service call
        return "data";
    }
}
```

## Best Practices

### ✅ DO
- Use appropriate thresholds for your use case
- Implement fallback mechanisms
- Monitor circuit breaker states
- Set reasonable timeouts
- Use exponential backoff
- Log state transitions
- Alert on frequent trips
- Test circuit breaker behavior
- Use per-dependency breakers
- Implement health checks

### ❌ DON'T
- Use same breaker for all dependencies
- Set unrealistic thresholds
- Skip fallback implementation
- Ignore open circuit breakers
- Use overly aggressive reset timeouts
- Forget to monitor

## Resources

- [Martin Fowler - Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html)
- [Resilience4j](https://resilience4j.readme.io/)
- [Opossum](https://nodeshift.dev/opossum/)
