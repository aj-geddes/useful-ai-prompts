---
name: github-actions-workflow
description: Build comprehensive GitHub Actions workflows for CI/CD, testing, security, and deployment. Master workflows, jobs, steps, and conditional execution.
---

# GitHub Actions Workflow

## Overview

Create powerful GitHub Actions workflows to automate testing, building, security scanning, and deployment processes directly from your GitHub repository.

## When to Use

- Continuous integration and testing
- Build automation
- Security scanning and analysis
- Dependency updates
- Automated deployments
- Release management
- Code quality checks

## Implementation Examples

### 1. **Complete CI/CD Workflow**

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16.x, 18.x, 20.x]
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node ${{ matrix.node-version }}
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

      - name: Run tests
        run: npm run test:coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v3

  build:
    runs-on: ubuntu-latest
    needs: test
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Log in to Registry
        uses: docker/login-action@v2
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v4
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=semver,pattern={{version}}

      - name: Build and push image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy results to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

  deploy:
    runs-on: ubuntu-latest
    needs: [test, build]
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    steps:
      - uses: actions/checkout@v3

      - name: Deploy to production
        run: |
          echo "Deploying to production..."
          # Add deployment script
```

### 3. **Automated Release Workflow**

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  create-release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Generate changelog
        id: changelog
        uses: mikepenz/action-github-changelog-generator@v3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Create Release
        uses: ncipollo/release-action@v1
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          tag: ${{ github.ref }}
          body: ${{ steps.changelog.outputs.changelog }}
          draft: false

      - name: Publish to npm
        uses: JS-DevTools/npm-publish@v1
        with:
          token: ${{ secrets.NPM_TOKEN }}
```

### 5. **Docker Build and Push**

```yaml
name: Docker Build
on: [push]
jobs:
  docker:
    runs-on: ubuntu-latest
    permissions:
      packages: write
    steps:
      - uses: actions/checkout@v3
      - uses: docker/setup-buildx-action@v2
      - uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ghcr.io/${{ github.repository }}:latest
```

## Best Practices

### ✅ DO
- Use caching for dependencies (npm, pip, Maven)
- Run tests in parallel with matrix strategy
- Require status checks on protected branches
- Use environment secrets and variables
- Implement conditional jobs with `if:`
- Lint and format before testing
- Set explicit permissions with permissions
- Use runner labels for specific hardware
- Cache Docker layers for faster builds

### ❌ DON'T
- Store secrets in workflow files
- Run untrusted code in workflows
- Use `secrets.*` with pull requests from forks
- Hardcode credentials or tokens
- Miss error handling with `continue-on-error`
- Create overly complex workflows
- Skip testing on pull requests

## Secrets and Variables

```bash
# Set secrets via CLI
gh secret set MY_SECRET --body "secret-value"
gh secret list

# Set organization variables
gh variable set MY_VAR --body "value" --org myorg
```

## Workflow Permissions

```yaml
permissions:
  actions: read
  contents: read
  checks: write
  pull-requests: write
  security-events: write
  packages: write
```

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
