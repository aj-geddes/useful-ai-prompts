# Breaking Change Detection Hook

A PreToolUse hook that detects breaking API changes before commits to prevent unintentional breaking changes in your codebase.

## Features

- Compares API signatures before and after changes
- Detects removed functions, classes, and methods
- Identifies changed function parameters
- Detects changed return types
- Warns about modified public interfaces
- Supports multiple languages (JavaScript, TypeScript, Python, Ruby, Go, etc.)
- Configurable breaking change rules
- Whitelist for intentional breaking changes
- Generates breaking change reports
- Integrates with semantic versioning

## Configuration

Add this to your `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/hooks/breaking-change-detection/hook.sh",
        "description": "Detect breaking API changes before commits"
      }
    ]
  }
}
```

## Installation

### 1. Install Dependencies (Optional)

For enhanced analysis, install language-specific parsers:

```bash
# JavaScript/TypeScript - TypeScript compiler
npm install --save-dev typescript

# Python - AST analysis (built-in)
# No installation needed

# API diff tools (optional)
npm install -g api-extractor
pip install pydiff
```

### 2. Set Up the Hook

```bash
# Copy the hook to your project
cp hook.sh /path/to/your/project/.claude/hooks/breaking-change-detection.sh
chmod +x /path/to/your/project/.claude/hooks/breaking-change-detection.sh

# Update .claude/settings.json with the correct path
```

### 3. Configure Detection Rules

Create a `.breaking-changes.yml` file in your project root:

```yaml
# .breaking-changes.yml - Breaking change detection configuration

# Enable breaking change detection
enabled: true

# Strictness level: strict, normal, permissive
strictness: normal

# What constitutes a breaking change
rules:
  removed_exports: error      # Removed exported functions/classes
  renamed_exports: error      # Renamed exports
  changed_signatures: error   # Changed function parameters
  changed_types: warning      # Changed parameter or return types
  removed_properties: error   # Removed object properties
  changed_defaults: warning   # Changed default parameter values

# Files/patterns to check
include:
  - "src/**/*.ts"
  - "lib/**/*.js"
  - "api/**/*.py"

# Files/patterns to exclude
exclude:
  - "**/*.test.js"
  - "**/*.spec.ts"
  - "internal/**"

# Whitelist of allowed breaking changes
whitelist:
  - function: deprecatedFunction
    reason: "Scheduled for removal in v2.0"
  - class: OldAPI
    reason: "Migrating to NewAPI"

# Version checking
semver:
  enabled: true
  # Allow breaking changes only on major version bumps
  allow_on_major: true
```

## Usage

The hook runs automatically before git commits:

```
🔍 Breaking Change Detection Starting...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analyzing changes in 3 file(s)...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  BREAKING CHANGES DETECTED

📄 src/api/users.ts

  ❌ BREAKING: Function signature changed
     Function: createUser
     Before:  createUser(name: string, email: string)
     After:   createUser(data: UserData)
     Impact:  All callers must be updated

  ❌ BREAKING: Export removed
     Export:  deleteUser
     Impact:  Function no longer available to consumers

  ⚠️  WARNING: Return type changed
     Function: getUser
     Before:  User | null
     After:   Promise<User | undefined>
     Impact:  May affect type checking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Summary:
  Breaking Changes: 2
  Warnings: 1

⚠️  COMMIT BLOCKED - Breaking changes detected

Recommended actions:
  1. Review breaking changes above
  2. Update version to 2.0.0 (major bump required)
  3. Document breaking changes in CHANGELOG.md
  4. Update migration guide
  5. Add to .breaking-changes.yml whitelist if intentional

To bypass (not recommended):
  export ALLOW_BREAKING_CHANGES=true

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Detection Capabilities

### JavaScript/TypeScript

Detects:
- Removed exports (functions, classes, interfaces, types)
- Changed function signatures
- Changed parameter types
- Changed return types
- Removed class methods
- Changed method signatures
- Removed interface properties
- Changed enum values

```typescript
// Before
export function createUser(name: string, email: string) { }

// After - BREAKING
export function createUser(data: UserData) { }
```

### Python

Detects:
- Removed module exports
- Changed function signatures
- Changed parameter names or order
- Removed default parameters
- Changed class methods
- Removed class attributes
- Changed decorator usage

```python
# Before
def create_user(name, email, role="user"):
    pass

# After - BREAKING
def create_user(user_data):
    pass
```

### Ruby

Detects:
- Removed module/class definitions
- Changed method signatures
- Removed method parameters
- Changed parameter defaults
- Removed public methods
- Changed attr_accessor definitions

```ruby
# Before
def create_user(name, email, role: "user")
end

# After - BREAKING
def create_user(user_data)
end
```

### Go

Detects:
- Removed exported functions
- Changed function signatures
- Removed struct fields
- Changed struct field types
- Removed interface methods
- Changed method receivers

```go
// Before
func CreateUser(name string, email string) error { }

// After - BREAKING
func CreateUser(data UserData) error { }
```

## Customization

### Strictness Levels

Configure detection sensitivity:

```yaml
# .breaking-changes.yml

# Strict - Block all breaking changes
strictness: strict

# Normal - Block most, warn some (default)
strictness: normal

# Permissive - Only block obvious breaking changes
strictness: permissive
```

### Custom Rules

Define your own breaking change rules:

```yaml
rules:
  # Error on these changes
  removed_exports: error
  changed_signatures: error
  removed_properties: error

  # Warn but allow
  changed_types: warning
  changed_defaults: warning

  # Ignore
  internal_changes: ignore
```

### Version-Based Rules

Allow breaking changes based on version:

```yaml
semver:
  enabled: true

  # Allow breaking changes on major version bumps
  allow_on_major: true

  # Require version bump for breaking changes
  require_major_bump: true

  # Current version (read from package.json)
  current_version: "1.2.3"

  # Next version (auto-detected or manual)
  next_version: "2.0.0"
```

### Whitelist Management

Allow specific breaking changes:

```yaml
whitelist:
  # Whitelist by function name
  - function: oldFunction
    reason: "Deprecated in v1.5, removing in v2.0"
    ticket: "JIRA-123"

  # Whitelist by file
  - file: "src/internal/api.ts"
    reason: "Internal API, not public"

  # Whitelist by pattern
  - pattern: "_internal*"
    reason: "Internal functions (underscore prefix)"
```

### Custom Analyzers

Add custom analysis logic:

```bash
# In hook.sh
custom_analysis() {
    local file=$1

    # Custom breaking change detection logic
    # e.g., check for database schema changes
    # e.g., check for configuration changes
    # e.g., check for API endpoint changes
}
```

## Best Practices

### 1. Semantic Versioning

Follow semver strictly:

```
MAJOR.MINOR.PATCH

MAJOR: Breaking changes
MINOR: New features (backward compatible)
PATCH: Bug fixes (backward compatible)
```

### 2. Deprecation Process

Use deprecation before removal:

```typescript
/**
 * @deprecated Use createUser(data: UserData) instead
 * Will be removed in v2.0
 */
export function createUser(name: string, email: string) {
  console.warn('createUser(name, email) is deprecated');
  return createUser({ name, email });
}
```

### 3. Migration Guides

Document breaking changes:

```markdown
# Migration Guide v1.x to v2.0

## Breaking Changes

### createUser signature changed

**Before:**
\`\`\`typescript
createUser(name: string, email: string)
\`\`\`

**After:**
\`\`\`typescript
createUser(data: UserData)
\`\`\`

**Migration:**
\`\`\`typescript
// Old
createUser('John', 'john@example.com')

// New
createUser({ name: 'John', email: 'john@example.com' })
\`\`\`
```

### 4. Changelog Updates

Track breaking changes:

```markdown
# CHANGELOG.md

## [2.0.0] - 2025-01-08

### BREAKING CHANGES

- Changed `createUser` signature to accept UserData object
- Removed `deleteUser` function (use `removeUser` instead)
- Changed `getUser` to return Promise

### Migration

See [MIGRATION.md](MIGRATION.md) for upgrade instructions.
```

### 5. Gradual Migration

Support both old and new APIs temporarily:

```typescript
// Support both signatures during transition
export function createUser(
  nameOrData: string | UserData,
  email?: string
) {
  if (typeof nameOrData === 'string') {
    // Old signature - log deprecation warning
    console.warn('Old createUser signature is deprecated');
    return createUserImpl({ name: nameOrData, email: email! });
  }
  return createUserImpl(nameOrData);
}
```

### 6. Testing Breaking Changes

Add tests for migration:

```typescript
describe('Breaking Changes', () => {
  it('should maintain backward compatibility', () => {
    // Test old API still works (if supported)
    const result = oldAPI();
    expect(result).toBeDefined();
  });

  it('should work with new API', () => {
    const result = newAPI();
    expect(result).toBeDefined();
  });
});
```

### 7. Communication

Notify users of breaking changes:

```bash
# Pre-release announcements
# Email to users
# Blog post
# GitHub release notes
# Slack/Discord announcements
```

### 8. Version Planning

Plan breaking changes for major releases:

```yaml
# Track planned breaking changes
planned_breaking_changes:
  v2.0:
    - Remove deprecated functions
    - Change API signatures
    - Update return types

  v3.0:
    - Remove legacy endpoints
    - Restructure module exports
```

## Advanced Features

### API Snapshot Comparison

Compare against baseline:

```bash
# Create API snapshot
./hook.sh --create-snapshot

# Compare current code against snapshot
./hook.sh --compare-snapshot

# Update snapshot
./hook.sh --update-snapshot
```

### Impact Analysis

Assess impact of breaking changes:

```bash
# Find all callers of changed functions
./hook.sh --find-usages createUser

# Generate impact report
./hook.sh --impact-report breaking-changes.json
```

### Automated Versioning

Auto-bump version based on changes:

```bash
# Auto-detect version bump needed
# Patch: bug fixes only
# Minor: new features, no breaking changes
# Major: breaking changes detected

./hook.sh --suggest-version
# Output: "2.0.0 (major bump required)"
```

### Integration with CI/CD

Run detection in CI:

```yaml
# .github/workflows/breaking-changes.yml
name: Breaking Change Detection
on: [pull_request]
jobs:
  detect:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0
      - name: Detect Breaking Changes
        run: |
          ./.claude/hooks/breaking-change-detection.sh
          if [ $? -ne 0 ]; then
            echo "Breaking changes detected!"
            echo "Requires major version bump"
            exit 1
          fi
```

## Troubleshooting

### False Positives

If hook incorrectly detects breaking changes:

```yaml
# Add to whitelist
whitelist:
  - function: falsePositiveFunction
    reason: "Internal function, not exported"
```

### Missing Detections

If hook misses actual breaking changes:

```yaml
# Increase strictness
strictness: strict

# Add custom rules
rules:
  internal_changes: warning
```

### Performance Issues

For large codebases:

```yaml
# Limit scope
include:
  - "src/api/**"
  - "lib/public/**"

exclude:
  - "**/*.test.*"
  - "internal/**"
```

### Language Support

For unsupported languages, add custom parser:

```bash
# In hook.sh
parse_custom_language() {
    local file=$1
    # Custom parsing logic
}
```

## Example Configurations

### Library/Framework

```yaml
enabled: true
strictness: strict
rules:
  removed_exports: error
  changed_signatures: error
  changed_types: error
semver:
  enabled: true
  allow_on_major: true
```

### Application

```yaml
enabled: true
strictness: normal
rules:
  removed_exports: warning
  changed_signatures: warning
semver:
  enabled: false
```

### Monorepo

```yaml
enabled: true
strictness: normal

# Different rules per package
packages:
  - name: "@myorg/public-api"
    strictness: strict
    include: ["packages/public-api/**"]

  - name: "@myorg/internal"
    strictness: permissive
    include: ["packages/internal/**"]
```

## License

MIT License - Use freely in your projects
