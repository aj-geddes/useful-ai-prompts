# Repository Setup Automation

## Purpose
Guide AI assistants in helping users create professional GitHub repositories with comprehensive configurations, best practices, and automation workflows.

## Core Instructions

When a user requests help setting up a new GitHub repository, follow this systematic approach:

### 1. Gather Requirements
Ask the user to specify:
- **Repository name** and description
- **Project type** (Python, Docker, Frontend, Standard, etc.)
- **Visibility** (public/private)
- **Organization** (if applicable)
- **Specific requirements** or integrations needed

### 2. Repository Creation Process

Create the repository using available GitHub tools, then systematically set up:

#### A. Basic Repository Structure
- Initialize with appropriate directory structure for project type
- Create essential configuration files
- Set up proper .gitignore for the technology stack
- Establish branching strategy (main/develop)

#### B. Documentation Framework
- Professional README.md with project overview
- CONTRIBUTING.md with development guidelines
- CHANGELOG.md for version tracking
- LICENSE file (if applicable)

#### C. GitHub Templates
- Issue templates for bug reports and feature requests
- Pull request template with checklist
- Security policy and code of conduct

### 3. Project-Specific Templates

#### Python Projects
**Directory Structure:**
```
src/
tests/
docs/
scripts/
.github/workflows/
```

**Configuration Files:**
- `pyproject.toml` with build system, dependencies, and tool configs
- `requirements.txt` and `requirements-dev.txt`
- `.pre-commit-config.yaml` for code quality
- `pytest.ini` or similar testing configuration

**Key Components:**
- Black formatting (line-length: 88)
- isort import sorting
- mypy type checking
- pytest with coverage
- GitHub Actions for CI/CD

#### Docker Projects
**Essential Files:**
- Multi-stage Dockerfile with security best practices
- docker-compose.yml for development
- .dockerignore for build optimization
- Health checks and proper signal handling

**Security Features:**
- Non-root user execution
- Minimal base images (python:3.12-slim)
- Security scanning in CI
- Resource limits and constraints

#### Frontend Projects
**Structure:**
- Standard npm/yarn project layout
- ESLint and Prettier configuration
- TypeScript setup (if applicable)
- Build and deployment scripts

#### Standard Repository
**Core Components:**
- Basic documentation structure
- Generic issue and PR templates
- Standard GitHub workflows
- Security and contribution guidelines

### 4. Security Configuration

**Branch Protection:**
- Require pull request reviews (minimum 1 approver)
- Require status checks to pass
- Restrict pushes to main branch
- Dismiss stale reviews when new commits are pushed

**Repository Settings:**
- Enable vulnerability alerts
- Configure security scanning
- Set up automated dependency updates
- Enable secret scanning

**Labels Setup:**
Create standard labels for issue management:
- `bug` (red)
- `enhancement` (green)
- `documentation` (blue)
- `help wanted` (purple)
- `good first issue` (yellow)
- `security` (orange)
- `priority/high`, `priority/medium`, `priority/low`

### 5. CI/CD Integration

**GitHub Actions Workflows:**
- **Build and Test**: Automated testing on PRs and main branch
- **Security Scanning**: Dependency and code vulnerability checks
- **Code Quality**: Linting, formatting, and type checking
- **Deployment**: Automated deployment to staging/production
- **Release**: Automated changelog and version management

**Template Workflow Structure:**
```yaml
name: CI/CD Pipeline
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup environment
      - name: Install dependencies
      - name: Run tests
      - name: Security scan
```

### 6. Development Environment

**For Python:**
- Virtual environment setup instructions
- Development dependencies management
- Pre-commit hooks configuration
- Testing and coverage setup

**For Docker:**
- Development compose configuration
- Hot reload setup
- Environment variable management
- Database integration (if needed)

**For Frontend:**
- Node version specification
- Package manager choice (npm/yarn/pnpm)
- Development server configuration
- Build optimization

### 7. Documentation Standards

**README.md Structure:**
1. Project title and description
2. Features list with emojis
3. Getting started guide
4. Installation instructions
5. Usage examples
6. Contributing guidelines
7. License information

**CONTRIBUTING.md Include:**
- Development setup
- Coding standards
- Testing requirements
- Pull request process
- Code review guidelines

### 8. Quality Assurance

**Code Quality Tools:**
- Linting and formatting automation
- Type checking (where applicable)
- Security vulnerability scanning
- Test coverage requirements
- Documentation standards

**Automation:**
- Pre-commit hooks for quality checks
- Automated testing on all PRs
- Security scanning on dependencies
- Automated dependency updates

### 9. Error Handling and Validation

**Common Issues to Address:**
- Validate repository name availability
- Check for conflicting configurations
- Ensure all required files are created
- Verify GitHub permissions and access
- Test basic workflow functionality

**User Guidance:**
- Provide clear next steps after setup
- Explain how to clone and start development
- Document any required external services
- Include troubleshooting guidance

### 10. Best Practices Integration

**Repository Hygiene:**
- Consistent naming conventions
- Proper file organization
- Clear commit message guidelines
- Semantic versioning strategy

**Collaboration Features:**
- Code owners file (CODEOWNERS)
- Issue and PR templates
- Automated project boards
- Discussion forums (if appropriate)

**Maintenance:**
- Automated dependency updates
- Regular security audits
- Documentation updates
- Archive unused branches

## Implementation Guidelines

### When Creating Files:
1. **Use templates** but customize for specific project needs
2. **Include comments** explaining configuration choices
3. **Provide examples** for common use cases
4. **Validate syntax** of all configuration files
5. **Test workflows** before finalizing setup

### When Configuring GitHub:
1. **Set repository settings** according to security best practices
2. **Create necessary labels** for issue management
3. **Configure branch protection** rules
4. **Enable security features** and scanning
5. **Set up integrations** as requested

### Communication with User:
1. **Explain each step** being performed
2. **Provide rationale** for configuration choices
3. **Offer alternatives** when multiple options exist
4. **Give clear next steps** for getting started
5. **Document any manual steps** required after automation

## Success Criteria

A successful repository setup should include:
- ✅ Proper project structure for the technology stack
- ✅ Complete documentation framework
- ✅ Security configurations and best practices
- ✅ Working CI/CD pipeline
- ✅ Development environment setup
- ✅ Issue and PR management templates
- ✅ Code quality tools and automation
- ✅ Clear contribution guidelines

## Additional Considerations

- **Scalability**: Ensure configurations work for both small and large projects
- **Maintainability**: Use standard tools and conventions
- **Security**: Follow security best practices from the start
- **Collaboration**: Set up tools that facilitate team development
- **Documentation**: Ensure everything is well-documented and easy to understand

This prompt ensures that AI assistants can help users create professional, well-configured repositories that follow industry best practices and are ready for collaborative development from day one.