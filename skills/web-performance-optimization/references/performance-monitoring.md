# Performance Monitoring

## Performance Monitoring

```typescript
// utils/performanceMonitor.ts
interface PerformanceMetrics {
  fcp: number; // First Contentful Paint
  lcp: number; // Largest Contentful Paint
  cls: number; // Cumulative Layout Shift
  fid: number; // First Input Delay
  ttfb: number; // Time to First Byte
}

export const observeWebVitals = (
  callback: (metrics: Partial<PerformanceMetrics>) => void,
) => {
  const metrics: Partial<PerformanceMetrics> = {};

  // LCP
  const lcpObserver = new PerformanceObserver((list) => {
    const entries = list.getEntries();
    const lastEntry = entries[entries.length - 1];
    metrics.lcp = lastEntry.renderTime || lastEntry.loadTime;
    callback(metrics);
  });

  try {
    lcpObserver.observe({ entryTypes: ["largest-contentful-paint"] });
  } catch (e) {
    console.warn("LCP observer not supported");
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
    clsObserver.observe({ entryTypes: ["layout-shift"] });
  } catch (e) {
    console.warn("CLS observer not supported");
  }

  // FID via INP
  const inputObserver = new PerformanceObserver((list) => {
    const entries = list.getEntries();
    const firstEntry = entries[0];
    metrics.fid = firstEntry.processingDuration;
    callback(metrics);
  });

  try {
    inputObserver.observe({ entryTypes: ["first-input", "event"] });
  } catch (e) {
    console.warn("FID observer not supported");
  }

  // TTFB
  const navigationTiming = performance.getEntriesByType("navigation")[0];
  if (navigationTiming) {
    metrics.ttfb =
      (navigationTiming as any).responseStart -
      (navigationTiming as any).requestStart;
    callback(metrics);
  }
};

// Usage
observeWebVitals((metrics) => {
  console.log("Performance metrics:", metrics);
  // Send to analytics
  fetch("/api/metrics", {
    method: "POST",
    body: JSON.stringify(metrics),
  });
});

// Chrome DevTools Protocol for performance testing
import puppeteer from "puppeteer";

async function measurePagePerformance(url: string) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto(url, { waitUntil: "networkidle2" });

  const metrics = JSON.parse(
    await page.evaluate(() => JSON.stringify(window.performance)),
  );

  console.log(
    "Page Load Time:",
    metrics.timing.loadEventEnd - metrics.timing.navigationStart,
  );
  console.log(
    "DOM Content Loaded:",
    metrics.timing.domContentLoadedEventEnd - metrics.timing.navigationStart,
  );

  await browser.close();
}
```
