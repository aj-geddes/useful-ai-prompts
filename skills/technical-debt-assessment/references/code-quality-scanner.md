# Code Quality Scanner

## Code Quality Scanner

```typescript
import * as ts from "typescript";
import * as fs from "fs";

interface QualityIssue {
  file: string;
  line: number;
  issue: string;
  severity: "info" | "warning" | "error";
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
    const sourceCode = fs.readFileSync(filePath, "utf-8");
    const sourceFile = ts.createSourceFile(
      filePath,
      sourceCode,
      ts.ScriptTarget.Latest,
      true,
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
      if (ts.isTypeReferenceNode(node) && node.typeName.getText() === "any") {
        const { line } = ts.getLineAndCharacterOfPosition(
          sourceFile,
          node.getStart(),
        );

        this.issues.push({
          file: filePath,
          line: line + 1,
          issue: "Use of any type reduces type safety",
          severity: "warning",
          debtHours: 0.5,
        });
      }

      ts.forEachChild(node, visit);
    };

    visit(sourceFile);
  }

  private checkForLongFunctions(
    sourceFile: ts.SourceFile,
    filePath: string,
  ): void {
    const visit = (node: ts.Node) => {
      if (ts.isFunctionDeclaration(node) || ts.isMethodDeclaration(node)) {
        if (node.body) {
          const lines = node.body.getFullText().split("\n").length;

          if (lines > 50) {
            const { line } = ts.getLineAndCharacterOfPosition(
              sourceFile,
              node.getStart(),
            );

            this.issues.push({
              file: filePath,
              line: line + 1,
              issue: `Function has ${lines} lines, should be refactored`,
              severity: "warning",
              debtHours: Math.ceil(lines / 10),
            });
          }
        }
      }

      ts.forEachChild(node, visit);
    };

    visit(sourceFile);
  }

  private checkForMagicNumbers(
    sourceFile: ts.SourceFile,
    filePath: string,
  ): void {
    const visit = (node: ts.Node) => {
      if (ts.isNumericLiteral(node)) {
        const value = parseFloat(node.text);

        // Ignore common constants
        if (![0, 1, -1, 2].includes(value)) {
          const { line } = ts.getLineAndCharacterOfPosition(
            sourceFile,
            node.getStart(),
          );

          this.issues.push({
            file: filePath,
            line: line + 1,
            issue: `Magic number ${value} should be a named constant`,
            severity: "info",
            debtHours: 0.1,
          });
        }
      }

      ts.forEachChild(node, visit);
    };

    visit(sourceFile);
  }

  private checkForConsoleStatements(
    sourceFile: ts.SourceFile,
    filePath: string,
  ): void {
    const text = sourceFile.getFullText();
    const lines = text.split("\n");

    lines.forEach((line, index) => {
      if (line.includes("console.log") || line.includes("console.error")) {
        this.issues.push({
          file: filePath,
          line: index + 1,
          issue: "Console statement should use proper logger",
          severity: "info",
          debtHours: 0.1,
        });
      }
    });
  }

  private checkForTodoComments(
    sourceFile: ts.SourceFile,
    filePath: string,
  ): void {
    const text = sourceFile.getFullText();
    const lines = text.split("\n");

    lines.forEach((line, index) => {
      if (/\/\/\s*TODO/.test(line)) {
        this.issues.push({
          file: filePath,
          line: index + 1,
          issue: "TODO comment indicates incomplete work",
          severity: "warning",
          debtHours: 2,
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
    let report = "# Code Quality Report\n\n";

    const bySeverity = this.issues.reduce(
      (acc, issue) => {
        acc[issue.severity] = acc[issue.severity] || [];
        acc[issue.severity].push(issue);
        return acc;
      },
      {} as Record<string, QualityIssue[]>,
    );

    report += `## Summary\n\n`;
    report += `- Total Issues: ${this.issues.length}\n`;
    report += `- Estimated Debt: ${this.getTotalDebt()} hours\n\n`;

    for (const [severity, issues] of Object.entries(bySeverity)) {
      report += `### ${severity.toUpperCase()} (${issues.length})\n\n`;

      for (const issue of issues.slice(0, 10)) {
        report += `- ${issue.file}:${issue.line} - ${issue.issue}\n`;
      }

      report += "\n";
    }

    return report;
  }
}
```
