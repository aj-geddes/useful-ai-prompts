# Lerna Commands

## Lerna Commands

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
