---
name: gitlab-cicd-pipeline
description: Design and implement GitLab CI/CD pipelines with stages, jobs, artifacts, and caching. Configure runners, Docker integration, and deployment strategies.
---

# GitLab CI/CD Pipeline

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

## Implementation Examples

### 1. **Complete Pipeline Configuration**

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
    - npm run lint
    - npm run format:check
  artifacts:
    reports:
      codequality: code-quality-report.json
    expire_in: 1 week

unit-tests:
  stage: test
  script:
    - npm install
    - npm run test:coverage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
      junit: test-results.xml
    paths:
      - coverage/
    expire_in: 1 week
  coverage: '/Coverage: \d+\.\d+%/'

integration-tests:
  stage: test
  services:
    - postgres:13
    - redis:7
  variables:
    POSTGRES_DB: test_db
    POSTGRES_USER: test_user
    POSTGRES_PASSWORD: test_password
  script:
    - npm run test:integration
  only:
    - merge_requests
    - main

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  variables:
    DOCKER_HOST: tcp://docker:2375
    REGISTRY: registry.gitlab.com
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA $CI_REGISTRY_IMAGE:latest
    - docker push $CI_REGISTRY_IMAGE:latest
  only:
    - main
    - tags

security-scan:
  stage: security
  image: alpine:latest
  script:
    - apk add --no-cache git
    - git clone https://github.com/aquasecurity/trivy.git
    - ./trivy image $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  allow_failure: true

deploy-review:
  stage: deploy-review
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    url: https://$CI_COMMIT_REF_SLUG.review.example.com
    auto_stop_in: 1 week
  script:
    - helm upgrade --install review-$CI_COMMIT_REF_SLUG ./chart
      --set image.tag=$CI_COMMIT_SHA
      --set environment=review
  only:
    - merge_requests

deploy-prod:
  stage: deploy-prod
  environment:
    name: production
    url: https://example.com
  script:
    - helm upgrade --install prod ./chart
      --set image.tag=$CI_COMMIT_SHA
      --set environment=production
  only:
    - main
  when: manual
```

### 2. **GitLab Runner Configuration**

```bash
#!/bin/bash
# install-runner.sh

# Register GitLab Runner
gitlab-runner register \
  --url https://gitlab.com/ \
  --registration-token $RUNNER_TOKEN \
  --executor docker \
  --docker-image alpine:latest \
  --docker-privileged \
  --docker-volumes /certs/client \
  --description "Docker Runner" \
  --tag-list "docker,linux" \
  --run-untagged=false \
  --locked=false \
  --access-level not_protected

# Start runner
gitlab-runner start
```

### 3. **Docker Layer Caching Optimization**

```yaml
# .gitlab-ci.yml
stages:
  - build

build-image:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  variables:
    DOCKER_HOST: tcp://docker:2375
    DOCKER_TLS_CERTDIR: ""
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY

    # Pull previous image for cache
    - docker pull $CI_REGISTRY_IMAGE:latest || true

    # Build with cache
    - docker build
        --cache-from $CI_REGISTRY_IMAGE:latest
        --tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
        --tag $CI_REGISTRY_IMAGE:latest
        .

    # Push images
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker push $CI_REGISTRY_IMAGE:latest
  cache:
    key: ${CI_COMMIT_REF_SLUG}-docker
    paths:
      - .docker/
```

### 4. **Multi-Project Pipeline**

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

build:backend:
  stage: build
  script:
    - cd backend && npm run build
  artifacts:
    paths:
      - backend/dist/

build:frontend:
  stage: build
  script:
    - cd frontend && npm run build
  artifacts:
    paths:
      - frontend/dist/

test:backend:
  stage: test
  needs: ["build:backend"]
  script:
    - cd backend && npm test
  artifacts:
    reports:
      junit: backend/test-results.xml

test:frontend:
  stage: test
  needs: ["build:frontend"]
  script:
    - cd frontend && npm test
  artifacts:
    reports:
      junit: frontend/test-results.xml

deploy:
  stage: deploy
  needs: ["test:backend", "test:frontend"]
  script:
    - echo "Deploying backend and frontend..."
  when: manual
```

### 5. **Kubernetes Deployment**

```yaml
# .gitlab-ci.yml
deploy-k8s:
  stage: deploy
  image: alpine/k8s:latest
  script:
    - mkdir -p $HOME/.kube
    - echo $KUBE_CONFIG_ENCODED | base64 -d > $HOME/.kube/config
    - chmod 600 $HOME/.kube/config

    # Update image in deployment
    - kubectl set image deployment/app-deployment
        app=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
        -n production

    # Wait for rollout
    - kubectl rollout status deployment/app-deployment -n production
  environment:
    name: production
    kubernetes:
      namespace: production
  only:
    - main
  when: manual
```

### 6. **Performance Testing Stage**

```yaml
# .gitlab-ci.yml
performance:
  stage: test
  image: grafana/k6:latest
  script:
    - k6 run tests/performance.js
  artifacts:
    reports:
      performance: performance-results.json
    expire_in: 1 week
  allow_failure: true
  only:
    - main
    - merge_requests
```

### 7. **Release Pipeline with Semantic Versioning**

```yaml
# .gitlab-ci.yml
release:
  stage: deploy-prod
  image: node:18-alpine
  script:
    - npm install -g semantic-release @semantic-release/gitlab

    # Configure git
    - git config user.email "ci@example.com"
    - git config user.name "CI Bot"

    # Run semantic-release
    - semantic-release
  only:
    - main
  when: manual
```

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

## Gitlab Runner Executor Types

```bash
# Docker executor (recommended)
gitlab-runner register --executor docker

# Kubernetes executor
gitlab-runner register --executor kubernetes

# Shell executor (local)
gitlab-runner register --executor shell

# Machine executor (for auto-scaling)
gitlab-runner register --executor machine
```

## Resources

- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [GitLab CI/CD Examples](https://docs.gitlab.com/ee/ci/examples/)
- [GitLab Runner Configuration](https://docs.gitlab.com/runner/configuration/)
- [Kubernetes Executor](https://docs.gitlab.com/runner/executors/kubernetes.html)
