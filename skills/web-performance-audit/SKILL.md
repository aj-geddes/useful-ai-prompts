---
name: web-performance-audit
description: Conduct comprehensive web performance audits. Measure page speed, identify bottlenecks, and recommend optimizations to improve user experience and SEO.
---

# Web Performance Audit

## Overview

Web performance audits measure load times, identify bottlenecks, and guide optimization efforts to create faster, better user experiences.

## When to Use

- Regular performance monitoring
- After major changes
- User complaints about slowness
- SEO optimization
- Mobile optimization
- Performance baseline setting

## Instructions

### 1. **Performance Metrics**

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
  Measure: First visible content appears
  Target: <1.8 seconds

Time to Interactive (TTI):
  Measure: Page is fully interactive
  Target: <3.8 seconds

Total Blocking Time (TBT):
  Measure: JavaScript blocking time
  Target: <300ms

Interaction to Next Paint (INP):
  Measure: Latency of user interactions
  Target: <200ms

---

Measurement Tools:
  - Google PageSpeed Insights
  - Lighthouse (Chrome DevTools)
  - WebPageTest
  - New Relic
  - Datadog
  - GTmetrix
```

### 2. **Performance Analysis Process**

```python
# Conduct performance audit

class PerformanceAudit:
    def measure_performance(self, url):
        """Baseline measurements"""
        return {
            'desktop_metrics': self.run_lighthouse_desktop(url),
            'mobile_metrics': self.run_lighthouse_mobile(url),
            'field_data': self.get_field_data(url),  # Real user data
            'lab_data': self.run_synthetic_tests(url),  # Lab measurements
            'comparative': self.compare_to_competitors(url)
        }

    def identify_opportunities(self, metrics):
        """Find improvement areas"""
        opportunities = []

        if metrics['fcp'] > 1.8:
            opportunities.append({
                'issue': 'First Contentful Paint slow',
                'current': metrics['fcp'],
                'target': 1.8,
                'impact': 'High',
                'solutions': [
                    'Reduce CSS/JS for critical path',
                    'Preload critical fonts',
                    'Defer non-critical JavaScript'
                ]
            })

        if metrics['cls'] > 0.1:
            opportunities.append({
                'issue': 'Cumulative Layout Shift high',
                'current': metrics['cls'],
                'target': 0.1,
                'impact': 'High',
                'solutions': [
                    'Reserve space for dynamic content',
                    'Avoid inserting content above existing',
                    'Use transform for animations'
                ]
            })

        return sorted(opportunities, key=lambda x: x['impact'])

    def create_audit_report(self, metrics, opportunities):
        """Generate comprehensive report"""
        return {
            'overall_score': self.calculate_score(metrics),
            'current_metrics': metrics,
            'target_metrics': self.define_targets(metrics),
            'opportunities': opportunities,
            'quick_wins': self.identify_quick_wins(opportunities),
            'timeline': self.estimate_effort(opportunities),
            'recommendations': self.prioritize_recommendations(opportunities)
        }
```

### 3. **Optimization Strategies**

```yaml
Performance Optimization Roadmap:

Quick Wins (1-2 days):
  - Enable gzip compression
  - Minify CSS/JavaScript
  - Compress images (lossless)
  - Remove unused CSS
  - Defer non-critical JavaScript
  - Preload critical fonts

Medium Effort (1-2 weeks):
  - Implement lazy loading
  - Code splitting (split routes)
  - Service worker for caching
  - Image optimization (WebP, srcset)
  - Critical CSS extraction
  - HTTP/2 server push

Long-term (1-3 months):
  - Migrate to faster framework
  - Database query optimization
  - Content delivery optimization
  - Architecture refactor
  - CDN implementation
  - Build process optimization

---

Optimization Checklist:

Network:
  [ ] Gzip compression enabled
  [ ] Brotli compression enabled
  [ ] HTTP/2 enabled
  [ ] CDN configured
  [ ] Browser caching configured
  [ ] Asset fingerprinting

JavaScript:
  [ ] Code split by route
  [ ] Unused code removed
  [ ] Minified and mangled
  [ ] Source maps generated
  [ ] Deferred non-critical

CSS:
  [ ] Critical CSS extracted
  [ ] Unused CSS removed
  [ ] Minified
  [ ] Preloaded fonts
  [ ] WOFF2 format used

Images:
  [ ] Optimized and compressed
  [ ] WebP with fallback
  [ ] Responsive srcset
  [ ] Lazy loading
  [ ] SVG where possible
```

### 4. **Monitoring & Continuous Improvement**

```javascript
// Setup performance monitoring

class PerformanceMonitoring {
  setupMonitoring() {
    return {
      tools: [
        'Google Analytics (Web Vitals)',
        'Datadog or New Relic',
        'Sentry for errors',
        'Custom monitoring'
      ],
      metrics: [
        'LCP (Largest Contentful Paint)',
        'FID (First Input Delay)',
        'CLS (Cumulative Layout Shift)',
        'FCP (First Contentful Paint)',
        'TTI (Time to Interactive)'
      ],
      frequency: 'Real-time monitoring',
      alerts: {
        lcp_degradation: 'Alert if >3 seconds',
        fid_degradation: 'Alert if >200ms',
        cls_degradation: 'Alert if >0.2'
      }
    };
  }

  defineBaselines(metrics) {
    return {
      baseline: {
        lcp: metrics.lcp,
        fid: metrics.fid,
        cls: metrics.cls
      },
      targets: {
        lcp: metrics.lcp * 0.9,  // 10% improvement
        fid: metrics.fid * 0.8,
        cls: metrics.cls * 0.8
      },
      review_frequency: 'Weekly',
      improvement_tracking: 'Month-over-month trends'
    };
  }

  setupPerformanceBudget() {
    return {
      javascript: {
        target: '150KB gzipped',
        monitor: 'Every build',
        alert: 'If exceeds 160KB'
      },
      css: {
        target: '50KB gzipped',
        monitor: 'Every build',
        alert: 'If exceeds 55KB'
      },
      images: {
        target: '500KB total',
        monitor: 'Every deployment',
        alert: 'If exceeds 550KB'
      }
    };
  }
}
```

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

## Performance Tips

- Start with Lighthouse audit (free, in DevTools)
- Use WebPageTest for detailed analysis
- Test on 3G mobile to find real bottlenecks
- Prioritize LCP optimization first
- Create performance budget for teams
