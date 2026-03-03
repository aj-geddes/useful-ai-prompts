---
name: docker-containerization
description: >
  Create optimized Docker containers with multi-stage builds, security best
  practices, and minimal image sizes. Use when containerizing applications,
  creating Dockerfiles, optimizing container images, or setting up Docker
  Compose services.
---

# Docker Containerization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build production-ready Docker containers following best practices for security, performance, and maintainability.

## When to Use

- Containerizing applications for deployment
- Creating Dockerfiles for new services
- Optimizing existing container images
- Setting up development environments
- Building CI/CD container pipelines
- Implementing microservices

## Quick Start

Minimal working example:

```dockerfile
# Multi-stage build for Node.js application
# Stage 1: Build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine
WORKDIR /app
# Copy only production dependencies and built files
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package*.json ./

# Security: Run as non-root user
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
USER nodejs

EXPOSE 3000
CMD ["node", "dist/index.js"]
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Multi-Stage Builds](references/multi-stage-builds.md) | Multi-Stage Builds |
| [Optimization Techniques](references/optimization-techniques.md) | Optimization Techniques |
| [Security Best Practices](references/security-best-practices.md) | Security Best Practices, Environment Configuration |
| [Docker Compose for Multi-Container](references/docker-compose-for-multi-container.md) | Docker Compose for Multi-Container |
| [.dockerignore File](references/dockerignore-file.md) | .dockerignore File |
| [Python](references/python.md) | Python (Django/Flask), Java (Spring Boot), Go |

## Best Practices

### ✅ DO

- Use official base images
- Implement multi-stage builds
- Run as non-root user
- Use .dockerignore
- Pin specific versions
- Include health checks
- Scan for vulnerabilities
- Minimize layers
- Use build caching effectively

### ❌ DON'T

- Use 'latest' tag in production
- Run as root user
- Include secrets in images
- Create unnecessary layers
- Install unnecessary packages
- Ignore security updates
- Store data in containers
