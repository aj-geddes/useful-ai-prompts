# Monitoring & Best Practices

## Monitoring & Best Practices

```yaml
Monitoring:

Production Profiling:
  - Lightweight sampling profiler
  - 1-5% overhead typical
  - Tools: New Relic, DataDog, Clinic
  - Alert on CPU spikes

Key Metrics:
  - CPU usage % per function
  - Call frequency
  - Time per call
  - GC pause times
  - P95/P99 latency

---

Best Practices:

Before Optimizing:
  [ ] Profile to find actual bottleneck
  [ ] Don't guess (verify with data)
  [ ] Establish baseline
  [ ] Measure improvement

During Optimization:
  [ ] Change one thing at a time
  [ ] Profile after each change
  [ ] Verify improvement
  [ ] Don't prematurely optimize

Premature Optimization:
  - Profile first
  - Hot path only (80/20 rule)
  - Measure impact
  - Consider readability

---

Tools Summary:

Framework: Chrome DevTools, Firefox, Node Profiler
Analysis: Flame graphs, Call trees, Timeline
Monitoring: APM tools, Clinic.js
Comparison: Before/after profiles

---

Red Flags:

- Unexpected high CPU
- GC pauses >100ms
- Function called 1M times per request
- Deep call stacks
- Synchronous I/O in loops
- Repeated calculations
- Memory allocation in hot loop
```
