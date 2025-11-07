---
category: technical-workflows
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Create production-ready, reusable Terraform modules for Azure resources with comprehensive validation, documentation, and testing
layout: prompt
slug: azurerm-terraform-module-maker
tags:
- technical
- terraform
- azure
- infrastructure-as-code
- devops
title: Azure Terraform Module Builder
use_cases:
- technical optimization
- professional workflow enhancement
- infrastructure automation
version: 3.0.0
prompt: |
  I'll help you create a production-ready Terraform module for Azure resources. Let me gather the requirements:

  ## Understanding Your Infrastructure Needs

  **Azure Resource Information:**
  - What Azure resource are you creating this module for? (Resource Group, Virtual Network, Storage Account, etc.)
  - What's the primary use case for this resource?
  - Are there specific Azure regions you're targeting?
  - Do you have naming conventions or organizational standards to follow?

  **GitHub Repository Details:**
  - What GitHub organization should host this module?
  - What repository name would you like? (e.g., terraform-azurerm-resourcegroup)
  - Should the repository be public or private?
  - Are there team access requirements or branch protection needs?

  **Module Configuration:**
  - Which Terraform and AzureRM provider versions do you need?
  - What variables should be configurable? (names, locations, tags, SKUs, etc.)
  - What outputs would be most useful for consumers of this module?
  - Are there required vs. optional parameters?

  **Security & Compliance:**
  - Do you need resource locks to prevent accidental deletion?
  - Should the module support RBAC role assignments?
  - Are there Azure Policy requirements?
  - Do you need audit logging or Azure Monitor integration?
  - Are there compliance standards to meet? (ISO 27001, SOC 2, etc.)

  **Documentation Requirements:**
  - What level of documentation detail do you need?
  - Should examples show basic and advanced usage?
  - Do you need contribution guidelines?
  - Are there specific usage scenarios to document?

  ---

  Based on your answers, I'll provide:

  ## 1. Complete Terraform Module Files

  Production-ready module structure:
  - **main.tf**: Resource definitions with proper configuration
  - **variables.tf**: Input variables with comprehensive validation
  - **outputs.tf**: All relevant resource outputs
  - **terraform.tf**: Version constraints and provider requirements
  - **versions.tf**: Alternative provider configuration

  ## 2. Enhanced Input Validation

  Comprehensive validation rules for:
  - Azure resource naming conventions (length, character sets, restricted patterns)
  - Azure region validation with helpful error messages
  - Tag constraints (count limits, key/value length, organizational standards)
  - Type constraints with clear documentation
  - Default values following Azure best practices

  ## 3. Security & Compliance Features

  Optional security enhancements:
  - Resource lock configurations (CanNotDelete, ReadOnly)
  - RBAC role assignment capabilities
  - Azure Policy integration options
  - Sensitive output handling
  - Azure Activity Log integration

  ## 4. Comprehensive Documentation

  Complete README.md with:
  - terraform-docs auto-generated tables
  - Multiple usage examples (basic, advanced, with tags)
  - Requirements, providers, inputs, and outputs tables
  - Validation rules documentation
  - Development setup and testing instructions
  - Contribution guidelines and support information

  ## 5. Testing & Examples

  Testing infrastructure:
  - **examples/basic/**: Simple usage with minimal configuration
  - **examples/advanced/**: Complex scenarios with all features
  - **tests/**: terraform-test files for validation
  - Example-specific provider configurations

  ## 6. Repository Structure

  Complete repository setup:
  - **LICENSE**: Apache 2.0 with proper attribution
  - **.gitignore**: Comprehensive Terraform exclusions
  - **.editorconfig**: Consistent development environment
  - **CONTRIBUTING.md**: Contribution guidelines
  - **SECURITY.md**: Security policy and vulnerability reporting
  - **CHANGELOG.md**: Version history template
  - **.github/ISSUE_TEMPLATE/**: Bug report and feature request templates

  ## 7. GitHub Repository Initialization

  Automated repository creation:
  - Repository initialization with proper settings
  - Branch protection rules
  - Issue and PR templates
  - Initial file structure
  - Semantic versioning setup

  ## 8. Quality Assurance

  Built-in quality checks:
  - terraform fmt validation
  - terraform validate syntax checking
  - Example testing (terraform plan)
  - terraform-docs compatibility
  - Security best practices validation

  ## 9. Version Management

  Release management setup:
  - Semantic versioning strategy
  - GitHub releases integration
  - Breaking changes documentation
  - Backward compatibility guidelines
  - Migration guides for major versions

  ## 10. Success Validation

  Verification checklist ensuring:
  - Module creates Azure resources successfully
  - All inputs properly validated with clear error messages
  - terraform-test suite passes
  - Documentation is comprehensive and accurate
  - Security best practices implemented
  - Repository follows industry standards
  - Module can be consumed via GitHub source immediately
  - Clear maintenance and contribution process

  Tell me about your Azure resource and I'll create a complete, production-ready Terraform module with comprehensive documentation and testing!
---
