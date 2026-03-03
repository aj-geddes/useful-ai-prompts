# Dependency Lock Files

## Dependency Lock Files

### package-lock.json (npm)

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

### poetry.lock (Python)

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
