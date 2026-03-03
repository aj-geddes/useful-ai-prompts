# Version Bumping Script

## Version Bumping Script

```bash
#!/bin/bash
# bump-version.sh

CURRENT_VERSION=$(grep '"version"' package.json | head -1 | sed 's/.*"version": "\([^"]*\)".*/\1/')
IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"

case "${1:-patch}" in
  major)
    NEW_VERSION="$((MAJOR + 1)).0.0"
    ;;
  minor)
    NEW_VERSION="$MAJOR.$((MINOR + 1)).0"
    ;;
  patch)
    NEW_VERSION="$MAJOR.$MINOR.$((PATCH + 1))"
    ;;
  *)
    echo "Usage: $0 {major|minor|patch}"
    exit 1
    ;;
esac

echo "Bumping version from $CURRENT_VERSION to $NEW_VERSION"

# Update package.json
npm version $NEW_VERSION --no-git-tag-v

# Update CHANGELOG
CHANGELOG_HEADER="## [$NEW_VERSION] - $(date +%Y-%m-%d)"
sed -i "1i\\$CHANGELOG_HEADER" CHANGELOG.md

# Commit and tag
git add package.json CHANGELOG.md package-lock.json
git commit -m "chore(release): version $NEW_VERSION"
git tag -a "v$NEW_VERSION" -m "Release $NEW_VERSION"

echo "✅ Version bumped to $NEW_VERSION"
```
