---
name: ssl-certificate-management
description: >
  Manage SSL/TLS certificates with automated provisioning, renewal, and
  monitoring using Let's Encrypt, ACM, or Vault.
---

# SSL Certificate Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement automated SSL/TLS certificate management across infrastructure, including provisioning, renewal, monitoring, and secure distribution to services.

## When to Use

- HTTPS/TLS enablement
- Certificate renewal automation
- Multi-domain certificate management
- Wildcard certificate handling
- Certificate monitoring and alerts
- Zero-downtime certificate rotation
- Internal PKI management

## Quick Start

Minimal working example:

```yaml
# cert-manager-setup.yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@myapp.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      # HTTP-01 solver for standard domains
      - http01:
          ingress:
            class: nginx
        selector:
          dnsNames:
            - "myapp.com"
            - "www.myapp.com"

      # DNS-01 solver for wildcard domains
      - dns01:
          route53:
            region: us-east-1
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Let's Encrypt with Cert-Manager](references/lets-encrypt-with-cert-manager.md) | Let's Encrypt with Cert-Manager |
| [AWS ACM Certificate Management](references/aws-acm-certificate-management.md) | AWS ACM Certificate Management |
| [Certificate Monitoring and Renewal](references/certificate-monitoring-and-renewal.md) | Certificate Monitoring and Renewal |
| [Automated Certificate Renewal](references/automated-certificate-renewal.md) | Automated Certificate Renewal |
| [Certificate Pinning](references/certificate-pinning.md) | Certificate Pinning |

## Best Practices

### ✅ DO

- Automate certificate renewal
- Use Let's Encrypt for public certs
- Monitor certificate expiration
- Use wildcard certs strategically
- Implement certificate pinning
- Rotate certificates regularly
- Store keys securely
- Use strong key sizes (2048+ RSA, 256+ ECDSA)

### ❌ DON'T

- Manual certificate management
- Self-signed certs in production
- Share private keys
- Ignore expiration warnings
- Use weak key sizes
- Mix dev and prod certs
- Commit certs to git
- Disable certificate validation
