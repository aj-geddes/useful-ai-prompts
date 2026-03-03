# Mobile-First Media Query Strategy

## Mobile-First Media Query Strategy

```css
/* Mobile styles (default) */
.container {
  display: flex;
  flex-direction: column;
  padding: 16px;
  gap: 16px;
}

.card {
  padding: 16px;
  border-radius: 8px;
  background: white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

/* Tablet (640px and up) */
@media (min-width: 640px) {
  .container {
    flex-direction: row;
    padding: 24px;
  }

  .grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .card {
    padding: 24px;
  }
}

/* Desktop (1024px and up) */
@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 32px;
  }

  .grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .card {
    padding: 32px;
  }
}

/* Large Desktop (1280px and up) */
@media (min-width: 1280px) {
  .container {
    max-width: 1400px;
  }

  .grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
  }
}
```
