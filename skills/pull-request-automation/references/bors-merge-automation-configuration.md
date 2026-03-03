# Bors: Merge Automation Configuration

## Bors: Merge Automation Configuration

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


## Conventional Commit Validation

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
