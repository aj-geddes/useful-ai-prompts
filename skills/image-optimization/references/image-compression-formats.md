# Image Compression & Formats

## Image Compression & Formats

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
  Compression: Minify XML
  Scalable: Works at any size
  Tools: SVGO
  Command: svgo image.svg --output optimized.svg

---
Compression Levels:

Conservative (95% quality):
  JPEG: 85-90 quality
  PNG: Lossless
  Use: High-value images

Moderate (90% quality):
  JPEG: 75-80 quality
  PNG: Quantized to 256 colors
  Use: General images

Aggressive (80% quality):
  JPEG: 60-70 quality
  PNG: Reduced colors
  Use: Thumbnails, backgrounds
```
