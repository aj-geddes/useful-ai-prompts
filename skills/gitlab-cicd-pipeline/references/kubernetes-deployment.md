# Kubernetes Deployment

## Kubernetes Deployment

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


## Performance Testing Stage

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


## Release Pipeline with Semantic Versioning

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
