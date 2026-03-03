---
name: gitlab-cicd-pipeline
description: >
  Design and implement GitLab CI/CD pipelines with stages, jobs, artifacts, and
  caching. Configure runners, Docker integration, and deployment strategies.
---

# GitLab CI/CD Pipeline

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create comprehensive GitLab CI/CD pipelines that automate building, testing, and deployment using GitLab Runner infrastructure and container execution.

## When to Use

- GitLab repository CI/CD setup
- Multi-stage build pipelines
- Docker registry integration
- Kubernetes deployment
- Review app deployment
- Cache optimization
- Dependency management

## Quick Start

Minimal working example:

```yaml
# .gitlab-ci.yml
image: node:18-alpine

variables:
  DOCKER_DRIVER: overlay2
  FF_USE_FASTZIP: "true"

stages:
  - lint
  - test
  - build
  - security
  - deploy-review
  - deploy-prod

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/

lint:
  stage: lint
  script:
    - npm install
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Complete Pipeline Configuration](references/complete-pipeline-configuration.md) | Complete Pipeline Configuration |
| [GitLab Runner Configuration](references/gitlab-runner-configuration.md) | GitLab Runner Configuration |
| [Docker Layer Caching Optimization](references/docker-layer-caching-optimization.md) | Docker Layer Caching Optimization |
| [Multi-Project Pipeline](references/multi-project-pipeline.md) | Multi-Project Pipeline |
| [Kubernetes Deployment](references/kubernetes-deployment.md) | Kubernetes Deployment, Performance Testing Stage, Release Pipeline with Semantic Versioning |

## Best Practices

### ✅ DO

- Use stages to organize pipeline flow
- Implement caching for dependencies
- Use artifacts for test reports
- Set appropriate cache keys
- Implement conditional execution with `only` and `except`
- Use `needs:` for job dependencies
- Clean up artifacts with `expire_in`
- Use Docker for consistent environments
- Implement security scanning stages
- Set resource limits for jobs
- Use merge request pipelines

### ❌ DON'T

- Run tests serially when parallelizable
- Cache everything unnecessarily
- Leave large artifacts indefinitely
- Store secrets in configuration files
- Run privileged Docker without necessity
- Skip security scanning
- Ignore pipeline failures
- Use `only: [main]` without proper controls
