# Container Image Build and Push

## Container Image Build and Push

```bash
#!/bin/bash
# build-and-push.sh - Build and push container images

set -euo pipefail

REGISTRY="${1:-123456789012.dkr.ecr.us-east-1.amazonaws.com}"
IMAGE_NAME="${2:-myapp}"
VERSION="${3:-latest}"
DOCKERFILE="${4:-Dockerfile}"

echo "Building and pushing container image..."

# Set full image path
FULL_IMAGE="$REGISTRY/$IMAGE_NAME:$VERSION"

# Login to ECR
echo "Authenticating to ECR..."
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin "$REGISTRY"

# Build image
echo "Building image: $FULL_IMAGE"
docker build \
  -f "$DOCKERFILE" \
  -t "$FULL_IMAGE" \
  -t "$REGISTRY/$IMAGE_NAME:latest" \
  --build-arg BUILD_DATE="$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
  --build-arg VCS_REF="$(git rev-parse --short HEAD)" \
  --build-arg VERSION="$VERSION" \
  .

# Scan with trivy before push
echo "Scanning image with Trivy..."
trivy image --severity HIGH,CRITICAL "$FULL_IMAGE"

# Push image
echo "Pushing image to ECR..."
docker push "$FULL_IMAGE"
docker push "$REGISTRY/$IMAGE_NAME:latest"

# Get image digest
DIGEST=$(docker inspect --format='{{index .RepoDigests 0}}' "$FULL_IMAGE" | cut -d@ -f2)

echo "Image pushed successfully"
echo "Image: $FULL_IMAGE"
echo "Digest: $DIGEST"
```
