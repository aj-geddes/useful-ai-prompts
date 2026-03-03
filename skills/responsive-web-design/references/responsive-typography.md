# Responsive Typography

## Responsive Typography

```css
/* Fluid typography */
html {
  font-size: 16px;
}

h1 {
  font-size: clamp(24px, 8vw, 48px);
  line-height: 1.2;
}

h2 {
  font-size: clamp(20px, 5vw, 36px);
  line-height: 1.3;
}

p {
  font-size: clamp(14px, 2vw, 18px);
  line-height: 1.6;
  max-width: 65ch;
}

/* Responsive spacing */
.container {
  padding: clamp(16px, 5vw, 48px);
  margin-left: auto;
  margin-right: auto;
  width: 90%;
  max-width: 1200px;
}

/* Responsive images */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

picture {
  display: block;
}
```
