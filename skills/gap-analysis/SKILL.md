---
name: gap-analysis
description: >
  Identify differences between current state and desired future state. Analyze
  gaps in capabilities, processes, skills, and technology to plan improvements
  and investments.
---

# Gap Analysis

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Gap analysis systematically compares current capabilities with desired future state, revealing what needs to change and what investments are required.

## When to Use

- Strategic planning and goal setting
- Technology modernization assessment
- Process improvement initiatives
- Skills and training planning
- System evaluation and selection
- Organizational change planning
- Capability building programs

## Quick Start

Minimal working example:

```python
# Systematic gap identification

class GapAnalysis:
    GAP_CATEGORIES = {
        'Business Capability': 'Functions organization can perform',
        'Process': 'How work gets done',
        'Technology': 'Tools and systems available',
        'Skills': 'Knowledge and expertise',
        'Data': 'Information available',
        'People/Culture': 'Team composition and mindset',
        'Organization': 'Structure and roles',
        'Metrics': 'Ability to measure performance'
    }

    def identify_gaps(self, current_state, future_state):
        """Compare current vs desired and find gaps"""
        gaps = []

        for capability in future_state['capabilities']:
            current_capability = self.find_capability(
                capability['name'],
                current_state['capabilities']
            )

            if current_capability is None:
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Gap Identification Framework](references/gap-identification-framework.md) | Gap Identification Framework |
| [Gap Analysis Template](references/gap-analysis-template.md) | Gap Analysis Template |
| [Gap Closure Planning](references/gap-closure-planning.md) | Gap Closure Planning |
| [Communication & Tracking](references/communication-tracking.md) | Communication & Tracking |

## Best Practices

### ✅ DO

- Compare current to clearly defined future state
- Include all relevant capability areas
- Involve stakeholders in gap identification
- Prioritize by value and effort
- Create detailed closure plans
- Track progress to closure
- Document gap analysis findings
- Review and update analysis quarterly
- Link gaps to business strategy
- Communicate findings transparently

### ❌ DON'T

- Skip current state assessment
- Create vague future state
- Identify gaps without solutions
- Ignore implementation effort
- Plan all gaps in parallel
- Forget about dependencies
- Ignore resource constraints
- Hide difficult findings
- Plan for 100% effort allocation
- Forget about change management
