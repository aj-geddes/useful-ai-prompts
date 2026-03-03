---
name: image-optimization
description: >
  Optimize images for web to reduce file size without sacrificing quality. Use
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

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
