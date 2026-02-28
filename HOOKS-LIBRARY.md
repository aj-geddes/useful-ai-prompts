# Claude Code Hooks Library

## Overview

A comprehensive collection of production-ready hooks for Claude Code. Hooks enable automated validation, testing, formatting, and environment setup at key points in your development workflow.

**Total Hooks**: 6 comprehensive examples covering all major use cases

## What Are Hooks?

Hooks are automated scripts that execute at specific events in Claude Code's workflow. They enable:

- **Automated Quality Control**: Run linters, tests, and security scans automatically
- **Environment Setup**: Initialize development environment on session start
- **Code Formatting**: Auto-format code after edits
- **Security**: Prevent commits with exposed secrets or vulnerable dependencies
- **Breaking Change Detection**: Warn before committing API-breaking changes

## Quick Start

### 1. Copy Hooks to Your Project

```bash
# Copy all hooks
cp -r hooks/ /path/to/your/project/.claude/hooks/

# Or copy individual hooks
cp -r hooks/security-scan /path/to/your/project/.claude/hooks/
```

### 2. Configure in Settings

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan/hook.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### 3. Make Scripts Executable

```bash
chmod +x .claude/hooks/*/hook.sh
```

## Available Hooks

### 🔒 security-scan

**Event:** PreToolUse (Bash) | **Purpose:** Prevent secret leaks

Scans for exposed secrets before commits:

- AWS keys, API tokens, private keys
- Database credentials and passwords
- 15+ secret pattern detections
- Whitelist support via `.secretsignore`

```json
{
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan/hook.sh"
        }
      ]
    }
  ]
}
```

**Key Features:**

- ✅ Blocks commits with exposed secrets
- ✅ Clear remediation guidance
- ✅ Configurable sensitivity levels
- ✅ False positive management

---

### ✅ test-runner

**Event:** PreToolUse (Bash) | **Purpose:** Run tests before commits

Automatically runs tests with smart framework detection:

- Jest, pytest, RSpec, Go test, Cargo test
- Runs tests for changed files only
- Parallel execution support
- Test result caching

```json
{
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/test-runner/hook.sh",
          "timeout": 300
        }
      ]
    }
  ]
}
```

**Key Features:**

- ✅ Multi-framework support
- ✅ Fast incremental testing
- ✅ Detailed failure reports
- ✅ Coverage tracking

---

### 🚀 session-setup

**Event:** SessionStart | **Purpose:** Initialize development environment

Prepares your environment on session start:

- Loads `.env` variables
- Checks dependency versions
- Verifies database connections
- Displays git status and reminders

```json
{
  "SessionStart": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/session-setup/hook.sh"
        }
      ]
    }
  ]
}
```

**Key Features:**

- ✅ Environment validation
- ✅ Dependency checking
- ✅ Status dashboard
- ✅ Project reminders

---

### 🎨 auto-format

**Event:** PostToolUse (Edit|Write) | **Purpose:** Auto-format code

Automatically formats code after edits:

- Prettier (JS/TS), Black (Python), RuboCop (Ruby)
- gofmt (Go), rustfmt (Rust), Spotless (Java)
- Shows formatting diff
- Optional auto-commit

```json
{
  "PostToolUse": [
    {
      "matcher": "Edit|Write",
      "hooks": [
        {
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/auto-format/hook.sh"
        }
      ]
    }
  ]
}
```

**Key Features:**

- ✅ 8+ language formatters
- ✅ Diff visualization
- ✅ Respects project configs
- ✅ Configurable behavior

---

### ⚠️ breaking-change-detection

**Event:** PreToolUse (Bash) | **Purpose:** Detect API breaking changes

Warns before committing breaking changes:

- Compares API signatures
- Detects removed exports
- Identifies parameter changes
- Semantic versioning integration

```json
{
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/breaking-change-detection/hook.sh"
        }
      ]
    }
  ]
}
```

**Key Features:**

- ✅ Multi-language support
- ✅ Signature comparison
- ✅ Clear change reports
- ✅ SemVer recommendations

---

### 🛡️ dependency-check

**Event:** PreToolUse (Bash) | **Purpose:** Check for vulnerable dependencies

Scans dependencies for security vulnerabilities:

- npm audit, pip-audit, bundle audit
- Severity-based blocking
- Auto-fix suggestions
- Security report generation

```json
{
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/dependency-check/hook.sh"
        }
      ]
    }
  ]
}
```

**Key Features:**

- ✅ 5+ package managers
- ✅ Configurable severity
- ✅ Upgrade suggestions
- ✅ Vulnerability whitelisting

---

## Hook Events Reference

| Event                | Trigger              | Common Uses                           |
| -------------------- | -------------------- | ------------------------------------- |
| **PreToolUse**       | Before tool executes | Validation, linting, security scans   |
| **PostToolUse**      | After tool completes | Auto-formatting, notifications        |
| **UserPromptSubmit** | User submits prompt  | Content filtering, policy enforcement |
| **SessionStart**     | Session begins       | Environment setup, status display     |
| **SessionEnd**       | Session ends         | Cleanup, report generation            |
| **Stop**             | Agent finishes       | Quality checks, summaries             |
| **Notification**     | Permission request   | Auto-approval rules                   |

## Recommended Configurations

### Minimal Setup (Security + Testing)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan/hook.sh"
          },
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/test-runner/hook.sh",
            "timeout": 300
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/session-setup/hook.sh"
          }
        ]
      }
    ]
  }
}
```

### Full Stack Development

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan/hook.sh"
          },
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/test-runner/hook.sh",
            "timeout": 300
          },
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/dependency-check/hook.sh"
          },
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/breaking-change-detection/hook.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/auto-format/hook.sh"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/session-setup/hook.sh"
          }
        ]
      }
    ]
  }
}
```

### API/Library Development

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/breaking-change-detection/hook.sh"
          },
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/test-runner/hook.sh",
            "timeout": 300
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/auto-format/hook.sh"
          }
        ]
      }
    ]
  }
}
```

## Hook Development Best Practices

### Input Validation

```bash
#!/bin/bash
set -euo pipefail

# Always parse and validate input
INPUT=$(cat)
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Validate before using
if [ -z "$TOOL_INPUT" ]; then
    echo '{"continue": true, "suppressOutput": true}'
    exit 0
fi
```

### Proper Quoting

```bash
# ✅ Good - variables are quoted
if [[ "$TOOL_INPUT" =~ git[[:space:]]+commit ]]; then
    FILES=$(git diff --cached --name-only --diff-filter=ACM)
    for FILE in "$FILES"; do
        check_file "$FILE"
    done
fi

# ❌ Bad - unquoted variables
if [[ $TOOL_INPUT =~ git commit ]]; then
    for FILE in $FILES; do
        check_file $FILE
    done
fi
```

### Error Handling

```bash
# Exit code 0: Success
echo '{"permissionDecision": "allow"}'
exit 0

# Exit code 2: Blocking error (fed to Claude)
echo '{"permissionDecision": "deny", "reason": "Tests failed"}'
exit 2

# Other codes: Non-blocking error (shown to user)
echo "Warning: Linter not found" >&2
exit 1
```

### Timeouts

```json
{
  "hooks": [
    {
      "type": "command",
      "command": "./hook.sh",
      "timeout": 300 // 5 minutes for slow operations
    }
  ]
}
```

## Security Considerations

⚠️ **Important**: Hooks execute arbitrary shell commands with your user permissions.

**Best Practices:**

1. ✅ Validate all input from hook JSON
2. ✅ Use absolute paths or `$CLAUDE_PROJECT_DIR`
3. ✅ Quote all variables
4. ✅ Check for path traversal (`..` in paths)
5. ✅ Review hook scripts before using
6. ✅ Use minimal permissions
7. ✅ Test in safe environment first

## Debugging

### Check Hook Registration

```bash
claude
> /hooks
```

### Debug Mode

```bash
claude --debug
```

### Test Hook Manually

```bash
# Simulate hook input
echo '{"tool_name":"Bash","tool_input":{"command":"git commit -m test"}}' | \
  .claude/hooks/security-scan/hook.sh
```

### Common Issues

**Hook not triggering:**

- Check matcher is case-sensitive and correct
- Verify script has executable permissions (`chmod +x`)
- Ensure JSON syntax is valid

**Permission errors:**

- Make scripts executable: `chmod +x .claude/hooks/*/hook.sh`
- Check file paths are correct

**Timeout errors:**

- Increase timeout value for slow operations
- Optimize hook script performance

## Contributing

To create custom hooks:

1. Create hook directory: `.claude/hooks/your-hook-name/`
2. Add `README.md` with documentation
3. Create `hook.sh` with script
4. Make executable: `chmod +x hook.sh`
5. Add configuration example
6. Test thoroughly

## Resources

- [Official Claude Code Hooks Documentation](https://code.claude.com/docs/en/hooks)
- [Hook Examples Repository](https://github.com/aj-geddes/useful-ai-prompts)
- [Settings Configuration Guide](https://code.claude.com/docs/en/settings)

---

**Total Hooks**: 6 production-ready examples
**Total Lines**: 6,135+ lines of code and documentation
**Languages Supported**: JavaScript, TypeScript, Python, Ruby, Go, Rust, PHP, Java, C/C++
**Package Managers**: npm, pip, bundler, cargo, go modules
