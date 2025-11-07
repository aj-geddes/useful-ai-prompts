---
name: code-metrics-analysis
description: Analyze code complexity, cyclomatic complexity, maintainability index, and code churn using metrics tools. Use when assessing code quality, identifying refactoring candidates, or monitoring technical debt.
---

# Code Metrics Analysis

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

## Key Metrics

| Metric | Description | Good Range |
|--------|-------------|-----------|
| **Cyclomatic Complexity** | Number of linearly independent paths | 1-10 |
| **Cognitive Complexity** | Measure of code understandability | <15 |
| **Lines of Code** | Total lines (LOC) | Function: <50 |
| **Maintainability Index** | Overall maintainability score | >65 |
| **Code Churn** | Frequency of changes | Low |
| **Test Coverage** | Percentage covered by tests | >80% |

## Implementation Examples

### 1. **TypeScript Complexity Analyzer**

```typescript
import * as ts from 'typescript';
import * as fs from 'fs';

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
    const sourceCode = fs.readFileSync(filePath, 'utf-8');
    const sourceFile = ts.createSourceFile(
      filePath,
      sourceCode,
      ts.ScriptTarget.Latest,
      true
    );

    const metrics: ComplexityMetrics = {
      cyclomaticComplexity: 0,
      cognitiveComplexity: 0,
      linesOfCode: sourceCode.split('\n').length,
      functionCount: 0,
      classCount: 0,
      maxNestingDepth: 0
    };

    this.visit(sourceFile, metrics);

    return metrics;
  }

  private visit(node: ts.Node, metrics: ComplexityMetrics, depth: number = 0): void {
    metrics.maxNestingDepth = Math.max(metrics.maxNestingDepth, depth);

    // Count functions
    if (
      ts.isFunctionDeclaration(node) ||
      ts.isMethodDeclaration(node) ||
      ts.isArrowFunction(node)
    ) {
      metrics.functionCount++;
      metrics.cyclomaticComplexity++;
    }

    // Count classes
    if (ts.isClassDeclaration(node)) {
      metrics.classCount++;
    }

    // Cyclomatic complexity contributors
    if (
      ts.isIfStatement(node) ||
      ts.isConditionalExpression(node) ||
      ts.isWhileStatement(node) ||
      ts.isForStatement(node) ||
      ts.isCaseClause(node)
    ) {
      metrics.cyclomaticComplexity++;
    }

    // Cognitive complexity (simplified)
    if (ts.isIfStatement(node)) {
      metrics.cognitiveComplexity += 1 + depth;
    }

    if (ts.isWhileStatement(node) || ts.isForStatement(node)) {
      metrics.cognitiveComplexity += 1 + depth;
    }

    // Recurse
    const newDepth = this.increasesNesting(node) ? depth + 1 : depth;

    ts.forEachChild(node, child => {
      this.visit(child, metrics, newDepth);
    });
  }

  private increasesNesting(node: ts.Node): boolean {
    return (
      ts.isIfStatement(node) ||
      ts.isWhileStatement(node) ||
      ts.isForStatement(node) ||
      ts.isFunctionDeclaration(node) ||
      ts.isMethodDeclaration(node)
    );
  }

  calculateMaintainabilityIndex(metrics: ComplexityMetrics): number {
    // Simplified maintainability index
    const halsteadVolume = metrics.linesOfCode * 4.5; // Simplified
    const cyclomaticComplexity = metrics.cyclomaticComplexity;
    const linesOfCode = metrics.linesOfCode;

    const mi = Math.max(
      0,
      (171 - 5.2 * Math.log(halsteadVolume) -
        0.23 * cyclomaticComplexity -
        16.2 * Math.log(linesOfCode)) * 100 / 171
    );

    return Math.round(mi);
  }

  analyzeProject(directory: string): Record<string, ComplexityMetrics> {
    const results: Record<string, ComplexityMetrics> = {};

    const files = this.getTypeScriptFiles(directory);

    for (const file of files) {
      results[file] = this.analyzeFile(file);
    }

    return results;
  }

  private getTypeScriptFiles(dir: string): string[] {
    const files: string[] = [];

    const items = fs.readdirSync(dir);

    for (const item of items) {
      const fullPath = `${dir}/${item}`;
      const stat = fs.statSync(fullPath);

      if (stat.isDirectory() && !item.startsWith('.') && item !== 'node_modules') {
        files.push(...this.getTypeScriptFiles(fullPath));
      } else if (item.endsWith('.ts') && !item.endsWith('.d.ts')) {
        files.push(fullPath);
      }
    }

    return files;
  }

  generateReport(results: Record<string, ComplexityMetrics>): string {
    let report = '# Code Metrics Report\n\n';

    // Summary
    const totalFiles = Object.keys(results).length;
    const avgComplexity = Object.values(results).reduce(
      (sum, m) => sum + m.cyclomaticComplexity, 0
    ) / totalFiles;

    report += `## Summary\n\n`;
    report += `- Total Files: ${totalFiles}\n`;
    report += `- Average Complexity: ${avgComplexity.toFixed(2)}\n\n`;

    // High complexity files
    report += `## High Complexity Files\n\n`;

    const highComplexity = Object.entries(results)
      .filter(([_, m]) => m.cyclomaticComplexity > 10)
      .sort((a, b) => b[1].cyclomaticComplexity - a[1].cyclomaticComplexity);

    if (highComplexity.length === 0) {
      report += 'None found.\n\n';
    } else {
      for (const [file, metrics] of highComplexity) {
        report += `- ${file}\n`;
        report += `  - Cyclomatic: ${metrics.cyclomaticComplexity}\n`;
        report += `  - Cognitive: ${metrics.cognitiveComplexity}\n`;
        report += `  - LOC: ${metrics.linesOfCode}\n\n`;
      }
    }

    return report;
  }
}

// Usage
const analyzer = new CodeMetricsAnalyzer();
const results = analyzer.analyzeProject('./src');
const report = analyzer.generateReport(results);
console.log(report);
```

### 2. **Python Code Metrics (using radon)**

```python
from radon.complexity import cc_visit
from radon.metrics import mi_visit, h_visit
from radon.raw import analyze
import os
from typing import Dict, List
import json

class CodeMetricsAnalyzer:
    def analyze_file(self, file_path: str) -> Dict:
        """Analyze a single Python file."""
        with open(file_path, 'r') as f:
            code = f.read()

        # Cyclomatic complexity
        complexity = cc_visit(code)

        # Maintainability index
        mi = mi_visit(code, True)

        # Halstead metrics
        halstead = h_visit(code)

        # Raw metrics
        raw = analyze(code)

        return {
            'file': file_path,
            'complexity': [{
                'name': block.name,
                'complexity': block.complexity,
                'lineno': block.lineno
            } for block in complexity],
            'maintainability_index': mi,
            'halstead': {
                'volume': halstead.total.volume if halstead.total else 0,
                'difficulty': halstead.total.difficulty if halstead.total else 0,
                'effort': halstead.total.effort if halstead.total else 0
            },
            'raw': {
                'loc': raw.loc,
                'lloc': raw.lloc,
                'sloc': raw.sloc,
                'comments': raw.comments,
                'multi': raw.multi,
                'blank': raw.blank
            }
        }

    def analyze_project(self, directory: str) -> List[Dict]:
        """Analyze all Python files in a project."""
        results = []

        for root, dirs, files in os.walk(directory):
            # Skip common directories
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'venv', 'node_modules']]

            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        result = self.analyze_file(file_path)
                        results.append(result)
                    except Exception as e:
                        print(f"Error analyzing {file_path}: {e}")

        return results

    def generate_report(self, results: List[Dict]) -> str:
        """Generate a markdown report."""
        report = "# Code Metrics Report\n\n"

        # Summary
        total_files = len(results)
        avg_mi = sum(r['maintainability_index'] for r in results) / total_files if total_files > 0 else 0
        total_loc = sum(r['raw']['loc'] for r in results)

        report += "## Summary\n\n"
        report += f"- Total Files: {total_files}\n"
        report += f"- Total LOC: {total_loc}\n"
        report += f"- Average Maintainability Index: {avg_mi:.2f}\n\n"

        # High complexity functions
        report += "## High Complexity Functions\n\n"

        high_complexity = []
        for result in results:
            for func in result['complexity']:
                if func['complexity'] > 10:
                    high_complexity.append({
                        'file': result['file'],
                        **func
                    })

        high_complexity.sort(key=lambda x: x['complexity'], reverse=True)

        if not high_complexity:
            report += "None found.\n\n"
        else:
            for func in high_complexity[:10]:  # Top 10
                report += f"- {func['file']}:{func['lineno']} - {func['name']}\n"
                report += f"  Complexity: {func['complexity']}\n\n"

        # Low maintainability files
        report += "## Low Maintainability Files\n\n"

        low_mi = [r for r in results if r['maintainability_index'] < 65]
        low_mi.sort(key=lambda x: x['maintainability_index'])

        if not low_mi:
            report += "None found.\n\n"
        else:
            for file in low_mi[:10]:
                report += f"- {file['file']}\n"
                report += f"  MI: {file['maintainability_index']:.2f}\n"
                report += f"  LOC: {file['raw']['loc']}\n\n"

        return report

    def export_json(self, results: List[Dict], output_file: str):
        """Export results as JSON."""
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)


# Usage
analyzer = CodeMetricsAnalyzer()
results = analyzer.analyze_project('./src')
report = analyzer.generate_report(results)
print(report)

# Export to JSON
analyzer.export_json(results, 'metrics.json')
```

### 3. **ESLint Plugin for Complexity**

```javascript
// eslint-plugin-complexity.js
module.exports = {
  rules: {
    'max-complexity': {
      create(context) {
        const maxComplexity = context.options[0] || 10;
        let complexity = 0;

        function increaseComplexity(node) {
          complexity++;
        }

        function checkComplexity(node) {
          if (complexity > maxComplexity) {
            context.report({
              node,
              message: `Function has complexity of ${complexity}. Maximum allowed is ${maxComplexity}.`
            });
          }
        }

        return {
          FunctionDeclaration(node) {
            complexity = 1;
          },
          'FunctionDeclaration:exit': checkComplexity,

          IfStatement: increaseComplexity,
          SwitchCase: increaseComplexity,
          ForStatement: increaseComplexity,
          WhileStatement: increaseComplexity,
          DoWhileStatement: increaseComplexity,
          ConditionalExpression: increaseComplexity,
          LogicalExpression(node) {
            if (node.operator === '&&' || node.operator === '||') {
              increaseComplexity();
            }
          }
        };
      }
    }
  }
};
```

### 4. **CI/CD Quality Gates**

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [pull_request]

jobs:
  metrics:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install

      - name: Run complexity analysis
        run: npx ts-node analyze-metrics.ts

      - name: Check quality gates
        run: |
          COMPLEXITY=$(cat metrics.json | jq '.avgComplexity')
          if (( $(echo "$COMPLEXITY > 10" | bc -l) )); then
            echo "Average complexity too high: $COMPLEXITY"
            exit 1
          fi

      - name: Upload metrics
        uses: actions/upload-artifact@v2
        with:
          name: code-metrics
          path: metrics.json
```

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

## Tools

- **TypeScript/JavaScript**: ESLint, ts-morph, complexity-report
- **Python**: radon, mccabe, pylint
- **Java**: PMD, Checkstyle, SonarQube
- **C#**: NDepend, SonarQube
- **Multi-language**: SonarQube, CodeClimate

## Resources

- [Cyclomatic Complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
- [Cognitive Complexity](https://www.sonarsource.com/resources/cognitive-complexity/)
- [SonarQube](https://www.sonarqube.org/)
