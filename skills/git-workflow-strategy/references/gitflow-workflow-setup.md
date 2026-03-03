# GitFlow Workflow Setup

## GitFlow Workflow Setup

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


## GitHub Flow Workflow

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


## Trunk-Based Development

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


## Git Configuration for Workflows

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


## Branch Naming Conventions

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
