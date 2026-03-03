---
name: accessibility-compliance
description: >
  Implement WCAG 2.1/2.2 accessibility standards, screen reader compatibility,
  keyboard navigation, and a11y testing. Use when building inclusive web
  applications, ensuring regulatory compliance, or improving user experience for
  people with disabilities.
---

# Accessibility Compliance

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive accessibility features following WCAG guidelines to ensure your application is usable by everyone, including people with disabilities.

## When to Use

- Building public-facing web applications
- Ensuring WCAG 2.1/2.2 AA or AAA compliance
- Supporting screen readers (NVDA, JAWS, VoiceOver)
- Implementing keyboard-only navigation
- Meeting ADA, Section 508, or similar regulations
- Improving SEO and overall user experience
- Conducting accessibility audits

## Quick Start

Minimal working example:

```html
<!-- Bad: Non-semantic markup -->
<div class="button" onclick="submit()">Submit</div>

<!-- Good: Semantic HTML -->
<button type="submit" aria-label="Submit form">Submit</button>

<!-- Custom components with proper ARIA -->
<div
  role="button"
  tabindex="0"
  aria-pressed="false"
  onclick="toggle()"
  onkeydown="handleKeyPress(event)"
>
  Toggle Feature
</div>

<!-- Form with proper labels and error handling -->
<form>
  <label for="email">Email Address</label>
  <input
    id="email"
    type="email"
    name="email"
    aria-required="true"
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Semantic HTML with ARIA](references/semantic-html-with-aria.md) | Semantic HTML with ARIA |
| [React Component with Accessibility](references/react-component-with-accessibility.md) | React Component with Accessibility |
| [Keyboard Navigation Handler](references/keyboard-navigation-handler.md) | Keyboard Navigation Handler |
| [Color Contrast Validator](references/color-contrast-validator.md) | Color Contrast Validator |
| [Screen Reader Announcements](references/screen-reader-announcements.md) | Screen Reader Announcements |
| [Focus Management](references/focus-management.md) | Focus Management |

## Best Practices

### ✅ DO

- Use semantic HTML elements
- Provide text alternatives for images
- Ensure sufficient color contrast (4.5:1 minimum)
- Support keyboard navigation
- Implement focus management
- Test with screen readers
- Use ARIA attributes correctly
- Provide skip links
- Make forms accessible with labels
- Support text resizing up to 200%

### ❌ DON'T

- Rely solely on color to convey information
- Remove focus indicators
- Use only mouse/touch interactions
- Auto-play media without controls
- Create keyboard traps
- Use positive tabindex values
- Override user preferences
- Hide content only visually that should be hidden from screen readers
