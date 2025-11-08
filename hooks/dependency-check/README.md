# Dependency Check Hook

A PreToolUse hook that checks for vulnerable dependencies before commits to prevent security vulnerabilities in your project.

## Features

- Runs npm audit, pip-audit, bundle audit, and other security scanners
- Blocks commits with high-severity vulnerabilities
- Suggests upgrade paths for vulnerable packages
- Generates detailed security reports
- Supports multiple package managers (npm, yarn, pip, bundler, cargo, etc.)
- Configurable severity thresholds
- Whitelist for accepted vulnerabilities
- Integration with security databases (CVE, npm advisory, etc.)
- Auto-fix suggestions for known vulnerabilities

## Configuration

Add this to your `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/hooks/dependency-check/hook.sh",
        "description": "Check for vulnerable dependencies before commits"
      }
    ]
  }
}
```

## Installation

### 1. Install Security Audit Tools

Install audit tools for your package manager:

```bash
# JavaScript/TypeScript - npm audit (built-in)
# No installation needed

# Python - pip-audit
pip install pip-audit

# Ruby - bundler-audit
gem install bundler-audit

# Rust - cargo audit
cargo install cargo-audit

# Go - govulncheck
go install golang.org/x/vuln/cmd/govulncheck@latest

# PHP - composer audit (built-in with Composer 2.4+)
# No installation needed
```

### 2. Set Up the Hook

```bash
# Copy the hook to your project
cp hook.sh /path/to/your/project/.claude/hooks/dependency-check.sh
chmod +x /path/to/your/project/.claude/hooks/dependency-check.sh

# Update .claude/settings.json with the correct path
```

### 3. Configure Security Policy

Create a `.dependency-check.yml` file in your project root:

```yaml
# .dependency-check.yml - Dependency security configuration

# Enable dependency checking
enabled: true

# Severity threshold: low, moderate, high, critical
# Block commits with vulnerabilities at or above this level
block_threshold: high

# Warn threshold: show warnings but don't block
warn_threshold: moderate

# Auto-fix vulnerabilities when possible
auto_fix: false

# Check on specific events
check_on_commit: true
check_on_dependency_change: true

# Package managers to check
package_managers:
  - npm
  - pip
  - bundler
  - cargo
  - go

# Whitelist known vulnerabilities
whitelist:
  - id: CVE-2023-12345
    reason: "False positive, not applicable to our use case"
    expires: "2025-12-31"

  - id: GHSA-xxxx-yyyy-zzzz
    reason: "Fix not yet available, mitigated with workaround"
    ticket: "SEC-123"

# Exclude dependencies from checking
exclude:
  - package: "lodash"
    versions: ["4.17.20"]
    reason: "Dev dependency only"

# Reporting
report:
  format: json  # json, text, sarif
  output: .security-report.json
  include_fix_suggestions: true
```

## Usage

The hook runs automatically before git commits:

```
🔒 Dependency Security Check Starting...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Scanning dependencies for vulnerabilities...

📦 npm audit
   Scanning 847 packages...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ VULNERABILITIES FOUND

🔴 HIGH Severity (2 vulnerabilities)

  Package: axios
  Version: 0.21.1
  Vulnerability: Server-Side Request Forgery (SSRF)
  CVE: CVE-2023-45857
  Recommendation: Upgrade to axios@1.6.1 or later

  Package: lodash
  Version: 4.17.20
  Vulnerability: Prototype Pollution
  CVE: CVE-2021-23337
  Recommendation: Upgrade to lodash@4.17.21 or later

🟡 MODERATE Severity (3 vulnerabilities)

  Package: moment
  Version: 2.29.1
  Vulnerability: Regular Expression Denial of Service
  CVE: CVE-2022-31129
  Recommendation: Migrate to alternative (dayjs, date-fns)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Summary:
  Total Vulnerabilities: 5
  Critical: 0
  High: 2 ❌
  Moderate: 3 ⚠️
  Low: 0

⚠️  COMMIT BLOCKED - High severity vulnerabilities detected

Recommended actions:
  1. Review vulnerabilities above
  2. Update vulnerable packages: npm audit fix
  3. For breaking changes: npm audit fix --force
  4. Verify fixes: npm audit
  5. Add to whitelist if vulnerability is not applicable

Quick fix:
  npm audit fix

Detailed report:
  See .security-report.json for full details

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Supported Package Managers

### JavaScript/TypeScript

**npm**
```bash
npm audit
npm audit fix         # Auto-fix
npm audit fix --force # Force fix with breaking changes
```

**yarn**
```bash
yarn audit
yarn audit --level high
```

**pnpm**
```bash
pnpm audit
pnpm audit --fix
```

### Python

**pip-audit**
```bash
pip-audit
pip-audit --fix       # Auto-fix
pip-audit --format json
```

**safety**
```bash
safety check
safety check --json
```

### Ruby

**bundler-audit**
```bash
bundle audit
bundle audit update   # Update vulnerability database
```

### Rust

**cargo-audit**
```bash
cargo audit
cargo audit --fix     # Auto-fix with cargo-edit
```

### Go

**govulncheck**
```bash
govulncheck ./...
govulncheck -json ./...
```

### PHP

**composer audit**
```bash
composer audit
composer audit --format json
```

### Java/Maven

**OWASP Dependency Check**
```bash
mvn org.owasp:dependency-check-maven:check
```

**Snyk**
```bash
snyk test
snyk monitor
```

## Customization

### Severity Thresholds

Configure what blocks commits:

```yaml
# Block on critical and high
block_threshold: high

# Block only on critical
block_threshold: critical

# Block on all severities
block_threshold: low

# Never block (warnings only)
block_threshold: none
```

### Auto-Fix

Enable automatic vulnerability fixes:

```yaml
auto_fix: true

# Package manager specific
auto_fix_npm: true
auto_fix_pip: true
auto_fix_cargo: true
```

### Selective Scanning

Scan only specific files or dependencies:

```yaml
# Only scan when package files change
scan_on_lockfile_change: true

# Files to watch
watch_files:
  - package.json
  - package-lock.json
  - requirements.txt
  - Gemfile.lock
  - Cargo.lock
```

### Whitelist Management

Accept known vulnerabilities:

```yaml
whitelist:
  # Whitelist by CVE
  - id: CVE-2023-12345
    reason: "Not exploitable in our context"

  # Whitelist by package
  - package: lodash
    version: "4.17.20"
    reason: "Dev dependency only"

  # Temporary whitelist with expiration
  - id: GHSA-xxxx-yyyy-zzzz
    expires: "2025-12-31"
    reason: "Waiting for fix release"
```

### Custom Security Policies

Define organization-wide policies:

```yaml
policies:
  # Disallow specific packages
  disallowed_packages:
    - event-stream  # Known malicious package
    - flatmap-stream

  # Require minimum versions
  minimum_versions:
    lodash: "4.17.21"
    axios: "1.6.0"

  # Require security updates within timeframe
  security_update_sla:
    critical: 1  # 1 day
    high: 7      # 7 days
    moderate: 30 # 30 days
```

## Best Practices

### 1. Regular Audits

Run audits regularly:

```bash
# Daily automated audits
cron: "0 9 * * * cd /project && npm audit"

# CI/CD integration
# Run on every PR and main branch commit
```

### 2. Keep Dependencies Updated

Maintain current dependencies:

```bash
# Check for updates
npm outdated
pip list --outdated
bundle outdated

# Update regularly
npm update
pip install -U -r requirements.txt
bundle update
```

### 3. Use Lock Files

Commit lock files for reproducible builds:

```bash
# Commit these files
package-lock.json
yarn.lock
Pipfile.lock
Gemfile.lock
Cargo.lock
```

### 4. Dependency Review

Review new dependencies before adding:

```bash
# Check package reputation
npm info package-name
pip show package-name

# Check for security history
# Review GitHub issues
# Check download statistics
```

### 5. Minimal Dependencies

Keep dependencies minimal:

```bash
# Regular dependency cleanup
npm prune
pip-autoremove

# Question each dependency
# "Do we really need this?"
```

### 6. Security Policies

Establish security guidelines:

```markdown
# Security Policy

## Dependency Management

1. All dependencies must pass security audit
2. High/Critical vulnerabilities must be fixed within 7 days
3. Use specific versions, not ranges (in production)
4. Review dependencies in PR process
5. Update dependencies monthly
```

### 7. Incident Response

Plan for security incidents:

```bash
# When vulnerability found:
1. Assess impact and severity
2. Check if actively exploited
3. Apply fix or mitigation
4. Test thoroughly
5. Deploy fix
6. Document incident
```

### 8. Monitoring

Continuous security monitoring:

```bash
# Use security services
Snyk
GitHub Dependabot
WhiteSource
Sonatype Nexus

# Enable automated alerts
# Set up Slack/email notifications
```

## Advanced Features

### Security Reporting

Generate comprehensive reports:

```bash
# JSON report for automation
npm audit --json > audit.json

# SARIF format for GitHub
pip-audit --format sarif > audit.sarif

# Upload to GitHub
gh api repos/:owner/:repo/code-scanning/sarifs \
  -F sarif=@audit.sarif
```

### Dependency Graph Analysis

Analyze dependency trees:

```bash
# Show dependency tree
npm ls
pip show --verbose package

# Find who requires vulnerable package
npm ls vulnerable-package
pip show vulnerable-package
```

### License Compliance

Check dependency licenses:

```bash
# npm license checker
npx license-checker

# Python license checker
pip-licenses

# Ensure compatible licenses
# No GPL in proprietary software
```

### Supply Chain Security

Protect against supply chain attacks:

```bash
# Verify package integrity
npm audit signatures

# Use package lock files
# Pin exact versions in production
# Monitor for suspicious updates
```

### Automated Remediation

Auto-fix and create PRs:

```bash
# Dependabot configuration
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
```

### Vulnerability Database

Maintain custom vulnerability database:

```yaml
# custom-vulnerabilities.yml
vulnerabilities:
  - id: INTERNAL-2025-001
    package: internal-package
    severity: high
    description: "Custom vulnerability"
    fix: "Upgrade to 2.0.0"
```

## Integration with CI/CD

### GitHub Actions

```yaml
# .github/workflows/security-check.yml
name: Security Check
on: [push, pull_request]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Run Security Audit
        run: |
          npm audit --audit-level=high
          if [ $? -ne 0 ]; then
            echo "Security vulnerabilities found!"
            exit 1
          fi

      - name: Upload Results
        if: failure()
        uses: actions/upload-artifact@v2
        with:
          name: security-report
          path: .security-report.json
```

### GitLab CI

```yaml
# .gitlab-ci.yml
security-check:
  stage: test
  script:
    - npm audit --audit-level=high
  allow_failure: false
```

### Jenkins

```groovy
// Jenkinsfile
stage('Security Check') {
    steps {
        sh 'npm audit --audit-level=high'
        sh 'pip-audit'
    }
}
```

## Troubleshooting

### False Positives

If audit reports false positives:

```yaml
# Add to whitelist
whitelist:
  - id: CVE-XXXX
    reason: "Not applicable - dev dependency"
```

### Audit Failures

If audit command fails:

```bash
# Update audit database
npm audit fix
bundle audit update

# Clear cache
npm cache clean --force
pip cache purge
```

### Performance Issues

For slow audits:

```bash
# Skip audit for dev dependencies
npm audit --production-only

# Use cached results
# Run audit less frequently
```

### No Fix Available

When fix is not available:

```yaml
# Document and whitelist
whitelist:
  - id: CVE-XXXX
    reason: "No fix available, risk accepted"
    mitigation: "Implemented input validation"
    ticket: "SEC-123"
```

## Example Configurations

### Strict Security

```yaml
enabled: true
block_threshold: moderate
warn_threshold: low
auto_fix: false
check_on_commit: true
whitelist: []  # No exceptions
```

### Balanced Approach

```yaml
enabled: true
block_threshold: high
warn_threshold: moderate
auto_fix: true
check_on_commit: true
```

### Permissive (CI Only)

```yaml
enabled: true
block_threshold: critical
warn_threshold: high
auto_fix: false
check_on_commit: false  # Check in CI instead
```

## License

MIT License - Use freely in your projects

## Security Disclosure

If you discover a security vulnerability in this hook, please report it responsibly. Do not open a public issue. Contact the maintainers directly.
