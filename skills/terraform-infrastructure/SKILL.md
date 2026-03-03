---
name: terraform-infrastructure
description: >
  Infrastructure as Code using Terraform with modular components, state
  management, and multi-cloud deployments. Use for provisioning and managing
  cloud resources.
---

# Terraform Infrastructure

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build scalable infrastructure as code with Terraform, managing AWS, Azure, GCP, and on-premise resources through declarative configuration, remote state, and automated provisioning.

## When to Use

- Cloud infrastructure provisioning
- Multi-environment management (dev, staging, prod)
- Infrastructure versioning and code review
- Cost tracking and resource optimization
- Disaster recovery and environment replication
- Automated infrastructure testing
- Cross-region deployments

## Quick Start

Minimal working example:

```hcl
# terraform/main.tf
terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # Remote state configuration
  backend "s3" {
    bucket         = "terraform-state-prod"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [AWS Infrastructure Module](references/aws-infrastructure-module.md) | AWS Infrastructure Module |
| [Variables and Outputs](references/variables-and-outputs.md) | Variables and Outputs |
| [Terraform Deployment Script](references/terraform-deployment-script.md) | Terraform Deployment Script |

## Best Practices

### ✅ DO

- Use remote state (S3, Terraform Cloud)
- Implement state locking (DynamoDB)
- Organize code into modules
- Use workspaces for environments
- Apply tags consistently
- Use variables for flexibility
- Implement code review before apply
- Keep sensitive data in separate variable files

### ❌ DON'T

- Store state files locally in git
- Use hardcoded values
- Mix environments in single state
- Skip terraform plan review
- Use root module for everything
- Store secrets in code
- Disable state locking
