# Monitoring & Targets

## Monitoring & Targets

```yaml
Memory Targets:

Web App:
  Initial: <10MB
  After use: <50MB
  Peak: <100MB
  Leak check: Should plateau

Node.js API:
  Per-process: 100-500MB
  Cluster total: 1-4GB
  Heap size: Monitor vs available RAM

Mobile:
  Initial: <20MB
  Working: <50MB
  Peak: <100MB (device dependent)

---

Tools:

Browser:
  - Chrome DevTools Memory
  - Firefox DevTools Memory
  - React DevTools Profiler
  - Redux DevTools

Node.js:
  - node --inspect
  - clinic.js
  - nodemon --exec with monitoring
  - New Relic / DataDog

Monitoring:
  - Application Performance Monitoring (APM)
  - Prometheus + Grafana
  - CloudWatch
  - New Relic

---

Checklist:

[ ] Profile baseline memory
[ ] Identify heavy components
[ ] Remove event listeners on cleanup
[ ] Clear timers on cleanup
[ ] Implement lazy loading
[ ] Use pagination for large lists
[ ] Monitor memory trends
[ ] Set up GC monitoring
[ ] Test with production data volume
[ ] Stress test for leaks
[ ] Establish memory budget
[ ] Set up alerts
```
