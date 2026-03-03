# Commit Message Validation

## Commit Message Validation

```bash
#!/bin/bash
# .husky/commit-msg

# Validate commit message format
COMMIT_MSG=$(<"$1")

# Pattern: type(scope): description
PATTERN="^(feat|fix|docs|style|refactor|test|chore|perf)(\([a-z\-]+\))?: .{1,50}"

if ! [[ $COMMIT_MSG =~ $PATTERN ]]; then
    echo "❌ Invalid commit message format"
    echo "Format: type(scope): description"
    echo "Types: feat, fix, docs, style, refactor, test, chore, perf"
    echo ""
    echo "Examples:"
    echo "  feat: add new feature"
    echo "  fix(auth): resolve login bug"
    echo "  docs: update README"
    exit 1
fi

# Check message length
FIRST_LINE=$(echo "$COMMIT_MSG" | head -n1)
if [ ${#FIRST_LINE} -gt 72 ]; then
    echo "❌ Commit message too long (max 72 characters)"
    exit 1
fi

echo "✅ Commit message is valid"
```
