---
name: refactor-legacy-code
description: >
  Modernize and improve legacy codebases while maintaining functionality. Use
  when you need to refactor old code, reduce technical debt, modernize
  deprecated patterns, or improve code maintainability without breaking existing
  behavior.
---

# Refactor Legacy Code

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

This skill helps you systematically refactor legacy code to improve maintainability, readability, and performance while preserving existing functionality. It follows industry best practices for safe refactoring with comprehensive testing.

## When to Use

- Modernizing outdated code patterns or deprecated APIs
- Reducing technical debt in existing codebases
- Improving code readability and maintainability
- Extracting reusable components from monolithic code
- Upgrading to newer language features or frameworks
- Preparing code for new feature development

## Quick Start

First, analyze the legacy code to understand:

```bash
# Review the codebase structure
tree -L 3 -I 'node_modules|dist|build'

# Check for outdated dependencies
npm outdated  # or pip list --outdated, composer outdated, etc.

# Identify code complexity hotspots
# Use tools like:
# - SonarQube for code smells
# - eslint for JavaScript
# - pylint for Python
# - RuboCop for Ruby
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Code Assessment](references/code-assessment.md) | Code Assessment |
| [Establish Safety Net](references/establish-safety-net.md) | Establish Safety Net |
| [Incremental Refactoring](references/incremental-refactoring.md) | Incremental Refactoring |
| [Modernize Patterns](references/modernize-patterns.md) | Modernize Patterns |
| [Reduce Dependencies](references/reduce-dependencies.md) | Reduce Dependencies, Documentation |
| [Complete Refactoring Example](references/complete-refactoring-example.md) | Complete Refactoring Example |
| [Benefits Achieved](references/benefits-achieved.md) | Benefits Achieved |

## Best Practices

### ✅ DO

- **Refactor incrementally**: Small, testable changes
- **Run tests frequently**: After each refactoring step
- **Commit often**: Create logical, atomic commits
- **Keep existing tests passing**: Don't break functionality
- **Use IDE refactoring tools**: Safer than manual edits
- **Review code coverage**: Ensure tests cover refactored code
- **Document decisions**: Why, not just what
- **Seek peer review**: Fresh eyes catch issues

### ❌ DON'T

- **Mix refactoring with new features**: Separate concerns
- **Refactor without tests**: Recipe for breaking changes
- **Change behavior**: Refactoring should preserve functionality
- **Refactor large chunks**: Increases risk and review difficulty
- **Ignore code smells**: Address them systematically
- **Skip documentation**: Future maintainers need context
