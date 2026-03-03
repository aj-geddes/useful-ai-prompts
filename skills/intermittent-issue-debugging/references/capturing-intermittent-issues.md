# Capturing Intermittent Issues

## Capturing Intermittent Issues

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
      stack: error.stack,
    });
    throw error;
  }
}

// Strategy 2: Correlation IDs
// Track requests across systems

const correlationId = generateId();
logger.info({
  correlationId,
  action: "payment_start",
  orderId: 123,
});

chargeCard(orderId, { headers: { correlationId } });

logger.info({
  correlationId,
  action: "payment_end",
  status: "success",
});

// Later, can grep logs by correlationId to see full trace

// Strategy 3: Error Sampling
// Capture full error context when occurs

window.addEventListener("error", (event) => {
  const errorData = {
    message: event.message,
    url: event.filename,
    line: event.lineno,
    col: event.colno,
    stack: event.error?.stack,
    userAgent: navigator.userAgent,
    memory: performance.memory?.usedJSHeapSize,
    timestamp: new Date().toISOString(),
  };

  sendToMonitoring(errorData); // Send to error tracking
});
```
