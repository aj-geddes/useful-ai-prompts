---
name: user-research-analysis
description: >
  Analyze user research data to uncover insights, identify patterns, and inform
  design decisions. Synthesize qualitative and quantitative research into
  actionable recommendations.
---

# User Research Analysis

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Effective research analysis transforms raw data into actionable insights that guide product development and design.

## When to Use

- Synthesis of user interviews and surveys
- Identifying patterns and themes
- Validating design assumptions
- Prioritizing user needs
- Communicating insights to stakeholders
- Informing design decisions

## Quick Start

Minimal working example:

```python
# Analyze qualitative and quantitative data

class ResearchAnalysis:
    def synthesize_interviews(self, interviews):
        """Extract themes and insights from interviews"""
        return {
            'interviews_analyzed': len(interviews),
            'methodology': 'Thematic coding and affinity mapping',
            'themes': self.identify_themes(interviews),
            'quotes': self.extract_key_quotes(interviews),
            'pain_points': self.identify_pain_points(interviews),
            'opportunities': self.identify_opportunities(interviews)
        }

    def identify_themes(self, interviews):
        """Find recurring patterns across interviews"""
        themes = {}
        theme_frequency = {}

        for interview in interviews:
            for statement in interview['statements']:
                theme = self.categorize_statement(statement)
                theme_frequency[theme] = theme_frequency.get(theme, 0) + 1

        # Sort by frequency
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Research Synthesis Methods](references/research-synthesis-methods.md) | Research Synthesis Methods |
| [Affinity Mapping](references/affinity-mapping.md) | Affinity Mapping |
| [Insight Documentation](references/insight-documentation.md) | Insight Documentation |
| [Research Validation Matrix](references/research-validation-matrix.md) | Research Validation Matrix |

## Best Practices

### ✅ DO

- Use multiple research methods
- Triangulate findings across sources
- Document quotes and evidence
- Look for patterns and frequency
- Separate findings from interpretation
- Validate findings with users
- Share insights across team
- Connect to design decisions
- Document methodology
- Iterate research approach based on learnings

### ❌ DON'T

- Over-interpret small samples
- Ignore conflicting data
- Base decisions on single data point
- Skip documentation
- Cherry-pick quotes that support assumptions
- Present without supporting evidence
- Forget to note limitations
- Analyze without involving participants
- Create insights without actionable recommendations
- Let research sit unused
