# Multi-Project Pipeline

## Multi-Project Pipeline

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
