---
name: monorepo-management
description: Manage monorepo architectures using Lerna, Turborepo, and Nx. Configure workspaces, dependency versioning, and cross-package testing.
---

# Monorepo Management

## Overview

Establish scalable monorepo structures that support multiple interdependent packages while maintaining build efficiency, dependency management, and deployment coordination.

## When to Use

- Multi-package projects
- Shared libraries across services
- Microservices architecture
- Plugin-based systems
- Multi-app platforms (web + mobile)
- Workspace dependency management
- Scaled team development

## Implementation Examples

### 1. **Npm Workspaces Configuration**

```json
{
  "name": "monorepo-root",
  "version": "1.0.0",
  "private": true,
  "workspaces": [
    "packages/*",
    "apps/*"
  ],
  "devDependencies": {
    "lerna": "^7.0.0",
    "turbo": "^1.10.0"
  },
  "scripts": {
    "lint": "npm run lint -r",
    "test": "npm run test -r",
    "build": "npm run build -r",
    "clean": "npm run clean -r"
  }
}
```

### 2. **Lerna Configuration**

```json
{
  "name": "monorepo-with-lerna",
  "version": "1.0.0",
  "private": true,
  "packages": [
    "packages/*",
    "apps/*"
  ],
  "command": {
    "bootstrap": {
      "hoist": true,
      "ignore": "@myorg/infra"
    },
    "publish": {
      "conventionalCommits": true,
      "createRelease": "github",
      "message": "chore(release): publish"
    }
  }
}
```

### 3. **Turborepo Configuration**

```json
{
  "turbo": {
    "globalDependencies": ["tsconfig.json"],
    "pipeline": {
      "build": {
        "dependsOn": ["^build"],
        "outputs": ["dist/**", ".next/**"],
        "cache": true
      },
      "test": {
        "dependsOn": ["^build"],
        "cache": true,
        "outputs": ["coverage/**"]
      },
      "lint": {
        "outputs": []
      },
      "dev": {
        "cache": false,
        "persistent": true
      }
    }
  }
}
```

### 4. **Nx Workspace Configuration**

```json
{
  "version": 2,
  "projectNameAndRootFormat": "as-provided",
  "plugins": [
    "@nx/next/plugin",
    "@nx/react/plugin",
    "@nx/node/plugin"
  ],
  "targetDefaults": {
    "build": {
      "cache": true,
      "inputs": [
        "production",
        "^production"
      ]
    },
    "test": {
      "cache": true,
      "inputs": [
        "default",
        "^production"
      ]
    }
  }
}
```

### 5. **Monorepo Directory Structure**

```bash
monorepo/
├── packages/
│   ├── core/
│   │   ├── src/
│   │   ├── package.json
│   │   └── tsconfig.json
│   ├── utils/
│   │   ├── src/
│   │   ├── package.json
│   │   └── tsconfig.json
│   └── shared/
│       ├── src/
│       ├── package.json
│       └── tsconfig.json
├── apps/
│   ├── web/
│   │   ├── pages/
│   │   ├── package.json
│   │   └── next.config.js
│   ├── api/
│   │   ├── src/
│   │   ├── package.json
│   │   └── tsconfig.json
│   └── mobile/
│       ├── src/
│       ├── package.json
│       └── app.json
├── tools/
│   ├── scripts/
│   └── generators/
├── lerna.json
├── turbo.json
├── nx.json
├── package.json
├── tsconfig.json
└── .github/workflows/
```

### 6. **Workspace Dependencies**

```json
{
  "name": "@myorg/web-app",
  "version": "1.0.0",
  "dependencies": {
    "@myorg/core": "workspace:*",
    "@myorg/shared-ui": "workspace:^",
    "@myorg/utils": "workspace:~"
  },
  "devDependencies": {
    "@myorg/test-utils": "workspace:*"
  }
}
```

### 7. **Lerna Commands**

```bash
# Bootstrap packages and install dependencies
lerna bootstrap

# Install dependencies and hoist common ones
lerna bootstrap --hoist

# Create a new version
lerna version --conventional-commits

# Publish all changed packages
lerna publish from-git

# Run command across all packages
lerna exec -- npm run build

# Run command in parallel
lerna exec --parallel -- npm run test

# List all packages
lerna list

# Show graph of dependencies
lerna graph

# Run script across specific packages
lerna run build --scope="@myorg/core" --include-dependents
```

### 8. **Turborepo Commands**

```bash
# Build all packages with dependency order
turbo run build

# Build with specific filters
turbo run build --filter=web --filter=api

# Build excluding certain packages
turbo run build --filter='!./apps/mobile'

# Run tests with caching
turbo run test --cache-dir=.turbo

# Run in development mode (no cache)
turbo run dev --parallel

# Show execution graph
turbo run build --graph

# Profile build times
turbo run build --profile=profile.json
```

### 9. **CI/CD for Monorepo**

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
          node-version: '18'
          cache: 'npm'

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

### 10. **Version Management Across Packages**

```bash
#!/bin/bash
# sync-versions.sh

# Use lerna to keep versions in sync
lerna version --exact --force-publish

# Or manually sync package.json versions
MONOREPO_VERSION=$(jq -r '.version' package.json)

for package in packages/*/package.json; do
    jq --arg version "$MONOREPO_VERSION" '.version = $version' "$package" > "$package.tmp"
    mv "$package.tmp" "$package"
done

echo "✅ All packages synced to version $MONOREPO_VERSION"
```

## Best Practices

### ✅ DO
- Use workspace protocols for dependencies
- Implement shared tsconfig for consistency
- Cache build outputs in CI/CD
- Filter packages in CI to avoid unnecessary builds
- Hoist common dependencies
- Document workspace structure
- Use consistent versioning strategy
- Implement pre-commit hooks across workspace
- Test cross-package dependencies
- Version packages independently when appropriate

### ❌ DON'T
- Create circular dependencies
- Use hardcoded versions for workspace packages
- Build all packages when only one changed
- Forget to update lock files
- Ignore workspace boundaries
- Create tightly coupled packages
- Skip dependency management
- Use different tooling per package

## Workspace Dependency Resolution

```bash
# workspace:* - Use exact version in workspace
"@myorg/core": "workspace:*"

# workspace:^ - Use compatible version
"@myorg/shared": "workspace:^"

# workspace:~ - Use patch-compatible version
"@myorg/utils": "workspace:~"
```

## Resources

- [Lerna Documentation](https://lerna.js.org/)
- [Turborepo Documentation](https://turbo.build/repo/docs)
- [Nx Documentation](https://nx.dev/)
- [npm Workspaces](https://docs.npmjs.com/cli/v7/using-npm/workspaces)
