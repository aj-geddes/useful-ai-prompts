# Test Metrics Dashboard

## Test Metrics Dashboard

```typescript
// scripts/generate-test-metrics.ts
import * as fs from "fs";

interface TestMetrics {
  totalTests: number;
  passedTests: number;
  failedTests: number;
  skippedTests: number;
  duration: number;
  coverage: number;
  timestamp: string;
}

class MetricsCollector {
  collectMetrics(): TestMetrics {
    const testResults = JSON.parse(
      fs.readFileSync("test-results.json", "utf-8"),
    );
    const coverage = JSON.parse(
      fs.readFileSync("coverage/coverage-summary.json", "utf-8"),
    );

    return {
      totalTests: testResults.numTotalTests,
      passedTests: testResults.numPassedTests,
      failedTests: testResults.numFailedTests,
      skippedTests: testResults.numPendingTests,
      duration: testResults.testResults.reduce(
        (sum, r) => sum + r.perfStats.runtime,
        0,
      ),
      coverage: coverage.total.lines.pct,
      timestamp: new Date().toISOString(),
    };
  }

  saveMetrics(metrics: TestMetrics) {
    const history = this.loadHistory();
    history.push(metrics);

    // Keep last 30 days
    const cutoff = Date.now() - 30 * 24 * 60 * 60 * 1000;
    const filtered = history.filter(
      (m) => new Date(m.timestamp).getTime() > cutoff,
    );

    fs.writeFileSync("metrics-history.json", JSON.stringify(filtered, null, 2));
  }

  loadHistory(): TestMetrics[] {
    try {
      return JSON.parse(fs.readFileSync("metrics-history.json", "utf-8"));
    } catch {
      return [];
    }
  }

  generateReport() {
    const history = this.loadHistory();

    console.log("\nTest Metrics (Last 7 days):");
    console.log("─".repeat(60));

    const recent = history.slice(-7);
    const avgCoverage =
      recent.reduce((sum, m) => sum + m.coverage, 0) / recent.length;
    const avgDuration =
      recent.reduce((sum, m) => sum + m.duration, 0) / recent.length;

    console.log(`Average Coverage: ${avgCoverage.toFixed(2)}%`);
    console.log(`Average Duration: ${(avgDuration / 1000).toFixed(2)}s`);
    console.log(`Total Tests: ${recent[recent.length - 1].totalTests}`);
  }
}

const collector = new MetricsCollector();
const metrics = collector.collectMetrics();
collector.saveMetrics(metrics);
collector.generateReport();
```
