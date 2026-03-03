---
name: user-persona-creation
description: >
  Create detailed user personas based on research and data. Develop realistic
  representations of target users to guide product decisions and ensure
  user-centered design.
---

# User Persona Creation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

User personas synthesize research into realistic user profiles that guide design, development, and marketing decisions.

## When to Use

- Starting product design
- Feature prioritization
- Marketing messaging
- User research synthesis
- Team alignment on users
- Journey mapping
- Success metrics definition

## Quick Start

Minimal working example:

```python
# Gather data for persona development

class PersonaResearch:
    def conduct_interviews(self, target_sample_size=12):
        """Interview target users"""
        interview_guide = {
            'demographics': [
                'Age, gender, location',
                'Job title, industry, company size',
                'Experience level, education',
                'Salary range, purchasing power'
            ],
            'goals': [
                'What are you trying to achieve?',
                'What's most important to you?',
                'What does success look like?'
            ],
            'pain_points': [
                'What frustrates you about current solutions?',
                'What takes too long or is complicated?',
                'What prevents you from achieving goals?'
            ],
            'behaviors': [
                'How do you currently solve this problem?',
                'What tools do you use?',
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Research & Data Collection](references/research-data-collection.md) | Research & Data Collection |
| [Persona Template](references/persona-template.md) | Persona Template |
| [Multiple Personas](references/multiple-personas.md) | Multiple Personas |
| [Using Personas](references/using-personas.md) | Using Personas |

## Best Practices

### ✅ DO

- Base personas on real research, not assumptions
- Include 2-3 primary personas
- Make personas specific and detailed
- Include direct user quotes
- Update personas based on new data
- Share personas across organization
- Use personas for all product decisions
- Include both goals and pain points
- Create personas for different user types
- Document research sources

### ❌ DON'T

- Create personas without research
- Create too many personas (>4 primary)
- Make personas too generic
- Ignore data in favor of assumptions
- Create personas, then forget them
- Use personas only for design
- Make personas unrealistically perfect
- Ignore secondary users
- Keep personas locked away
- Never update personas
