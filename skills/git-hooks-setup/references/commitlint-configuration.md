# Commitlint Configuration

## Commitlint Configuration

```javascript
// commitlint.config.js
module.exports = {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "type-enum": [
      2,
      "always",
      ["feat", "fix", "docs", "style", "refactor", "test", "chore"],
    ],
    "subject-case": [2, "never", ["start-case", "pascal-case", "upper-case"]],
    "type-empty": [2, "never"],
  },
};
```


## Pre-push Hook (Comprehensive)

```bash
#!/usr/bin/env bash
# .husky/pre-push
BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Prevent direct pushes to main
if [[ "$BRANCH" =~ ^(main|master)$ ]]; then
  echo "❌ Direct push to $BRANCH not allowed"
  exit 1
fi

npm test && npm run lint && npm run build
```
