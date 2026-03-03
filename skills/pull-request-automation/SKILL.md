---
name: pull-request-automation
description: >
  Automate pull request workflows with templates, checklists, auto-merge rules,
  and review assignments. Reduce manual overhead and improve consistency.
---

# Pull Request Automation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement pull request automation to streamline code review processes, enforce quality standards, and reduce manual overhead through templated workflows and intelligent assignment rules.

## When to Use

- Code review standardization
- Quality gate enforcement
- Contributor guidance
- Review assignment automation
- Merge automation
- PR labeling and organization

## Quick Start

Minimal working example:

```markdown
# .github/pull_request_template.md

## Description

Briefly describe the changes made in this PR.

## Type of Change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## Related Issues

Closes #(issue number)

## Changes Made

- Change 1
- Change 2

## Testing

- [ ] Unit tests added/updated
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [GitHub Actions: Auto Review Assignment](references/github-actions-auto-review-assignment.md) | GitHub Actions: Auto Review Assignment |
| [GitHub Actions: Auto Merge on Approval](references/github-actions-auto-merge-on-approval.md) | GitHub Actions: Auto Merge on Approval |
| [GitLab Merge Request Automation](references/gitlab-merge-request-automation.md) | GitLab Merge Request Automation |
| [Bors: Merge Automation Configuration](references/bors-merge-automation-configuration.md) | Bors: Merge Automation Configuration, Conventional Commit Validation |
| [PR Title Validation Workflow](references/pr-title-validation-workflow.md) | PR Title Validation Workflow |
| [Code Coverage Requirement](references/code-coverage-requirement.md) | Code Coverage Requirement |

## Best Practices

### ✅ DO

- Use PR templates for consistency
- Require code reviews before merge
- Enforce CI/CD checks pass
- Auto-assign reviewers based on code ownership
- Label PRs for organization
- Validate commit messages
- Use squash commits for cleaner history
- Set minimum coverage requirements
- Provide detailed PR descriptions

### ❌ DON'T

- Approve without reviewing code
- Merge failing CI checks
- Use vague PR titles
- Skip automated checks
- Merge to protected branches without review
- Ignore code coverage drops
- Force push to shared branches
- Merge directly without PR
