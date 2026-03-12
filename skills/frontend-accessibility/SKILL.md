---
name: frontend-accessibility
description: >
  Implement WCAG compliance using semantic HTML, ARIA, keyboard navigation, and
  screen reader support. Use when building inclusive applications for all users.
---

# Frontend Accessibility

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build accessible web applications following WCAG guidelines with semantic HTML, ARIA attributes, keyboard navigation, and screen reader support for inclusive user experiences.

## When to Use

- Compliance with accessibility standards
- Inclusive design requirements
- Screen reader support
- Keyboard navigation
- Color contrast issues

## Quick Start

Minimal working example:

```html
<!-- Good semantic structure -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<main>
  <article>
    <header>
      <h1>Article Title</h1>
      <time datetime="2024-01-15">January 15, 2024</time>
    </header>
    <p>Article content...</p>
  </article>

  <aside aria-label="Related articles">
    <h2>Related Articles</h2>
    <ul>
      <li><a href="/article1">Article 1</a></li>
      <li><a href="/article2">Article 2</a></li>
    </ul>
  </aside>
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Semantic HTML and ARIA](references/semantic-html-and-aria.md) | Semantic HTML and ARIA |
| [Keyboard Navigation](references/keyboard-navigation.md) | Keyboard Navigation |
| [Color Contrast and Visual Accessibility](references/color-contrast-and-visual-accessibility.md) | Color Contrast and Visual Accessibility |
| [Screen Reader Announcements](references/screen-reader-announcements.md) | Screen Reader Announcements |
| [Accessibility Testing](references/accessibility-testing.md) | Accessibility Testing |

## Best Practices

### ✅ DO

- Use semantic HTML elements (nav, main, article, button) before reaching for ARIA roles
- Ensure all interactive elements are keyboard-operable with visible focus indicators
- Maintain a minimum 4.5:1 color contrast ratio for normal text (WCAG AA)
- Provide text alternatives for all non-decorative images and meaningful icons
- Test with a screen reader (VoiceOver, NVDA) and keyboard-only navigation on every major feature
- Use aria-live regions to announce dynamic content changes to assistive technology

### ❌ DON'T

- Use div or span with onClick handlers instead of button or anchor elements
- Remove or hide the browser's default focus outline without providing a custom visible focus style
- Rely on color alone to convey meaning (e.g., red for error) — add text or icons as well
- Add aria-label or aria-describedby that duplicates already-visible text — it creates redundant announcements
