---
name: technical-debt-assessment
description: >
  Assess, quantify, and prioritize technical debt using code analysis, metrics,
  and impact analysis. Use when planning refactoring, evaluating codebases, or
  making architectural decisions.
---

# Technical Debt Assessment

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Systematically identify, measure, and manage technical debt to make informed decisions about code quality investments.

## When to Use

- Legacy code evaluation
- Refactoring prioritization
- Sprint planning
- Code quality initiatives
- Acquisition due diligence
- Architectural decisions

## Quick Start

Minimal working example:

```typescript
interface DebtItem {
  id: string;
  title: string;
  description: string;
  category: "code" | "architecture" | "test" | "documentation" | "security";
  severity: "low" | "medium" | "high" | "critical";
  effort: number; // hours
  impact: number; // 1-10 scale
  interest: number; // cost per sprint if not fixed
}

class TechnicalDebtAssessment {
  private items: DebtItem[] = [];

  addDebtItem(item: DebtItem): void {
    this.items.push(item);
  }

  calculatePriority(item: DebtItem): number {
    const severityWeight = {
      low: 1,
      medium: 2,
      high: 3,
      critical: 4,
    };
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Technical Debt Calculator](references/technical-debt-calculator.md) | Technical Debt Calculator |
| [Code Quality Scanner](references/code-quality-scanner.md) | Code Quality Scanner |

## Best Practices

### ✅ DO

- Quantify debt impact
- Prioritize by ROI
- Track debt over time
- Include debt in sprints
- Document debt decisions
- Set quality gates

### ❌ DON'T

- Ignore technical debt
- Fix everything at once
- Skip impact analysis
- Make emotional decisions
