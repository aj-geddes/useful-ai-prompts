---
name: web-performance-optimization
description: Optimize web application performance using code splitting, lazy loading, caching, compression, and monitoring. Use when improving Core Web Vitals and user experience.
---

# Web Performance Optimization

## Overview

Implement performance optimization strategies including lazy loading, code splitting, caching, compression, and monitoring to improve Core Web Vitals and user experience.

## When to Use

- Slow page load times
- High Largest Contentful Paint (LCP)
- Large bundle sizes
- Frequent Cumulative Layout Shift (CLS)
- Mobile performance issues

## Implementation Examples

### 1. **Code Splitting and Lazy Loading (React)**

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
    path: '/users',
    lazy: lazyLoad(import('./pages/Users'))
  }
];

// App.tsx with Suspense
import { Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

export const App = () => {
  return (
    <BrowserRouter>
      <Suspense fallback={<LoadingSpinner />}>
        <Routes>
          {routes.map(route => (
            <Route key={route.path} path={route.path} element={<route.lazy />} />
          ))}
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
};

// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 10
        },
        common: {
          minChunks: 2,
          priority: 5,
          reuseExistingChunk: true
        }
      }
    }
  }
};
```

### 2. **Image Optimization**

```html
<!-- Picture element with srcset for responsive images -->
<picture>
  <source media="(min-width: 1024px)" srcset="image-large.jpg, image-large@2x.jpg 2x" />
  <source media="(min-width: 640px)" srcset="image-medium.jpg, image-medium@2x.jpg 2x" />
  <source srcset="image-small.jpg, image-small@2x.jpg 2x" />
  <img src="image-fallback.jpg" alt="Description" loading="lazy" />
</picture>

<!-- WebP format with fallback -->
<picture>
  <source srcset="image.webp" type="image/webp" />
  <img src="image.jpg" alt="Description" loading="lazy" />
</picture>

<!-- TypeScript Image Component -->
<script lang="typescript">
interface ImageProps {
  src: string;
  alt: string;
  width: number;
  height: number;
  sizes?: string;
  loading?: 'lazy' | 'eager';
}

const OptimizedImage: React.FC<ImageProps> = ({
  src,
  alt,
  width,
  height,
  sizes = '100vw',
  loading = 'lazy'
}) => {
  const webpSrc = src.replace(/\.(jpg|png)$/, '.webp');

  return (
    <picture>
      <source srcSet={webpSrc} type="image/webp" />
      <img
        src={src}
        alt={alt}
        width={width}
        height={height}
        sizes={sizes}
        loading={loading}
        decoding="async"
      />
    </picture>
  );
};
</script>
```

### 3. **HTTP Caching and Service Workers**

```typescript
// service-worker.ts
const CACHE_NAME = 'v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/css/style.css',
  '/js/app.js'
];

self.addEventListener('install', (event: ExtendableEvent) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
});

self.addEventListener('fetch', (event: FetchEvent) => {
  // Cache first, fall back to network
  event.respondWith(
    caches.match(event.request).then(response => {
      if (response) return response;

      return fetch(event.request).then(response => {
        // Clone the response
        const cloned = response.clone();

        // Cache successful responses
        if (response.status === 200) {
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, cloned);
          });
        }

        return response;
      }).catch(() => {
        // Return offline page if available
        return caches.match('/offline.html');
      });
    })
  );
});

// Register service worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/service-worker.js')
      .catch(err => console.error('SW registration failed:', err));
  });
}
```

### 4. **Gzip Compression and Asset Optimization**

```javascript
// webpack.config.js with compression
const CompressionPlugin = require('compression-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
  mode: 'production',
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: {
            drop_console: true
          }
        }
      })
    ]
  },
  plugins: [
    new CompressionPlugin({
      algorithm: 'gzip',
      test: /\.(js|css|html|svg)$/,
      threshold: 8192,
      minRatio: 0.8
    })
  ]
};

// .htaccess (Apache)
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/javascript application/javascript
</IfModule>

# nginx.conf
gzip on;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
gzip_min_length 1000;
gzip_proxied any;
```

### 5. **Performance Monitoring**

```typescript
// utils/performanceMonitor.ts
interface PerformanceMetrics {
  fcp: number;  // First Contentful Paint
  lcp: number;  // Largest Contentful Paint
  cls: number;  // Cumulative Layout Shift
  fid: number;  // First Input Delay
  ttfb: number; // Time to First Byte
}

export const observeWebVitals = (callback: (metrics: Partial<PerformanceMetrics>) => void) => {
  const metrics: Partial<PerformanceMetrics> = {};

  // LCP
  const lcpObserver = new PerformanceObserver((list) => {
    const entries = list.getEntries();
    const lastEntry = entries[entries.length - 1];
    metrics.lcp = lastEntry.renderTime || lastEntry.loadTime;
    callback(metrics);
  });

  try {
    lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
  } catch (e) {
    console.warn('LCP observer not supported');
  }

  // CLS
  const clsObserver = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
      if (!(entry as any).hadRecentInput) {
        metrics.cls = (metrics.cls || 0) + (entry as any).value;
        callback(metrics);
      }
    }
  });

  try {
    clsObserver.observe({ entryTypes: ['layout-shift'] });
  } catch (e) {
    console.warn('CLS observer not supported');
  }

  // FID via INP
  const inputObserver = new PerformanceObserver((list) => {
    const entries = list.getEntries();
    const firstEntry = entries[0];
    metrics.fid = firstEntry.processingDuration;
    callback(metrics);
  });

  try {
    inputObserver.observe({ entryTypes: ['first-input', 'event'] });
  } catch (e) {
    console.warn('FID observer not supported');
  }

  // TTFB
  const navigationTiming = performance.getEntriesByType('navigation')[0];
  if (navigationTiming) {
    metrics.ttfb = (navigationTiming as any).responseStart - (navigationTiming as any).requestStart;
    callback(metrics);
  }
};

// Usage
observeWebVitals((metrics) => {
  console.log('Performance metrics:', metrics);
  // Send to analytics
  fetch('/api/metrics', {
    method: 'POST',
    body: JSON.stringify(metrics)
  });
});

// Chrome DevTools Protocol for performance testing
import puppeteer from 'puppeteer';

async function measurePagePerformance(url: string) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto(url, { waitUntil: 'networkidle2' });

  const metrics = JSON.parse(
    await page.evaluate(() => JSON.stringify(window.performance))
  );

  console.log('Page Load Time:', metrics.timing.loadEventEnd - metrics.timing.navigationStart);
  console.log('DOM Content Loaded:', metrics.timing.domContentLoadedEventEnd - metrics.timing.navigationStart);

  await browser.close();
}
```

## Best Practices

- Minimize bundle size with code splitting
- Optimize images with appropriate formats
- Implement lazy loading strategically
- Use HTTP caching headers
- Enable gzip/brotli compression
- Monitor Core Web Vitals continuously
- Implement service workers
- Defer non-critical JavaScript
- Optimize critical rendering path
- Test on real devices and networks

## Resources

- [Web Vitals](https://web.dev/vitals/)
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [WebPageTest](https://www.webpagetest.org/)
- [Performance API](https://developer.mozilla.org/en-US/docs/Web/API/Performance)
