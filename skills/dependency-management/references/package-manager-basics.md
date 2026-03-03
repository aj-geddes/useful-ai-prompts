# Package Manager Basics

## Package Manager Basics

### Node.js / npm/yarn/pnpm

```bash
# Initialize project
npm init -y

# Install dependencies
npm install express
npm install --save-dev jest
npm install --save-exact lodash  # Exact version

# Update dependencies
npm update
npm outdated  # Check for outdated packages

# Audit security
npm audit
npm audit fix

# Clean install from lock file
npm ci  # Use in CI/CD

# View dependency tree
npm list
npm list --depth=0  # Top-level only
```

### Python / pip/poetry

```bash
# Using pip
pip install requests
pip install -r requirements.txt
pip freeze > requirements.txt

# Using poetry (recommended)
poetry init
poetry add requests
poetry add --dev pytest
poetry add "django>=3.2,<4.0"
poetry update
poetry show --tree
poetry check  # Verify lock file
```

### Ruby / Bundler

```bash
# Initialize
bundle init

# Install
bundle install
bundle update gem_name

# Audit
bundle audit check --update

# View dependencies
bundle list
bundle viz  # Generate dependency graph
```
