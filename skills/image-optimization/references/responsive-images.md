# Responsive Images

## Responsive Images

```html
<!-- Responsive image techniques -->

<!-- srcset: Let browser choose -->
<img
  src="image.jpg"
  srcset="small.jpg 480w, medium.jpg 768w, large.jpg 1200w"
  sizes="
    (max-width: 480px) 100vw,
    (max-width: 768px) 90vw,
    80vw
  "
  alt="Description"
/>

<!-- picture: Format selection -->
<picture>
  <source srcset="image.webp" type="image/webp" />
  <source srcset="image.jpg" type="image/jpeg" />
  <img src="image.jpg" alt="Description" />
</picture>

<!-- Lazy loading -->
<img src="placeholder.jpg" loading="lazy" alt="Description" />
```
