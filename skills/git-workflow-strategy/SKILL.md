---
name: git-workflow-strategy
description: Master Git workflows including GitFlow, GitHub Flow, Trunk-Based Development. Configure branches, merge strategies, and collaboration patterns for team environments.
---

# Git Workflow Strategy

## Overview

Establish efficient Git workflows that support team collaboration, code quality, and deployment readiness through structured branching strategies and merge patterns.

## When to Use

- Team collaboration setup
- Release management
- Feature development coordination
- Hotfix procedures
- Code review processes
- CI/CD integration planning

## Implementation Examples

### 1. **GitFlow Workflow Setup**

```bash
# Initialize GitFlow
git flow init -d

# Start a feature
git flow feature start new-feature
# Work on feature
git add .
git commit -m "feat: implement new feature"
git flow feature finish new-feature

# Start a release
git flow release start 1.0.0
# Update version numbers, changelog
git add .
git commit -m "chore: bump version to 1.0.0"
git flow release finish 1.0.0

# Create hotfix
git flow hotfix start 1.0.1
# Fix critical bug
git add .
git commit -m "fix: critical bug in production"
git flow hotfix finish 1.0.1
```

### 2. **GitHub Flow Workflow**

```bash
# Clone and setup
git clone https://github.com/org/repo.git
cd repo

# Create feature branch from main
git checkout -b feature/add-auth-service
git add .
git commit -m "feat: add authentication service"
git push origin feature/add-auth-service

# Push changes, create PR, request reviews
# After approval and CI passes, merge to main
git checkout main
git pull origin main
git merge feature/add-auth-service
git push origin main

# Deploy and cleanup
git branch -d feature/add-auth-service
git push origin -d feature/add-auth-service
```

### 3. **Trunk-Based Development**

```bash
# Create short-lived feature branch
git checkout -b feature/toggle-feature
# Keep commits small and atomic
git add specific_file.js
git commit -m "feat: add feature flag configuration"

# Rebase on main frequently
git fetch origin
git rebase origin/main

# Create PR with small changeset
git push origin feature/toggle-feature

# After PR merge, delete branch
git checkout main
git pull origin main
git branch -d feature/toggle-feature
```

### 4. **Git Configuration for Workflows**

```bash
# Configure user
git config --global user.name "Developer Name"
git config --global user.email "dev@example.com"

# Set default branch
git config --global init.defaultBranch main

# Configure merge strategy
git config --global pull.ff only
git config --global merge.ff false

# Enable rerere (reuse recorded resolution)
git config --global rerere.enabled true

# Configure commit message format
git config --global commit.template ~/.gitmessage

# Setup branch protection rules
git config --global branch.main.rebase true
git config --global branch.develop.rebase true
```

### 5. **Branch Naming Conventions**

```bash
# Feature branches
git checkout -b feature/user-authentication
git checkout -b feature/JIRA-123-payment-integration

# Bug fix branches
git checkout -b bugfix/JIRA-456-login-timeout
git checkout -b fix/null-pointer-exception

# Release branches
git checkout -b release/v2.1.0
git checkout -b release/2024-Q1

# Hotfix branches
git checkout -b hotfix/critical-security-patch
git checkout -b hotfix/v2.0.1

# Chore branches
git checkout -b chore/update-dependencies
git checkout -b chore/refactor-auth-module
```

### 6. **Merge Strategy Script**

```bash
#!/bin/bash
# merge-with-strategy.sh

BRANCH=$1
STRATEGY=${2:-"squash"}

if [ -z "$BRANCH" ]; then
    echo "Usage: ./merge-with-strategy.sh <branch> [squash|rebase|merge]"
    exit 1
fi

# Update main
git checkout main
git pull origin main

case "$STRATEGY" in
    squash)
        git merge --squash origin/$BRANCH
        git commit -m "Merge $BRANCH"
        ;;
    rebase)
        git rebase origin/$BRANCH
        ;;
    merge)
        git merge --no-ff origin/$BRANCH
        ;;
    *)
        echo "Unknown strategy: $STRATEGY"
        exit 1
        ;;
esac

git push origin main
git push origin -d $BRANCH
```

### 7. **Collaborative Workflow with Code Review**

```bash
# Developer creates feature
git checkout -b feature/search-optimization
# Make changes
git add .
git commit -m "perf: optimize search algorithm"
git push origin feature/search-optimization

# Create pull request with detailed description
# Reviewer reviews and suggests changes

# Developer makes requested changes
git add .
git commit -m "refactor: improve search efficiency per review"
git push origin feature/search-optimization

# After approval
git checkout main
git pull origin main
git merge feature/search-optimization
git push origin main

# Cleanup
git branch -d feature/search-optimization
git push origin -d feature/search-optimization
```

## Best Practices

### ✅ DO
- Choose workflow matching team size and release cycle
- Keep feature branches short-lived (< 3 days)
- Use descriptive branch names with type prefix
- Require code review before merging to main
- Enforce protection rules on main/release branches
- Rebase frequently to minimize conflicts
- Write atomic, logical commits
- Keep commit messages clear and consistent

### ❌ DON'T
- Commit directly to main branch
- Create long-lived feature branches
- Use vague branch names (dev, test, temp)
- Merge without code review
- Mix multiple features in one branch
- Force push to shared branches
- Ignore failing CI checks
- Merge with merge commits in TBD

## Branch Protection Rules (GitHub)

```yaml
# .github/branch-protection-rules.yml
branches:
  main:
    required_status_checks: true
    required_code_review: true
    dismiss_stale_reviews: true
    require_branches_up_to_date: true
    enforce_admins: true
    required_signatures: false
```

## Resources

- [Git Branching Strategies](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [A Successful Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Trunk Based Development](https://trunkbaseddevelopment.com/)
