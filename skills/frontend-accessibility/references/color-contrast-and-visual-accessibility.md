# Color Contrast and Visual Accessibility

## Color Contrast and Visual Accessibility

```css
/* Proper color contrast (WCAG AA: 4.5:1 for text, 3:1 for large text) */
:root {
  --color-text: #1a1a1a; /* Black - high contrast */
  --color-background: #ffffff;
  --color-primary: #0066cc; /* Blue with good contrast */
  --color-success: #008000; /* Not pure green */
  --color-error: #d32f2f; /* Not pure red */
  --color-warning: #ff8c00; /* Not yellow */
}

body {
  color: var(--color-text);
  background-color: var(--color-background);
  font-size: 16px;
  line-height: 1.5;
}

a {
  color: var(--color-primary);
  text-decoration: underline; /* Don't rely on color alone */
}

button {
  min-height: 44px; /* Touch target size */
  min-width: 44px;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

/* Focus visible for keyboard navigation */
button:focus-visible,
a:focus-visible,
input:focus-visible {
  outline: 3px solid var(--color-primary);
  outline-offset: 2px;
}

/* High contrast mode support */
@media (prefers-contrast: more) {
  body {
    font-weight: 500;
  }

  button {
    border: 2px solid currentColor;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #e0e0e0;
    --color-background: #1a1a1a;
    --color-primary: #6495ed;
  }
}
```
