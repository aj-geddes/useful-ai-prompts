# Repository Setup Automation

## Overview
Automated workflows for setting up professional GitHub repositories with comprehensive configurations.

## The Prompt

```
Create a comprehensive GitHub repository setup automation with professional configuration:

## 1. Repository Creation Workflow

### Initial Repository Setup
```bash
#!/bin/bash
# create-repo.sh

set -euo pipefail

# Configuration
REPO_NAME="$1"
DESCRIPTION="$2"
TEMPLATE="${3:-standard}"
VISIBILITY="${4:-private}"
ORG="${5:-}"

if [[ -z "$REPO_NAME" || -z "$DESCRIPTION" ]]; then
    echo "Usage: $0 <repo-name> <description> [template] [visibility] [org]"
    echo "Templates: standard, python, terraform, docker, frontend"
    echo "Visibility: public, private"
    exit 1
fi

echo "🚀 Creating repository: $REPO_NAME"
echo "📝 Description: $DESCRIPTION"
echo "📋 Template: $TEMPLATE"
echo "👁️ Visibility: $VISIBILITY"

# Create repository using GitHub CLI
if [[ -n "$ORG" ]]; then
    gh repo create "$ORG/$REPO_NAME" \
        --description "$DESCRIPTION" \
        --"$VISIBILITY" \
        --clone
else
    gh repo create "$REPO_NAME" \
        --description "$DESCRIPTION" \
        --"$VISIBILITY" \
        --clone
fi

cd "$REPO_NAME"

# Apply template configuration
case "$TEMPLATE" in
    "python")
        apply_python_template
        ;;
    "terraform")
        apply_terraform_template
        ;;
    "docker")
        apply_docker_template
        ;;
    "frontend")
        apply_frontend_template
        ;;
    "standard")
        apply_standard_template
        ;;
    *)
        echo "❌ Unknown template: $TEMPLATE"
        exit 1
        ;;
esac

# Initialize git with proper configuration
setup_git_configuration

# Create initial commit
git add .
git commit -m "🎉 Initial repository setup with $TEMPLATE template"
git push -u origin main

echo "✅ Repository created successfully!"
echo "🔗 URL: $(gh repo view --web --json url -q .url)"
```

## 2. Template Application Functions

### Python Project Template
```bash
function apply_python_template() {
    echo "🐍 Applying Python project template..."
    
    # Create directory structure
    mkdir -p {
        src,
        tests,
        docs,
        scripts,
        .github/{workflows,ISSUE_TEMPLATE,PULL_REQUEST_TEMPLATE}
    }
    
    # Create Python configuration files
    create_python_configs
    create_python_workflows
    create_development_files
}

function create_python_configs() {
    # pyproject.toml
    cat > pyproject.toml << 'EOF'
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "PROJECT_NAME"
version = "0.1.0"
description = "PROJECT_DESCRIPTION"
readme = "README.md"
requires-python = ">=3.10"

[tool.black]
line-length = 88
target-version = ['py310', 'py311', 'py312']

[tool.isort]
profile = "black"

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q --strict-markers --strict-config"
testpaths = ["tests"]

[tool.coverage.run]
source = ["src"]
branch = true

[tool.coverage.report]
show_missing = true
fail_under = 80
EOF

    # requirements.txt
    cat > requirements.txt << 'EOF'
# Production dependencies
requests>=2.31.0
click>=8.1.0
pydantic>=2.0.0
EOF

    # requirements-dev.txt
    cat > requirements-dev.txt << 'EOF'
# Development dependencies
black>=23.9.1
isort>=5.12.0
flake8>=6.1.0
mypy>=1.5.1
pytest>=7.4.2
pytest-cov>=4.1.0
bandit[toml]>=1.7.5
safety>=2.3.5
pre-commit>=3.4.0
EOF
}
```

### Standard Repository Files
```bash
function apply_standard_template() {
    echo "📋 Applying standard repository template..."
    
    create_common_files
    create_github_templates
    create_standard_workflows
}

function create_common_files() {
    # README.md
    cat > README.md << EOF
# $REPO_NAME

$DESCRIPTION

## Features

- 🚀 Feature 1
- 🔧 Feature 2
- 📦 Feature 3

## Getting Started

### Prerequisites

- Requirement 1
- Requirement 2

### Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/USERNAME/$REPO_NAME.git
cd $REPO_NAME

# Install dependencies
# Add installation steps here
\`\`\`

### Usage

\`\`\`bash
# Add usage examples here
\`\`\`

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
EOF

    # Create standard project files
    create_license_file
    create_gitignore_file
    create_changelog_file
    create_contributing_file
}

function create_github_templates() {
    mkdir -p .github/{ISSUE_TEMPLATE,PULL_REQUEST_TEMPLATE}
    
    # Bug report template
    cat > .github/ISSUE_TEMPLATE/bug-report.yml << 'EOF'
name: 🐛 Bug Report
description: Create a report to help us improve
title: "[BUG]: "
labels: ["bug", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
  
  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: A clear description of what the bug is
    validations:
      required: true
  
  - type: textarea
    id: reproduction
    attributes:
      label: Reproduction steps
      description: Steps to reproduce the behavior
    validations:
      required: true
  
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
      description: What you expected to happen
    validations:
      required: true
EOF

    # Feature request template
    cat > .github/ISSUE_TEMPLATE/feature-request.yml << 'EOF'
name: 🚀 Feature Request
description: Suggest an idea for this project
title: "[FEATURE]: "
labels: ["enhancement", "triage"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem description
      description: Is your feature request related to a problem?
    validations:
      required: true
  
  - type: textarea
    id: solution
    attributes:
      label: Proposed solution
      description: What you'd like to happen
    validations:
      required: true
EOF

    # Pull request template
    cat > .github/PULL_REQUEST_TEMPLATE/pull_request_template.md << 'EOF'
# Pull Request

## Description

Briefly describe the changes in this PR.

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing

- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] I have tested this change manually

## Checklist

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have updated the CHANGELOG.md
EOF
}
```

## 3. Repository Enhancement Scripts

### Security Setup
```bash
#!/bin/bash
# setup-security.sh

echo "🔒 Setting up repository security..."

# Enable security features
gh repo edit --enable-auto-merge=false
gh repo edit --enable-wiki=false
gh repo edit --enable-projects=true
gh repo edit --enable-issues=true

# Set up branch protection
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["build","test"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null

echo "✅ Security setup completed"
```

### Repository Automation
```bash
#!/bin/bash
# setup-automation.sh

echo "🤖 Setting up repository automation..."

# Add labels
labels=(
    "bug:red"
    "enhancement:green"
    "documentation:blue"
    "help wanted:purple"
    "good first issue:yellow"
    "security:orange"
    "priority/high:red"
    "priority/medium:yellow"
    "priority/low:green"
)

for label in "${labels[@]}"; do
    name=${label%:*}
    color=${label#*:}
    gh label create "$name" --color "$color" --force
done

echo "✅ Automation setup completed"
```

## 4. Template Variations

### Docker Project Template
```bash
function apply_docker_template() {
    echo "🐳 Applying Docker project template..."
    
    mkdir -p {scripts,docker,tests,.github/workflows}
    
    # Multi-stage Dockerfile
    cat > Dockerfile << 'EOF'
# Multi-stage build for production optimization
FROM python:3.12-slim-bookworm AS builder

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python -m compileall .

# Production stage
FROM python:3.12-slim-bookworm AS production

# Security updates
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        dumb-init && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r -g 1001 appuser && \
    useradd -r -g appuser -u 1001 -d /app -s /bin/bash appuser

WORKDIR /app

# Copy from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder --chown=appuser:appuser /build/ .

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["python", "-u", "app.py"]
EOF

    # Docker Compose
    cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  app:
    build: .
    container_name: PROJECT_NAME
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
    volumes:
      - ./data:/app/data:ro
    networks:
      - app-network
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    read_only: true
    tmpfs:
      - /tmp:noexec,nosuid,size=100m
    mem_limit: 512m
    cpus: '1.0'

networks:
  app-network:
    driver: bridge
EOF

    # Build script
    cat > scripts/build.sh << 'EOF'
#!/bin/bash
set -euo pipefail

IMAGE_NAME="PROJECT_NAME"
TAG="${1:-latest}"
BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
VCS_REF=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")

echo "🐳 Building Docker image: $IMAGE_NAME:$TAG"

docker build \
    --target production \
    --build-arg BUILD_DATE="$BUILD_DATE" \
    --build-arg VCS_REF="$VCS_REF" \
    --label "org.opencontainers.image.created=$BUILD_DATE" \
    --label "org.opencontainers.image.revision=$VCS_REF" \
    --tag "$IMAGE_NAME:$TAG" \
    .

echo "✅ Build completed successfully!"
echo "📦 Image: $IMAGE_NAME:$TAG"
EOF

    chmod +x scripts/build.sh
}
```

Requirements:
- Create comprehensive repository templates for different project types
- Include proper directory structures and configuration files
- Add GitHub Actions workflows for CI/CD
- Generate issue and PR templates
- Include security configurations and best practices
- Provide automated setup scripts
- Add proper documentation templates
- Include development and deployment configurations
```

## Key Components

### Automation Features
- **Template System**: Multiple project type templates
- **GitHub CLI Integration**: Automated repository creation
- **Directory Structure**: Proper project organization
- **Configuration Files**: Language-specific setups
- **CI/CD Workflows**: GitHub Actions integration

### Security Features
- **Branch Protection**: Required reviews and status checks
- **Issue Templates**: Structured bug reports and feature requests
- **Security Scanning**: Automated vulnerability detection
- **Access Control**: Proper permissions and settings

### Development Features
- **Code Quality**: Linting, formatting, and testing
- **Documentation**: README, CONTRIBUTING, CHANGELOG
- **Version Control**: Proper .gitignore and Git configuration
- **Dependency Management**: Requirements and package files

## Benefits
- **Rapid Setup**: Automated repository creation with templates
- **Consistency**: Standardized project structures
- **Best Practices**: Built-in security and quality configurations
- **CI/CD Ready**: Pre-configured workflows and automation
- **Professional**: Complete documentation and issue templates
- **Scalable**: Template system for different project types

## Tags
`repository-automation` `github` `project-setup` `templates` `ci-cd` `development-workflow`