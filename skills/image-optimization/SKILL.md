---
name: image-optimization
description: >
  Optimize images for web to reduce file size without sacrificing quality. Use.
  Use when website optimization, responsive image implementation, performance improvement, or mobile experience enhancement.
  compression, modern formats, and responsive techniques for faster loading.
---

# Image Optimization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Images typically comprise 50% of page weight. Optimization dramatically improves performance, especially on mobile networks.

## When to Use

- Website optimization
- Responsive image implementation
- Performance improvement
- Mobile experience enhancement
- Before deployment

## Quick Start

Minimal working example:

```yaml
Format Selection:

JPEG:
  Best for: Photographs, complex images
  Compression: Lossy (quality 70-85)
  Size: ~50-70% reduction
  Tools: ImageMagick, TinyJPEG
  Command: convert image.jpg -quality 75 optimized.jpg

PNG:
  Best for: Icons, screenshots, transparent images
  Compression: Lossless
  Size: 10-30% reduction
  Tools: PNGQuant, OptiPNG
  Command: optipng -o3 image.png

WebP:
  Best for: Modern browsers (90% support)
  Compression: 25-35% better than JPEG/PNG
  Fallback: Use <picture> element
  Tools: cwebp
  Command: cwebp -q 75 image.jpg -o image.webp

SVG:
  Best for: Icons, logos, simple graphics
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Image Compression & Formats](references/image-compression-formats.md) | Image Compression & Formats |
| [Responsive Images](references/responsive-images.md) | Responsive Images |
| [Optimization Process](references/optimization-process.md) | Optimization Process |
| [Monitoring & Best Practices](references/monitoring-best-practices.md) | Monitoring & Best Practices |

## Best Practices

### ✅ DO

- Serve WebP/AVIF with `<picture>` fallbacks to JPEG/PNG for older browsers
- Use responsive `srcset` and `sizes` attributes so devices download only the resolution they need
- Lazy-load below-the-fold images with `loading="lazy"` or Intersection Observer
- Automate compression in the build pipeline (e.g., sharp, imagemin) so optimized assets are never skipped
- Set explicit `width` and `height` attributes or use CSS `aspect-ratio` to prevent Cumulative Layout Shift

### ❌ DON'T

- Serve uncompressed originals directly from a CMS or upload directory
- Use PNG for photographic content — JPEG or WebP will be a fraction of the size at comparable quality
- Resize images in CSS while delivering full-resolution files over the network
- Strip all EXIF metadata blindly — preserve copyright and orientation data when legally required
