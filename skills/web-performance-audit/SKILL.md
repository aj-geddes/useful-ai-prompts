---
name: web-performance-audit
description: >
  Conduct comprehensive web performance audits. Measure page speed, identify
  bottlenecks, and recommend optimizations to improve user experience and SEO.
---

# Web Performance Audit

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Web performance audits measure load times, identify bottlenecks, and guide optimization efforts to create faster, better user experiences.

## When to Use

- Regular performance monitoring
- After major changes
- User complaints about slowness
- SEO optimization
- Mobile optimization
- Performance baseline setting

## Quick Start

Minimal working example:

```yaml
Core Web Vitals (Google):

Largest Contentful Paint (LCP):
  Measure: Time to load largest visible element
  Good: <2.5 seconds
  Poor: >4 seconds
  Impacts: User perception of speed

First Input Delay (FID):
  Measure: Time from user input to response
  Good: <100 milliseconds
  Poor: >300 milliseconds
  Impacts: Responsiveness

Cumulative Layout Shift (CLS):
  Measure: Visual stability (unexpected layout shifts)
  Good: <0.1
  Poor: >0.25
  Impacts: User frustration

---

Additional Metrics:

First Contentful Paint (FCP):
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Performance Metrics](references/performance-metrics.md) | Performance Metrics |
| [Performance Analysis Process](references/performance-analysis-process.md) | Performance Analysis Process |
| [Optimization Strategies](references/optimization-strategies.md) | Optimization Strategies |
| [Monitoring & Continuous Improvement](references/monitoring-continuous-improvement.md) | Monitoring & Continuous Improvement |

## Best Practices

### ✅ DO

- Measure regularly (not just once)
- Use field data (real users) + lab data
- Focus on Core Web Vitals
- Set realistic targets
- Prioritize by impact
- Monitor continuously
- Setup performance budgets
- Test on slow networks
- Include mobile in testing
- Document improvements

### ❌ DON'T

- Ignore field data
- Focus on one metric only
- Set impossible targets
- Optimize without measurement
- Forget about images
- Ignore JavaScript costs
- Skip mobile performance
- Over-optimize prematurely
- Forget about monitoring
- Expect improvements without effort
