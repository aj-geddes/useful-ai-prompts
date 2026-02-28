# Claude Code Hooks Library

A comprehensive collection of production-ready hooks for Claude Code to enhance your development workflow with automated security scanning, testing, formatting, and more.

## Overview

This library contains 6 professional hooks that automate common development tasks:

1. **[security-scan](security-scan/)** - Scan for secrets and API keys before commits
2. **[test-runner](test-runner/)** - Automatically run tests before commits
3. **[session-setup](session-setup/)** - Initialize development environment on session start
4. **[auto-format](auto-format/)** - Auto-format code after file edits
5. **[breaking-change-detection](breaking-change-detection/)** - Detect breaking API changes
6. **[dependency-check](dependency-check/)** - Check for vulnerable dependencies

## Quick Start

### Installation

1. Choose the hooks you want to use from the list above
2. Copy the hook directory to your project:

```bash
# Copy a single hook
cp -r hooks/security-scan /your/project/.claude/hooks/

# Or copy all hooks
cp -r hooks/* /your/project/.claude/hooks/
```

3. Configure in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/.claude/hooks/security-scan/hook.sh",
        "description": "Scan for secrets before commits"
      },
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/.claude/hooks/test-runner/hook.sh",
        "description": "Run tests before commits"
      }
    ],
    "PostToolUse": [
      {
        "pattern": "^(Edit|Write)$",
        "command": "/absolute/path/to/.claude/hooks/auto-format/hook.sh",
        "description": "Auto-format code after edits"
      }
    ],
    "SessionStart": [
      {
        "command": "/absolute/path/to/.claude/hooks/session-setup/hook.sh",
        "description": "Initialize development environment"
      }
    ]
  }
}
```

## Hook Descriptions

### 1. Security Scan

**Type:** PreToolUse (before git commits)

Prevents accidental exposure of secrets by scanning for:

- AWS keys and secrets
- API tokens and keys
- Private keys (RSA, SSH, PEM)
- Database connection strings
- Passwords and secrets
- OAuth tokens and JWTs

[View Documentation](security-scan/README.md)

**Quick Example:**

```json
{
  "pattern": "^Bash$",
  "command": "/path/to/hooks/security-scan/hook.sh",
  "description": "Scan for secrets before commits"
}
```

### 2. Test Runner

**Type:** PreToolUse (before git commits)

Automatically runs tests before commits to ensure code quality:

- Auto-detects test framework (Jest, pytest, RSpec, Go test, etc.)
- Runs tests for changed files
- Blocks commits if tests fail
- Shows detailed test results

[View Documentation](test-runner/README.md)

**Quick Example:**

```json
{
  "pattern": "^Bash$",
  "command": "/path/to/hooks/test-runner/hook.sh",
  "description": "Run tests before commits"
}
```

### 3. Session Setup

**Type:** SessionStart (when Claude Code session starts)

Initializes your development environment:

- Loads environment variables from .env
- Checks required dependencies
- Verifies runtime versions
- Tests database connections
- Shows git status and TODO reminders

[View Documentation](session-setup/README.md)

**Quick Example:**

```json
{
  "command": "/path/to/hooks/session-setup/hook.sh",
  "description": "Initialize development environment"
}
```

### 4. Auto-Format

**Type:** PostToolUse (after file edits)

Automatically formats code after edits:

- Detects file type and runs appropriate formatter
- Supports Prettier, Black, RuboCop, gofmt, rustfmt, etc.
- Shows formatting changes
- Optional auto-commit of formatting

[View Documentation](auto-format/README.md)

**Quick Example:**

```json
{
  "pattern": "^(Edit|Write)$",
  "command": "/path/to/hooks/auto-format/hook.sh",
  "description": "Auto-format code after edits"
}
```

### 5. Breaking Change Detection

**Type:** PreToolUse (before git commits)

Prevents unintentional breaking changes:

- Compares API signatures before/after
- Detects removed functions and classes
- Identifies changed function parameters
- Warns about modified public interfaces

[View Documentation](breaking-change-detection/README.md)

**Quick Example:**

```json
{
  "pattern": "^Bash$",
  "command": "/path/to/hooks/breaking-change-detection/hook.sh",
  "description": "Detect breaking API changes"
}
```

### 6. Dependency Check

**Type:** PreToolUse (before git commits)

Checks for vulnerable dependencies:

- Runs npm audit, pip-audit, bundle audit, etc.
- Blocks commits with high-severity vulnerabilities
- Suggests upgrade paths
- Generates security reports

[View Documentation](dependency-check/README.md)

**Quick Example:**

```json
{
  "pattern": "^Bash$",
  "command": "/path/to/hooks/dependency-check/hook.sh",
  "description": "Check for vulnerable dependencies"
}
```

## Hook Types

Claude Code supports three types of hooks:

### PreToolUse

Runs **before** a tool is executed. Common uses:

- Validate input before operations
- Check conditions before commits
- Scan for issues before changes

**Configuration:**

```json
{
  "PreToolUse": [
    {
      "pattern": "^Bash$", // Regex matching tool name
      "command": "/path/to/hook.sh",
      "description": "Hook description"
    }
  ]
}
```

### PostToolUse

Runs **after** a tool is executed. Common uses:

- Format code after edits
- Generate documentation after changes
- Update indexes after file operations

**Configuration:**

```json
{
  "PostToolUse": [
    {
      "pattern": "^(Edit|Write)$", // Match multiple tools
      "command": "/path/to/hook.sh",
      "description": "Hook description"
    }
  ]
}
```

### SessionStart

Runs when a Claude Code session starts. Common uses:

- Initialize environment
- Load configuration
- Display project status
- Start required services

**Configuration:**

```json
{
  "SessionStart": [
    {
      "command": "/path/to/hook.sh",
      "description": "Hook description"
    }
  ]
}
```

## Complete Example Configuration

Here's a complete `.claude/settings.json` with all hooks:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/.claude/hooks/security-scan/hook.sh",
        "description": "Scan for secrets before commits"
      },
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/.claude/hooks/test-runner/hook.sh",
        "description": "Run tests before commits"
      },
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/.claude/hooks/breaking-change-detection/hook.sh",
        "description": "Detect breaking API changes"
      },
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/.claude/hooks/dependency-check/hook.sh",
        "description": "Check for vulnerable dependencies"
      }
    ],
    "PostToolUse": [
      {
        "pattern": "^(Edit|Write)$",
        "command": "/absolute/path/to/.claude/hooks/auto-format/hook.sh",
        "description": "Auto-format code after edits"
      }
    ],
    "SessionStart": [
      {
        "command": "/absolute/path/to/.claude/hooks/session-setup/hook.sh",
        "description": "Initialize development environment"
      }
    ]
  }
}
```

## Recommended Combinations

### For Security-Focused Projects

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/path/to/hooks/security-scan/hook.sh"
      },
      {
        "pattern": "^Bash$",
        "command": "/path/to/hooks/dependency-check/hook.sh"
      }
    ]
  }
}
```

### For Library/Framework Development

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/path/to/hooks/test-runner/hook.sh"
      },
      {
        "pattern": "^Bash$",
        "command": "/path/to/hooks/breaking-change-detection/hook.sh"
      }
    ],
    "PostToolUse": [
      {
        "pattern": "^(Edit|Write)$",
        "command": "/path/to/hooks/auto-format/hook.sh"
      }
    ]
  }
}
```

### For Application Development

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/path/to/hooks/test-runner/hook.sh"
      },
      {
        "pattern": "^Bash$",
        "command": "/path/to/hooks/security-scan/hook.sh"
      }
    ],
    "PostToolUse": [
      {
        "pattern": "^(Edit|Write)$",
        "command": "/path/to/hooks/auto-format/hook.sh"
      }
    ],
    "SessionStart": [
      {
        "command": "/path/to/hooks/session-setup/hook.sh"
      }
    ]
  }
}
```

## Features Common to All Hooks

All hooks in this library include:

- **Comprehensive Documentation** - Detailed README with examples
- **Production-Ready** - Robust error handling and input validation
- **Configurable** - Extensive configuration options
- **Multi-Language Support** - Works with multiple programming languages
- **Best Practices** - Follows industry standards
- **Customizable** - Easy to modify for your needs
- **Well-Commented** - Clear code comments for understanding
- **Exit Codes** - Proper exit codes for CI/CD integration

## Customization

Each hook can be customized through:

1. **Configuration Files** - `.hookconfig` files in project root
2. **Environment Variables** - Override settings via environment
3. **Whitelist Files** - Exclude specific items from checks
4. **Script Modification** - Edit bash scripts directly

See individual hook documentation for specific customization options.

## Troubleshooting

### Hooks Not Running

Check:

1. Hook script is executable: `chmod +x hook.sh`
2. Path in settings.json is absolute and correct
3. Pattern matches the tool being used
4. No syntax errors: `bash -n hook.sh`

### Permission Errors

```bash
# Make all hooks executable
chmod +x hooks/*/hook.sh

# Or individually
chmod +x hooks/security-scan/hook.sh
```

### Path Issues

Use absolute paths in settings.json:

```bash
# Get absolute path
readlink -f hooks/security-scan/hook.sh

# Use in settings.json
"/home/user/project/.claude/hooks/security-scan/hook.sh"
```

### Performance Issues

- Disable hooks temporarily: Set `"disabled": true` in config
- Run only essential hooks in development
- Use full suite in CI/CD

## Best Practices

### 1. Start Small

Don't enable all hooks at once:

```
Day 1: Add session-setup
Day 2: Add auto-format
Day 3: Add security-scan
etc.
```

### 2. Configure Appropriately

Tune hook settings for your workflow:

- Use `permissive` mode during development
- Use `strict` mode in CI/CD
- Whitelist known issues

### 3. Document Your Setup

Add to your project README:

```markdown
## Development Setup

This project uses Claude Code hooks for:

- Security scanning
- Automated testing
- Code formatting

See `.claude/settings.json` for configuration.
```

### 4. Team Consistency

Share hook configuration across team:

```bash
# Commit hooks configuration
git add .claude/settings.json
git add hooks/

# Team members get same hooks
```

### 5. Monitor Performance

Track hook execution time:

```bash
# Add timing to hooks
time ./hook.sh

# Optimize slow hooks
# Consider caching results
```

### 6. CI/CD Integration

Run same hooks in CI:

```yaml
# .github/workflows/ci.yml
- name: Run Hooks
  run: |
    ./.claude/hooks/security-scan/hook.sh
    ./.claude/hooks/test-runner/hook.sh
```

## Contributing

To add a new hook:

1. Create directory: `hooks/my-hook/`
2. Add `README.md` with full documentation
3. Add `hook.sh` with implementation
4. Make executable: `chmod +x hook.sh`
5. Update this README with hook description

## License

MIT License - Use freely in your projects

## Support

For issues or questions:

- Check individual hook documentation
- Review troubleshooting sections
- Open an issue in the repository

## Credits

Created for the Claude Code community. Contributions welcome!
