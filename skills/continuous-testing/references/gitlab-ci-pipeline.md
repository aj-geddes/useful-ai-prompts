# GitLab CI Pipeline

## GitLab CI Pipeline

```yaml
# .gitlab-ci.yml
stages:
  - test
  - security
  - deploy

variables:
  POSTGRES_DB: test
  POSTGRES_USER: postgres
  POSTGRES_PASSWORD: postgres

# Test template
.test_template:
  image: node:18
  cache:
    paths:
      - node_modules/
  before_script:
    - npm ci

# Unit tests - Runs on every commit
unit-tests:
  extends: .test_template
  stage: test
  script:
    - npm run test:unit -- --coverage
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
    paths:
      - coverage/

# Integration tests
integration-tests:
  extends: .test_template
  stage: test
  services:
    - postgres:14
    - redis:7
  variables:
    DATABASE_URL: postgresql://postgres:postgres@postgres:5432/test
  script:
    - npm run db:migrate
    - npm run test:integration

# E2E tests - Parallel execution
e2e-tests:
  extends: .test_template
  stage: test
  parallel: 4
  script:
    - npx playwright install --with-deps chromium
    - npm run build
    - npx playwright test --shard=$CI_NODE_INDEX/$CI_NODE_TOTAL
  artifacts:
    when: always
    paths:
      - playwright-report/
    expire_in: 7 days

# Security scanning
security-scan:
  stage: security
  image: node:18
  script:
    - npm audit --audit-level=moderate
    - npx snyk test --severity-threshold=high
  allow_failure: true

# Contract tests
contract-tests:
  extends: .test_template
  stage: test
  script:
    - npm run test:pact
    - npx pact-broker publish ./pacts \
      --consumer-app-version=$CI_COMMIT_SHA \
      --broker-base-url=$PACT_BROKER_URL \
      --broker-token=$PACT_BROKER_TOKEN
  only:
    - merge_requests
    - main
```
