---
name: load-balancer-setup
description: >
  Configure and deploy load balancers (HAProxy, AWS ELB/ALB/NLB) for
  distributing traffic, session management, and high availability.
---

# Load Balancer Setup

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Deploy and configure load balancers to distribute traffic across multiple backend servers, ensuring high availability, fault tolerance, and optimal resource utilization across your infrastructure.

## When to Use

- Multi-server traffic distribution
- High availability and failover
- Session persistence and sticky sessions
- Health checking and auto-recovery
- SSL/TLS termination
- Cross-region load balancing
- API rate limiting at load balancer
- DDoS mitigation

## Quick Start

Minimal working example:

```conf
# /etc/haproxy/haproxy.cfg
global
    log stdout local0
    log stdout local1 notice
    maxconn 4096
    daemon

    # Security
    tune.ssl.default-dh-param 2048
    ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256
    ssl-default-bind-options ssl-min-ver TLSv1.2

defaults
    log global
    mode http
    option httplog
    option denylogin
    option forwardfor
    option http-server-close

    # Timeouts
    timeout connect 5000
    timeout client 50000
    timeout server 50000

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [HAProxy Configuration](references/haproxy-configuration.md) | HAProxy Configuration |
| [AWS Application Load Balancer (CloudFormation)](references/aws-application-load-balancer-cloudformation.md) | AWS Application Load Balancer (CloudFormation) |
| [Load Balancer Health Check Script](references/load-balancer-health-check-script.md) | Load Balancer Health Check Script |
| [Load Balancer Monitoring](references/load-balancer-monitoring.md) | Load Balancer Monitoring |

## Best Practices

### ✅ DO

- Implement health checks
- Use connection pooling
- Enable session persistence when needed
- Monitor load balancer metrics
- Implement rate limiting
- Use multiple availability zones
- Enable SSL/TLS termination
- Implement graceful connection draining

### ❌ DON'T

- Allow single point of failure
- Skip health check configuration
- Mix HTTP and HTTPS without redirect
- Ignore backend server limits
- Over-provision without monitoring
- Cache sensitive responses
- Use default security groups
- Neglect backup load balancers
