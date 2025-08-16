---
category: technical
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for technical optimization and expert consultation
slug: azurerm-terraform-module-maker
tags:
- technical
title: Azurerm Terraform Module Maker
use_cases:
- technical optimization
- professional workflow enhancement
version: 3.0.0
---

Create a new **private repository** in the GitHub organization `Ask USer for GitHub Orginization Name` named ` Ask User for Repository Name`.

Initialize it as a **production-ready, reusable Terraform module** using the `azurerm` provider with comprehensive validation, documentation, and development workflows.

## Core Requirements

### Terraform Configuration

- **Provider**: `azurerm` >= 3.0 with `features {}` block enabled
- **Terraform version**: >= 1.5.0 with explicit constraint
- **Module structure**: Standard layout with `main.tf`, `variables.tf`, `outputs.tf`

### Resource Implementation

- **Primary resource**: Ask the User "What Primary Resource are we writing this module for?"
- **Variables**: Using AzureRM Provider documentation set Variables appropriate for the Primary Resource.
- **Validation**: Implement Azure naming conventions, region validation, tag limits
- **Outputs**: Using AzureRM Provider documentation set Outputs that are useful and appropriate for the Primary Resource.

## Enhanced Documentation & Quality

### README.md Requirements

- **terraform-docs format** with auto-generated tables
- **Multiple usage examples**: basic, advanced with tags, output referencing
- **Requirements/Providers/Inputs/Outputs tables**: Properly formatted with links
- **Validation rules section**: Document all constraints clearly
- **Development section**: Prerequisites, testing workflow, contribution guidelines
- **Support section**: Issue reporting, troubleshooting guidance

### Repository Files

- **LICENSE**: Apache 2.0 with proper copyright attribution
- **.gitignore**: Comprehensive coverage (Terraform, IDE, OS, development files)
- **.terraform.lock.hcl**: Sample lock file with realistic provider versions

## Advanced Features (New)

### Development Workflow Enhancement

- **terraform.tf**: Separate file for Terraform/provider requirements
- **versions.tf**: Alternative naming convention option
- **examples/ directory**: Create with basic and advanced usage examples
- **CHANGELOG.md**: Version history and breaking changes documentation

### Code Quality & Validation

- **Enhanced input validation**:
  - Resource Group name: Length, character set, ending restrictions
  - Location: Comprehensive Azure region list validation
  - Tags: Key/value length limits, reserved tag validation
- **Variable descriptions**: Detailed, user-friendly explanations
- **Output descriptions**: Clear purpose and usage guidance

### Security & Compliance Features

- **Resource locks**: Optional management lock configuration
- **RBAC integration**: Role assignment capabilities for Resource Group
- **Azure Policy**: Policy assignment options for compliance
- **Sensitive data**: Proper handling of sensitive outputs and variables
- **Audit logging**: Integration with Azure Activity Log and Monitor

### Versioning & Release Management

- **Semantic versioning**: Implement proper version tagging strategy
- **Release automation**: GitHub releases with changelog generation
- **Breaking changes**: Clear documentation and migration guides
- **Backward compatibility**: Maintain compatibility across minor versions
- **Branch protection**: Protect main branch with PR requirements

## Implementation Strategy

### MCP Tool Optimization

- **Use `create_or_update_file`** for individual file creation to handle empty repository initialization
- **Leverage `push_files`** for bulk operations when repository has content
- **Handle empty repository pattern**: Start with single file, then add remaining files
- **Systematic commits**: One file per commit with descriptive messages for better history

### Repository Setup Process

1. **Initialize repository** with proper privacy settings and description
2. **Create first file** (main.tf) to establish main branch
3. **Add remaining core files** individually with proper commit messages
4. **Create directory structure** with examples/ and docs/ folders
5. **Implement development files** (.editorconfig, .terraform-docs.yml if needed)
6. **Validate completion** by checking repository structure

### Validation & Testing

- **Terraform fmt**: Ensure consistent formatting across all .tf files
- **Terraform validate**: Syntax and configuration validation
- **terraform-test**: Create basic unit tests for variable validation
- **Example testing**: Verify examples work with module (terraform plan)
- **Documentation generation**: terraform-docs compatibility verification
- **Security validation**: Check for sensitive data exposure in outputs

### Quality Assurance

- **Input edge cases**: Test boundary conditions for all variables
- **Error handling**: Meaningful error messages for validation failures
- **Resource naming**: Follow Azure best practices and conventions
- **Tag standardization**: Implement common organizational tagging patterns

## Deliverables

### Core Module Files

- `main.tf` - Resource definitions with provider configuration
- `variables.tf` - Input variables with comprehensive validation
- `outputs.tf` - All relevant resource outputs
- `terraform.tf` - Requirements block (alternative structure)

### Documentation & Examples

- `README.md` - Production-ready documentation with terraform-docs format
- `examples/basic/` - Simple usage example with minimal configuration
- `examples/advanced/` - Complex usage with all features demonstrated
- `CHANGELOG.md` - Version history preparation

### Testing & Validation Files

- `tests/` - Directory with terraform-test files for validation testing
- `examples/basic/main.tf` - Working basic example with required variables only
- `examples/advanced/main.tf` - Complex example showcasing all features
- `examples/*/terraform.tf` - Example-specific requirements and provider configs

### Repository Management

- `LICENSE` - Apache 2.0 with proper attribution
- `.gitignore` - Comprehensive exclusions (include .terraform.lock.hcl in examples)
- `.editorconfig` - Consistent development environment
- `CONTRIBUTING.md` - Guidelines for contributors
- `SECURITY.md` - Security policy and vulnerability reporting
- `.github/ISSUE_TEMPLATE/` - Bug report and feature request templates

### Validation Features

- **Name validation**: 1-90 chars, Azure character set, no period ending
- **Location validation**: Complete Azure region enumeration with error guidance
- **Tag validation**: Count limits, key/value length, organizational standards
- **Type constraints**: Proper variable typing with examples

## Success Criteria

✅ **Functional**: Module creates Azure Resource Group successfully  
✅ **Validated**: All inputs properly validated with clear error messages  
✅ **Tested**: terraform-test suite passes with example validation  
✅ **Documented**: terraform-docs compatible with comprehensive examples  
✅ **Secure**: Security best practices implemented with proper RBAC options  
✅ **Professional**: Repository structure follows industry best practices  
✅ **Reusable**: Module can be consumed via GitHub source immediately  
✅ **Maintainable**: Clear structure for future enhancements and contributions  
✅ **Versioned**: Proper semantic versioning and release management setup

## Quality Standards

- **Documentation**: Every variable, output, and validation rule documented
- **Examples**: Working examples that demonstrate all module capabilities
- **Validation**: Comprehensive input checking with user-friendly error messages
- **Structure**: Clean, logical file organization following Terraform conventions
- **Licensing**: Proper open-source licensing with attribution
- **Version control**: Meaningful commit history with atomic changes
