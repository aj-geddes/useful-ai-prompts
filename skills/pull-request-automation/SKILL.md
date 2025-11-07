---
name: pull-request-automation
description: Automate pull request workflows with templates, checklists, auto-merge rules, and review assignments. Reduce manual overhead and improve consistency.
---

# Pull Request Automation

## Overview

Implement pull request automation to streamline code review processes, enforce quality standards, and reduce manual overhead through templated workflows and intelligent assignment rules.

## When to Use

- Code review standardization
- Quality gate enforcement
- Contributor guidance
- Review assignment automation
- Merge automation
- PR labeling and organization

## Implementation Examples

### 1. **GitHub Pull Request Template**

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
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests pass locally

## Screenshots (if applicable)
Add screenshots for UI changes

## Performance Impact
- [ ] No performance impact
- [ ] Performance improved
- [ ] Potential performance implications (describe)

## Dependencies
List any new dependencies or version changes
```

### 2. **GitHub Actions: Auto Review Assignment**

```yaml
# .github/workflows/auto-assign.yml
name: Auto Assign PR

on:
  pull_request:
    types: [opened, reopened]

jobs:
  assign:
    runs-on: ubuntu-latest
    steps:
      - name: Assign reviewers
        uses: actions/github-script@v7
        with:
          script: |
            const pr = context.payload.pull_request;
            const reviewers = ['reviewer1', 'reviewer2', 'reviewer3'];

            // Select random reviewers
            const selected = reviewers.sort(() => 0.5 - Math.random()).slice(0, 2);

            await github.rest.pulls.requestReviewers({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: pr.number,
              reviewers: selected
            });

      - name: Add labels
        uses: actions/github-script@v7
        with:
          script: |
            const pr = context.payload.pull_request;
            const labels = [];

            if (pr.title.startsWith('feat:')) labels.push('feature');
            if (pr.title.startsWith('fix:')) labels.push('bugfix');
            if (pr.title.startsWith('docs:')) labels.push('documentation');

            if (labels.length > 0) {
              await github.rest.issues.addLabels({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: pr.number,
                labels: labels
              });
            }
```

### 3. **GitHub Actions: Auto Merge on Approval**

```yaml
# .github/workflows/auto-merge.yml
name: Auto Merge PR

on:
  pull_request_review:
    types: [submitted]
  check_suite:
    types: [completed]

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    if: github.event.review.state == 'approved'
    steps:
      - name: Check PR status
        uses: actions/github-script@v7
        with:
          script: |
            const pr = await github.rest.pulls.get({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number
            });

            // Check if all required checks passed
            const checkRuns = await github.rest.checks.listForRef({
              owner: context.repo.owner,
              repo: context.repo.repo,
              ref: pr.data.head.ref
            });

            const allPassed = checkRuns.data.check_runs.every(
              run => run.status === 'completed' && run.conclusion === 'success'
            );

            if (allPassed && pr.data.approved_reviews_count >= 2) {
              // Auto merge with squash strategy
              await github.rest.pulls.merge({
                owner: context.repo.owner,
                repo: context.repo.repo,
                pull_number: context.issue.number,
                merge_method: 'squash'
              });
            }
```

### 4. **GitLab Merge Request Automation**

```yaml
# .gitlab/merge_request_templates/default.md
## Description
<!-- Briefly describe what this MR does -->

## Related Issue
Closes #(issue number)

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Code review self-check completed
- [ ] No new console errors/warnings

## Type of Change
- [ ] Bug fix
- [ ] Feature
- [ ] Breaking change
- [ ] Documentation
```

### 5. **Bors: Merge Automation Configuration**

```toml
# bors.toml
status = [
  "continuous-integration/travis-ci/pr",
  "continuous-integration/circleci",
  "codecov/project/overall"
]

# Reviewers
reviewers = ["reviewer1", "reviewer2"]

# Block merge if status checks fail
block_labels = ["blocked", "no-merge"]

# Automatically merge if all checks pass
timeout_sec = 3600

# Delete branch after merge
delete_merged_branches = true

# Squash commits on merge
squash_commits = true
```

### 6. **Conventional Commit Validation**

```bash
#!/bin/bash
# commit-msg validation script

COMMIT_MSG=$(<"$1")

# Pattern: type(scope): subject
PATTERN="^(feat|fix|docs|style|refactor|test|chore)(\([a-z\-]+\))?: .{1,50}$"

if ! [[ $COMMIT_MSG =~ $PATTERN ]]; then
    echo "❌ Commit message does not follow Conventional Commits format"
    echo "Format: type(scope): subject"
    echo "Types: feat, fix, docs, style, refactor, test, chore"
    exit 1
fi

echo "✅ Commit message format is valid"
exit 0
```

### 7. **PR Title Validation Workflow**

```yaml
# .github/workflows/validate-pr-title.yml
name: Validate PR Title

on:
  pull_request:
    types: [opened, reopened, edited]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Validate PR title format
        uses: actions/github-script@v7
        with:
          script: |
            const pr = context.payload.pull_request;
            const title = pr.title;

            // Pattern: type: description
            const pattern = /^(feat|fix|docs|style|refactor|test|chore|perf)(\(.+\))?: .{1,80}$/;

            if (!pattern.test(title)) {
              core.setFailed(
                'PR title must follow: type: description\n' +
                'Types: feat, fix, docs, style, refactor, test, chore, perf'
              );
            }
```

### 8. **Code Coverage Requirement**

```yaml
# .github/workflows/coverage-check.yml
name: Coverage Check

on: [pull_request]

jobs:
  coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Run tests with coverage
        run: npm run test:coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./coverage/lcov.info
          fail_ci_if_error: true
          minimum-coverage: 80
```

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

## CODEOWNERS Configuration

```bash
# .github/CODEOWNERS

# Global owners
* @owner1 @owner2

# Documentation
/docs/ @doc-owner
*.md @doc-owner

# Backend
/backend/ @backend-lead @backend-team
/src/api/ @api-team

# Frontend
/frontend/ @frontend-lead @frontend-team
/src/components/ @component-team

# DevOps
/infra/ @devops-team
/.github/workflows/ @devops-team
```

## Resources

- [GitHub PR Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- [GitLab Merge Request Templates](https://docs.gitlab.com/ee/user/project/description_templates.html)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Bors: Merge Bot](https://bors.tech/)
