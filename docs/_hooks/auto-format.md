---
date: "2025-01-01"
description:
  A PostToolUse hook that automatically formats code after file edits to
  maintain consistent code style across your project.
event_type: PostToolUse
features:
  - Prettier support
  - Black (Python)
  - gofmt (Go)
  - rustfmt (Rust)
  - 8+ language formatters
  - Auto-detection
icon: fa-magic
icon_class: format
layout: hook
lines_of_code: 565
matcher: Edit|Write
slug: auto-format
title: auto-format
---

A PostToolUse hook that automatically formats code after file edits to maintain consistent code style across your project.

## Features

- Auto-detects file type (JavaScript, TypeScript, Python, Ruby, Go, Rust, etc.)
- Runs appropriate formatter (Prettier, Black, RuboCop, gofmt, rustfmt, etc.)
- Auto-applies formatting changes
- Reports what was formatted
- Supports custom formatter configurations
- Respects .prettierignore, .eslintignore, etc.
- Works with multiple formatters in monorepos
- Configurable formatting rules
- Optional auto-commit of formatting changes

## Configuration

Add this to your `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "pattern": "^(Edit|Write)$",
        "command": "/absolute/path/to/hooks/auto-format/hook.sh",
        "description": "Auto-format code after file edits"
      }
    ]
  }
}
```

## Installation

### 1. Install Formatters

Install formatters for your language(s):

```bash
# JavaScript/TypeScript - Prettier
npm install --save-dev prettier

# Python - Black
pip install black

# Ruby - RuboCop
gem install rubocop

# Go - gofmt (built-in with Go)
# No installation needed

# Rust - rustfmt (built-in with Rust)
# No installation needed

# PHP - PHP-CS-Fixer
composer require --dev friendsofphp/php-cs-fixer

# Java - google-java-format
# Download from https://github.com/google/google-java-format

# C/C++ - clang-format
# macOS: brew install clang-format
# Linux: apt-get install clang-format
```

### 2. Set Up the Hook

```bash
# Copy the hook to your project
cp hook.sh /path/to/your/project/.claude/hooks/auto-format.sh
chmod +x /path/to/your/project/.claude/hooks/auto-format.sh

# Update .claude/settings.json with the correct path
```

### 3. Configure Formatters (Optional)

Create formatter configuration files:

```bash
# Prettier (.prettierrc)
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}

# Black (pyproject.toml)
[tool.black]
line-length = 88
target-version = ['py39']

# RuboCop (.rubocop.yml)
AllCops:
  NewCops: enable
  TargetRubyVersion: 3.0

# EditorConfig (.editorconfig)
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

### 4. Configure Hook Behavior

Create a `.formatconfig` file in your project root:

```bash
# .formatconfig - Auto-format configuration

# Enable auto-formatting
AUTO_FORMAT=true

# Auto-commit formatted files
AUTO_COMMIT_FORMAT=false

# Show formatting changes
SHOW_CHANGES=true

# Formatters to use (comma-separated)
# Leave empty to auto-detect
FORMATTERS=

# File patterns to format (comma-separated)
# Leave empty to format all supported files
FORMAT_PATTERNS=

# File patterns to exclude
EXCLUDE_PATTERNS="*.min.js,*.bundle.js,dist/*,build/*"

# Verbose output
VERBOSE=false
```

## Usage

The hook runs automatically after you edit or create files:

```
🎨 Auto-Format Running...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 Formatting file: src/components/Header.tsx

✅ Formatted with Prettier
   - Fixed 3 formatting issues
   - Added missing semicolons
   - Adjusted indentation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Changes:
  src/components/Header.tsx
    -   const name = "App"
    +   const name = 'App';

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ Formatting complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Supported Formatters

### JavaScript/TypeScript

- **Prettier** - Opinionated code formatter
- **ESLint** - With --fix flag
- **Standard** - JavaScript Standard Style

### Python

- **Black** - The uncompromising formatter
- **autopep8** - PEP 8 compliance
- **yapf** - Yet Another Python Formatter
- **isort** - Import sorting

### Ruby

- **RuboCop** - Ruby static code analyzer
- **Prettier (Ruby plugin)** - Alternative formatter

### Go

- **gofmt** - Official Go formatter
- **goimports** - Manages imports and formats

### Rust

- **rustfmt** - Official Rust formatter

### PHP

- **PHP-CS-Fixer** - PHP Coding Standards Fixer
- **PHP_CodeSniffer** - With phpcbf

### Java

- **google-java-format** - Google's Java formatter
- **prettier-java** - Prettier plugin for Java

### C/C++

- **clang-format** - LLVM code formatter

### CSS/SCSS/Less

- **Prettier** - Supports CSS and preprocessors
- **stylelint** - With --fix flag

### HTML

- **Prettier** - HTML formatting
- **js-beautify** - Multi-language beautifier

### JSON/YAML/Markdown

- **Prettier** - Supports multiple formats

## Customization

### Formatter Selection

Override automatic detection:

```bash
# In .formatconfig
# Force specific formatters for file types
JS_FORMATTER=prettier
PYTHON_FORMATTER=black
RUBY_FORMATTER=rubocop
```

### Custom Formatting Rules

Each formatter respects its own configuration:

```javascript
// .prettierrc.js
module.exports = {
  printWidth: 100,
  tabWidth: 2,
  useTabs: false,
  semi: true,
  singleQuote: true,
  quoteProps: "as-needed",
  trailingComma: "all",
  bracketSpacing: true,
  arrowParens: "always",
};
```

```python
# pyproject.toml
[tool.black]
line-length = 100
target-version = ['py39', 'py310']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | build
  | dist
)/
'''
```

### Selective Formatting

Format only specific file types:

```bash
# In .formatconfig
FORMAT_PATTERNS="*.js,*.ts,*.jsx,*.tsx"

# Or in hook.sh
case "$extension" in
  js|ts|jsx|tsx)
    format_with_prettier "$file"
    ;;
  py)
    format_with_black "$file"
    ;;
esac
```

### Pre/Post Format Hooks

Add custom logic before or after formatting:

```bash
# In hook.sh
pre_format_hook() {
    local file=$1
    # Custom logic before formatting
    # e.g., backup file, run linter, etc.
}

post_format_hook() {
    local file=$1
    # Custom logic after formatting
    # e.g., validate syntax, notify user, etc.
}
```

### Auto-Commit Formatted Changes

Automatically commit formatting changes:

```bash
# In .formatconfig
AUTO_COMMIT_FORMAT=true

# Hook will create commits like:
# "chore: auto-format src/components/Header.tsx"
```

## Best Practices

### 1. Team Consistency

Share formatter configs in repository:

```bash
# Commit formatter configs
git add .prettierrc .editorconfig
git commit -m "Add formatter configuration"

# Team members use same formatting rules
```

### 2. Editor Integration

Use formatter in your editor too:

```json
// VS Code settings.json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

### 3. Pre-Commit Hooks

Combine with pre-commit for double safety:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.0.0
    hooks:
      - id: prettier

  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
```

### 4. Ignore Generated Files

Don't format generated or minified files:

```
# .prettierignore
dist/
build/
coverage/
*.min.js
*.bundle.js
node_modules/
```

### 5. Format on Save

Configure auto-format to run immediately:

```bash
# In .formatconfig
# Run immediately after edit (no delay)
FORMAT_DELAY=0
```

### 6. Gradual Adoption

Introduce formatting gradually:

```bash
# Phase 1: Format new files only
FORMAT_NEW_FILES_ONLY=true

# Phase 2: Format changed files
FORMAT_CHANGED_FILES=true

# Phase 3: Format entire codebase
npm run format:all
```

### 7. Review Changes

Always review formatting changes:

```bash
# In .formatconfig
SHOW_CHANGES=true

# Shows diff of formatting changes
# Review before committing
```

### 8. Performance Optimization

For large files or projects:

```bash
# Format only changed lines (if supported)
# Prettier doesn't support this, but some formatters do

# Cache formatting results
# Skip files that haven't changed

# Run formatters in parallel
PARALLEL_FORMAT=true
```

## Advanced Features

### Multi-Formatter Support

Use different formatters in a monorepo:

```bash
detect_formatter() {
    local file=$1

    # Check package.json for formatter
    if [[ -f "package.json" ]] && grep -q "prettier" package.json; then
        echo "prettier"
    elif [[ -f "pyproject.toml" ]] && grep -q "black" pyproject.toml; then
        echo "black"
    else
        # Default by extension
        detect_by_extension "$file"
    fi
}
```

### Conditional Formatting

Format based on context:

```bash
should_format() {
    local file=$1

    # Don't format files in certain directories
    if [[ "$file" =~ (vendor|node_modules|dist)/ ]]; then
        return 1
    fi

    # Don't format during CI
    if [[ -n "$CI" ]]; then
        return 1
    fi

    # Don't format generated files
    if head -n 1 "$file" | grep -q "auto-generated"; then
        return 1
    fi

    return 0
}
```

### Format Validation

Verify formatting without applying:

```bash
# Check if file needs formatting
npx prettier --check src/**/*.js

# Exit code 1 if formatting needed
# Exit code 0 if already formatted
```

### Formatting Metrics

Track formatting statistics:

```bash
# Log formatting activity
echo "$(date): Formatted $file" >> .format.log

# Count formatting changes
git diff --numstat | awk '{sum+=$1+$2} END {print sum}'
```

### Smart Formatting

Only format changed lines:

```bash
# For Git-aware formatters
# prettier --changed (experimental)

# Or use git diff to identify changed lines
# and format only those sections
```

## Troubleshooting

### Formatter Not Found

Install the formatter:

```bash
# Check if formatter is installed
which prettier
which black

# Install if missing
npm install -g prettier
pip install black
```

### Configuration Not Respected

Verify config files are:

1. In correct location (project root)
2. Named correctly (.prettierrc, pyproject.toml, etc.)
3. Valid format (JSON, YAML, TOML)
4. Not being overridden

### Formatting Conflicts

When multiple formatters conflict:

```bash
# Choose one formatter per file type
# Disable conflicting formatters
# Or run formatters in specific order
```

### Performance Issues

For slow formatting:

```bash
# Format only changed files
# Use faster formatters
# Disable some checks
# Run formatters in parallel
```

### Hook Not Running

Check:

1. Hook is in PostToolUse section
2. Pattern matches: "^(Edit|Write)$"
3. Script is executable
4. Path is correct

## Example Configurations

### JavaScript Project

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "printWidth": 100
}
```

```bash
# .formatconfig
AUTO_FORMAT=true
FORMATTERS=prettier
SHOW_CHANGES=true
```

### Python Project

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py39']

[tool.isort]
profile = "black"
```

```bash
# .formatconfig
AUTO_FORMAT=true
FORMATTERS=black,isort
SHOW_CHANGES=true
```

### Multi-Language Project

```bash
# .formatconfig
AUTO_FORMAT=true
# Auto-detect formatters
FORMATTERS=
SHOW_CHANGES=true
EXCLUDE_PATTERNS="*.min.js,dist/*,vendor/*"
```

## Integration with CI/CD

Verify formatting in CI:

```yaml
# .github/workflows/format-check.yml
name: Format Check
on: [push, pull_request]
jobs:
  format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check Formatting
        run: |
          npx prettier --check "src/**/*.{js,ts}"
          black --check .
```

## License

MIT License - Use freely in your projects
