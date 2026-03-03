---
name: aws-ec2-setup
description: >
  Launch and configure EC2 instances with security groups, IAM roles, key pairs,
  AMIs, and auto-scaling. Use for virtual servers and managed infrastructure.
---

# AWS EC2 Setup

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Amazon EC2 provides resizable compute capacity in the cloud. Launch and configure virtual servers with complete control over networking, storage, and security settings. Scale automatically based on demand.

## When to Use

- Web application servers
- Application backends and APIs
- Batch processing and compute jobs
- Development and testing environments
- Containerized applications (ECS)
- Kubernetes clusters (EKS)
- Database servers
- VPN and proxy servers

## Quick Start

Minimal working example:

```bash
# Create security group
aws ec2 create-security-group \
  --group-name web-server-sg \
  --description "Web server security group" \
  --vpc-id vpc-12345678

# Add ingress rules
aws ec2 authorize-security-group-ingress \
  --group-id sg-0123456789abcdef0 \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress \
  --group-id sg-0123456789abcdef0 \
  --protocol tcp \
  --port 443 \
  --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress \
  --group-id sg-0123456789abcdef0 \
  --protocol tcp \
  --port 22 \
  --cidr YOUR_IP/32

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [EC2 Instance Creation with AWS CLI](references/ec2-instance-creation-with-aws-cli.md) | EC2 Instance Creation with AWS CLI |
| [User Data Script](references/user-data-script.md) | User Data Script |
| [Terraform EC2 Configuration](references/terraform-ec2-configuration.md) | Terraform EC2 Configuration |

## Best Practices

### ✅ DO

- Use security groups for network control
- Attach IAM roles for AWS access
- Enable CloudWatch monitoring
- Use AMI for consistent deployments
- Implement auto-scaling for variable load
- Use EBS for persistent storage
- Enable termination protection for production
- Keep systems patched and updated

### ❌ DON'T

- Use overly permissive security groups
- Store credentials in user data
- Ignore CloudWatch metrics
- Use outdated AMIs
- Create hardcoded configurations
- Forget to monitor costs
