---
name: intermittent-issue-debugging
description: Debug issues that occur sporadically and are hard to reproduce. Use monitoring and systematic investigation to identify root causes of flaky behavior.
---

# Intermittent Issue Debugging

## Overview

Intermittent issues are the most difficult to debug because they don't occur consistently. Systematic approach and comprehensive monitoring are essential.

## When to Use

- Sporadic errors in logs
- Users report occasional issues
- Flaky tests
- Race conditions suspected
- Timing-dependent bugs
- Resource exhaustion issues

## Instructions

### 1. **Capturing Intermittent Issues**

```javascript
// Strategy 1: Comprehensive Logging
// Add detailed logging around suspected code

function processPayment(orderId) {
  const startTime = Date.now();
  console.log(`[${startTime}] Payment start: order=${orderId}`);

  try {
    const result = chargeCard(orderId);
    console.log(`[${Date.now()}] Payment success: ${orderId}`);
    return result;
  } catch (error) {
    const duration = Date.now() - startTime;
    console.error(`[${Date.now()}] Payment FAILED:`, {
      order: orderId,
      error: error.message,
      duration_ms: duration,
      error_type: error.constructor.name,
      stack: error.stack
    });
    throw error;
  }
}

// Strategy 2: Correlation IDs
// Track requests across systems

const correlationId = generateId();
logger.info({
  correlationId,
  action: 'payment_start',
  orderId: 123
});

chargeCard(orderId, {headers: {correlationId}});

logger.info({
  correlationId,
  action: 'payment_end',
  status: 'success'
});

// Later, can grep logs by correlationId to see full trace

// Strategy 3: Error Sampling
// Capture full error context when occurs

window.addEventListener('error', (event) => {
  const errorData = {
    message: event.message,
    url: event.filename,
    line: event.lineno,
    col: event.colno,
    stack: event.error?.stack,
    userAgent: navigator.userAgent,
    memory: performance.memory?.usedJSHeapSize,
    timestamp: new Date().toISOString()
  };

  sendToMonitoring(errorData);  // Send to error tracking
});
```

### 2. **Common Intermittent Issues**

```yaml
Issue: Race Condition

Symptom: Inconsistent behavior depending on timing

Example:
  Thread 1: Read count (5)
  Thread 2: Read count (5), increment to 6, write
  Thread 1: Increment to 6, write (overrides Thread 2)
  Result: Should be 7, but is 6

Debug:
  1. Add detailed timestamps
  2. Log all operations
  3. Look for overlapping operations
  4. Check if order matters

Solution:
  - Use locks/mutexes
  - Use atomic operations
  - Use message queues
  - Ensure single writer

---

Issue: Timing-Dependent Bug

Symptom: Test passes sometimes, fails others

Example:
  test_user_creation:
    1. Create user (sometimes slow)
    2. Check user exists
    3. Fails if create took too long

Debug:
  - Add timeout logging
  - Increase wait time
  - Add explicit waits
  - Mock slow operations

Solution:
  - Explicit wait for condition
  - Remove time-dependent assertions
  - Use proper test fixtures

---

Issue: Resource Exhaustion

Symptom: Works fine, but after time fails

Example:
  - Memory grows over time
  - Connections pool exhausted
  - Disk space fills up
  - Max open files reached

Debug:
  - Monitor resources continuously
  - Check for leaks (memory growth)
  - Monitor connection count
  - Check long-running processes

Solution:
  - Fix memory leak
  - Increase resource limits
  - Implement cleanup
  - Add monitoring/alerts

---

Issue: Intermittent Network Failure

Symptom: API calls occasionally fail

Debug:
  - Check network logs
  - Identify timeout patterns
  - Check if time-of-day dependent
  - Check if load dependent

Solution:
  - Implement exponential backoff retry
  - Add circuit breaker
  - Increase timeout
  - Add redundancy
```

### 3. **Systematic Investigation Process**

```yaml
Step 1: Understand the Pattern
  Questions:
    - How often does it occur? (1/100, 1/1000?)
    - When does it occur? (time of day, load, specific user?)
    - What are the conditions? (network, memory, load?)
    - Is it reproducible? (deterministic or random?)
    - Any recent changes?

  Analysis:
    - Review error logs
    - Check error rate trends
    - Identify patterns
    - Correlate with changes

Step 2: Reproduce Reliably
  Methods:
    - Increase test frequency (run 1000 times)
    - Stress test (heavy load)
    - Simulate poor conditions (network, memory)
    - Run on different machines
    - Run in production-like environment

  Goal: Make issue consistent to analyze

Step 3: Add Instrumentation
  - Add detailed logging
  - Add monitoring metrics
  - Add trace IDs
  - Capture errors fully
  - Log system state

Step 4: Capture the Issue
  - Recreate scenario
  - Capture full context
  - Note system state
  - Document conditions
  - Get reproduction case

Step 5: Analyze Data
  - Review logs
  - Look for patterns
  - Compare normal vs error cases
  - Check timing correlations
  - Identify root cause

Step 6: Implement Fix
  - Based on root cause
  - Verify with reproduction case
  - Test extensively
  - Add regression test
```

### 4. **Monitoring & Prevention**

```yaml
Monitoring Strategy:

Real User Monitoring (RUM):
  - Error rates by feature
  - Latency percentiles
  - User impact
  - Trend analysis

Application Performance Monitoring (APM):
  - Request traces
  - Database query performance
  - External service calls
  - Resource usage

Synthetic Monitoring:
  - Regular test execution
  - Simulate user flows
  - Alert on failures
  - Trend tracking

---

Alerting:

Setup alerts for:
  - Error rate spike
  - Response time >threshold
  - Memory growth trend
  - Failed transactions

---

Prevention Checklist:

[ ] Comprehensive logging in place
[ ] Error tracking configured
[ ] Performance monitoring active
[ ] Resource monitoring enabled
[ ] Correlation IDs used
[ ] Failed requests captured
[ ] Timeout values appropriate
[ ] Retry logic implemented
[ ] Circuit breakers in place
[ ] Load testing performed
[ ] Stress testing performed
[ ] Race conditions reviewed
[ ] Timing dependencies checked

---

Tools:

Monitoring:
  - New Relic / DataDog
  - Prometheus / Grafana
  - Sentry / Rollbar
  - Custom logging

Testing:
  - Load testing (k6, JMeter)
  - Chaos engineering (gremlin)
  - Property-based testing (hypothesis)
  - Fuzz testing

Debugging:
  - Distributed tracing (Jaeger)
  - Correlation IDs
  - Detailed logging
  - Debuggers
```

## Key Points

- Comprehensive logging is essential
- Add correlation IDs for tracing
- Monitor for patterns and trends
- Stress test to reproduce
- Use detailed error context
- Implement exponential backoff for retries
- Monitor resource exhaustion
- Add circuit breakers for external services
- Log system state with errors
- Implement proper monitoring/alerting
