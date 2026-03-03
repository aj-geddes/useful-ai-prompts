# Detection & Measurement

## Detection & Measurement

```javascript
// Before: 500ms response time
// After: 1000ms response time (2x slower = regression)

// Capture baseline metrics
const baseline = {
  responseTime: 500, // ms
  timeToInteractive: 2000, // ms
  largestContentfulPaint: 1500, // ms
  memoryUsage: 50, // MB
  bundleSize: 150, // KB gzipped
};

// Monitor after change
const current = {
  responseTime: 1000,
  timeToInteractive: 4000,
  largestContentfulPaint: 3000,
  memoryUsage: 150,
  bundleSize: 200,
};

// Calculate regression
const regressions = {};
for (let metric in baseline) {
  const change = (current[metric] - baseline[metric]) / baseline[metric];
  if (change > 0.1) {
    // >10% degradation
    regressions[metric] = {
      baseline: baseline[metric],
      current: current[metric],
      percentChange: (change * 100).toFixed(1) + "%",
      severity: change > 0.5 ? "Critical" : "High",
    };
  }
}

// Results:
// responseTime: 500ms → 1000ms (100% slower = CRITICAL)
// largestContentfulPaint: 1500ms → 3000ms (100% slower = CRITICAL)
```
