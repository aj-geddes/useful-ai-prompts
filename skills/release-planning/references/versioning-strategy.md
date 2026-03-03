# Versioning Strategy

## Versioning Strategy

```yaml
Versioning Strategy:

Format: MAJOR.MINOR.PATCH

Examples: v2.5.1 - Patch release (bug fixes)
  v2.6.0 - Minor release (new features, backwards compatible)
  v3.0.0 - Major release (breaking changes)

---
Release Cadence:
  Major: Annually (Jan)
  Minor: Quarterly (Jan, Apr, Jul, Oct)
  Patch: Weekly or as-needed
---
Version Naming Convention:
  Feature Release: v2.5.0
  Hotfix: v2.5.1
  Release Candidate: v2.5.0-rc.1
  Beta: v2.5.0-beta.1
  Alpha: v2.5.0-alpha.1
---
Backwards Compatibility:
  - Maintain n-1 and n-2 major versions
  - Deprecate APIs 2 quarters before removal
  - Provide migration guide for breaking changes
  - Support API v1 through June 2025 (6-month sunset)
```
