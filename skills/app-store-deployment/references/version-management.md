# Version Management

## Version Management

```bash
# Version tracking
# package.json
{
  "name": "myapp",
  "version": "1.0.0",
  "build": {
    "ios": { "buildNumber": "1" },
    "android": { "versionCode": 1 }
  }
}

# Increment version script
#!/bin/bash
CURRENT=$(jq -r '.version' package.json)
IFS='.' read -ra VER <<< "$CURRENT"

MAJOR=${VER[0]}
MINOR=${VER[1]}
PATCH=${VER[2]}

PATCH=$((PATCH + 1))
NEW_VERSION="$MAJOR.$MINOR.$PATCH"

jq ".version = \"$NEW_VERSION\"" package.json > package.json.tmp
mv package.json.tmp package.json

echo "Version updated to $NEW_VERSION"
```
