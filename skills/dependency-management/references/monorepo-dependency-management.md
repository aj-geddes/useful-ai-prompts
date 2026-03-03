# Monorepo Dependency Management

## Monorepo Dependency Management

### Workspace Structure (npm/yarn/pnpm)

```json
// package.json (root)
{
  "name": "my-monorepo",
  "private": true,
  "workspaces": ["packages/*", "apps/*"]
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

### Lerna Example

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
