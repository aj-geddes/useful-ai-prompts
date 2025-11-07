---
name: wireframe-prototyping
description: Create wireframes and interactive prototypes to visualize user interfaces and gather feedback early. Use tools and techniques to communicate design ideas before development.
---

# Wireframe Prototyping

## Overview

Wireframes and prototypes bridge the gap between ideas and implementation, enabling teams to test concepts, get feedback, and refine designs before costly development.

## When to Use

- Early concept validation
- Stakeholder alignment
- User testing and feedback
- Developer handoff
- Feature exploration
- UX problem-solving
- Rapid iteration

## Instructions

### 1. **Wireframing Fundamentals**

```yaml
Wireframe Principles:

Low Fidelity (Sketches):
  Tools: Paper, whiteboard, Balsamiq
  Time: 30 minutes - 2 hours
  Detail: Basic layout, no colors/fonts
  Best For: Brainstorming, exploration
  Cost: Free

Medium Fidelity:
  Tools: Figma, Sketch, Adobe XD
  Time: 2-8 hours
  Detail: Layout, content, basic interaction
  Best For: Team alignment, feedback
  Cost: Low

High Fidelity:
  Tools: Figma, Framer, web dev tools
  Time: 8+ hours
  Detail: Visual design, interactions, animations
  Best For: Developer handoff, user testing
  Cost: Medium

---

## Wireframe Components

Header:
  - Logo/branding
  - Navigation menu
  - Search bar (if applicable)
  - User account menu

Main Content:
  - Hero section or headline
  - Primary content area
  - Call-to-action buttons
  - Supporting information

Sidebar (if applicable):
  - Secondary navigation
  - Filters
  - Related content

Footer:
  - Footer links
  - Copyright
  - Social media

---

## Layout Patterns

Grid Systems:
  - 12-column grid (most flexible)
  - 8-column for mobile
  - Consistent spacing

Responsive Breakpoints:
  - Mobile: 320px - 480px
  - Tablet: 768px - 1024px
  - Desktop: 1200px+

Common Layouts:
  - Hero + Features
  - Two-column with sidebar
  - Three-column grid
  - Masonry/card layout
```

### 2. **Prototyping Tools & Techniques**

```python
# Create interactive prototypes

class PrototypeFramework:
    TOOLS = {
        'Figma': {
            'fidelity': 'Medium-High',
            'interactivity': 'Full',
            'collaboration': 'Real-time',
            'cost': 'Free-$30/month'
        },
        'Framer': {
            'fidelity': 'High',
            'interactivity': 'Advanced',
            'collaboration': 'Limited',
            'cost': '$12+/month'
        },
        'Adobe XD': {
            'fidelity': 'High',
            'interactivity': 'Full',
            'collaboration': 'Good',
            'cost': '$20/month'
        }
    }

    def create_prototype_flow(self):
        """Define user interaction flows"""
        return {
            'screens': [
                {'name': 'Login', 'interactions': ['Email input', 'Password input', 'Submit button']},
                {'name': 'Dashboard', 'interactions': ['View projects', 'Create new', 'Search']},
                {'name': 'Project Detail', 'interactions': ['View tasks', 'Edit project', 'Share']}
            ],
            'flows': [
                {'from': 'Login', 'to': 'Dashboard', 'trigger': 'Valid credentials'},
                {'from': 'Dashboard', 'to': 'Project Detail', 'trigger': 'Click project'},
                {'from': 'Project Detail', 'to': 'Dashboard', 'trigger': 'Back button'}
            ]
        }

    def define_interactions(self, screen):
        """Map user interactions"""
        return {
            'screen': screen,
            'interactions': [
                {
                    'element': 'Submit button',
                    'trigger': 'Click',
                    'action': 'Validate form and submit'
                },
                {
                    'element': 'Email field',
                    'trigger': 'Focus',
                    'action': 'Show placeholder, hint text'
                }
            ]
        }

    def test_prototype(self, prototype):
        """Gather feedback on prototype"""
        return {
            'testing_method': 'Unmoderated user testing',
            'participants': 5,
            'duration': '30 minutes each',
            'tasks': [
                'Complete user registration',
                'Create first project',
                'Invite team member'
            ],
            'metrics': [
                'Task completion rate',
                'Time to complete',
                'Error rate',
                'User satisfaction'
            ]
        }
```

### 3. **Wireframe Examples**

```yaml
Example: E-commerce Product Page

Header:
  [Logo] [Search bar] [Cart] [Account]

Hero Section:
  [Product image] [Price] [Add to cart] [Reviews: 4.5★]

Product Details:
  Description | Specs | Size guide

Product Images:
  [Main] [Thumb1] [Thumb2] [Thumb3]

Related Products:
  [Product card] [Product card] [Product card]

Footer:
  Contact | FAQ | Returns | Shipping info
```

### 4. **Prototype Testing**

```yaml
Testing Plan:

Objective: Validate primary user flows and UX clarity

Test Method: Unmoderated remote testing

Participants:
  - 5 representative users
  - Mix of experience levels
  - Similar to target persona

Tasks:
  1. Register a new account
  2. Create your first project
  3. Invite a team member
  4. Edit project settings

Success Criteria:
  - 80%+ task completion rate
  - Average time <5 min per task
  - SUS score >70
  - No critical usability issues

Feedback Areas:
  - Navigation clarity
  - Button placement
  - Form fields
  - Visual hierarchy
  - Error handling

Analysis:
  - Top 3 friction points
  - User quotes
  - Design recommendations
```

## Best Practices

### ✅ DO
- Start with low-fidelity sketches
- Get feedback early and often
- Test with real users
- Iterate based on feedback
- Use consistent grids and spacing
- Document interaction flows
- Include edge cases (empty states, errors)
- Create mobile-first wireframes
- Share prototypes for collaboration
- Keep wireframes simple and focused

### ❌ DON'T
- Jump directly to high-fidelity
- Over-design before validation
- Ignore mobile/responsive needs
- Create wireframes without user input
- Leave interactions undefined
- Make wireframes too detailed
- Test only with team members
- Ignore accessibility
- Lock into designs too early
- Create unrealistic user flows

## Wireframing Tips

- Use wireframe grids for consistency
- Name screens clearly and consistently
- Show all states (empty, loading, error)
- Include labels and descriptions
- Use annotations for complex interactions
