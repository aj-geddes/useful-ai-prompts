# CSS Grid Responsive Layout

## CSS Grid Responsive Layout

```css
/* 12-column grid system */
.grid-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 16px;
  padding: 16px;
}

.grid-item {
  grid-column: span 12;
  padding: 16px;
  background: white;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
}

/* Mobile: stacked */
.header {
  grid-column: span 12;
}
.sidebar {
  grid-column: span 12;
}
.main {
  grid-column: span 12;
}
.footer {
  grid-column: span 12;
}

/* Tablet: 2-column layout */
@media (min-width: 768px) {
  .header {
    grid-column: span 12;
  }
  .sidebar {
    grid-column: span 3;
  }
  .main {
    grid-column: span 9;
  }
  .footer {
    grid-column: span 12;
  }
}

/* Desktop: 3-column with sidebar */
@media (min-width: 1024px) {
  .header {
    grid-column: span 12;
  }
  .sidebar {
    grid-column: span 2;
  }
  .main {
    grid-column: span 8;
  }
  .aside {
    grid-column: span 2;
  }
  .footer {
    grid-column: span 12;
  }
}
```
