---
name: deployment-documentation
description: >
  Document deployment processes, infrastructure setup, CI/CD pipelines, and
  configuration management. Use when creating deployment guides, infrastructure
  docs, or CI/CD documentation.
---

# Deployment Documentation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create comprehensive deployment documentation covering infrastructure setup, CI/CD pipelines, deployment procedures, and rollback strategies.

## When to Use

- Deployment guides
- Infrastructure documentation
- CI/CD pipeline setup
- Configuration management
- Container orchestration
- Cloud infrastructure docs
- Release procedures
- Rollback procedures

## Quick Start

Minimal working example:

````markdown
# Deployment Guide

## Overview

This document describes the deployment process for [Application Name].

**Deployment Methods:**

- Manual deployment (emergency only)
- Automated CI/CD (preferred)
- Blue-green deployment
- Canary deployment

**Environments:**

- Development: https://dev.example.com
- Staging: https://staging.example.com
- Production: https://example.com

---

## Prerequisites

### Required Tools

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [GitHub Actions Workflow](references/github-actions-workflow.md) | GitHub Actions Workflow |
| [Dockerfile](references/dockerfile.md) | Dockerfile |
| [docker-compose.yml](references/docker-composeyml.md) | docker-compose.yml |
| [Deployment Manifest](references/deployment-manifest.md) | Deployment Manifest |

## Best Practices

### ✅ DO

- Use infrastructure as code
- Implement CI/CD pipelines
- Use container orchestration
- Implement health checks
- Use rolling deployments
- Have rollback procedures
- Monitor deployments
- Document emergency procedures
- Use secrets management
- Implement blue-green or canary deployments

### ❌ DON'T

- Deploy directly to production
- Skip testing before deploy
- Forget to backup before migrations
- Deploy without rollback plan
- Skip monitoring after deployment
- Hardcode credentials
- Deploy during peak hours (unless necessary)
