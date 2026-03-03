# Mobile Performance

## Mobile Performance

```yaml
Mobile Performance Optimization:

Image Optimization:
  - Responsive images (srcset, picture element)
  - WebP format with fallback
  - Lazy loading for below-fold
  - Compress ruthlessly
  - Serve appropriately sized images

Metric Goals:
  - Mobile: <3 second First Contentful Paint
  - Mobile: <4 second Largest Contentful Paint
  - Mobile: < 100 Cumulative Layout Shift

Bundle Size:
  - Mobile: <100KB JavaScript (gzipped)
  - Mobile: <50KB CSS (gzipped)
  - Critical CSS inline

Network:
  - Minimize requests (combine files)
  - Enable gzip compression
  - Use CDN for assets
  - Cache aggressively

---
Testing Devices:

Physical Devices:
  - iPhone SE (320px baseline)
  - iPhone 13 Pro (390px)
  - Samsung S21 (360px)
  - iPad (768px)

Emulation:
  - Chrome DevTools device mode
  - Responsive design mode
  - Test orientation changes

Real Device Testing:
  - Test on actual devices
  - Check touch interactions
  - Verify performance
  - Test with slow network
```
