---
name: interaction-design
description: >
  Design meaningful interactions and microinteractions. Create delightful user
  experiences through thoughtful animation, feedback, and responsive interface
  design.
---

# Interaction Design

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Interaction design focuses on how users engage with systems, creating intuitive and delightful experiences through feedback and responsiveness.

## When to Use

- Designing user flows and touchpoints
- Creating animations and transitions
- Defining error and loading states
- Building microinteractions
- Improving usability and feedback
- Mobile interaction patterns

## Quick Start

Minimal working example:

```yaml
Common Interaction Patterns:

Swipe:
  Use: Mobile lists, carousels
  Feedback: Visual sliding, momentum
  Accessibility: Keyboard alternative (arrows)

Tap & Hold:
  Use: Context menus, drag prep
  Feedback: Visual feedback after delay
  Duration: ~500ms before trigger

Pinch & Zoom:
  Use: Image viewing, maps
  Feedback: Smooth zoom animation
  Boundaries: Set min/max zoom levels

Drag & Drop:
  Use: Reordering, moving items
  Feedback: Visual during drag, drop confirmation
  Fallback: Alternative method (buttons)

Double Tap:
  Use: Zoom, favorite, select
  Feedback: Immediate visual response
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Animation & Transition Design](references/animation-transition-design.md) | Animation & Transition Design |
| [Error Handling & Feedback](references/error-handling-feedback.md) | Error Handling & Feedback |
| [Accessibility in Interactions](references/accessibility-in-interactions.md) | Accessibility in Interactions |

## Best Practices

### ✅ DO

- Keep animations under 400ms
- Provide clear visual feedback
- Use animations to guide attention
- Respect motion preferences
- Make interactions reversible
- Test with keyboard and screen readers
- Provide multiple interaction methods
- Design for touch and mouse
- Use appropriate easing curves
- Document interaction behavior

### ❌ DON'T

- Animate for decoration only
- Use animations longer than 500ms
- Ignore motion-sensitive users
- Remove focus indicators
- Trap users in modals
- Use confusing animations
- Animate everything
- Ignore loading states
- Forget error states
- Skip accessibility testing
