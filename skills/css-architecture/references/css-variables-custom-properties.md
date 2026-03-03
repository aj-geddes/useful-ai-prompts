# CSS Variables (Custom Properties)

## CSS Variables (Custom Properties)

```css
/* Root variables */
:root {
  /* Colors */
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-danger: #dc3545;
  --color-success: #28a745;
  --color-warning: #ffc107;
  --color-text: #333;
  --color-background: #fff;
  --color-border: #e0e0e0;

  /* Typography */
  --font-family-base:
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-size-base: 16px;
  --font-size-lg: 18px;
  --font-size-sm: 14px;
  --line-height-base: 1.6;

  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 2px 4px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 4px 8px rgba(0, 0, 0, 0.15);

  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
}

/* Dark theme override */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #e0e0e0;
    --color-background: #1e1e1e;
    --color-border: #333;
  }
}

/* Usage */
.button {
  background-color: var(--color-primary);
  color: white;
  padding: var(--spacing-md) var(--spacing-lg);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  font-family: var(--font-family-base);
  font-size: var(--font-size-base);
  line-height: var(--line-height-base);
}

.card {
  background-color: var(--color-background);
  color: var(--color-text);
  border: 1px solid var(--color-border);
  padding: var(--spacing-lg);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
}
```
