# Dependency Update Strategies

## Dependency Update Strategies

### Automated Updates (Dependabot)

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

### Manual Update Strategy

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
