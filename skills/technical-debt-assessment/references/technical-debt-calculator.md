# Technical Debt Calculator

## Technical Debt Calculator

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

    const priority =
      (item.impact * 10 +
        item.interest * 5 +
        severityWeight[item.severity] * 3) /
      (item.effort + 1);

    return priority;
  }

  getPrioritizedList(): Array<DebtItem & { priority: number }> {
    return this.items
      .map((item) => ({
        ...item,
        priority: this.calculatePriority(item),
      }))
      .sort((a, b) => b.priority - a.priority);
  }

  getDebtByCategory(): Record<string, DebtItem[]> {
    return this.items.reduce(
      (acc, item) => {
        acc[item.category] = acc[item.category] || [];
        acc[item.category].push(item);
        return acc;
      },
      {} as Record<string, DebtItem[]>,
    );
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

    let report = "# Technical Debt Assessment\n\n";

    // Summary
    report += "## Summary\n\n";
    report += `- Total Items: ${this.items.length}\n`;
    report += `- Total Effort: ${this.getTotalEffort()} hours\n`;
    report += `- Monthly Interest: ${this.getTotalInterest()} hours\n\n`;

    // By Category
    report += "## By Category\n\n";
    for (const [category, items] of Object.entries(byCategory)) {
      const effort = items.reduce((sum, item) => sum + item.effort, 0);
      report += `- ${category}: ${items.length} items (${effort} hours)\n`;
    }
    report += "\n";

    // Top Priority Items
    report += "## Top Priority Items\n\n";
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
  id: "debt-1",
  title: "Legacy API endpoints",
  description: "Old API v1 endpoints still in use, need migration",
  category: "architecture",
  severity: "high",
  effort: 40,
  impact: 8,
  interest: 5,
});

assessment.addDebtItem({
  id: "debt-2",
  title: "Missing unit tests",
  description: "30% of codebase lacks test coverage",
  category: "test",
  severity: "medium",
  effort: 80,
  impact: 7,
  interest: 3,
});

console.log(assessment.generateReport());
```
