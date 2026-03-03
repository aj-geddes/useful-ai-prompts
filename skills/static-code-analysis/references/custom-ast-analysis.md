# Custom AST Analysis

## Custom AST Analysis

```typescript
import * as ts from "typescript";
import * as fs from "fs";

interface Issue {
  file: string;
  line: number;
  column: number;
  message: string;
  severity: "error" | "warning" | "info";
  rule: string;
}

class CustomLinter {
  private issues: Issue[] = [];

  lintFile(filePath: string): Issue[] {
    this.issues = [];

    const sourceCode = fs.readFileSync(filePath, "utf-8");
    const sourceFile = ts.createSourceFile(
      filePath,
      sourceCode,
      ts.ScriptTarget.Latest,
      true,
    );

    this.visit(sourceFile, filePath);

    return this.issues;
  }

  private visit(node: ts.Node, filePath: string): void {
    // Check for console.log
    if (
      ts.isCallExpression(node) &&
      ts.isPropertyAccessExpression(node.expression) &&
      node.expression.expression.getText() === "console" &&
      node.expression.name.getText() === "log"
    ) {
      const { line, character } = ts.getLineAndCharacterOfPosition(
        node.getSourceFile(),
        node.getStart(),
      );

      this.issues.push({
        file: filePath,
        line: line + 1,
        column: character + 1,
        message: "Unexpected console.log statement",
        severity: "warning",
        rule: "no-console",
      });
    }

    // Check for any type
    if (ts.isTypeReferenceNode(node) && node.typeName.getText() === "any") {
      const { line, character } = ts.getLineAndCharacterOfPosition(
        node.getSourceFile(),
        node.getStart(),
      );

      this.issues.push({
        file: filePath,
        line: line + 1,
        column: character + 1,
        message: "Avoid using any type",
        severity: "warning",
        rule: "no-any",
      });
    }

    // Check for long functions
    if (ts.isFunctionDeclaration(node) || ts.isMethodDeclaration(node)) {
      const body = node.body;
      if (body && body.getFullText().split("\n").length > 50) {
        const { line, character } = ts.getLineAndCharacterOfPosition(
          node.getSourceFile(),
          node.getStart(),
        );

        this.issues.push({
          file: filePath,
          line: line + 1,
          column: character + 1,
          message: "Function is too long (>50 lines)",
          severity: "warning",
          rule: "max-lines-per-function",
        });
      }
    }

    ts.forEachChild(node, (child) => this.visit(child, filePath));
  }

  formatIssues(issues: Issue[]): string {
    if (issues.length === 0) {
      return "No issues found.";
    }

    return issues
      .map(
        (issue) =>
          `${issue.file}:${issue.line}:${issue.column} - ${issue.severity}: ${issue.message} (${issue.rule})`,
      )
      .join("\n");
  }
}

// Usage
const linter = new CustomLinter();
const issues = linter.lintFile("./src/example.ts");
console.log(linter.formatIssues(issues));
```
