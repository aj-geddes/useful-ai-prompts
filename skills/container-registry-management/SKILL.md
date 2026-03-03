---
name: container-registry-management
description: >
  Manage container registries (Docker Hub, ECR, GCR) with image scanning,
  retention policies, and access control.
---

# Container Registry Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive container registry management including image scanning, vulnerability detection, retention policies, access control, and multi-region replication.

## When to Use

- Container image storage and distribution
- Security scanning and compliance
- Image retention and cleanup
- Registry access control
- Multi-region deployments
- Image signing and verification
- Cost optimization

## Quick Start

Minimal working example:

```yaml
# ecr-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: ecr-management
  namespace: operations
data:
  setup-ecr.sh: |
    #!/bin/bash
    set -euo pipefail

    REGISTRY_NAME="myapp"
    REGION="us-east-1"
    ACCOUNT_ID="123456789012"

    echo "Setting up ECR repository..."

    # Create ECR repository
    aws ecr create-repository \
      --repository-name "$REGISTRY_NAME" \
      --region "$REGION" \
      --encryption-configuration encryptionType=KMS,kmsKey=arn:aws:kms:$REGION:$ACCOUNT_ID:key/12345678-1234-1234-1234-123456789012 \
      --image-tag-mutability IMMUTABLE \
      --image-scanning-configuration scanOnPush=true || true

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [AWS ECR Setup and Management](references/aws-ecr-setup-and-management.md) | AWS ECR Setup and Management |
| [Container Image Build and Push](references/container-image-build-and-push.md) | Container Image Build and Push |
| [Image Signing with Notary](references/image-signing-with-notary.md) | Image Signing with Notary |
| [Registry Access Control](references/registry-access-control.md) | Registry Access Control |
| [Registry Monitoring](references/registry-monitoring.md) | Registry Monitoring |

## Best Practices

### ✅ DO

- Scan images before deployment
- Use image tag immutability
- Implement retention policies
- Control registry access with IAM
- Sign images for verification
- Replicate across regions
- Monitor registry storage
- Use private registries

### ❌ DON'T

- Push to public registries
- Use `latest` tag in production
- Allow anonymous pulls
- Store secrets in images
- Keep old images indefinitely
- Push without scanning
- Use default credentials
- Share registry credentials
