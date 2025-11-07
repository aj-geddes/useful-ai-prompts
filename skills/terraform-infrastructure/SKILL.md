---
name: terraform-infrastructure
description: Infrastructure as Code using Terraform with modular components, state management, and multi-cloud deployments. Use for provisioning and managing cloud resources.
---

# Terraform Infrastructure

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

## Implementation Examples

### 1. **AWS Infrastructure Module**

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
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Project     = var.project_name
    }
  }
}

# VPC and networking
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "${var.project_name}-vpc"
  }
}

resource "aws_subnet" "public" {
  count                   = length(var.public_subnets)
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnets[count.index]
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name = "${var.project_name}-public-${count.index + 1}"
  }
}

resource "aws_subnet" "private" {
  count             = length(var.private_subnets)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnets[count.index]
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "${var.project_name}-private-${count.index + 1}"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-igw"
  }
}

# NAT Gateway for private subnets
resource "aws_eip" "nat" {
  count  = length(var.public_subnets)
  domain = "vpc"

  tags = {
    Name = "${var.project_name}-eip-${count.index + 1}"
  }

  depends_on = [aws_internet_gateway.main]
}

resource "aws_nat_gateway" "main" {
  count         = length(var.public_subnets)
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id

  tags = {
    Name = "${var.project_name}-nat-${count.index + 1}"
  }

  depends_on = [aws_internet_gateway.main]
}

# Route tables
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "${var.project_name}-public-rt"
  }
}

resource "aws_route_table" "private" {
  count  = length(var.private_subnets)
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.main[count.index].id
  }

  tags = {
    Name = "${var.project_name}-private-rt-${count.index + 1}"
  }
}

# Route table associations
resource "aws_route_table_association" "public" {
  count          = length(var.public_subnets)
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  count          = length(var.private_subnets)
  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

# Security Group
resource "aws_security_group" "alb" {
  name        = "${var.project_name}-alb-sg"
  description = "Security group for ALB"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-alb-sg"
  }
}

# Application Load Balancer
resource "aws_lb" "main" {
  name               = "${var.project_name}-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb.id]
  subnets            = aws_subnet.public[*].id

  enable_deletion_protection = var.environment == "production" ? true : false

  tags = {
    Name = "${var.project_name}-alb"
  }
}

# Data source for availability zones
data "aws_availability_zones" "available" {
  state = "available"
}
```

### 2. **Variables and Outputs**

```hcl
# terraform/variables.tf
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment must be dev, staging, or production."
  }
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnets" {
  description = "Public subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnets" {
  description = "Private subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.10.0/24", "10.0.11.0/24"]
}

# terraform/outputs.tf
output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "vpc_cidr" {
  description = "VPC CIDR block"
  value       = aws_vpc.main.cidr_block
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "Private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "alb_dns_name" {
  description = "DNS name of the ALB"
  value       = aws_lb.main.dns_name
}

output "alb_arn" {
  description = "ARN of the ALB"
  value       = aws_lb.main.arn
}
```

### 3. **Terraform Deployment Script**

```bash
#!/bin/bash
# deploy-terraform.sh - Terraform deployment automation

set -euo pipefail

ENVIRONMENT="${1:-dev}"
ACTION="${2:-plan}"
TF_DIR="terraform"

echo "Terraform $ACTION for environment: $ENVIRONMENT"

cd "$TF_DIR"

# Initialize Terraform
echo "Initializing Terraform..."
terraform init -upgrade

# Format and validate
echo "Validating Terraform configuration..."
terraform fmt -recursive -check .
terraform validate

# Create/select workspace
echo "Creating/selecting workspace: $ENVIRONMENT"
terraform workspace select -or-create "$ENVIRONMENT"

# Plan or apply
case "$ACTION" in
  plan)
    echo "Creating Terraform plan..."
    terraform plan \
      -var-file="environments/$ENVIRONMENT.tfvars" \
      -out="tfplan-$ENVIRONMENT"
    ;;
  apply)
    echo "Applying Terraform changes..."
    terraform apply \
      -var-file="environments/$ENVIRONMENT.tfvars" \
      -auto-approve
    ;;
  destroy)
    echo "WARNING: Destroying infrastructure in $ENVIRONMENT"
    read -p "Are you sure? (yes/no): " confirm
    if [ "$confirm" = "yes" ]; then
      terraform destroy \
        -var-file="environments/$ENVIRONMENT.tfvars" \
        -auto-approve
    fi
    ;;
  *)
    echo "Unknown action: $ACTION"
    exit 1
    ;;
esac

echo "Terraform $ACTION complete!"
```

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

## Terraform Commands

```bash
terraform init        # Initialize Terraform
terraform validate    # Validate configuration
terraform fmt         # Format code
terraform plan        # Preview changes
terraform apply       # Apply changes
terraform destroy     # Remove resources
terraform workspace   # Manage workspaces
```

## Resources

- [Terraform Documentation](https://www.terraform.io/docs/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest)
- [Terraform Module Registry](https://registry.terraform.io/)
- [Terraform Best Practices](https://www.terraform.io/docs/language/values/variables#best-practices)
