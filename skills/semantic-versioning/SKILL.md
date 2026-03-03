---
name: semantic-versioning
description: >
  Implement semantic versioning (SemVer) with automated release management. Use
  conventional commits, semantic-release, and version bumping strategies.
---

# Semantic Versioning

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Establish semantic versioning practices to maintain consistent version numbering aligned with release significance, enabling automated version management and release notes generation.

## When to Use

- Package and library releases
- API versioning
- Version bumping automation
- Release note generation
- Breaking change tracking
- Dependency management
- Changelog management

## Quick Start

Minimal working example:

```yaml
# package.json
{
  "name": "my-awesome-package",
  "version": "1.2.3",
  "description": "An awesome package",
  "main": "dist/index.js",
  "repository": { "type": "git", "url": "https://github.com/org/repo.git" },
  "scripts": { "release": "semantic-release" },
  "devDependencies":
    {
      "semantic-release": "^21.0.0",
      "@semantic-release/changelog": "^6.0.0",
      "@semantic-release/git": "^10.0.0",
      "@semantic-release/github": "^9.0.0",
      "conventional-changelog-cli": "^3.0.0",
    },
}
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Semantic Versioning Configuration](references/semantic-versioning-configuration.md) | Semantic Versioning Configuration |
| [Conventional Commits Format](references/conventional-commits-format.md) | Conventional Commits Format |
| [Semantic Release Configuration](references/semantic-release-configuration.md) | Semantic Release Configuration |
| [Version Bumping Script](references/version-bumping-script.md) | Version Bumping Script |
| [Changelog Generation](references/changelog-generation.md) | Changelog Generation |

## Best Practices

### ✅ DO

- Follow strict MAJOR.MINOR.PATCH format
- Use conventional commits
- Automate version bumping
- Generate changelogs automatically
- Tag releases in git
- Document breaking changes
- Use prerelease versions for testing

### ❌ DON'T

- Manually bump versions inconsistently
- Skip breaking change documentation
- Use arbitrary version numbering
- Mix features in patch releases
