# Security Scanning

## Security Scanning

```typescript
import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

interface SecurityIssue {
  severity: "critical" | "high" | "medium" | "low";
  title: string;
  description: string;
  file?: string;
  line?: number;
  remediation?: string;
}

class SecurityScanner {
  async scanDependencies(): Promise<SecurityIssue[]> {
    try {
      const { stdout } = await execAsync("npm audit --json");
      const auditResult = JSON.parse(stdout);

      const issues: SecurityIssue[] = [];

      for (const [name, advisory] of Object.entries(
        auditResult.vulnerabilities || {},
      )) {
        const vuln = advisory as any;

        issues.push({
          severity: vuln.severity,
          title: vuln.via[0]?.title || name,
          description: vuln.via[0]?.url || "",
          remediation: `Update ${name} to ${vuln.fixAvailable || "latest"}`,
        });
      }

      return issues;
    } catch (error) {
      console.error("Dependency scan failed:", error);
      return [];
    }
  }

  async scanSecrets(directory: string): Promise<SecurityIssue[]> {
    const issues: SecurityIssue[] = [];

    // Simple regex-based secret detection
    const patterns = [
      {
        name: "API Key",
        pattern: /api[_-]?key['"]?\s*[:=]\s*['"]([a-zA-Z0-9]{32,})['"]/,
      },
      { name: "AWS Key", pattern: /(AKIA[0-9A-Z]{16})/ },
      {
        name: "Private Key",
        pattern: /-----BEGIN (RSA |EC )?PRIVATE KEY-----/,
      },
      {
        name: "Password",
        pattern: /password['"]?\s*[:=]\s*['"]((?!<%= ).{8,})['"]/,
      },
    ];

    // Scan files
    const files = this.getFiles(directory);

    for (const file of files) {
      const content = fs.readFileSync(file, "utf-8");
      const lines = content.split("\n");

      for (let i = 0; i < lines.length; i++) {
        for (const { name, pattern } of patterns) {
          if (pattern.test(lines[i])) {
            issues.push({
              severity: "critical",
              title: `Potential ${name} detected`,
              description: `Found in ${file}:${i + 1}`,
              file,
              line: i + 1,
              remediation: "Remove secret and use environment variables",
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
    let report = "# Security Scan Report\n\n";

    const grouped = issues.reduce(
      (acc, issue) => {
        acc[issue.severity] = acc[issue.severity] || [];
        acc[issue.severity].push(issue);
        return acc;
      },
      {} as Record<string, SecurityIssue[]>,
    );

    for (const [severity, items] of Object.entries(grouped)) {
      report += `## ${severity.toUpperCase()} (${items.length})\n\n`;

      for (const issue of items) {
        report += `### ${issue.title}\n`;
        report += `${issue.description}\n`;
        if (issue.remediation) {
          report += `**Remediation:** ${issue.remediation}\n`;
        }
        report += "\n";
      }
    }

    return report;
  }
}

// Usage
const scanner = new SecurityScanner();
const depIssues = await scanner.scanDependencies();
const secretIssues = await scanner.scanSecrets("./src");

const allIssues = [...depIssues, ...secretIssues];
console.log(scanner.generateReport(allIssues));
```
