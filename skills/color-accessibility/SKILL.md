---
name: color-accessibility
description: >
  Design color palettes that are accessible to all users including those with
  color blindness. Ensure sufficient contrast, meaningful use of color, and
  inclusive design.
---

# Color Accessibility

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Accessible color design ensures all users, including those with color vision deficiency, can access and understand information.

## When to Use

- Creating color palettes
- Designing data visualizations
- Testing interface designs
- Status indicators and alerts
- Form validation states
- Charts and graphs

## Quick Start

Minimal working example:

```yaml
WCAG Contrast Ratios:

WCAG AA (Minimum):
  - Normal text: 4.5:1
  - Large text (18pt+): 3:1
  - UI components & graphical elements: 3:1
  - Focus indicators: 3:1

WCAG AAA (Enhanced):
  - Normal text: 7:1
  - Large text: 4.5:1
  - Better for accessibility

---
Testing Contrast:

Tools:
  - WebAIM Contrast Checker
  - Color Contrast Analyzer
  - Figma plugins
  - Browser DevTools

Formula (WCAG): Contrast = (L1 + 0.05) / (L2 + 0.05)
  Where L = relative luminance

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Color Contrast Standards](references/color-contrast-standards.md) | Color Contrast Standards |
| [Color Vision Deficiency Simulation](references/color-vision-deficiency-simulation.md) | Color Vision Deficiency Simulation |
| [Accessible Color Usage](references/accessible-color-usage.md) | Accessible Color Usage |
| [Testing & Validation](references/testing-validation.md) | Testing & Validation |

## Best Practices

### ✅ DO

- Ensure 4.5:1 contrast minimum (WCAG AA)
- Test with color blindness simulator
- Use patterns or icons with color
- Label states with text, not color alone
- Test with real users with color blindness
- Document color usage in design system
- Choose accessible color palettes
- Use sequential colors for ordered data
- Validate all color combinations
- Include focus indicators

### ❌ DON'T

- Use color alone to convey information
- Create low-contrast text
- Assume users see colors correctly
- Use red-green combinations
- Forget about focus states
- Mix too many colors (>5-8)
- Use pure red and pure green together
- Skip contrast testing
- Assume AA is sufficient (AAA better)
- Ignore color blindness in testing
