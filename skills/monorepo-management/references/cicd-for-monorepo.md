# CI/CD for Monorepo

## CI/CD for Monorepo

```yaml
# .github/workflows/monorepo-ci.yml
name: Monorepo CI

on: [push, pull_request]

jobs:
  affected:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v3
        with:
          node-version: "18"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Get changed packages
        id: changed
        run: |
          npx lerna changed --json > changed.json
          echo "packages=$(cat changed.json | jq -r '.[].name')" >> $GITHUB_OUTPUT

      - name: Build changed
        run: npx turbo run build --filter='${{ steps.changed.outputs.packages }}'

      - name: Test changed
        run: npx turbo run test --filter='${{ steps.changed.outputs.packages }}'

      - name: Lint changed
        run: npx turbo run lint --filter='${{ steps.changed.outputs.packages }}'
```
