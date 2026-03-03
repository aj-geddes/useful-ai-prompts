# Semantic Versioning (SemVer)

## Semantic Versioning (SemVer)

**Format:** MAJOR.MINOR.PATCH (e.g., 2.4.1)

```json
// package.json version ranges
{
  "dependencies": {
    "exact": "1.2.3", // Exactly 1.2.3
    "patch": "~1.2.3", // >=1.2.3 <1.3.0
    "minor": "^1.2.3", // >=1.2.3 <2.0.0
    "major": "*", // Any version (avoid!)
    "range": ">=1.2.3 <2.0.0", // Explicit range
    "latest": "latest" // Always latest (dangerous!)
  }
}
```

**Best Practices:**

- `^` for libraries: allows backward-compatible updates
- `~` for applications: more conservative, patch updates only
- Exact versions for critical dependencies
- Lock files for reproducible builds
