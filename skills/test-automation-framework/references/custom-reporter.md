# Custom Reporter

## Custom Reporter

```typescript
// framework/reporters/CustomReporter.ts
import { Reporter, TestCase, TestResult } from "@playwright/test/reporter";

class CustomReporter implements Reporter {
  private stats = {
    passed: 0,
    failed: 0,
    skipped: 0,
    total: 0,
  };

  onBegin() {
    console.log("Starting test run...");
  }

  onTestEnd(test: TestCase, result: TestResult) {
    this.stats.total++;

    if (result.status === "passed") {
      this.stats.passed++;
      console.log(`✓ ${test.title}`);
    } else if (result.status === "failed") {
      this.stats.failed++;
      console.log(`✗ ${test.title}`);
      console.log(`  Error: ${result.error?.message}`);
    } else if (result.status === "skipped") {
      this.stats.skipped++;
      console.log(`⊘ ${test.title}`);
    }
  }

  onEnd() {
    console.log("\nTest Summary:");
    console.log(`  Total: ${this.stats.total}`);
    console.log(`  Passed: ${this.stats.passed}`);
    console.log(`  Failed: ${this.stats.failed}`);
    console.log(`  Skipped: ${this.stats.skipped}`);
  }
}

export default CustomReporter;
```
