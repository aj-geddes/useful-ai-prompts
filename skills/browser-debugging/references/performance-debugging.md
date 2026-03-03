# Performance Debugging

## Performance Debugging

```yaml
Network Performance:

1. Open Network tab
2. Reload page
3. Identify slow resources:
   - Large images (>500KB)
   - Large JavaScript (>300KB)
   - Slow requests (>2s)
   - Waterfall bottlenecks

Solutions:
  - Optimize images
  - Code split JavaScript
  - Lazy load resources
  - Compress assets
  - Use CDN

Runtime Performance:

1. Performance tab
2. Record interaction
3. Analyze flame chart:
   - Long red bars = slow
   - Identify functions
   - Check main thread blocking
   - Monitor frame rate

Solutions:
  - Move work to Web Workers
  - Defer non-critical work
  - Optimize algorithms
  - Use requestAnimationFrame

---

Checklist:

Console:
  [ ] No errors
  [ ] No warnings (expected ones)
  [ ] No unhandled promise rejections

Elements:
  [ ] HTML structure correct
  [ ] CSS applied correctly
  [ ] No accessibility issues
  [ ] Responsive at all breakpoints

Network:
  [ ] All resources load successfully
  [ ] No excessive requests
  [ ] File sizes reasonable
  [ ] No blocked resources

Performance:
  [ ] Frame rate >60 FPS
  [ ] No long tasks (>50ms)
  [ ] LCP <2.5s
  [ ] Memory stable
```
