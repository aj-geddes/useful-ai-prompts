---
name: web-performance-optimization
description: >
  Optimize web application performance using code splitting, lazy loading,
  caching, compression, and monitoring. Use when improving Core Web Vitals and
  user experience.
---

# Web Performance Optimization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement performance optimization strategies including lazy loading, code splitting, caching, compression, and monitoring to improve Core Web Vitals and user experience.

## When to Use

- Slow page load times
- High Largest Contentful Paint (LCP)
- Large bundle sizes
- Frequent Cumulative Layout Shift (CLS)
- Mobile performance issues

## Quick Start

Minimal working example:

```typescript
// utils/lazyLoad.ts
import React from 'react';

export const lazyLoad = (importStatement: Promise<any>) => {
  return React.lazy(() =>
    importStatement.then(module => ({
      default: module.default
    }))
  );
};

// routes.tsx
import { lazyLoad } from './utils/lazyLoad';

export const routes = [
  {
    path: '/',
    component: () => import('./pages/Home'),
    lazy: lazyLoad(import('./pages/Home'))
  },
  {
    path: '/dashboard',
    lazy: lazyLoad(import('./pages/Dashboard'))
  },
  {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Code Splitting and Lazy Loading (React)](references/code-splitting-and-lazy-loading-react.md) | Code Splitting and Lazy Loading (React) |
| [Image Optimization](references/image-optimization.md) | Image Optimization |
| [HTTP Caching and Service Workers](references/http-caching-and-service-workers.md) | HTTP Caching and Service Workers |
| [Gzip Compression and Asset Optimization](references/gzip-compression-and-asset-optimization.md) | Gzip Compression and Asset Optimization |
| [Performance Monitoring](references/performance-monitoring.md) | Performance Monitoring |

## Best Practices

### ✅ DO

- Measure Core Web Vitals (LCP, FID/INP, CLS) before and after every optimization to confirm impact
- Code-split routes and heavy components with dynamic `import()` to reduce initial bundle size
- Serve images in modern formats (WebP/AVIF) with proper `width`/`height` attributes to prevent layout shift
- Enable gzip or Brotli compression for text-based assets and set long-lived `Cache-Control` headers for static files
- Use `<link rel="preload">` for critical fonts and above-the-fold images; use `<link rel="preconnect">` for third-party origins
- Lazy-load below-the-fold images and iframes with `loading="lazy"` or Intersection Observer

### ❌ DON'T

- Load third-party scripts synchronously in the `<head>` — use `async` or `defer` attributes
- Optimize based on Lighthouse scores alone without checking real-user metrics (RUM data)
- Inline large CSS or JS blocks that defeat caching — extract them into cacheable files
- Ignore Cumulative Layout Shift caused by ads, dynamically injected content, or web fonts without `font-display`
