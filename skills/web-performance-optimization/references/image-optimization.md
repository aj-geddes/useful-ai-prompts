# Image Optimization

## Image Optimization

```html
<!-- Picture element with srcset for responsive images -->
<picture>
  <source
    media="(min-width: 1024px)"
    srcset="image-large.jpg, image-large@2x.jpg 2x"
  />
  <source
    media="(min-width: 640px)"
    srcset="image-medium.jpg, image-medium@2x.jpg 2x"
  />
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
    loading?: "lazy" | "eager";
  }

  const OptimizedImage: React.FC<ImageProps> = ({
    src,
    alt,
    width,
    height,
    sizes = "100vw",
    loading = "lazy",
  }) => {
    const webpSrc = src.replace(/\.(jpg|png)$/, ".webp");

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
