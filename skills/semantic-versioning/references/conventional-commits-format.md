# Conventional Commits Format

## Conventional Commits Format

```bash
# Feature commit (MINOR bump)
git commit -m "feat: add new search feature"
git commit -m "feat(api): add pagination support"

# Bug fix commit (PATCH bump)
git commit -m "fix: resolve null pointer exception"
git commit -m "fix(auth): fix login timeout issue"

# Breaking change (MAJOR bump)
git commit -m "feat!: redesign API endpoints"
git commit -m "feat(api)!: remove deprecated methods"

# Documentation
git commit -m "docs: update README"

# Performance improvement
git commit -m "perf: optimize database queries"

# Refactoring
git commit -m "refactor: simplify authentication logic"

# Tests
git commit -m "test: add integration tests"

# Chore
git commit -m "chore: update dependencies"

# Complete example with body and footer
git commit -m "feat(payment): add Stripe integration

Add support for processing credit card payments via Stripe.
Includes webhook handling for payment confirmations.

BREAKING CHANGE: Payment API endpoint changed from /pay to /api/v2/payments
Closes #123"
```
