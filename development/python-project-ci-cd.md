# Python Project CI/CD with GitHub Actions

## Overview
Comprehensive GitHub Actions workflow for Python projects with quality checks, security scanning, and automated testing.

## The Prompt

```
Create a production-ready GitHub Actions CI/CD pipeline for a Python project with comprehensive quality checks:

## GitHub Actions Workflow (.github/workflows/python-quality.yml)

```yaml
name: Python Code Quality

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
  schedule:
    # Run daily at 2 AM UTC
    - cron: '0 2 * * *'

jobs:
  quality-check:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Code formatting check (Black)
      run: |
        black --check --diff .
    
    - name: Import sorting check (isort)
      run: |
        isort --check-only --diff .
    
    - name: Linting (Flake8)
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
    
    - name: Type checking (MyPy)
      run: |
        mypy .
    
    - name: Security scanning (Bandit)
      run: |
        bandit -r . -f json -o bandit-report.json
        bandit -r . -f txt
      continue-on-error: true
    
    - name: Dependency vulnerability scanning (Safety)
      run: |
        safety check --json --output safety-report.json
        safety check
      continue-on-error: true
    
    - name: Run tests with coverage
      run: |
        pytest --cov=. --cov-report=html --cov-report=xml --cov-report=term
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella
    
    - name: Upload test artifacts
      uses: actions/upload-artifact@v3
      if: always()
      with:
        name: test-results-${{ matrix.python-version }}
        path: |
          htmlcov/
          coverage.xml
          bandit-report.json
          safety-report.json
```

## Project Configuration (pyproject.toml)

```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py310', 'py311', 'py312']
include = '\.pyi?$'

[tool.isort]
profile = "black"
line_length = 88
multi_line_output = 3
include_trailing_comma = true

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q --strict-markers --strict-config"
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]

[tool.coverage.run]
source = ["src", "."]
omit = [
    "tests/*",
    "setup.py",
    "venv/*",
    ".venv/*",
]
branch = true

[tool.coverage.report]
show_missing = true
skip_covered = false
fail_under = 80

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]
```

## Development Dependencies (requirements-dev.txt)

```
black>=23.9.1
isort>=5.12.0
flake8>=6.1.0
mypy>=1.5.1
bandit[toml]>=1.7.5
safety>=2.3.5
pytest>=7.4.2
pytest-cov>=4.1.0
pytest-asyncio>=0.21.1
pre-commit>=3.4.0
coverage[toml]>=7.3.2
```

Requirements:
- Multi-Python version testing (3.10, 3.11, 3.12)
- Comprehensive quality checks (Black, isort, Flake8, MyPy)
- Security scanning (Bandit, Safety)
- Test coverage reporting with Codecov integration
- Automated issue creation on failures
- Pre-commit hooks for local development
- Proper configuration files (pyproject.toml)
- Artifact uploads for debugging
- Scheduled runs for dependency monitoring
```

## Key Features

### Quality Checks
- **Black**: Code formatting
- **isort**: Import sorting
- **Flake8**: Linting and style
- **MyPy**: Static type checking
- **Bandit**: Security vulnerability scanning
- **Safety**: Dependency vulnerability checking

### Testing & Coverage
- **pytest**: Test execution
- **Coverage.py**: Code coverage measurement
- **Codecov**: Coverage reporting integration
- Multi-version testing matrix

### Automation Features
- Automated issue creation on failures
- Pre-commit hooks for local development
- Scheduled daily runs
- Artifact uploads for debugging
- Caching for faster builds

## Benefits
- **Quality Assurance**: Comprehensive code quality checks
- **Security First**: Built-in vulnerability scanning
- **Fast Feedback**: Pre-commit hooks catch issues early
- **Detailed Reporting**: Coverage and security reports
- **Multi-Version Support**: Tests across Python versions
- **Issue Tracking**: Automated failure notifications

## Tags
`github-actions` `ci-cd` `python` `quality` `testing` `security` `automation`