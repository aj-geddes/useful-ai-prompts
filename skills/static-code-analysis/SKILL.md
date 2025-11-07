---
name: static-code-analysis
description: Implement static code analysis with linters, formatters, and security scanners to catch bugs early. Use when enforcing code standards, detecting security vulnerabilities, or automating code review.
---

# Static Code Analysis

## Overview

Use automated tools to analyze code without executing it, catching bugs, security issues, and style violations early.

## When to Use

- Enforcing coding standards
- Security vulnerability detection
- Bug prevention
- Code review automation
- CI/CD pipelines
- Pre-commit hooks
- Refactoring assistance

## Implementation Examples

### 1. **ESLint Configuration**

```javascript
// .eslintrc.js
module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:security/recommended'
  ],
  plugins: ['@typescript-eslint', 'security', 'import'],
  rules: {
    'no-console': ['warn', { allow: ['error', 'warn'] }],
    'no-unused-vars': 'error',
    'prefer-const': 'error',
    'eqeqeq': ['error', 'always'],
    'no-eval': 'error',
    'security/detect-object-injection': 'warn',
    'security/detect-non-literal-regexp': 'warn',
    '@typescript-eslint/no-explicit-any': 'warn',
    '@typescript-eslint/explicit-function-return-type': 'error',
    'import/order': ['error', {
      'groups': ['builtin', 'external', 'internal', 'parent', 'sibling', 'index'],
      'newlines-between': 'always'
    }]
  }
};
```

### 2. **Python Linting (pylint + mypy)**

```python
# .pylintrc
[MASTER]
ignore=venv,.git,__pycache__
jobs=4

[MESSAGES CONTROL]
disable=
    missing-docstring,
    too-few-public-methods

[FORMAT]
max-line-length=100
max-module-lines=1000

[DESIGN]
max-args=5
max-locals=15
max-returns=6
max-branches=12
max-statements=50
```

```python
# mypy.ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_calls = True
warn_redundant_casts = True
warn_unused_ignores = True
strict_equality = True
```

### 3. **Pre-commit Hooks**

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-merge-conflict
      - id: detect-private-key

  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v8.50.0
    hooks:
      - id: eslint
        files: \.[jt]sx?$
        types: [file]

  - repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/pylint
    rev: v3.0.0
    hooks:
      - id: pylint

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.1
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]

  - repo: https://github.com/trufflesecurity/trufflehog
    rev: v3.58.0
    hooks:
      - id: trufflehog
        entry: trufflehog filesystem --directory .
```

### 4. **SonarQube Integration**

```yaml
# sonar-project.properties
sonar.projectKey=my-project
sonar.projectName=My Project
sonar.projectVersion=1.0

sonar.sources=src
sonar.tests=tests
sonar.exclusions=**/node_modules/**,**/*.test.ts

sonar.typescript.lcov.reportPaths=coverage/lcov.info

sonar.qualitygate.wait=true

# Quality gates
sonar.coverage.exclusions=**/*.test.ts
```

```yaml
# .github/workflows/sonar.yml
name: SonarQube Analysis

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  sonar:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: SonarQube Scan
        uses: sonarsource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}

      - name: Quality Gate Check
        uses: sonarsource/sonarqube-quality-gate-action@master
        timeout-minutes: 5
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

### 5. **Custom AST Analysis**

```typescript
import * as ts from 'typescript';
import * as fs from 'fs';

interface Issue {
  file: string;
  line: number;
  column: number;
  message: string;
  severity: 'error' | 'warning' | 'info';
  rule: string;
}

class CustomLinter {
  private issues: Issue[] = [];

  lintFile(filePath: string): Issue[] {
    this.issues = [];

    const sourceCode = fs.readFileSync(filePath, 'utf-8');
    const sourceFile = ts.createSourceFile(
      filePath,
      sourceCode,
      ts.ScriptTarget.Latest,
      true
    );

    this.visit(sourceFile, filePath);

    return this.issues;
  }

  private visit(node: ts.Node, filePath: string): void {
    // Check for console.log
    if (
      ts.isCallExpression(node) &&
      ts.isPropertyAccessExpression(node.expression) &&
      node.expression.expression.getText() === 'console' &&
      node.expression.name.getText() === 'log'
    ) {
      const { line, character } = ts.getLineAndCharacterOfPosition(
        node.getSourceFile(),
        node.getStart()
      );

      this.issues.push({
        file: filePath,
        line: line + 1,
        column: character + 1,
        message: 'Unexpected console.log statement',
        severity: 'warning',
        rule: 'no-console'
      });
    }

    // Check for any type
    if (
      ts.isTypeReferenceNode(node) &&
      node.typeName.getText() === 'any'
    ) {
      const { line, character } = ts.getLineAndCharacterOfPosition(
        node.getSourceFile(),
        node.getStart()
      );

      this.issues.push({
        file: filePath,
        line: line + 1,
        column: character + 1,
        message: 'Avoid using any type',
        severity: 'warning',
        rule: 'no-any'
      });
    }

    // Check for long functions
    if (ts.isFunctionDeclaration(node) || ts.isMethodDeclaration(node)) {
      const body = node.body;
      if (body && body.getFullText().split('\n').length > 50) {
        const { line, character } = ts.getLineAndCharacterOfPosition(
          node.getSourceFile(),
          node.getStart()
        );

        this.issues.push({
          file: filePath,
          line: line + 1,
          column: character + 1,
          message: 'Function is too long (>50 lines)',
          severity: 'warning',
          rule: 'max-lines-per-function'
        });
      }
    }

    ts.forEachChild(node, child => this.visit(child, filePath));
  }

  formatIssues(issues: Issue[]): string {
    if (issues.length === 0) {
      return 'No issues found.';
    }

    return issues.map(issue =>
      `${issue.file}:${issue.line}:${issue.column} - ${issue.severity}: ${issue.message} (${issue.rule})`
    ).join('\n');
  }
}

// Usage
const linter = new CustomLinter();
const issues = linter.lintFile('./src/example.ts');
console.log(linter.formatIssues(issues));
```

### 6. **Security Scanning**

```typescript
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

interface SecurityIssue {
  severity: 'critical' | 'high' | 'medium' | 'low';
  title: string;
  description: string;
  file?: string;
  line?: number;
  remediation?: string;
}

class SecurityScanner {
  async scanDependencies(): Promise<SecurityIssue[]> {
    try {
      const { stdout } = await execAsync('npm audit --json');
      const auditResult = JSON.parse(stdout);

      const issues: SecurityIssue[] = [];

      for (const [name, advisory] of Object.entries(auditResult.vulnerabilities || {})) {
        const vuln = advisory as any;

        issues.push({
          severity: vuln.severity,
          title: vuln.via[0]?.title || name,
          description: vuln.via[0]?.url || '',
          remediation: `Update ${name} to ${vuln.fixAvailable || 'latest'}`
        });
      }

      return issues;
    } catch (error) {
      console.error('Dependency scan failed:', error);
      return [];
    }
  }

  async scanSecrets(directory: string): Promise<SecurityIssue[]> {
    const issues: SecurityIssue[] = [];

    // Simple regex-based secret detection
    const patterns = [
      { name: 'API Key', pattern: /api[_-]?key['"]?\s*[:=]\s*['"]([a-zA-Z0-9]{32,})['"]/ },
      { name: 'AWS Key', pattern: /(AKIA[0-9A-Z]{16})/ },
      { name: 'Private Key', pattern: /-----BEGIN (RSA |EC )?PRIVATE KEY-----/ },
      { name: 'Password', pattern: /password['"]?\s*[:=]\s*['"]((?!<%= ).{8,})['"]/ }
    ];

    // Scan files
    const files = this.getFiles(directory);

    for (const file of files) {
      const content = fs.readFileSync(file, 'utf-8');
      const lines = content.split('\n');

      for (let i = 0; i < lines.length; i++) {
        for (const { name, pattern } of patterns) {
          if (pattern.test(lines[i])) {
            issues.push({
              severity: 'critical',
              title: `Potential ${name} detected`,
              description: `Found in ${file}:${i + 1}`,
              file,
              line: i + 1,
              remediation: 'Remove secret and use environment variables'
            });
          }
        }
      }
    }

    return issues;
  }

  private getFiles(dir: string): string[] {
    // Implementation to recursively get files
    return [];
  }

  generateReport(issues: SecurityIssue[]): string {
    let report = '# Security Scan Report\n\n';

    const grouped = issues.reduce((acc, issue) => {
      acc[issue.severity] = acc[issue.severity] || [];
      acc[issue.severity].push(issue);
      return acc;
    }, {} as Record<string, SecurityIssue[]>);

    for (const [severity, items] of Object.entries(grouped)) {
      report += `## ${severity.toUpperCase()} (${items.length})\n\n`;

      for (const issue of items) {
        report += `### ${issue.title}\n`;
        report += `${issue.description}\n`;
        if (issue.remediation) {
          report += `**Remediation:** ${issue.remediation}\n`;
        }
        report += '\n';
      }
    }

    return report;
  }
}

// Usage
const scanner = new SecurityScanner();
const depIssues = await scanner.scanDependencies();
const secretIssues = await scanner.scanSecrets('./src');

const allIssues = [...depIssues, ...secretIssues];
console.log(scanner.generateReport(allIssues));
```

## Best Practices

### ✅ DO
- Run linters in CI/CD
- Use pre-commit hooks
- Configure IDE integration
- Fix issues incrementally
- Document custom rules
- Share configuration across team
- Automate security scanning

### ❌ DON'T
- Ignore all warnings
- Skip linter setup
- Commit lint violations
- Use overly strict rules initially
- Skip security scans
- Disable rules without reason

## Tools

- **JavaScript/TypeScript**: ESLint, TSLint, Prettier
- **Python**: Pylint, Flake8, Black, Bandit
- **Java**: PMD, Checkstyle, SpotBugs
- **Security**: Snyk, Semgrep, Bandit, TruffleHog
- **Multi-language**: SonarQube, CodeQL

## Resources

- [ESLint](https://eslint.org/)
- [SonarQube](https://www.sonarqube.org/)
- [Snyk](https://snyk.io/)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
