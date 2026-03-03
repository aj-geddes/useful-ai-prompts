# Optimization Process

## Optimization Process

```yaml
Workflow:

1. Preparation
  - Export at correct size (don't scale in HTML)
  - Use appropriate format
  - Batch process similar images

2. Compression
  - Lossy: TinyJPEG/TinyPNG
  - Lossless: ImageMagick
  - Target: <100KB for main images
  - Thumbnails: <20KB

3. Format Conversion
  - WebP with JPEG fallback
  - Consider PNG for transparency
  - SVG for scalable graphics

4. Implementation
  - Use srcset for responsive
  - Lazy load below-fold
  - Optimize critical images first
  - Monitor file sizes in CI/CD

5. Validation
  - Check file sizes in DevTools
  - Test on slow networks
  - Verify quality acceptable
  - Measure performance impact

---

Quick Wins:

Remove EXIF data (saves 20-50KB):
  identify -verbose image.jpg | grep -i exif
  convert image.jpg -strip image-clean.jpg

Convert to WebP (25-35% smaller):
  cwebp -q 75 *.jpg

Batch compress with ImageMagick:
  mogrify -quality 75 -resize 1920x1080 *.jpg

Expected Results:
  - Homepage: 850KB → 300KB images
  - Performance: 3s → 1.5s load time
  - Mobile: Significant improvement on 3G
```
