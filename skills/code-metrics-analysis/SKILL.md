---
name: code-metrics-analysis
description: >
  Analyze code complexity, cyclomatic complexity, maintainability index, and
  code churn using metrics tools. Use when assessing code quality, identifying
  refactoring candidates, or monitoring technical debt.
---

# Code Metrics Analysis

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Measure and analyze code quality metrics to identify complexity, maintainability issues, and areas for improvement.

## When to Use

- Code quality assessment
- Identifying refactoring candidates
- Technical debt monitoring
- Code review automation
- CI/CD quality gates
- Team performance tracking
- Legacy code analysis

## Quick Start

Minimal working example:

```typescript
import * as ts from "typescript";
import * as fs from "fs";

interface ComplexityMetrics {
  cyclomaticComplexity: number;
  cognitiveComplexity: number;
  linesOfCode: number;
  functionCount: number;
  classCount: number;
  maxNestingDepth: number;
}

class CodeMetricsAnalyzer {
  analyzeFile(filePath: string): ComplexityMetrics {
    const sourceCode = fs.readFileSync(filePath, "utf-8");
    const sourceFile = ts.createSourceFile(
      filePath,
      sourceCode,
      ts.ScriptTarget.Latest,
      true,
    );

    const metrics: ComplexityMetrics = {
      cyclomaticComplexity: 0,
      cognitiveComplexity: 0,
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [TypeScript Complexity Analyzer](references/typescript-complexity-analyzer.md) | TypeScript Complexity Analyzer |
| [Python Code Metrics (using radon)](references/python-code-metrics-using-radon.md) | Python Code Metrics (using radon) |
| [ESLint Plugin for Complexity](references/eslint-plugin-for-complexity.md) | ESLint Plugin for Complexity |
| [CI/CD Quality Gates](references/cicd-quality-gates.md) | CI/CD Quality Gates |

## Best Practices

### ✅ DO

- Monitor metrics over time
- Set reasonable thresholds
- Focus on trends, not absolute numbers
- Automate metric collection
- Use metrics to guide refactoring
- Combine multiple metrics
- Include metrics in code reviews

### ❌ DON'T

- Use metrics as sole quality indicator
- Set unrealistic thresholds
- Ignore context and domain
- Punish developers for metrics
- Focus only on one metric
- Skip documentation
