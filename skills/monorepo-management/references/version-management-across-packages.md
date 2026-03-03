# Version Management Across Packages

## Version Management Across Packages

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
