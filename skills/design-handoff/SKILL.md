---
name: design-handoff
description: >
  Prepare designs for development handoff. Document specifications,
  interactions, and assets to enable efficient development and maintain design
  quality.
---

# Design Handoff

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Design handoff bridges design and development, ensuring developers have all information needed to implement designs accurately and efficiently.

## When to Use

- Before development starts
- Feature completion in design
- Component library updates
- Design system changes
- Iterative refinement handoff

## Quick Start

Minimal working example:

```yaml
Design Handoff Package:

Overview:
  - Feature description
  - User flows
  - Key interactions
  - Platform (web, iOS, Android)

Screens & Components:
  - All screen designs
  - Responsive variants (mobile, tablet, desktop)
  - All component states (default, hover, focus, disabled, error)
  - Dark mode variants (if applicable)

Specifications:
  - Typography (font, size, weight, line-height)
  - Spacing & layout (padding, margin, gaps)
  - Colors (hex values, opacity)
  - Shadows & elevations
  - Border radius
  - Animations & transitions

Interactions:
  - Click/tap behaviors
  - Hover states
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Developer-Friendly Documentation](references/developer-friendly-documentation.md) | Developer-Friendly Documentation |
| [Handoff Checklist](references/handoff-checklist.md) | Handoff Checklist |
| [Design-Dev Collaboration](references/design-dev-collaboration.md) | Design-Dev Collaboration |

## Best Practices

### ✅ DO

- Create comprehensive documentation
- Export all assets and specifications
- Document every component state
- Include responsive variants
- Explain design decisions
- Provide developer-friendly specs
- Use shared design tools
- Schedule kickoff meeting
- Make yourself available for questions
- Review implementations and iterate

### ❌ DON'T

- Expect developers to guess
- Leave responsive design to chance
- Skip edge case documentation
- Use unclear specifications
- Disappear after handoff
- Change designs mid-development without notification
- Provide images instead of vector files
- Ignore technical constraints
- Miss performance considerations
- Skip accessibility in handoff
