## Solicit User Input for \[Comprehensive CI/CD Pipeline Design for Python-Based Systems]

To rigorously align the GitHub Actions workflow with your system architecture, quality strategy, and regulatory posture, please provide detailed responses to the following:

* **Project Taxonomy and Operational Role**: Define the architectural class and operational intent of the project (e.g., microservice API, distributed analytics engine, CLI automation tool). Include relevant dependency chains, concurrency models, or integration points.
* **Python Runtime Spectrum**: Specify the complete range of Python interpreter versions that must be supported, tested, and validated.
* **Enforcement Thresholds for Code Quality**: Articulate strict expectations for static formatting (Black), import structuring (isort), linting compliance (Flake8), and type completeness (MyPy), including code coverage requirements.
* **Security Governance Constraints**: Indicate any internal compliance regimes, threat models, or industry-specific regulations (e.g., OWASP, NIST 800-53, ISO 27001) that must be enforced via Bandit or Safety scans.
* **Testing Architecture Profile**: Describe the breadth and depth of the test suite, including coverage of unit, integration, async/event loop testing, mocking libraries, and fixture conventions.
* **Artifact Durability and Observability**: Specify which test artifacts, coverage profiles, and scan outputs must persist beyond the job context and be accessible for audit, regression analysis, or developer triage.
* **Deployment Coupling Strategy**: Clarify whether pipeline-triggered deployments should be tag-based, branch-gated, or conditioned on minimum quality and security thresholds.
* **Tooling Ecosystem Requirements**: Enumerate any additional linters, code analyzers, secrets scanners, or organizational pre-commit policies that must be integrated.

These inputs will facilitate the construction of a traceable, deterministic, and security-conscious CI/CD apparatus for Python codebases.

---

## Foundational Requirements

* **Multi-Version Runtime Validation**: Matrix test execution across Python 3.10, 3.11, and 3.12 for future-proofing and regression control.
* **Stylistic and Structural Enforcement**: Canonicalize formatting via Black, ensure deterministic imports via isort, and enforce idiomatic style rules via Flake8.
* **Static Typing Conformance**: Execute strict type checking with MyPy using `disallow_untyped_defs` and `disallow_incomplete_defs` for API contract reliability.
* **Vulnerability Surface Analysis**: Perform source-level scan with Bandit and dependency-level analysis with Safety, both in fail-safe and non-blocking modes.
* **Test Coverage Instrumentation**: Integrate Pytest with multi-format coverage outputs (HTML, XML, terminal) and enforce coverage thresholds at or above 80%.
* **Audit Trail Preservation**: Upload all security, quality, and coverage artifacts as first-class CI outputs.
* **Scheduled Regression Detection**: Execute the full pipeline nightly via GitHub’s `cron` schedule for stale dependency detection and drift analysis.

---

## Canonical GitHub Actions Workflow

```yaml
name: Python Code Quality

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
  schedule:
    - cron: '0 2 * * *'

jobs:
  quality-check:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']

    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt

    - name: Code formatting (Black)
      run: black --check --diff .

    - name: Import sorting (isort)
      run: isort --check-only --diff .

    - name: Linting (Flake8)
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics

    - name: Type checking (MyPy)
      run: mypy .

    - name: Static security scan (Bandit)
      run: |
        bandit -r . -f json -o bandit-report.json
        bandit -r . -f txt
      continue-on-error: true

    - name: Dependency vulnerability scan (Safety)
      run: |
        safety check --json --output safety-report.json
        safety check
      continue-on-error: true

    - name: Test execution with coverage
      run: pytest --cov=. --cov-report=html --cov-report=xml --cov-report=term

    - name: Upload to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella

    - name: Upload artifacts
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

---

## pyproject.toml: Unified Configuration Schema

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
omit = ["tests/*", "setup.py", "venv/*", ".venv/*"]
branch = true

[tool.coverage.report]
show_missing = true
skip_covered = false
fail_under = 80

[tool.bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]
```

---

## Development Dependency Manifest

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

---

## Evaluation Criteria

* ✅ Pipeline validates across all declared Python versions
* ✅ Code conforms to type, linting, and formatting constraints
* ✅ Coverage threshold enforced and reported
* ✅ Security scan artifacts captured and optionally surfaced
* ✅ Pipeline runs are observable, deterministic, and auditable
* ✅ Execution performance is optimized through dependency caching

---

## Quality Standards

* **Reproducibility**: Execution is idempotent across runners and environments
* **Traceability**: Every build artifact and scan result must be linkable to its commit
* **Security Enforcement**: Vulnerabilities must be logged, classified, and optionally escalated
* **Policy Compliance**: Workflow must enforce PEP8, typing integrity, and CVE compliance
* **Maintainability**: All configurations must remain modular, version-controlled, and testable
