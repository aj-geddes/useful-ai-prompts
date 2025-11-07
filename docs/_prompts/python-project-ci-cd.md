---
category: learning-development
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Set up a comprehensive CI/CD pipeline for Python projects with GitHub Actions, code quality tools, and security scanning
layout: prompt
slug: python-project-ci-cd
tags:
- development
- ci-cd
- python
- github-actions
- code-quality
title: Python Project CI/CD Pipeline Design
use_cases:
- development optimization
- professional workflow enhancement
- continuous integration setup
version: 3.0.0
prompt: |
  I'll help you design a comprehensive CI/CD pipeline for your Python project. Let me understand your requirements:

  ## Understanding Your Project

  **Project Architecture:**
  - What type of Python project are you building? (microservice API, distributed analytics engine, CLI tool, web application, library)
  - What are your key dependencies and integration points?
  - Are there specific concurrency models or architectural patterns I should know about?

  **Python Runtime Requirements:**
  - Which Python versions do you need to support? (e.g., 3.10, 3.11, 3.12)
  - Do you have any version-specific features or compatibility requirements?
  - Are you targeting specific operating systems?

  **Code Quality Standards:**
  - What are your expectations for code formatting? (Black, autopep8, or custom)
  - Do you need import sorting? (isort standards)
  - What linting rules should be enforced? (Flake8 configuration)
  - Do you require type checking? (MyPy strictness level)
  - What code coverage threshold is acceptable? (typically 80%+)

  **Security & Compliance:**
  - Are there specific compliance requirements? (OWASP, NIST 800-53, ISO 27001)
  - What level of security scanning do you need? (Bandit, Safety)
  - Should security scans block deployments or just warn?
  - Are there internal security policies to enforce?

  **Testing Requirements:**
  - What types of tests do you have? (unit, integration, async/event loop)
  - What testing frameworks and libraries do you use? (pytest, unittest, mocking libraries)
  - Do you need specific test fixtures or conventions documented?

  ---

  Based on your answers, I'll provide:

  ## 1. Complete GitHub Actions Workflow

  A production-ready `.github/workflows/ci.yml` file that includes:
  - Multi-version Python testing matrix
  - Automated code formatting checks (Black)
  - Import sorting verification (isort)
  - Linting with configurable rules (Flake8)
  - Strict type checking (MyPy)
  - Security scanning (Bandit for code, Safety for dependencies)
  - Test execution with coverage reporting
  - Artifact preservation for audit trails
  - Scheduled nightly runs for dependency drift detection

  ## 2. Unified Configuration File

  A complete `pyproject.toml` with:
  - Build system configuration
  - Tool-specific settings (Black, isort, MyPy, pytest, coverage, Bandit)
  - Consistent formatting standards across all tools
  - Coverage thresholds and reporting options

  ## 3. Development Dependencies

  A `requirements-dev.txt` file with pinned versions for:
  - Code formatters and linters
  - Type checkers
  - Security scanners
  - Testing frameworks
  - Coverage tools
  - Pre-commit hooks

  ## 4. Pre-commit Configuration

  Setup for local development with:
  - Automatic formatting before commits
  - Fast local validation
  - Consistency with CI pipeline

  ## 5. Pipeline Optimization Features

  - Dependency caching for faster builds
  - Codecov integration for coverage tracking
  - Multi-format coverage reports (HTML, XML, terminal)
  - Configurable security scan behavior (blocking vs. warning)
  - Matrix testing across Python versions
  - Artifact uploads for debugging and compliance

  ## 6. Quality Assurance Checklist

  A validation checklist to ensure:
  - Pipeline validates across all declared Python versions
  - Code conforms to formatting, linting, and type constraints
  - Coverage thresholds are enforced
  - Security scan artifacts are captured
  - Builds are reproducible and deterministic
  - All configurations are version-controlled

  Tell me about your Python project and I'll create a complete, production-ready CI/CD pipeline tailored to your needs!
---
