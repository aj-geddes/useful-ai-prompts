---
category: management-leadership
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Automate GitHub repository creation with project-specific templates, CI/CD workflows, and best practices
layout: prompt
slug: repository-setup-automation
tags:
- project management
- github
- automation
- devops
title: GitHub Repository Setup Automation
use_cases:
- project-management optimization
- professional workflow enhancement
- repository automation
version: 3.0.0
prompt: |
  I'll help you create a fully configured GitHub repository with all necessary files and workflows. Let me understand your project:

  ## Understanding Your Repository Needs

  **Basic Repository Information:**
  - What would you like to name your repository?
  - What's the project description?
  - Should this be a public or private repository?
  - Do you want to create it in a specific GitHub organization? (or your personal account)

  **Project Type:**
  - What type of project is this?
    - Python (application, library, data science)
    - Node.js (web app, API, CLI tool)
    - Docker (containerized application)
    - React (frontend application)
    - Standard (general purpose, documentation, other)

  **Development Standards:**
  - What code quality tools do you want? (linters, formatters, type checkers)
  - Do you have specific testing requirements?
  - Are there organizational coding standards to follow?
  - Do you need security scanning or vulnerability checks?

  **Team and Workflow:**
  - How many developers will work on this project?
  - Do you need branch protection rules?
  - Should pull requests require reviews before merging?
  - Do you want issue and PR templates?

  **CI/CD Requirements:**
  - What should automated workflows test or build?
  - Do you need deployment automation?
  - Are there specific platforms to target? (Docker Hub, npm, PyPI, etc.)
  - Do you need scheduled workflows?

  ---

  Based on your answers, I'll provide:

  ## 1. Repository Initialization

  Complete repository setup:
  - Repository creation with proper visibility settings
  - Organization or personal account placement
  - Default branch configuration
  - Description and topics/tags
  - Homepage and documentation links

  ## 2. Project-Specific Structure

  **For Python Projects:**
  - `src/` and `tests/` directories
  - `requirements.txt` and `requirements-dev.txt` with appropriate dependencies
  - `pyproject.toml` with tool configurations (Black, isort, MyPy, pytest, coverage)
  - `.gitignore` for Python
  - `pytest.ini` for test configuration

  **For Node.js Projects:**
  - `src/` directory structure
  - `package.json` with scripts and dependencies
  - `.gitignore` for Node.js
  - `.eslintrc.json` and `.prettierrc` configurations
  - `jest.config.js` or test setup

  **For Docker Projects:**
  - Multi-stage `Dockerfile` with best practices
  - `docker-compose.yml` for development
  - `.dockerignore` for build optimization
  - `scripts/build.sh` and deployment scripts

  **For React Projects:**
  - Component directory structure (`src/components/`, `src/utils/`)
  - Enhanced `package.json` with React-specific scripts
  - `.env.example` for configuration
  - Testing setup with React Testing Library

  **For Standard Projects:**
  - Basic directory structure
  - Generic `.gitignore`
  - Flexible configuration for any project type

  ## 3. Documentation Files

  Professional documentation package:
  - **README.md**: Project overview, installation, usage, examples
  - **CONTRIBUTING.md**: Development setup, coding standards, PR process
  - **LICENSE**: MIT, Apache 2.0, or preferred license
  - **CODE_OF_CONDUCT.md**: Community guidelines
  - **SECURITY.md**: Security policy and vulnerability reporting

  ## 4. GitHub Templates

  Standardized templates for collaboration:
  - `.github/ISSUE_TEMPLATE/bug_report.md`: Structured bug reporting
  - `.github/ISSUE_TEMPLATE/feature_request.md`: Feature proposal format
  - `.github/pull_request_template.md`: PR checklist and description guide
  - `.github/CODEOWNERS`: Automatic reviewer assignment

  ## 5. GitHub Labels

  Organized issue management:
  - Standard labels: `bug`, `enhancement`, `documentation`, `good first issue`, `help wanted`
  - Priority labels: `priority-high`, `priority-medium`, `priority-low`
  - Status labels: `in-progress`, `blocked`, `needs-review`
  - Type labels: `type-feature`, `type-bugfix`, `type-refactor`

  ## 6. Branch Protection Rules

  Repository security configuration:
  - Protect main/master branch
  - Require pull request reviews (configurable number)
  - Require status checks to pass before merging
  - Enforce linear history (optional)
  - Restrict force pushes and deletions

  ## 7. CI/CD Workflows

  Automated GitHub Actions workflows:

  **For Python:**
  - Multi-version testing (3.10, 3.11, 3.12)
  - Code quality checks (Black, isort, Flake8, MyPy)
  - Security scanning (Bandit, Safety)
  - Test execution with coverage reporting

  **For Node.js:**
  - Node version matrix testing
  - ESLint and Prettier checks
  - Jest test execution
  - Build verification

  **For Docker:**
  - Image build and security scanning
  - Multi-architecture builds
  - Container structure tests
  - Registry push on release

  **For React:**
  - Build and test workflow
  - Component testing
  - Production build verification
  - Deployment automation (optional)

  ## 8. Security Features

  GitHub security configuration:
  - Enable Dependabot vulnerability alerts
  - Configure Dependabot version updates
  - Enable secret scanning
  - Configure code scanning (CodeQL)
  - Security policy documentation

  ## 9. Development Tools

  Developer productivity files:
  - `.editorconfig`: Consistent editor settings
  - `.nvmrc` or `.python-version`: Runtime version specification
  - Pre-commit hook configuration
  - Local development scripts
  - Debug configurations

  ## 10. Repository Settings

  Optimal repository configuration:
  - Wiki disabled/enabled based on needs
  - Issues enabled with templates
  - Projects enabled for task tracking
  - Discussions enabled for community (optional)
  - Merge button options configured

  ## 11. Initial Commit Strategy

  Proper repository initialization:
  - All files created in organized structure
  - Comprehensive initial commit message
  - Proper file permissions set
  - Clone URL provided for immediate use

  ## 12. Quick Start Guide

  Getting started documentation:
  - Repository clone instructions
  - Development environment setup steps
  - First contribution guide
  - Common commands and workflows
  - Troubleshooting section

  Tell me about your project and I'll create a complete, production-ready GitHub repository with all the best practices built in!
---
