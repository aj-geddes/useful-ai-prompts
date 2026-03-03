# Complete Pipeline Configuration

## Complete Pipeline Configuration

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
