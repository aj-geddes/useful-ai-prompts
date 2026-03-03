# Secret Detection Hook

## Secret Detection Hook

```bash
#!/bin/bash
# .husky/pre-commit-secrets
git diff --cached | grep -E 'password|api_key|secret|token' && exit 1
echo "✅ No secrets detected"
```


## Husky in package.json

```json
{
  "scripts": { "prepare": "husky install" },
  "devDependencies": {
    "husky": "^8.0.0",
    "@commitlint/cli": "^17.0.0"
  },
  "lint-staged": {
    "*.{js,ts}": "eslint --fix"
  }
}
```
