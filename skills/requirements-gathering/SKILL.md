---
name: requirements-gathering
description: >
  Systematically collect, document, and validate requirements from stakeholders.
  Ensure clarity, completeness, and agreement before development begins to
  reduce scope creep and rework.
---

# Requirements Gathering

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Effective requirements gathering establishes a shared understanding of what will be built, preventing misalignment and expensive changes later in the project.

## When to Use

- Project kickoff and planning
- Feature development initiation
- Product roadmap planning
- System modernization projects
- Customer discovery
- Stakeholder alignment sessions
- Writing user stories and acceptance criteria

## Quick Start

Minimal working example:

```python
# Identify and analyze stakeholders

class StakeholderDiscovery:
    STAKEHOLDER_CATEGORIES = [
        'End Users',
        'Business Owners',
        'Technical Leads',
        'Operations/Support',
        'Customers',
        'Regulatory Bodies',
        'Integration Partners'
    ]

    def identify_stakeholders(self, project):
        """Map all stakeholder groups"""
        return {
            'primary': self.get_primary_stakeholders(project),
            'secondary': self.get_secondary_stakeholders(project),
            'tertiary': self.get_tertiary_stakeholders(project),
            'total_to_engage': self.calculate_engagement_strategy(project)
        }

    def analyze_stakeholder_needs(self, stakeholder):
        """Understand what each stakeholder needs"""
        return {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Stakeholder Discovery](references/stakeholder-discovery.md) | Stakeholder Discovery |
| [Requirements Elicitation Techniques](references/requirements-elicitation-techniques.md) | Requirements Elicitation Techniques |
| [Requirements Documentation](references/requirements-documentation.md) | Requirements Documentation |
| [Requirement Validation & Sign-Off](references/requirement-validation-sign-off.md) | Requirement Validation & Sign-Off |
| [Requirements Traceability Matrix](references/requirements-traceability-matrix.md) | Requirements Traceability Matrix |

## Best Practices

### ✅ DO

- Engage all key stakeholders early
- Document requirements in writing
- Use specific, measurable language
- Define acceptance criteria
- Prioritize using MoSCoW method
- Get stakeholder sign-off
- Create traceability matrix
- Review requirements regularly
- Distinguish must-haves from nice-to-haves
- Document assumptions and constraints

### ❌ DON'T

- Rely on memory or verbal agreements
- Create requirements without stakeholder input
- Use ambiguous language (quickly, easily, etc.)
- Skip non-functional requirements
- Ignore constraints and dependencies
- Over-document trivial details
- Rush through requirements phase
- Build without stakeholder agreement
- Make scope changes without process
- Forget about edge cases and error conditions
