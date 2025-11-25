---
date: '2025-01-01'
description: Automatically run linters before committing code to catch issues early.
event_type: PreToolUse
features: []
icon: fa-code
icon_class: default
layout: hook
lines_of_code: 300
matcher: Bash
slug: pre-commit-linting
title: pre-commit-linting
---

Automatically run linters before committing code to catch issues early.

## Hook Configuration

Add to your `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/pre-commit-linting/check.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Hook Script

Save as `.claude/hooks/pre-commit-linting/check.sh`:

```bash
#!/bin/bash
set -euo pipefail

# Parse hook input
INPUT=$(cat)
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Only check git commit commands
if [[ ! "$TOOL_INPUT" =~ git[[:space:]]+commit ]]; then
    echo '{"continue": true, "suppressOutput": true}'
    exit 0
fi

# Run linters
echo "Running pre-commit linters..." >&2

ERRORS=()

# ESLint for JavaScript/TypeScript
if command -v eslint &> /dev/null && [ -f .eslintrc.json ] || [ -f .eslintrc.js ]; then
    if ! eslint . --max-warnings 0 2>&1; then
        ERRORS+=("ESLint found issues")
    fi
fi

# Prettier for formatting
if command -v prettier &> /dev/null && [ -f .prettierrc ]; then
    if ! prettier --check . 2>&1; then
        ERRORS+=("Prettier formatting issues found")
    fi
fi

# Pylint for Python
if command -v pylint &> /dev/null && find . -name "*.py" -not -path "./venv/*" | head -1 | grep -q .; then
    if ! pylint **/*.py --fail-under=8.0 2>&1; then
        ERRORS+=("Pylint found issues")
    fi
fi

# RuboCop for Ruby
if command -v rubocop &> /dev/null && [ -f .rubocop.yml ]; then
    if ! rubocop 2>&1; then
        ERRORS+=("RuboCop found issues")
    fi
fi

# Report results
if [ ${#ERRORS[@]} -gt 0 ]; then
    ERROR_MSG="Pre-commit linting failed:\\n"
    for error in "${ERRORS[@]}"; do
        ERROR_MSG+="  - $error\\n"
    done
    ERROR_MSG+="\\nPlease fix these issues before committing."

    echo "{\"permissionDecision\": \"deny\", \"reason\": \"$ERROR_MSG\"}" | jq -c
    exit 2
fi

echo '{"permissionDecision": "allow"}'
exit 0
```

## Setup

1. Make the script executable:
```bash
chmod +x .claude/hooks/pre-commit-linting/check.sh
```

2. Install linters for your stack:

**JavaScript/TypeScript:**
```bash
npm install --save-dev eslint prettier
npx eslint --init
```

**Python:**
```bash
pip install pylint black
```

**Ruby:**
```bash
gem install rubocop
```

3. Configure each linter with project-specific rules

## Features

- ✅ Automatically runs before git commits
- ✅ Checks multiple file types (JS, TS, Python, Ruby)
- ✅ Blocks commits with linting errors
- ✅ Fast execution with 30-second timeout
- ✅ Provides clear error messages
- ✅ Skips non-commit Bash commands

## Customization

Add more linters by extending the script:

```bash
# Go
if command -v golangci-lint &> /dev/null && [ -f go.mod ]; then
    if ! golangci-lint run 2>&1; then
        ERRORS+=("golangci-lint found issues")
    fi
fi

# Rust
if command -v cargo &> /dev/null && [ -f Cargo.toml ]; then
    if ! cargo clippy -- -D warnings 2>&1; then
        ERRORS+=("Clippy found issues")
    fi
fi
```

## Bypassing (When Necessary)

For emergency commits, you can temporarily disable:

```bash
# Commit without hooks
git commit --no-verify -m "Emergency fix"
```

## Best Practices

- Keep linting rules consistent across team
- Run linters in CI/CD as well
- Auto-fix when possible (prettier --write)
- Configure IDE integration for real-time feedback
- Use .gitignore patterns to exclude generated files