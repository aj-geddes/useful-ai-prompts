---
name: dns-management
description: >
  Manage DNS records, routing policies, and failover configurations for high
  availability and disaster recovery.
---

# DNS Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement DNS management strategies for traffic routing, failover, geo-routing, and high availability using Route53, Azure DNS, or CloudFlare.

## When to Use

- Domain management and routing
- Failover and disaster recovery
- Geographic load balancing
- Multi-region deployments
- DNS-based traffic management
- CDN integration
- Health check routing
- Zero-downtime migrations

## Quick Start

Minimal working example:

```yaml
# route53-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: route53-config
  namespace: operations
data:
  setup-dns.sh: |
    #!/bin/bash
    set -euo pipefail

    DOMAIN="myapp.com"
    HOSTED_ZONE_ID="Z1234567890ABC"
    PRIMARY_ENDPOINT="myapp-primary.example.com"
    SECONDARY_ENDPOINT="myapp-secondary.example.com"

    echo "Setting up Route53 DNS for $DOMAIN"

    # Create health check for primary
    PRIMARY_HEALTH=$(aws route53 create-health-check \
      --health-check-config '{
        "Type": "HTTPS",
        "ResourcePath": "/health",
        "FullyQualifiedDomainName": "'${PRIMARY_ENDPOINT}'",
        "Port": 443,
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [AWS Route53 Configuration](references/aws-route53-configuration.md) | AWS Route53 Configuration |
| [DNS Failover Script](references/dns-failover-script.md) | DNS Failover Script |
| [CloudFlare DNS Configuration](references/cloudflare-dns-configuration.md) | CloudFlare DNS Configuration |
| [DNS Monitoring and Validation](references/dns-monitoring-and-validation.md) | DNS Monitoring and Validation |

## Best Practices

### ✅ DO

- Use health checks with failover
- Set appropriate TTL values
- Implement geolocation routing
- Use weighted routing for canary
- Monitor DNS resolution
- Document DNS changes
- Test failover procedures
- Use DNS DNSSEC

### ❌ DON'T

- Use TTL of 0
- Point to single endpoint
- Forget health checks
- Mix DNS and application failover
- Change DNS during incidents
- Ignore DNS propagation time
- Use generic names
- Skip DNS monitoring
