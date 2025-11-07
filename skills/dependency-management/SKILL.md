---
name: dependency-management
description: Manage project dependencies across languages including npm install, package versioning, dependency conflicts, security scanning, and lock files. Use when dealing with dependencies, version pinning, semantic versioning, or resolving conflicts.
---

# Dependency Management

## Overview

Comprehensive dependency management across JavaScript/Node.js, Python, Ruby, Java, and other ecosystems. Covers version control, conflict resolution, security auditing, and best practices for maintaining healthy dependencies.

## When to Use

- Installing or updating project dependencies
- Resolving version conflicts
- Auditing security vulnerabilities
- Managing lock files (package-lock.json, Gemfile.lock, etc.)
- Implementing semantic versioning
- Setting up monorepo dependencies
- Optimizing dependency trees
- Managing peer dependencies

## Instructions

### 1. **Package Manager Basics**

#### Node.js / npm/yarn/pnpm
```bash
# Initialize project
npm init -y

# Install dependencies
npm install express
npm install --save-dev jest
npm install --save-exact lodash  # Exact version

# Update dependencies
npm update
npm outdated  # Check for outdated packages

# Audit security
npm audit
npm audit fix

# Clean install from lock file
npm ci  # Use in CI/CD

# View dependency tree
npm list
npm list --depth=0  # Top-level only
```

#### Python / pip/poetry
```bash
# Using pip
pip install requests
pip install -r requirements.txt
pip freeze > requirements.txt

# Using poetry (recommended)
poetry init
poetry add requests
poetry add --dev pytest
poetry add "django>=3.2,<4.0"
poetry update
poetry show --tree
poetry check  # Verify lock file
```

#### Ruby / Bundler
```bash
# Initialize
bundle init

# Install
bundle install
bundle update gem_name

# Audit
bundle audit check --update

# View dependencies
bundle list
bundle viz  # Generate dependency graph
```

### 2. **Semantic Versioning (SemVer)**

**Format:** MAJOR.MINOR.PATCH (e.g., 2.4.1)

```json
// package.json version ranges
{
  "dependencies": {
    "exact": "1.2.3",           // Exactly 1.2.3
    "patch": "~1.2.3",          // >=1.2.3 <1.3.0
    "minor": "^1.2.3",          // >=1.2.3 <2.0.0
    "major": "*",               // Any version (avoid!)
    "range": ">=1.2.3 <2.0.0",  // Explicit range
    "latest": "latest"          // Always latest (dangerous!)
  }
}
```

**Best Practices:**
- `^` for libraries: allows backward-compatible updates
- `~` for applications: more conservative, patch updates only
- Exact versions for critical dependencies
- Lock files for reproducible builds

### 3. **Dependency Lock Files**

#### package-lock.json (npm)
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "node_modules/express": {
      "version": "4.18.2",
      "resolved": "https://registry.npmjs.org/express/-/express-4.18.2.tgz",
      "integrity": "sha512-...",
      "dependencies": {
        "body-parser": "1.20.1"
      }
    }
  }
}
```

**Lock File Rules:**
- ✅ Always commit lock files to version control
- ✅ Use `npm ci` in CI/CD (faster, more reliable)
- ✅ Regenerate if corrupted: delete and run `npm install`
- ❌ Never manually edit lock files
- ❌ Don't mix package managers (npm + yarn)

#### poetry.lock (Python)
```toml
[[package]]
name = "requests"
version = "2.28.1"
description = "HTTP library"
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
certifi = ">=2017.4.17"
charset-normalizer = ">=2,<3"
```

### 4. **Resolving Dependency Conflicts**

#### Scenario: Version Conflict
```bash
# Problem: Two packages require different versions
# package-a requires lodash@^4.17.0
# package-b requires lodash@^3.10.0

# Solution 1: Check if newer versions are compatible
npm update lodash

# Solution 2: Use resolutions (yarn/package.json)
{
  "resolutions": {
    "lodash": "^4.17.21"
  }
}

# Solution 3: Use overrides (npm 8.3+)
{
  "overrides": {
    "lodash": "^4.17.21"
  }
}

# Solution 4: Fork and patch
npm install patch-package
npx patch-package some-package
```

#### Python Conflict Resolution
```bash
# Find conflicts
pip check

# Using pip-tools for constraint resolution
pip install pip-tools
pip-compile requirements.in  # Generates locked requirements.txt

# Poetry automatically resolves conflicts
poetry add package-a package-b  # Will find compatible versions
```

### 5. **Security Vulnerability Management**

#### npm Security Audit
```bash
# Audit current dependencies
npm audit

# Show detailed report
npm audit --json

# Fix automatically (may introduce breaking changes)
npm audit fix

# Fix only non-breaking changes
npm audit fix --production --audit-level=moderate

# Audit in CI/CD
npm audit --audit-level=high  # Fail if high vulnerabilities
```

#### Using Snyk
```bash
# Install Snyk CLI
npm install -g snyk

# Authenticate
snyk auth

# Test for vulnerabilities
snyk test

# Monitor project
snyk monitor

# Fix vulnerabilities interactively
snyk wizard
```

#### Python Security
```bash
# Using safety
pip install safety
safety check
safety check --json

# Using pip-audit (official tool)
pip install pip-audit
pip-audit
```

### 6. **Monorepo Dependency Management**

#### Workspace Structure (npm/yarn/pnpm)
```json
// package.json (root)
{
  "name": "my-monorepo",
  "private": true,
  "workspaces": [
    "packages/*",
    "apps/*"
  ]
}
```

```bash
# Install all dependencies
npm install

# Add dependency to specific workspace
npm install lodash --workspace=@myorg/package-a

# Run script in workspace
npm run test --workspace=@myorg/package-a

# Run script in all workspaces
npm run test --workspaces
```

#### Lerna Example
```bash
# Initialize lerna
npx lerna init

# Bootstrap (install + link)
lerna bootstrap

# Add dependency to all packages
lerna add lodash

# Version and publish
lerna version
lerna publish
```

### 7. **Peer Dependencies**

```json
// library package.json
{
  "name": "my-react-library",
  "peerDependencies": {
    "react": ">=16.8.0",
    "react-dom": ">=16.8.0"
  },
  "peerDependenciesMeta": {
    "react-dom": {
      "optional": true  // Makes peer dependency optional
    }
  }
}
```

**When to Use Peer Dependencies:**
- Plugin architecture (webpack plugins, babel plugins)
- React/Vue component libraries
- Framework extensions
- Prevents multiple versions of same package

### 8. **Performance Optimization**

#### Reduce Bundle Size
```bash
# Analyze bundle size
npm install -g bundle-buddy
npm install --save-dev webpack-bundle-analyzer

# Use production build
npm install --production

# Prune unused dependencies
npm prune

# Find duplicate packages
npm dedupe
npx yarn-deduplicate  # For yarn
```

#### package.json Optimization
```json
{
  "dependencies": {
    // ❌ Don't install entire lodash
    "lodash": "^4.17.21",

    // ✅ Install only what you need
    "lodash.debounce": "^4.0.8",
    "lodash.throttle": "^4.1.1"
  }
}
```

### 9. **CI/CD Best Practices**

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

### 10. **Dependency Update Strategies**

#### Automated Updates (Dependabot)
```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    groups:
      dev-dependencies:
        dependency-type: "development"
    ignore:
      - dependency-name: "react"
        versions: ["17.x"]
```

#### Manual Update Strategy
```bash
# Step 1: Check outdated
npm outdated

# Step 2: Update dev dependencies first
npm update --save-dev

# Step 3: Test thoroughly
npm test

# Step 4: Update production deps (one by one for major updates)
npm update express

# Step 5: Review changelog
npm view express versions
npm view express@latest
```

## Best Practices

### ✅ DO
- Commit lock files to version control
- Use `npm ci` or equivalent in CI/CD pipelines
- Regular dependency audits (weekly/monthly)
- Keep dependencies up-to-date (automate with Dependabot)
- Use exact versions for critical dependencies
- Document why specific versions are pinned
- Test after updating dependencies
- Use semantic versioning correctly
- Minimize dependency count
- Review dependency licenses

### ❌ DON'T
- Manually edit lock files
- Mix package managers (npm + yarn in same project)
- Use `npm install` in CI/CD (use `npm ci`)
- Ignore security vulnerabilities
- Use wildcards (*) for versions
- Install packages globally when local install is possible
- Commit node_modules to git
- Use `latest` tag in production
- Blindly run `npm audit fix`
- Install unnecessary dependencies

## Common Patterns

### Pattern 1: Strict Version Control
```json
{
  "dependencies": {
    "critical-package": "1.2.3",  // Exact version
    "stable-package": "~2.3.4"    // Patch updates only
  },
  "engines": {
    "node": ">=16.0.0 <19.0.0",
    "npm": ">=8.0.0"
  }
}
```

### Pattern 2: Optional Dependencies
```json
{
  "optionalDependencies": {
    "fsevents": "^2.3.2"  // macOS only, won't break on other OS
  }
}
```

### Pattern 3: Custom Registry
```bash
# .npmrc
registry=https://registry.npmjs.org/
@myorg:registry=https://npm.pkg.github.com/

# Or scoped
npm install --registry=https://custom-registry.com/
```

## Tools & Resources

- **npm**: Default Node.js package manager
- **Yarn**: Fast, reliable, secure dependency management
- **pnpm**: Efficient disk space usage, strict node_modules
- **Poetry**: Modern Python dependency management
- **Bundler**: Ruby dependency management
- **Snyk**: Security vulnerability scanning
- **Dependabot**: Automated dependency updates
- **Renovate**: Advanced dependency update automation
- **npm-check-updates**: Interactive dependency updates

## Quick Reference

```bash
# Check versions
node --version
npm --version

# Clear cache if issues
npm cache clean --force
yarn cache clean
pnpm store prune

# Reinstall all dependencies
rm -rf node_modules package-lock.json
npm install

# Why is this dependency installed?
npm ls package-name
yarn why package-name

# Find security issues
npm audit
snyk test

# Update all dependencies to latest
npx npm-check-updates -u
npm install
```
