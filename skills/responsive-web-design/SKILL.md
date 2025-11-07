---
name: responsive-web-design
description: Create responsive layouts using CSS Grid, Flexbox, media queries, and mobile-first design. Use when building adaptive interfaces that work across all devices.
---

# Responsive Web Design

## Overview

Build mobile-first responsive interfaces using modern CSS techniques including Flexbox, Grid, and media queries to create adaptable user experiences.

## When to Use

- Multi-device applications
- Mobile-first development
- Accessible layouts
- Flexible UI systems
- Cross-browser compatibility

## Implementation Examples

### 1. **Mobile-First Media Query Strategy**

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
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
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

### 2. **Flexbox Responsive Navigation**

```html
<!-- HTML -->
<nav class="navbar">
  <div class="navbar-brand">Logo</div>
  <button class="navbar-toggle" id="menuToggle">Menu</button>
  <ul class="navbar-menu" id="navMenu">
    <li><a href="#home">Home</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#services">Services</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>

<style>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background-color: #333;
  color: white;
}

.navbar-brand {
  font-size: 24px;
  font-weight: bold;
}

.navbar-toggle {
  display: block;
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 24px;
}

.navbar-menu {
  display: none;
  list-style: none;
  flex-direction: column;
  position: absolute;
  top: 60px;
  left: 0;
  right: 0;
  background-color: #222;
  padding: 16px;
  gap: 8px;
}

.navbar-menu.active {
  display: flex;
}

@media (min-width: 768px) {
  .navbar-toggle {
    display: none;
  }

  .navbar-menu {
    display: flex;
    flex-direction: row;
    position: static;
    background-color: transparent;
    padding: 0;
    gap: 32px;
  }
}

.navbar-menu a {
  color: white;
  text-decoration: none;
}
</style>
```

### 3. **CSS Grid Responsive Layout**

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
.header { grid-column: span 12; }
.sidebar { grid-column: span 12; }
.main { grid-column: span 12; }
.footer { grid-column: span 12; }

/* Tablet: 2-column layout */
@media (min-width: 768px) {
  .header { grid-column: span 12; }
  .sidebar { grid-column: span 3; }
  .main { grid-column: span 9; }
  .footer { grid-column: span 12; }
}

/* Desktop: 3-column with sidebar */
@media (min-width: 1024px) {
  .header { grid-column: span 12; }
  .sidebar { grid-column: span 2; }
  .main { grid-column: span 8; }
  .aside { grid-column: span 2; }
  .footer { grid-column: span 12; }
}
```

### 4. **Responsive Typography**

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

### 5. **Responsive Cards Component**

```html
<div class="card-grid">
  <div class="card">
    <img src="image.jpg" alt="Card image" class="card-image">
    <div class="card-content">
      <h3>Card Title</h3>
      <p>Card description goes here</p>
      <a href="#" class="card-link">Learn More</a>
    </div>
  </div>
</div>

<style>
.card-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
  padding: 16px;
}

@media (min-width: 640px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    padding: 20px;
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    padding: 24px;
  }
}

.card {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

.card-image {
  width: 100%;
  height: auto;
  aspect-ratio: 16/9;
  object-fit: cover;
}

.card-content {
  padding: 16px;
}

.card-content h3 {
  margin: 0 0 8px;
  font-size: 18px;
}

.card-content p {
  margin: 0 0 12px;
  color: #666;
  font-size: 14px;
}

.card-link {
  display: inline-block;
  color: #0066cc;
  text-decoration: none;
  font-weight: 500;
}
</style>
```

## Best Practices

- Start with mobile-first approach
- Use flexible units (%, em, rem)
- Implement CSS Grid and Flexbox
- Test on real devices
- Optimize images with srcset
- Use CSS media queries strategically
- Consider touch targets on mobile
- Provide readable text sizes
- Test accessibility at all sizes

## Resources

- [MDN CSS Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries)
- [CSS Flexbox Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout)
- [CSS Grid Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
