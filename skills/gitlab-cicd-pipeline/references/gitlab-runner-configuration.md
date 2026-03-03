# GitLab Runner Configuration

## GitLab Runner Configuration

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
