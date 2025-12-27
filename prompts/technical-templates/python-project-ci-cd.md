# Python Project CI/CD Pipeline

## Metadata
- **ID**: `python-cicd-pipeline`
- **Version**: 1.0.0
- **Category**: Technical / DevOps
- **Tags**: python, ci-cd, github-actions, testing, security, code-quality, automation
- **Complexity**: intermediate
- **Interaction**: single-shot
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Comprehensive template for designing and implementing robust CI/CD pipelines for Python-based systems using GitHub Actions. Includes quality gates, security scanning, multi-version testing matrices, and artifact management for reproducible, traceable builds.

## When to Use

**Ideal Scenarios:**
- Setting up CI/CD for new Python projects (APIs, libraries, CLIs)
- Adding quality gates and security scanning to existing pipelines
- Implementing multi-version Python testing matrices
- Configuring code coverage thresholds and static analysis automation

**Anti-patterns (Don't Use For):**
- Non-Python projects (use language-specific templates)
- Manual deployment workflows without automation goals
- Projects without automated testing requirements

---

## Prompt

```xml
<role>
You are a DevOps Engineer specializing in Python CI/CD pipelines with deep expertise in GitHub Actions, static analysis tooling, security scanning, and quality gate configuration. You build reproducible, traceable pipelines that catch issues early and enable confident deployments.
</role>

<context>
Modern Python projects require comprehensive CI/CD covering code formatting, linting, type checking, security scanning, and multi-version testing. GitHub Actions provides the platform for automating these checks on every push and pull request, with scheduled runs for drift detection.
</context>

<input_handling>
Required inputs:
- Project type and architecture (API, CLI, library, microservice)
- Python version requirements (which versions to support)
- Testing and quality expectations (coverage thresholds, strictness)

Infer if not provided:
- CI/CD platform: GitHub Actions
- Coverage threshold: 80% minimum
- Security scanning: Bandit (SAST) + Safety (dependency scanning)
- Formatting: Black + isort
- Linting: Flake8 + MyPy for type checking
</input_handling>

<task>
Design a comprehensive CI/CD pipeline for Python projects:

1. Configure multi-version Python matrix testing (typically 3.10, 3.11, 3.12)
2. Implement code formatting enforcement using Black and isort with check mode
3. Set up linting with Flake8 and strict type checking with MyPy
4. Configure security scanning with Bandit (SAST) and Safety (dependency vulnerabilities)
5. Integrate test coverage with threshold enforcement and reporting
6. Set up artifact preservation for audit trails and debugging
7. Configure scheduled regression runs for detecting dependency drift
</task>

<output_specification>
Format: GitHub Actions workflow with pyproject.toml configuration
Length: 500-1500 words with complete YAML examples
Structure:
- Workflow file (.github/workflows/ci.yml) with full job definitions
- Tool configuration (pyproject.toml sections for each tool)
- Requirements-dev.txt with pinned development dependencies
- Usage notes explaining customization options
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- Pipeline validates successfully across all declared Python versions
- Code quality enforced through formatting, linting, and type checking
- Coverage threshold enforced with clear failure messages
- Security scan artifacts captured for compliance audit
- Caching configured for faster subsequent runs

Avoid:
- Non-deterministic builds with unpinned dependencies
- Missing artifact preservation for debugging failed runs
- Blocking on non-critical warnings without override documentation
- Ignoring scheduled runs for regression and drift detection
</quality_criteria>

<constraints>
- All tools must be configurable via pyproject.toml where supported
- Security scans should not block pipeline on informational findings
- Artifacts must be retained for compliance (minimum 30 days)
- Matrix builds should fail fast to reduce compute usage
</constraints>
```

---

## Example Usage

### Input

We're building a FastAPI microservice API with PostgreSQL. Need to support Python 3.11 and 3.12. We have async tests with pytest-asyncio. Want 85% coverage minimum, strict type checking, and SOC 2 compliance for security scanning. Using GitHub Actions.

### Output

**GitHub Actions Workflow (.github/workflows/ci.yml)**

```yaml
name: Python CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]
  schedule:
    - cron: "0 2 * * *"  # Daily regression at 2 AM UTC

jobs:
  quality-check:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: true
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: "pip"

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r requirements-dev.txt

      - name: Code formatting (Black)
        run: black --check --diff .

      - name: Import sorting (isort)
        run: isort --check-only --diff .

      - name: Linting (Flake8)
        run: flake8 . --max-complexity=10 --max-line-length=88

      - name: Type checking (MyPy)
        run: mypy . --strict

      - name: Security scan (Bandit)
        run: bandit -r src/ -f json -o bandit-report.json
        continue-on-error: true

      - name: Dependency scan (Safety)
        run: safety check --json > safety-report.json
        continue-on-error: true

      - name: Tests with coverage
        run: |
          pytest --cov=src --cov-report=xml --cov-report=term --cov-fail-under=85

      - name: Upload security artifacts
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: security-reports-${{ matrix.python-version }}
          path: |
            bandit-report.json
            safety-report.json
          retention-days: 90

      - name: Upload coverage
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: coverage-${{ matrix.python-version }}
          path: coverage.xml
          retention-days: 30
```

**pyproject.toml Configuration**

```toml
[tool.black]
line-length = 88
target-version = ['py311', 'py312']

[tool.isort]
profile = "black"
line_length = 88

[tool.coverage.run]
source = ["src"]
branch = true
omit = ["*/tests/*", "*/__pycache__/*"]

[tool.coverage.report]
fail_under = 85
show_missing = true
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
]

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true

[tool.bandit]
exclude_dirs = ["tests", "venv"]
skips = ["B101"]  # Skip assert warnings in tests
```

**requirements-dev.txt**

```
black==24.1.0
isort==5.13.0
flake8==7.0.0
mypy==1.8.0
bandit==1.7.7
safety==2.3.5
pytest==8.0.0
pytest-asyncio==0.23.0
pytest-cov==4.1.0
```

---

## Related Prompts

- [Deployment Pipeline Creation Expert](../technical-workflows/deployment-pipeline-creation-expert.md) - Full deployment automation
- [Test Strategy Development Expert](../technical-workflows/test-strategy-development-expert.md) - Comprehensive testing strategies
- [DevOps Workflow Design Expert](../technical-workflows/devops-workflow-design-expert.md) - End-to-end DevOps practices
