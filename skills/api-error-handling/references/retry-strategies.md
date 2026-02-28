# Retry Strategies & Circuit Breaker

## Exponential Backoff with Jitter

```javascript
/**
 * Retry a function with exponential backoff.
 * Only retries on transient errors (5xx, network failures).
 * Never retries client errors (4xx) — they won't succeed on retry.
 */
async function retryWithBackoff(fn, options = {}) {
  const {
    maxRetries = 3,
    baseDelay = 1000,   // ms
    maxDelay = 30000,   // ms cap
    jitter = true,      // add randomness to avoid thundering herd
    retryOn = (err) => !err.statusCode || err.statusCode >= 500,
  } = options;

  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      const isLastAttempt = attempt === maxRetries - 1;
      const shouldRetry = retryOn(error);

      if (isLastAttempt || !shouldRetry) throw error;

      const exponential = Math.min(baseDelay * Math.pow(2, attempt), maxDelay);
      const delay = jitter
        ? exponential * (0.5 + Math.random() * 0.5)  // ±50% jitter
        : exponential;

      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }
}

// Usage
const user = await retryWithBackoff(
  () => fetchUser(userId),
  { maxRetries: 3, baseDelay: 500 }
);
```

## Circuit Breaker Pattern

Prevents cascade failures by short-circuiting calls to a failing dependency.

```javascript
class CircuitBreaker {
  /**
   * States:
   *   CLOSED   — normal operation, requests pass through
   *   OPEN     — dependency is failing, requests short-circuit immediately
   *   HALF_OPEN — testing recovery, allows one probe request
   */
  constructor(options = {}) {
    this.failureThreshold = options.failureThreshold ?? 5;
    this.timeout = options.timeout ?? 60_000;     // ms before trying again
    this.successThreshold = options.successThreshold ?? 2;  // to close from HALF_OPEN

    this.failureCount = 0;
    this.successCount = 0;
    this.state = "CLOSED";
    this.nextAttempt = Date.now();
  }

  async execute(fn) {
    if (this.state === "OPEN") {
      if (Date.now() < this.nextAttempt) {
        throw new ApiError("SERVICE_UNAVAILABLE", "Circuit breaker is open", 503);
      }
      this.state = "HALF_OPEN";
    }

    try {
      const result = await fn();
      this._onSuccess();
      return result;
    } catch (error) {
      this._onFailure();
      throw error;
    }
  }

  _onSuccess() {
    this.failureCount = 0;
    if (this.state === "HALF_OPEN") {
      this.successCount++;
      if (this.successCount >= this.successThreshold) {
        this.state = "CLOSED";
        this.successCount = 0;
      }
    }
  }

  _onFailure() {
    this.failureCount++;
    this.successCount = 0;
    if (this.failureCount >= this.failureThreshold) {
      this.state = "OPEN";
      this.nextAttempt = Date.now() + this.timeout;
    }
  }

  get status() {
    return { state: this.state, failures: this.failureCount };
  }
}

// Usage — one breaker per downstream service
const paymentBreaker = new CircuitBreaker({ failureThreshold: 3, timeout: 30_000 });

app.post("/api/payments", asyncHandler(async (req, res) => {
  const result = await paymentBreaker.execute(() =>
    paymentService.charge(req.body)
  );
  res.json({ data: result });
}));
```

## Combining Both Patterns

```javascript
// Retry inside the circuit breaker for transient blips,
// but let the circuit trip on sustained failures.
async function resilientCall(fn) {
  return serviceBreaker.execute(() =>
    retryWithBackoff(fn, { maxRetries: 2, baseDelay: 200 })
  );
}
```
