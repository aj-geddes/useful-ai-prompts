# Optimization Techniques

## Optimization Techniques

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
