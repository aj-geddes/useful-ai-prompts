---
name: aws-s3-management
description: >
  Manage S3 buckets with versioning, encryption, access control, lifecycle
  policies, and replication. Use for object storage, static sites, and data
  lakes.
---

# AWS S3 Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Amazon S3 provides secure, durable, and highly scalable object storage. Manage buckets with encryption, versioning, access controls, lifecycle policies, and cross-region replication for reliable data storage and retrieval.

## When to Use

- Static website hosting
- Data backup and archival
- Media library and CDN origin
- Data lake and analytics
- Log storage and analysis
- Application asset storage
- Disaster recovery
- Data sharing and collaboration

## Quick Start

Minimal working example:

```bash
# Create bucket
aws s3api create-bucket \
  --bucket my-app-bucket-$(date +%s) \
  --region us-east-1

# Enable versioning
aws s3api put-bucket-versioning \
  --bucket my-app-bucket \
  --versioning-configuration Status=Enabled

# Block public access
aws s3api put-public-access-block \
  --bucket my-app-bucket \
  --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,\
    BlockPublicPolicy=true,RestrictPublicBuckets=true

# Enable encryption
aws s3api put-bucket-encryption \
  --bucket my-app-bucket \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [S3 Bucket Creation and Configuration with AWS CLI](references/s3-bucket-creation-and-configuration-with-aws-cli.md) | S3 Bucket Creation and Configuration with AWS CLI |
| [S3 Lifecycle Policy Configuration](references/s3-lifecycle-policy-configuration.md) | S3 Lifecycle Policy Configuration |
| [Terraform S3 Configuration](references/terraform-s3-configuration.md) | Terraform S3 Configuration |
| [S3 Access with Presigned URLs](references/s3-access-with-presigned-urls.md) | S3 Access with Presigned URLs |

## Best Practices

### ✅ DO

- Enable versioning for important data
- Use server-side encryption
- Block public access by default
- Implement lifecycle policies
- Enable logging and monitoring
- Use bucket policies for access control
- Enable MFA delete for critical buckets
- Use IAM roles instead of access keys
- Implement cross-region replication

### ❌ DON'T

- Make buckets publicly accessible
- Store sensitive credentials
- Ignore CloudTrail logging
- Use overly permissive policies
- Forget to set lifecycle rules
- Ignore encryption requirements
