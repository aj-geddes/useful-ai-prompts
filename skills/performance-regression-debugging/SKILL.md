---
name: performance-regression-debugging
description: Identify and debug performance regressions from code changes. Use comparison and profiling to locate what degraded performance and restore baseline metrics.
---

# Performance Regression Debugging

## Overview

Performance regressions occur when code changes degrade application performance. Detection and quick resolution are critical.

## When to Use

- After deployment performance degrades
- Metrics show negative trend
- User complaints about slowness
- A/B testing shows variance
- Regular performance monitoring

## Instructions

### 1. **Detection & Measurement**

```javascript
// Before: 500ms response time
// After: 1000ms response time (2x slower = regression)

// Capture baseline metrics
const baseline = {
  responseTime: 500,  // ms
  timeToInteractive: 2000,  // ms
  largestContentfulPaint: 1500,  // ms
  memoryUsage: 50,  // MB
  bundleSize: 150  // KB gzipped
};

// Monitor after change
const current = {
  responseTime: 1000,
  timeToInteractive: 4000,
  largestContentfulPaint: 3000,
  memoryUsage: 150,
  bundleSize: 200
};

// Calculate regression
const regressions = {};
for (let metric in baseline) {
  const change = (current[metric] - baseline[metric]) / baseline[metric];
  if (change > 0.1) {  // >10% degradation
    regressions[metric] = {
      baseline: baseline[metric],
      current: current[metric],
      percentChange: (change * 100).toFixed(1) + '%',
      severity: change > 0.5 ? 'Critical' : 'High'
    };
  }
}

// Results:
// responseTime: 500ms → 1000ms (100% slower = CRITICAL)
// largestContentfulPaint: 1500ms → 3000ms (100% slower = CRITICAL)
```

### 2. **Root Cause Identification**

```yaml
Systematic Search:

Step 1: Identify Changed Code
  - Check git commits between versions
  - Review code review comments
  - Identify risky changes
  - Prioritize by likelyhood

Step 2: Binary Search (Bisect)
  - Start with suspected change
  - Disable the change
  - Re-measure performance
  - If improves → this is the issue
  - If not → disable other changes

  git bisect start
  git bisect bad HEAD
  git bisect good v1.0.0
  # Test each commit

Step 3: Profile the Change
  - Run profiler on old vs new code
  - Compare flame graphs
  - Identify expensive functions
  - Check allocation patterns

Step 4: Analyze Impact
  - Code review the change
  - Understand what changed
  - Check for O(n²) algorithms
  - Look for new database queries
  - Check for missing indexes

---

Common Regressions:

N+1 Query:
  Before: 1 query (10ms)
  After: 1000 queries (1000ms)
  Caused: Removed JOIN, now looping
  Fix: Restore JOIN or use eager loading

Missing Index:
  Before: Index Scan (10ms)
  After: Seq Scan (500ms)
  Caused: New filter column, no index
  Fix: Add index

Memory Leak:
  Before: 50MB memory
  After: 500MB after 1 hour
  Caused: Listener not removed, cache grows
  Fix: Clean up properly

Bundle Size:
  Before: 150KB gzipped
  After: 250KB gzipped
  Caused: Added library without tree-shaking
  Fix: Use lighter alternative or split

Algorithm Efficiency:
  Before: O(n) = 1ms for 1000 items
  After: O(n²) = 1000ms for 1000 items
  Caused: Nested loops added
  Fix: Use better algorithm
```

### 3. **Fixing & Verification**

```yaml
Fix Process:

1. Understand the Problem
  - Profile and identify exactly what's slow
  - Measure impact quantitatively
  - Understand root cause

2. Implement Fix
  - Make minimal changes
  - Don't introduce new issues
  - Test locally first
  - Measure improvement

3. Verify Fix
  - Run same measurement
  - Check regression gone
  - Ensure no new issues
  - Compare metrics

  Before regression: 500ms
  After regression: 1000ms
  After fix: 550ms (acceptable, minor overhead)

4. Prevent Recurrence
  - Add performance test
  - Set performance budget
  - Alert on regressions
  - Code review for perf
```

### 4. **Prevention Measures**

```yaml
Performance Testing:

Baseline Testing:
  - Establish baseline metrics
  - Record for each release
  - Track trends over time
  - Alert on degradation

Load Testing:
  - Test with realistic load
  - Measure under stress
  - Identify bottlenecks
  - Catch regressions

Performance Budgets:
  - Set max bundle size
  - Set max response time
  - Set max LCP/FCP
  - Enforce in CI/CD

Monitoring:
  - Track real user metrics
  - Alert on degradation
  - Compare releases
  - Analyze trends

---

Checklist:

[ ] Baseline metrics established
[ ] Regression detected and measured
[ ] Changed code identified
[ ] Root cause found (code, data, infra)
[ ] Fix implemented
[ ] Fix verified
[ ] No new issues introduced
[ ] Performance test added
[ ] Budget set
[ ] Monitoring updated
[ ] Team notified
[ ] Prevention measures in place
```

## Key Points

- Establish baseline metrics for comparison
- Use binary search to find culprit commits
- Profile to identify exact bottleneck
- Measure before/after fix
- Add performance regression tests
- Set and enforce performance budgets
- Monitor production metrics
- Alert on significant degradation
- Document root cause
- Prevent through code review
