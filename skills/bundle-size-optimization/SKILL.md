---
name: bundle-size-optimization
description: >
  Reduce JavaScript and CSS bundle sizes through code splitting, tree shaking,
  and optimization techniques. Improve load times and overall application.
  Use when build process optimization, bundle analysis before deployment, performance baseline improvement, or mobile performance focus.
  performance.
---

# Bundle Size Optimization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Smaller bundles download faster, parse faster, and execute faster, dramatically improving perceived performance especially on slower networks.

## When to Use

- Build process optimization
- Bundle analysis before deployment
- Performance baseline improvement
- Mobile performance focus
- After adding new dependencies

## Quick Start

Minimal working example:

```javascript
// Analyze bundle composition

class BundleAnalysis {
  analyzeBundle() {
    return {
      tools: [
        "webpack-bundle-analyzer",
        "Source Map Explorer",
        "Bundle Buddy",
        "Bundlephobia",
      ],
      metrics: {
        total_size: "850KB gzipped",
        main_js: "450KB",
        main_css: "120KB",
        vendor: "250KB",
        largest_lib: "moment.js (67KB)",
      },
      breakdown: {
        react: "85KB (10%)",
        lodash: "45KB (5%)",
        moment: "67KB (8%)",
        other: "653KB (77%)",
      },
    };
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Bundle Analysis](references/bundle-analysis.md) | Bundle Analysis |
| [Optimization Techniques](references/optimization-techniques.md) | Optimization Techniques |
| [Implementation Strategy](references/implementation-strategy.md) | Implementation Strategy |
| [Best Practices](references/best-practices.md) | Best Practices |

## Best Practices

### ✅ DO

- Run `webpack-bundle-analyzer` or `source-map-explorer` before and after changes to measure impact
- Use dynamic `import()` for routes and heavy components to enable code splitting
- Prefer tree-shakeable ESM imports (`import { debounce } from 'lodash-es'`) over default/namespace imports
- Replace large libraries with lighter alternatives (e.g., `date-fns` instead of `moment.js`)
- Set a bundle size budget in CI and fail the build when it's exceeded
- Enable scope hoisting and minification in production builds

### ❌ DON'T

- Import entire libraries when you only use a few functions (`import _ from 'lodash'`)
- Add polyfills for APIs already supported by your browser target matrix
- Include development-only code (source maps, verbose logging) in production bundles
- Optimize blindly — always measure first to focus effort on the largest chunks
