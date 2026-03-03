# Flaky Test Detection

## Flaky Test Detection

```yaml
# .github/workflows/flaky-test-detection.yml
name: Flaky Test Detection

on:
  schedule:
    - cron: "0 2 * * *" # Run nightly

jobs:
  detect-flaky-tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: "18"

      - name: Install dependencies
        run: npm ci

      - name: Run tests 10 times
        run: |
          for i in {1..10}; do
            echo "Run $i"
            npm test -- --json --outputFile=results-$i.json || true
          done

      - name: Analyze flaky tests
        run: node scripts/analyze-flaky-tests.js
```

```javascript
// scripts/analyze-flaky-tests.js
const fs = require("fs");

const runs = Array.from({ length: 10 }, (_, i) =>
  JSON.parse(fs.readFileSync(`results-${i + 1}.json`, "utf-8")),
);

const testResults = new Map();

// Aggregate results
runs.forEach((run) => {
  run.testResults.forEach((suite) => {
    suite.assertionResults.forEach((test) => {
      const key = `${suite.name}::${test.title}`;
      if (!testResults.has(key)) {
        testResults.set(key, { passed: 0, failed: 0 });
      }
      const stats = testResults.get(key);
      if (test.status === "passed") {
        stats.passed++;
      } else {
        stats.failed++;
      }
    });
  });
});

// Identify flaky tests
const flakyTests = [];
testResults.forEach((stats, test) => {
  if (stats.passed > 0 && stats.failed > 0) {
    flakyTests.push({
      test,
      passRate: (stats.passed / 10) * 100,
      ...stats,
    });
  }
});

if (flakyTests.length > 0) {
  console.log("\nFlaky Tests Detected:");
  flakyTests.forEach(({ test, passRate, passed, failed }) => {
    console.log(`  ${test}`);
    console.log(`    Pass rate: ${passRate}% (${passed}/10 runs)`);
  });

  // Fail if too many flaky tests
  if (flakyTests.length > 5) {
    process.exit(1);
  }
}
```
