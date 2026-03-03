---
name: responsive-web-design
description: >
  Create responsive layouts using CSS Grid, Flexbox, media queries, and
  mobile-first design. Use when building adaptive interfaces that work across
  all devices.
---

# Responsive Web Design

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build mobile-first responsive interfaces using modern CSS techniques including Flexbox, Grid, and media queries to create adaptable user experiences.

## When to Use

- Multi-device applications
- Mobile-first development
- Accessible layouts
- Flexible UI systems
- Cross-browser compatibility

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Mobile-First Media Query Strategy](references/mobile-first-media-query-strategy.md) | Mobile-First Media Query Strategy |
| [Flexbox Responsive Navigation](references/flexbox-responsive-navigation.md) | Flexbox Responsive Navigation |
| [CSS Grid Responsive Layout](references/css-grid-responsive-layout.md) | CSS Grid Responsive Layout |
| [Responsive Typography](references/responsive-typography.md) | Responsive Typography |
| [Responsive Cards Component](references/responsive-cards-component.md) | Responsive Cards Component |

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
