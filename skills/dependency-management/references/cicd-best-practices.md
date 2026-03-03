# CI/CD Best Practices

## CI/CD Best Practices

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      # Cache dependencies
      - uses: actions/cache@v3
        with:
          path: ~/.npm
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}

      # Use ci command (faster, more reliable)
      - run: npm ci

      # Security audit
      - run: npm audit --audit-level=high

      # Check for outdated dependencies
      - run: npm outdated || true

      - run: npm test
```
