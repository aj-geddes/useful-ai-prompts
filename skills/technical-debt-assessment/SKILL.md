---
name: technical-debt-assessment
description: Assess, quantify, and prioritize technical debt using code analysis, metrics, and impact analysis. Use when planning refactoring, evaluating codebases, or making architectural decisions.
---

# Technical Debt Assessment

## Overview

Systematically identify, measure, and manage technical debt to make informed decisions about code quality investments.

## When to Use

- Legacy code evaluation
- Refactoring prioritization
- Sprint planning
- Code quality initiatives
- Acquisition due diligence
- Architectural decisions

## Implementation Examples

### 1. **Technical Debt Calculator**

```typescript
interface DebtItem {
  id: string;
  title: string;
  description: string;
  category: 'code' | 'architecture' | 'test' | 'documentation' | 'security';
  severity: 'low' | 'medium' | 'high' | 'critical';
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
      critical: 4
    };

    const priority =
      (item.impact * 10 + item.interest * 5 + severityWeight[item.severity] * 3) /
      (item.effort + 1);

    return priority;
  }

  getPrioritizedList(): Array<DebtItem & { priority: number }> {
    return this.items
      .map(item => ({
        ...item,
        priority: this.calculatePriority(item)
      }))
      .sort((a, b) => b.priority - a.priority);
  }

  getDebtByCategory(): Record<string, DebtItem[]> {
    return this.items.reduce((acc, item) => {
      acc[item.category] = acc[item.category] || [];
      acc[item.category].push(item);
      return acc;
    }, {} as Record<string, DebtItem[]>);
  }

  getTotalEffort(): number {
    return this.items.reduce((sum, item) => sum + item.effort, 0);
  }

  getTotalInterest(): number {
    return this.items.reduce((sum, item) => sum + item.interest, 0);
  }

  generateReport(): string {
    const prioritized = this.getPrioritizedList();
    const byCategory = this.getDebtByCategory();

    let report = '# Technical Debt Assessment\n\n';

    // Summary
    report += '## Summary\n\n';
    report += `- Total Items: ${this.items.length}\n`;
    report += `- Total Effort: ${this.getTotalEffort()} hours\n`;
    report += `- Monthly Interest: ${this.getTotalInterest()} hours\n\n`;

    // By Category
    report += '## By Category\n\n';
    for (const [category, items] of Object.entries(byCategory)) {
      const effort = items.reduce((sum, item) => sum + item.effort, 0);
      report += `- ${category}: ${items.length} items (${effort} hours)\n`;
    }
    report += '\n';

    // Top Priority Items
    report += '## Top Priority Items\n\n';
    for (const item of prioritized.slice(0, 10)) {
      report += `### ${item.title} (Priority: ${item.priority.toFixed(2)})\n`;
      report += `- Category: ${item.category}\n`;
      report += `- Severity: ${item.severity}\n`;
      report += `- Effort: ${item.effort} hours\n`;
      report += `- Impact: ${item.impact}/10\n`;
      report += `- Interest: ${item.interest} hours/sprint\n`;
      report += `\n${item.description}\n\n`;
    }

    return report;
  }
}

// Usage
const assessment = new TechnicalDebtAssessment();

assessment.addDebtItem({
  id: 'debt-1',
  title: 'Legacy API endpoints',
  description: 'Old API v1 endpoints still in use, need migration',
  category: 'architecture',
  severity: 'high',
  effort: 40,
  impact: 8,
  interest: 5
});

assessment.addDebtItem({
  id: 'debt-2',
  title: 'Missing unit tests',
  description: '30% of codebase lacks test coverage',
  category: 'test',
  severity: 'medium',
  effort: 80,
  impact: 7,
  interest: 3
});

console.log(assessment.generateReport());
```

### 2. **Code Quality Scanner**

```typescript
import * as ts from 'typescript';
import * as fs from 'fs';

interface QualityIssue {
  file: string;
  line: number;
  issue: string;
  severity: 'info' | 'warning' | 'error';
  debtHours: number;
}

class CodeQualityScanner {
  private issues: QualityIssue[] = [];

  scanProject(directory: string): QualityIssue[] {
    this.issues = [];

    const files = this.getTypeScriptFiles(directory);

    for (const file of files) {
      this.scanFile(file);
    }

    return this.issues;
  }

  private scanFile(filePath: string): void {
    const sourceCode = fs.readFileSync(filePath, 'utf-8');
    const sourceFile = ts.createSourceFile(
      filePath,
      sourceCode,
      ts.ScriptTarget.Latest,
      true
    );

    // Check for anti-patterns
    this.checkForAnyTypes(sourceFile, filePath);
    this.checkForLongFunctions(sourceFile, filePath);
    this.checkForMagicNumbers(sourceFile, filePath);
    this.checkForConsoleStatements(sourceFile, filePath);
    this.checkForTodoComments(sourceFile, filePath);
  }

  private checkForAnyTypes(sourceFile: ts.SourceFile, filePath: string): void {
    const visit = (node: ts.Node) => {
      if (ts.isTypeReferenceNode(node) && node.typeName.getText() === 'any') {
        const { line } = ts.getLineAndCharacterOfPosition(
          sourceFile,
          node.getStart()
        );

        this.issues.push({
          file: filePath,
          line: line + 1,
          issue: 'Use of any type reduces type safety',
          severity: 'warning',
          debtHours: 0.5
        });
      }

      ts.forEachChild(node, visit);
    };

    visit(sourceFile);
  }

  private checkForLongFunctions(sourceFile: ts.SourceFile, filePath: string): void {
    const visit = (node: ts.Node) => {
      if (ts.isFunctionDeclaration(node) || ts.isMethodDeclaration(node)) {
        if (node.body) {
          const lines = node.body.getFullText().split('\n').length;

          if (lines > 50) {
            const { line } = ts.getLineAndCharacterOfPosition(
              sourceFile,
              node.getStart()
            );

            this.issues.push({
              file: filePath,
              line: line + 1,
              issue: `Function has ${lines} lines, should be refactored`,
              severity: 'warning',
              debtHours: Math.ceil(lines / 10)
            });
          }
        }
      }

      ts.forEachChild(node, visit);
    };

    visit(sourceFile);
  }

  private checkForMagicNumbers(sourceFile: ts.SourceFile, filePath: string): void {
    const visit = (node: ts.Node) => {
      if (ts.isNumericLiteral(node)) {
        const value = parseFloat(node.text);

        // Ignore common constants
        if (![0, 1, -1, 2].includes(value)) {
          const { line } = ts.getLineAndCharacterOfPosition(
            sourceFile,
            node.getStart()
          );

          this.issues.push({
            file: filePath,
            line: line + 1,
            issue: `Magic number ${value} should be a named constant`,
            severity: 'info',
            debtHours: 0.1
          });
        }
      }

      ts.forEachChild(node, visit);
    };

    visit(sourceFile);
  }

  private checkForConsoleStatements(sourceFile: ts.SourceFile, filePath: string): void {
    const text = sourceFile.getFullText();
    const lines = text.split('\n');

    lines.forEach((line, index) => {
      if (line.includes('console.log') || line.includes('console.error')) {
        this.issues.push({
          file: filePath,
          line: index + 1,
          issue: 'Console statement should use proper logger',
          severity: 'info',
          debtHours: 0.1
        });
      }
    });
  }

  private checkForTodoComments(sourceFile: ts.SourceFile, filePath: string): void {
    const text = sourceFile.getFullText();
    const lines = text.split('\n');

    lines.forEach((line, index) => {
      if (/\/\/\s*TODO/.test(line)) {
        this.issues.push({
          file: filePath,
          line: index + 1,
          issue: 'TODO comment indicates incomplete work',
          severity: 'warning',
          debtHours: 2
        });
      }
    });
  }

  private getTypeScriptFiles(dir: string): string[] {
    // Implementation
    return [];
  }

  getTotalDebt(): number {
    return this.issues.reduce((sum, issue) => sum + issue.debtHours, 0);
  }

  generateReport(): string {
    let report = '# Code Quality Report\n\n';

    const bySeverity = this.issues.reduce((acc, issue) => {
      acc[issue.severity] = acc[issue.severity] || [];
      acc[issue.severity].push(issue);
      return acc;
    }, {} as Record<string, QualityIssue[]>);

    report += `## Summary\n\n`;
    report += `- Total Issues: ${this.issues.length}\n`;
    report += `- Estimated Debt: ${this.getTotalDebt()} hours\n\n`;

    for (const [severity, issues] of Object.entries(bySeverity)) {
      report += `### ${severity.toUpperCase()} (${issues.length})\n\n`;

      for (const issue of issues.slice(0, 10)) {
        report += `- ${issue.file}:${issue.line} - ${issue.issue}\n`;
      }

      report += '\n';
    }

    return report;
  }
}
```

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

## Debt Categories

- **Code Quality**: Complex code, duplicates
- **Architecture**: Poor design, tight coupling
- **Testing**: Missing tests, flaky tests
- **Documentation**: Missing docs, outdated
- **Security**: Vulnerabilities, outdated deps
- **Performance**: Inefficient code, N+1 queries

## Resources

- [Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html)
- [SonarQube](https://www.sonarqube.org/)
- [Code Climate](https://codeclimate.com/)
