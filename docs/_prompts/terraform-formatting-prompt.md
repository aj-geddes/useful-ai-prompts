---
category: technical-workflows
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Automate Terraform code validation, formatting, linting, and Git workflow integration with comprehensive quality checks
layout: prompt
slug: terraform-formatting-prompt
tags:
- technical
- terraform
- code-quality
- automation
- git
title: Terraform Quality Automation and Git Integration
use_cases:
- technical optimization
- professional workflow enhancement
- code quality assurance
version: 3.0.0
prompt: |
  I'll help you set up automated Terraform validation and quality control with Git integration. Let me understand your project:

  ## Understanding Your Terraform Project

  **Project Information:**
  - What is the path to your Terraform project? (local directory path)
  - What Git repository URL should I use for commits? (GitHub, GitLab, Bitbucket)
  - What type of Terraform project is this? (infrastructure, modules, multi-environment)
  - Are there multiple environments or workspaces to consider?

  **Quality Standards:**
  - What formatting standard do you follow? (default Terraform, custom rules)
  - Are there specific linting rules you want to enforce?
  - Do you have security scanning requirements?
  - Are there naming conventions or organizational policies?

  **Git Workflow:**
  - What branch should changes be committed to? (main, develop, feature branch)
  - Do you have a preferred commit message style?
  - Are there any pre-commit hooks or CI/CD processes to consider?
  - Do you need automated branch protection or PR creation?

  **Validation Requirements:**
  - Should validation block on errors or just warn?
  - Do you need dependency version checking?
  - Are there provider-specific validations needed?
  - Should deprecated resources or syntax be flagged?

  ---

  Based on your answers, I'll provide:

  ## 1. Automated Formatting (terraform fmt)

  Comprehensive code beautification:
  - Recursive formatting across all .tf files
  - Before/after diff display for review
  - Consistent indentation and spacing
  - Canonical HCL syntax formatting
  - Line length optimization
  - Automatic fixes applied to filesystem

  ## 2. Configuration Validation (terraform validate)

  Schema and syntax checking:
  - Configuration structure validation
  - Required input verification
  - Resource dependency validation
  - Provider configuration checks
  - Backend initialization (without state)
  - File-by-file error reporting with line numbers
  - Auto-fix suggestions for common issues

  ## 3. Advanced Linting (TFLint)

  Static code analysis including:
  - Deprecated syntax detection
  - Unused variable identification
  - Security best practices checking
  - Provider-specific rule enforcement
  - Complexity analysis
  - Issue categorization (ERROR, WARNING, INFO)
  - File-specific recommendations
  - Automatic remediation for simple issues

  ## 4. Git Integration Workflow

  Automated version control:
  - Repository initialization (if needed)
  - Automatic staging of modified files
  - Descriptive commit message generation
  - Push to specified remote repository
  - Branch detection and management
  - Commit hash tracking
  - Push verification

  ## 5. Multi-Phase Execution Report

  Structured Markdown summary with:
  - **Phase 0: Initialization** - Project setup and Git configuration
  - **Phase 1: Formatting** - Files changed, formatting diffs
  - **Phase 2: Validation** - Configuration errors and fixes
  - **Phase 3: Linting** - Static analysis results and recommendations
  - **Phase 4: Git Commit** - Commit details and push status
  - **Final Summary** - Overall results and next steps

  ## 6. Error Handling and Recovery

  Intelligent error management:
  - Clear error messages with context
  - Suggested fixes for common issues
  - Graceful degradation on non-critical failures
  - Validation checkpoint before commits
  - Rollback capabilities for failed operations

  ## 7. Project State Verification

  Pre-execution checks:
  - Project path existence confirmation
  - .tf file detection
  - Git repository status
  - Provider availability
  - Terraform version compatibility

  ## 8. Quality Metrics

  Comprehensive reporting:
  - Number of files formatted
  - Validation issues found and fixed
  - Linting warnings by severity
  - Code quality score
  - Comparison with previous runs

  ## 9. Integration with Development Tools

  Seamless workflow integration:
  - MCP tool compatibility
  - CI/CD pipeline preparation
  - Pre-commit hook generation
  - IDE integration guidance
  - Team workflow documentation

  ## 10. Best Practices Implementation

  Following Terraform standards:
  - HCL style guide compliance
  - HashiCorp recommended patterns
  - Security scanning integration
  - Documentation requirements
  - Module best practices

  Tell me about your Terraform project and I'll set up a complete automated quality control and Git workflow system!
---
