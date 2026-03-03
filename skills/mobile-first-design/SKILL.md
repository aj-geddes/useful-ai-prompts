---
name: mobile-first-design
description: >
  Design for mobile devices first, then scale up to larger screens. Create
  responsive interfaces that work seamlessly across all device sizes.
---

# Mobile-First Design

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Mobile-first design prioritizes small screens as the starting point, ensuring core functionality works on all devices while leveraging larger screens for enhanced experience.

## When to Use

- Web application design
- Responsive website creation
- Feature prioritization
- Performance optimization
- Progressive enhancement
- Cross-device experience design

## Quick Start

Minimal working example:

```yaml
Mobile-First Approach:

Step 1: Design for Mobile (320px - 480px)
  - Constrained space forces priorities
  - Focus on essential content and actions
  - Single column layout
  - Touch-friendly interactive elements

Step 2: Enhance for Tablet (768px - 1024px)
  - Add secondary content
  - Multi-column layouts possible
  - Optimize spacing and readability
  - Take advantage of hover states

Step 3: Optimize for Desktop (1200px+)
  - Full-featured experience
  - Advanced layouts
  - Rich interactions
  - Multiple columns and sidebars

---
## Responsive Breakpoints:

Mobile: 320px - 480px
  - iPhone SE, older phones
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Responsive Design Implementation](references/responsive-design-implementation.md) | Responsive Design Implementation |
| [Mobile Performance](references/mobile-performance.md) | Mobile Performance |
| [Progressive Enhancement](references/progressive-enhancement.md) | Progressive Enhancement |

## Best Practices

### ✅ DO

- Design for smallest screen first
- Test on real mobile devices
- Use responsive images
- Optimize for mobile performance
- Make touch targets 44x44px minimum
- Stack content vertically on mobile
- Use hamburger menu on mobile
- Hide non-essential content on mobile
- Test with slow networks
- Progressive enhancement approach

### ❌ DON'T

- Assume all mobile users have fast networks
- Use desktop-only patterns on mobile
- Ignore touch interaction needs
- Make buttons too small
- Forget about landscape orientation
- Over-complicate mobile layout
- Ignore mobile performance
- Assume no keyboard (iPad users)
- Skip mobile user testing
- Forget about notches and safe areas
