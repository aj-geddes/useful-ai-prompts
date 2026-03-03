---
name: secrets-management
description: >
  Implement secrets management with HashiCorp Vault, AWS Secrets Manager, or
  Kubernetes Secrets for secure credential storage and rotation.
---

# Secrets Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Deploy and configure secure secrets management systems to store, rotate, and audit access to sensitive credentials, API keys, and certificates across your infrastructure.

## When to Use

- Database credentials management
- API key and token storage
- Certificate management
- SSH key distribution
- Credential rotation automation
- Audit and compliance logging
- Multi-environment secrets
- Encryption key management

## Quick Start

Minimal working example:

```hcl
# vault-config.hcl
storage "raft" {
  path    = "/vault/data"
  node_id = "node1"
}

listener "tcp" {
  address       = "0.0.0.0:8200"
  tls_cert_file = "/vault/config/vault.crt"
  tls_key_file  = "/vault/config/vault.key"
}

api_addr     = "https://0.0.0.0:8200"
cluster_addr = "https://0.0.0.0:8201"

ui = true
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [HashiCorp Vault Setup](references/hashicorp-vault-setup.md) | HashiCorp Vault Setup |
| [Vault Kubernetes Integration](references/vault-kubernetes-integration.md) | Vault Kubernetes Integration |
| [Vault Secret Configuration](references/vault-secret-configuration.md) | Vault Secret Configuration |
| [AWS Secrets Manager Configuration](references/aws-secrets-manager-configuration.md) | AWS Secrets Manager Configuration |
| [Kubernetes Secrets](references/kubernetes-secrets.md) | Kubernetes Secrets |

## Best Practices

### ✅ DO

- Rotate secrets regularly
- Use strong encryption
- Implement access controls
- Audit secret access
- Use managed services
- Implement secret versioning
- Encrypt secrets in transit
- Use separate secrets per environment

### ❌ DON'T

- Store secrets in code
- Use weak encryption
- Share secrets via email/chat
- Commit secrets to version control
- Use single master password
- Log secret values
- Hardcode credentials
- Disable rotation
