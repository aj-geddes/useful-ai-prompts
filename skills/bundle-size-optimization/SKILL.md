---
name: bundle-size-optimization
description: Reduce JavaScript and CSS bundle sizes through code splitting, tree shaking, and optimization techniques. Improve load times and overall application performance.
---

# Bundle Size Optimization

## Overview

Smaller bundles download faster, parse faster, and execute faster, dramatically improving perceived performance especially on slower networks.

## When to Use

- Build process optimization
- Bundle analysis before deployment
- Performance baseline improvement
- Mobile performance focus
- After adding new dependencies

## Instructions

### 1. **Bundle Analysis**

```javascript
// Analyze bundle composition

class BundleAnalysis {
  analyzeBundle() {
    return {
      tools: [
        'webpack-bundle-analyzer',
        'Source Map Explorer',
        'Bundle Buddy',
        'Bundlephobia'
      ],
      metrics: {
        total_size: '850KB gzipped',
        main_js: '450KB',
        main_css: '120KB',
        vendor: '250KB',
        largest_lib: 'moment.js (67KB)'
      },
      breakdown: {
        react: '85KB (10%)',
        lodash: '45KB (5%)',
        moment: '67KB (8%)',
        other: '653KB (77%)'
      }
    };
  }

  identifyOpportunities(bundle) {
    const opportunities = [];

    // Check for duplicate dependencies
    if (bundle.duplicates.length > 0) {
      opportunities.push({
        issue: 'Duplicate dependencies',
        impact: '50KB reduction possible',
        solution: 'Deduplicate packages'
      });
    }

    // Check for unused packages
    if (bundle.unused.length > 0) {
      opportunities.push({
        issue: 'Unused dependencies',
        impact: '100KB reduction',
        solution: 'Remove unused packages'
      });
    }

    // Check bundle size vs targets
    if (bundle.gzipped > 250) {
      opportunities.push({
        issue: 'Bundle too large',
        impact: 'Exceeds target',
        solution: 'Code splitting or tree shaking'
      });
    }

    return opportunities;
  }
}
```

### 2. **Optimization Techniques**

```yaml
Code Splitting:
  Route-based: Split by route (each route ~50-100KB)
  Component-based: Split large components
  Library splitting: Separate vendor bundles
  Tools: webpack, dynamic imports, React.lazy()

Tree Shaking:
  Remove unused exports
  Enable in webpack/rollup
  Works best with ES modules
  Check: bundle-analyzer shows unused

Minification:
  JavaScript: Terser, esbuild
  CSS: cssnano, clean-css
  Results: 20-30% reduction typical
  Examples: 100KB → 70KB

Remove Dependencies:
  Moment.js (67KB) → date-fns (13KB)
  Lodash (70KB) → lodash-es (30KB, can tree-shake)
  Old packages check: npm outdated

Dynamic Imports:
  import('module') loads on-demand
  Reduces initial bundle
  Used for: Modals, off-screen features
  Example: 850KB → 400KB initial + lazy

---

Bundle Size Targets:

JavaScript:
  Initial: <150KB gzipped
  Per route: <50KB gzipped
  Total: <300KB gzipped

CSS:
  Initial: <50KB gzipped
  Per page: <20KB gzipped

Images:
  Total: <500KB optimized
  Per image: <100KB
```

### 3. **Implementation Strategy**

```yaml
Optimization Plan:

Week 1: Analysis & Quick Wins
  - Run bundle analyzer
  - Remove unused dependencies
  - Update large libraries
  - Enable tree shaking
  - Expected: 20% reduction

Week 2: Code Splitting
  - Implement route-based splitting
  - Lazy load heavy components
  - Split vendor bundles
  - Expected: 40% reduction from initial

Week 3: Advanced Optimization
  - Remove unused polyfills
  - Upgrade transpiler
  - Optimize images in bundle
  - Expected: 50-60% total reduction

---

Monitoring:

Setup Budget:
  - Track bundle size in CI/CD
  - Alert if exceeds threshold
  - Track per commit
  - Historical trending

Tools:
  - bundlesize npm package
  - webpack-bundle-analyzer
  - GitHub checks integration

Process:
  - Measure before
  - Implement changes
  - Measure after
  - Document findings
```

### 4. **Best Practices**

- Monitor bundle size regularly (every build)
- Set strict bundle budgets for teams
- Use modern syntax (don't polyfill all browsers)
- Prefer lighter alternatives to heavy libraries
- Lazy load non-critical code
- Keep vendors separate for better caching
- Remove unused dependencies (npm audit)
- Use production build for measurements
- Test on real 3G network simulation

## Checklist

- [ ] Bundle analyzer installed and configured
- [ ] Unused dependencies removed
- [ ] Code splitting implemented
- [ ] Tree shaking enabled
- [ ] Bundle budget set in CI/CD
- [ ] Large libraries replaced with lighter alternatives
- [ ] Dynamic imports for large features
- [ ] Vendor bundles separated
- [ ] Assets optimized
- [ ] Performance baseline established

## Tips

- Focus on initial bundle first (affects load time most)
- Measure gzipped size (what users receive)
- Tree shaking works best with ES modules only
- Most libraries have lighter alternatives
- Use webpack/vite analyze tools built-in
