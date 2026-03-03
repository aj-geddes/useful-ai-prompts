# npm Package Publishing

## npm Package Publishing

```json
{
  "name": "@myorg/awesome-library",
  "version": "1.2.3",
  "description": "Awesome library for developers",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "files": ["dist", "README.md", "LICENSE"],
  "publishConfig": {
    "registry": "https://npm.pkg.github.com",
    "access": "public"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/myorg/awesome-library.git"
  },
  "scripts": {
    "prepublishOnly": "npm run build && npm run test",
    "prepack": "npm run build"
  }
}
```


## Artifact Retention Policy

```yaml
# .github/workflows/cleanup-artifacts.yml
name: Cleanup Old Artifacts

on:
  schedule:
    - cron: "0 2 * * *" # Daily at 2 AM
  workflow_dispatch:

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - name: Delete artifacts older than 30 days
        uses: geekyeggo/delete-artifact@v2
        with:
          name: "*"
          minCreatedTime: 30d
          failOnError: false
```


## Artifact Versioning

```bash
#!/bin/bash
# artifact-version.sh

BUILD_DATE=$(date -u +'%Y%m%d')
GIT_HASH=$(git rev-parse --short HEAD)
VERSION=$(grep '"version"' package.json | sed 's/.*"version": "\([^"]*\)".*/\1/')

# Full version tag
FULL_VERSION="${VERSION}-${BUILD_DATE}.${GIT_HASH}"

# Create artifact with version
docker build -t myapp:${FULL_VERSION} .
docker tag myapp:${FULL_VERSION} myapp:latest

echo "Built artifact version: ${FULL_VERSION}"
```


## GitLab Package Registry

```yaml
# .gitlab-ci.yml
publish-package:
  stage: publish
  script:
    - npm config set @myorg:registry https://gitlab.example.com/api/v4/packages/npm/
    - npm config set '//gitlab.example.com/api/v4/packages/npm/:_authToken' "${CI_JOB_TOKEN}"
    - npm publish
  only:
    - tags
```
