# TypeScript Complexity Analyzer

## TypeScript Complexity Analyzer

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
      linesOfCode: sourceCode.split("\n").length,
      functionCount: 0,
      classCount: 0,
      maxNestingDepth: 0,
    };

    this.visit(sourceFile, metrics);

    return metrics;
  }

  private visit(
    node: ts.Node,
    metrics: ComplexityMetrics,
    depth: number = 0,
  ): void {
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

    ts.forEachChild(node, (child) => {
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
      ((171 -
        5.2 * Math.log(halsteadVolume) -
        0.23 * cyclomaticComplexity -
        16.2 * Math.log(linesOfCode)) *
        100) /
        171,
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

      if (
        stat.isDirectory() &&
        !item.startsWith(".") &&
        item !== "node_modules"
      ) {
        files.push(...this.getTypeScriptFiles(fullPath));
      } else if (item.endsWith(".ts") && !item.endsWith(".d.ts")) {
        files.push(fullPath);
      }
    }

    return files;
  }

  generateReport(results: Record<string, ComplexityMetrics>): string {
    let report = "# Code Metrics Report\n\n";

    // Summary
    const totalFiles = Object.keys(results).length;
    const avgComplexity =
      Object.values(results).reduce(
        (sum, m) => sum + m.cyclomaticComplexity,
        0,
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
      report += "None found.\n\n";
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
const results = analyzer.analyzeProject("./src");
const report = analyzer.generateReport(results);
console.log(report);
```
