---
name: design-system-creation
description: Build comprehensive design systems with components, patterns, and guidelines. Enable consistent design, faster development, and better collaboration across teams.
---

# Design System Creation

## Overview

A design system is a structured set of components, guidelines, and principles that ensure consistency, accelerate development, and improve product quality.

## When to Use

- Multiple product interfaces or teams
- Scaling design consistency
- Reducing redundant component development
- Improving design-to-dev handoff
- Creating shared language across teams
- Building reusable components
- Documenting design standards

## Instructions

### 1. **Design System Components**

```yaml
Design System Structure:

Foundation Layer:
  Typography:
    - Typefaces (Roboto, Inter)
    - Font sizes (scale: 12, 14, 16, 20, 28, 36, 48)
    - Font weights (Regular, Medium, Bold)
    - Line heights and letter spacing

Colors:
    - Primary brand color (#2196F3)
    - Secondary colors
    - Neutral palette (grays)
    - Semantic colors (success, error, warning)
    - Dark mode variants

Spacing:
    - Base unit: 4px
    - Scale: 4, 8, 12, 16, 24, 32, 48, 64px
    - Apply consistently across UI

Shadows & Elevation:
    - Elevation 0 (flat)
    - Elevation 1, 2, 4, 8, 16 (increasing depth)
    - Used for modals, cards, overlays

---

Component Layer:

Basic Components:
  - Button (primary, secondary, outline, disabled states)
  - Input fields (text, password, number, email)
  - Dropdown / Select
  - Checkbox & Radio buttons
  - Toggle switch
  - Textarea

Form Components:
  - Form group (label + input + error)
  - Error messages
  - Help text
  - Required indicators
  - Validation states

Navigation:
  - Breadcrumbs
  - Tabs
  - Navigation drawer
  - Pagination
  - Stepper

Feedback:
  - Toast notifications
  - Modal dialogs
  - Alerts
  - Loading indicators
  - Progress bars

Data Display:
  - Tables
  - Lists
  - Cards
  - Badges
  - Chips

---

Pattern Layer:

Layout Patterns:
  - Main layout (header + nav + content + footer)
  - Two-column (main + sidebar)
  - Form layouts
  - Grid layouts

Content Patterns:
  - Empty states
  - Loading states
  - Error states
  - Confirmation dialogs
  - Onboarding flows

Interaction Patterns:
  - Hover states
  - Focus states
  - Disabled states
  - Transitions/animations
  - Keyboard navigation
```

### 2. **Component Documentation**

```python
# Document each component thoroughly

class ComponentDocumentation:
    def create_component_doc(self, component):
        """Document complete component"""
        return {
            'name': component.name,
            'description': component.description,
            'usage': component.when_to_use,
            'anatomy': {
                'elements': component.sub_elements,
                'diagram': 'Show with labels'
            },
            'properties': {
                'size': ['Small', 'Medium', 'Large'],
                'variant': component.variants,
                'state': ['Default', 'Hover', 'Focus', 'Disabled'],
                'disabled': True/False,
                'required': True/False
            },
            'code_examples': [
                'React example',
                'CSS example',
                'HTML example'
            ],
            'accessibility': {
                'aria_roles': component.aria_roles,
                'keyboard_support': component.keyboard_behavior,
                'screen_reader': component.sr_text
            },
            'do_dont': {
                'do': ['Guideline 1', 'Guideline 2'],
                'dont': ['Guideline 1', 'Guideline 2']
            }
        }

    def create_live_component_library(self):
        """Build interactive component showcase"""
        return {
            'tool': 'Storybook / Zeroheight',
            'features': [
                'Live component preview',
                'Interactive controls',
                'Code examples',
                'Documentation',
                'Version history'
            ],
            'coverage': 'All components with all variants'
        }
```

### 3. **Design System Governance**

```yaml
Design System Governance:

Ownership:
  Owner: Design System Lead
  Committee: 1 Designer, 1 Developer, 1 Product Manager
  Review Frequency: Biweekly
  Approval Process: Committee sign-off required

Component Lifecycle:

Proposed:
  - Submitted by team
  - Reviewed for duplication
  - Assessed for scope

In Review:
  - Design review
  - Accessibility audit
  - Developer implementation review
  - 1-2 week review period

Approved:
  - Documented in system
  - Available in component library
  - Semver version bump
  - Teams notified

Deprecated:
  - Clear timeline for migration
  - Updated component provided
  - Support period: 2 major versions

Retired:
  - Removed from library
  - Historical documentation archived

---

Contribution Guidelines:

To Add Component:
  1. Check existing components
  2. Submit RFC (Request for Comments)
  3. Attend design review
  4. Implement per standards
  5. Get committee approval
  6. Document in library
  7. Release in new version

Standards:
  - Accessibility (WCAG 2.1 AA minimum)
  - Mobile-first responsive design
  - Dark mode support
  - Internationalization (i18n)
  - Performance (<100kb added to bundle)
```

### 4. **Design System Documentation**

```yaml
Documentation Structure:

Getting Started:
  - What is the design system?
  - How to use in your project
  - Installation instructions
  - Quick start guide

Foundations:
  - Color system
  - Typography scale
  - Spacing/grid system
  - Icons
  - Accessibility standards

Components:
  - [Detailed component docs]

Patterns:
  - Common layouts
  - Content patterns
  - Interaction patterns
  - Form patterns

Guidelines:
  - Voice & tone
  - Imagery & photography
  - Brand identity
  - Copy guidelines

Use Cases:
  - Real-world examples
  - Case studies
  - Do's and don'ts

Updates:
  - Release notes
  - Migration guides
  - Roadmap
  - Contribution process
```

## Best Practices

### ✅ DO
- Start with essential components
- Document every component thoroughly
- Include code examples
- Test components across browsers
- Include accessibility guidance
- Version the design system
- Have clear governance
- Communicate updates proactively
- Gather feedback from users
- Maintain incrementally

### ❌ DON'T
- Create too many components initially
- Skip documentation
- Ignore accessibility
- Make breaking changes without migration path
- Allow inconsistent implementations
- Ignore user feedback
- Let design system stagnate
- Create components without proven need
- Make components too prescriptive
- Ignore performance impact

## Design System Tips

- Start with colors, typography, spacing
- Build most-used components first
- Use Storybook or similar for documentation
- Version using semantic versioning
- Establish clear contribution process
