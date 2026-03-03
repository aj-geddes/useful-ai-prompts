# CI/CD Quality Gates

## CI/CD Quality Gates

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
          node-version: "18"

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
