# Resolving Dependency Conflicts

## Resolving Dependency Conflicts

### Scenario: Version Conflict

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

### Python Conflict Resolution

```bash
# Find conflicts
pip check

# Using pip-tools for constraint resolution
pip install pip-tools
pip-compile requirements.in  # Generates locked requirements.txt

# Poetry automatically resolves conflicts
poetry add package-a package-b  # Will find compatible versions
```
