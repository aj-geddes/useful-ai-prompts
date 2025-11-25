---
date: '2025-01-01'
description: A PreToolUse hook that scans for secrets, API keys, and sensitive data
  before commits to prevent accidental exposure of credentials.
event_type: PreToolUse
features:
- AWS key detection
- API token scanning
- Private key detection
- 15+ secret patterns
- Whitelist support
- JSON output for CI/CD
icon: fa-shield-alt
icon_class: security
layout: hook
lines_of_code: 450
matcher: Bash
slug: security-scan
title: security-scan
---

A PreToolUse hook that scans for secrets, API keys, and sensitive data before commits to prevent accidental exposure of credentials.

## Features

- Detects AWS keys, API tokens, private keys, and other sensitive data
- Scans for common secret patterns using regex
- Blocks commits containing exposed secrets
- Provides clear remediation guidance
- Customizable pattern matching
- Whitelist support for false positives
- JSON output for integration with CI/CD

## Configuration

Add this to your `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/hooks/security-scan/hook.sh",
        "description": "Scan for secrets and sensitive data before git commits"
      }
    ]
  }
}
```

Or for more specific git commit detection:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/hooks/security-scan/hook.sh",
        "description": "Scan for secrets before git commits",
        "disabled": false
      }
    ]
  }
}
```

## Installation

### 1. Install Dependencies

The hook uses standard Unix tools (grep, awk, sed) that are typically pre-installed. For enhanced scanning, optionally install:

```bash
# Optional: Install gitleaks for advanced secret scanning
# macOS
brew install gitleaks

# Linux
wget https://github.com/gitleaks/gitleaks/releases/download/v8.18.0/gitleaks_8.18.0_linux_x64.tar.gz
tar -xzf gitleaks_8.18.0_linux_x64.tar.gz
sudo mv gitleaks /usr/local/bin/

# Or use the built-in regex patterns (no dependencies required)
```

### 2. Set Up the Hook

```bash
# Copy the hook to your project
cp hook.sh /path/to/your/project/.claude/hooks/security-scan.sh
chmod +x /path/to/your/project/.claude/hooks/security-scan.sh

# Update .claude/settings.json with the correct path
```

### 3. Configure Whitelist (Optional)

Create a `.secretsignore` file in your project root to whitelist false positives:

```
# .secretsignore - patterns to exclude from secret scanning
example-key-in-documentation
test-api-key-12345
dummy-secret-for-tests
```

## Usage

The hook automatically runs before git commits. When a potential secret is detected:

```
🔒 Security Scan Starting...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ SECURITY ISSUE DETECTED

Found 2 potential secret(s) in staged files:

  📄 config/database.yml
     Line 12: aws_access_key_id: AKIAIOSFODNN7EXAMPLE
     Pattern: AWS Access Key

  📄 src/api.js
     Line 45: const apiKey = "sk-1234567890abcdef"
     Pattern: API Key

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  COMMIT BLOCKED - Remove secrets before committing

Remediation steps:
  1. Remove the secrets from your code
  2. Use environment variables instead: process.env.API_KEY
  3. Add secrets to .env file (ensure .env is in .gitignore)
  4. Update .secretsignore if these are false positives
  5. Rotate any exposed credentials immediately

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Customization

### Adding Custom Patterns

Edit the `hook.sh` script to add custom secret patterns:

```bash
# Add to the PATTERNS array
declare -A PATTERNS=(
    # Existing patterns...

    # Custom patterns
    ["Custom API Key"]='custom-api-[a-zA-Z0-9]{32}'
    ["Internal Token"]='internal_token_[a-f0-9]{40}'
    ["Database Password"]='db_password\s*=\s*["\x27][^"\x27]{8,}["\x27]'
)
```

### Adjusting Sensitivity

Configure the scanning level:

```bash
# In hook.sh, set the scanning mode
SCAN_MODE="strict"   # Block all potential secrets
# SCAN_MODE="normal"   # Block obvious secrets only
# SCAN_MODE="permissive"  # Warn but allow commits
```

### Whitelist Configuration

The `.secretsignore` file supports:

```
# Exact matches
example-api-key-12345

# Wildcards
test-*-key
*-example-*

# File-specific
config/test.yml:dummy-secret

# Comments and blank lines are ignored
```

## Best Practices

### 1. Run Before Every Commit

Always keep this hook enabled to prevent accidental secret exposure.

### 2. Use Environment Variables

Replace hardcoded secrets with environment variables:

```javascript
// Bad
const apiKey = "sk-1234567890abcdef";

// Good
const apiKey = process.env.API_KEY;
```

### 3. Maintain .gitignore

Ensure sensitive files are ignored:

```
# .gitignore
.env
.env.local
secrets/
credentials.json
*.pem
*.key
```

### 4. Rotate Exposed Credentials

If secrets are accidentally committed:
1. Rotate/revoke the exposed credentials immediately
2. Remove secrets from git history using `git filter-branch` or BFG Repo-Cleaner
3. Force push the cleaned history (coordinate with team)

### 5. Regular Pattern Updates

Keep secret patterns up-to-date with new services and key formats:

```bash
# Periodically review and update patterns
# Check security advisories for new key formats
# Add organization-specific patterns
```

### 6. Team Coordination

- Document whitelisted patterns
- Share .secretsignore across team
- Establish secret rotation procedures
- Train team on secure credential management

### 7. Integration with CI/CD

Export scan results for pipeline integration:

```bash
# Enable JSON output
SECURITY_SCAN_JSON=1 ./hook.sh

# Integrate with CI
- name: Security Scan
  run: |
    if ! ./.claude/hooks/security-scan.sh; then
      echo "Security issues detected"
      exit 1
    fi
```

### 8. Performance Optimization

For large repositories:

```bash
# Scan only staged files (default)
# Or scan entire repository periodically
SCAN_ALL=1 ./hook.sh

# Exclude large binary files
# Add to .secretsignore: *.pdf, *.zip, *.tar.gz
```

## Supported Secret Types

- AWS Access Keys (AKIA...)
- AWS Secret Keys
- GitHub Personal Access Tokens
- API Keys (generic patterns)
- Private Keys (RSA, SSH, PEM)
- OAuth Tokens
- JWT Tokens
- Database Connection Strings
- Password assignments
- Slack Tokens
- Stripe API Keys
- Google API Keys
- Azure Keys
- And more...

## Troubleshooting

### False Positives

If the hook incorrectly flags safe content:

1. Add to `.secretsignore`
2. Adjust pattern sensitivity
3. Use inline comments: `# nosecret`

### Hook Not Running

Check:
- Hook script is executable: `chmod +x hook.sh`
- Path in settings.json is absolute and correct
- Pattern matches the tool being used (e.g., "^Bash$")

### Performance Issues

For very large files or repositories:

```bash
# Add file size limits
MAX_FILE_SIZE=1048576  # 1MB limit

# Exclude directories
EXCLUDED_DIRS="node_modules|vendor|.git"
```

## License

MIT License - Use freely in your projects

## Contributing

Contributions welcome! Please submit:
- New secret patterns
- Performance improvements
- Additional features
- Bug fixes

## Security Disclosure

If you discover a security vulnerability in this hook, please email security@example.com (replace with your contact).