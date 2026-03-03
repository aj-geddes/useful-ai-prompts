---
name: api-gateway-configuration
description: >
  Configure API gateways for routing, authentication, rate limiting, and
  request/response transformation. Use when deploying microservices, setting up
  reverse proxies, or managing API traffic.
---

# API Gateway Configuration

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Design and configure API gateways to handle routing, authentication, rate limiting, and request/response transformation for microservice architectures.

## When to Use

- Setting up reverse proxies for microservices
- Centralizing API authentication
- Implementing request/response transformation
- Managing traffic across backend services
- Rate limiting and quota enforcement
- API versioning and routing

## Quick Start

Minimal working example:

```yaml
# kong.yml - Kong Gateway configuration
_format_version: "2.1"
_transform: true

services:
  - name: user-service
    url: http://user-service:3000
    routes:
      - name: user-routes
        paths:
          - /api/users
          - /api/profile
    plugins:
      - name: rate-limiting
        config:
          minute: 100
          policy: local
      - name: jwt
        config:
          secret: your-secret-key
          key_claim_name: "sub"
      - name: cors
        config:
          origins:
            - "http://localhost:3000"
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Kong Configuration](references/kong-configuration.md) | Kong Configuration |
| [Nginx Configuration](references/nginx-configuration.md) | Nginx Configuration |
| [AWS API Gateway Configuration](references/aws-api-gateway-configuration.md) | AWS API Gateway Configuration |
| [Traefik Configuration](references/traefik-configuration.md) | Traefik Configuration |
| [Node.js Gateway Implementation](references/nodejs-gateway-implementation.md) | Node.js Gateway Implementation |

## Best Practices

### ✅ DO

- Centralize authentication at gateway level
- Implement rate limiting globally
- Add comprehensive logging
- Use health checks for backends
- Cache responses when appropriate
- Implement circuit breakers
- Monitor gateway metrics
- Use HTTPS in production

### ❌ DON'T

- Expose backend service details
- Skip request validation
- Forget to log API usage
- Use weak authentication
- Over-cache dynamic data
- Ignore backend timeouts
- Skip security headers
- Expose internal IPs
