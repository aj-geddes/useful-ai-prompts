# Monitoring & Best Practices

## Monitoring & Best Practices

```yaml
Performance Targets:

Hero Image: <200KB
Thumbnail: <30KB
Icon: <5KB
Total images: <500KB
Target gzipped: <300KB

Tools:
  - ImageOptim (Mac)
  - ImageMagick (CLI)
  - TinyJPEG/TinyPNG (web)
  - Squoosh (web)
  - Lighthouse (audit)

Checklist:
  [ ] All images optimized
  [ ] WebP with fallback
  [ ] Responsive srcset
  [ ] Lazy loading implemented
  [ ] Correct format per image
  [ ] File size <100KB each
  [ ] Benchmarks established
  [ ] Monitoring in place
  [ ] Documented process

Tips:
  - Optimize before uploading
  - Use CDN with image optimization
  - Consider Image CDN (Imgix, Cloudinary)
  - Batch process during build
  - Monitor image additions
  - Test real devices on 3G
```
