---
name: container-registry-management
description: Manage container registries (Docker Hub, ECR, GCR) with image scanning, retention policies, and access control.
---

# Container Registry Management

## Overview

Implement comprehensive container registry management including image scanning, vulnerability detection, retention policies, access control, and multi-region replication.

## When to Use

- Container image storage and distribution
- Security scanning and compliance
- Image retention and cleanup
- Registry access control
- Multi-region deployments
- Image signing and verification
- Cost optimization

## Implementation Examples

### 1. **AWS ECR Setup and Management**

```yaml
# ecr-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: ecr-management
  namespace: operations
data:
  setup-ecr.sh: |
    #!/bin/bash
    set -euo pipefail

    REGISTRY_NAME="myapp"
    REGION="us-east-1"
    ACCOUNT_ID="123456789012"

    echo "Setting up ECR repository..."

    # Create ECR repository
    aws ecr create-repository \
      --repository-name "$REGISTRY_NAME" \
      --region "$REGION" \
      --encryption-configuration encryptionType=KMS,kmsKey=arn:aws:kms:$REGION:$ACCOUNT_ID:key/12345678-1234-1234-1234-123456789012 \
      --image-tag-mutability IMMUTABLE \
      --image-scanning-configuration scanOnPush=true || true

    echo "Repository: $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REGISTRY_NAME"

    # Set lifecycle policy
    aws ecr put-lifecycle-policy \
      --repository-name "$REGISTRY_NAME" \
      --region "$REGION" \
      --lifecycle-policy-text '{
        "rules": [
          {
            "rulePriority": 1,
            "description": "Keep last 20 images tagged with release",
            "selection": {
              "tagStatus": "tagged",
              "tagPrefixList": ["release"],
              "countType": "imageCountMoreThan",
              "countNumber": 20
            },
            "action": {
              "type": "expire"
            }
          },
          {
            "rulePriority": 2,
            "description": "Remove untagged images older than 7 days",
            "selection": {
              "tagStatus": "untagged",
              "countType": "sinceImagePushed",
              "countUnit": "days",
              "countNumber": 7
            },
            "action": {
              "type": "expire"
            }
          },
          {
            "rulePriority": 3,
            "description": "Keep all development images for 30 days",
            "selection": {
              "tagStatus": "tagged",
              "tagPrefixList": ["dev"],
              "countType": "sinceImagePushed",
              "countUnit": "days",
              "countNumber": 30
            },
            "action": {
              "type": "expire"
            }
          }
        ]
      }'

    # Enable cross-region replication
    aws ecr create-registry \
      --region "$REGION" \
      --replication-configuration '{
        "rules": [
          {
            "destinations": [
              {
                "region": "eu-west-1",
                "registryId": "'$ACCOUNT_ID'"
              },
              {
                "region": "ap-northeast-1",
                "registryId": "'$ACCOUNT_ID'"
              }
            ],
            "repositoryFilters": [
              {
                "filter": "'$REGISTRY_NAME'",
                "filterType": "PREFIX_MATCH"
              }
            ]
          }
        ]
      }' || true

    echo "ECR setup complete"

  scan-images.sh: |
    #!/bin/bash
    set -euo pipefail

    REGISTRY_NAME="myapp"
    REGION="us-east-1"

    echo "Scanning all images in $REGISTRY_NAME"

    # Get all image IDs
    IMAGE_IDS=$(aws ecr list-images \
      --repository-name "$REGISTRY_NAME" \
      --region "$REGION" \
      --query 'imageIds[*]' \
      --output json)

    # Scan each image
    echo "$IMAGE_IDS" | jq -r '.[] | @base64' | while read image; do
      IMAGE=$(echo "$image" | base64 -d | jq -r '.imageTag')
      DIGEST=$(echo "$image" | base64 -d | jq -r '.imageDigest')

      echo "Scanning image: $IMAGE ($DIGEST)"

      # Start scan
      aws ecr start-image-scan \
        --repository-name "$REGISTRY_NAME" \
        --image-id imageTag="$IMAGE" \
        --region "$REGION" || true

      # Get scan results
      sleep 5
      RESULTS=$(aws ecr describe-image-scan-findings \
        --repository-name "$REGISTRY_NAME" \
        --image-id imageTag="$IMAGE" \
        --region "$REGION")

      CRITICAL=$(echo "$RESULTS" | jq '.imageScanFindings.findingSeverityCounts.CRITICAL // 0')
      HIGH=$(echo "$RESULTS" | jq '.imageScanFindings.findingSeverityCounts.HIGH // 0')

      if [ "$CRITICAL" -gt 0 ]; then
        echo "WARNING: Image has $CRITICAL critical vulnerabilities"
      fi

      if [ "$HIGH" -gt 0 ]; then
        echo "WARNING: Image has $HIGH high vulnerabilities"
      fi
    done

    echo "Image scanning complete"

---
# Terraform ECR configuration
resource "aws_ecr_repository" "myapp" {
  name                 = "myapp"
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  encryption_configuration {
    encryption_type = "KMS"
    kms_key         = aws_kms_key.ecr.arn
  }

  tags = {
    Name = "myapp-registry"
  }
}

resource "aws_ecr_lifecycle_policy" "myapp" {
  repository = aws_ecr_repository.myapp.name

  policy = jsonencode({
    rules = [
      {
        rulePriority = 1
        description  = "Keep last 20 production images"
        selection = {
          tagStatus       = "tagged"
          tagPrefixList   = ["release"]
          countType       = "imageCountMoreThan"
          countNumber     = 20
        }
        action = {
          type = "expire"
        }
      },
      {
        rulePriority = 2
        description  = "Remove untagged images after 7 days"
        selection = {
          tagStatus     = "untagged"
          countType     = "sinceImagePushed"
          countUnit     = "days"
          countNumber   = 7
        }
        action = {
          type = "expire"
        }
      }
    ]
  })
}

resource "aws_ecr_repository_policy" "myapp" {
  repository = aws_ecr_repository.myapp.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/EcsTaskExecutionRole"
        }
        Action = [
          "ecr:GetDownloadUrlForLayer",
          "ecr:BatchGetImage",
          "ecr:GetImage"
        ]
      }
    ]
  })
}
```

### 2. **Container Image Build and Push**

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

### 3. **Image Signing with Notary**

```bash
#!/bin/bash
# sign-image.sh - Sign container images with Notary

set -euo pipefail

IMAGE="${1}"
NOTATION_KEY="${2:-mykey}"

echo "Signing image: $IMAGE"

# Initialize Notary
notary key list

# Sign image
notation sign \
  --key "$NOTATION_KEY" \
  --allow-missing \
  "$IMAGE"

echo "Image signed successfully"

# Verify signature
notation verify "$IMAGE"
```

### 4. **Registry Access Control**

```yaml
# registry-access-control.yaml
apiVersion: v1
kind: Secret
metadata:
  name: ecr-pull-secret
  namespace: production
type: kubernetes.io/dockercfg
stringData:
  .dockercfg: |
    {
      "123456789012.dkr.ecr.us-east-1.amazonaws.com": {
        "auth": "base64-encoded-credentials",
        "email": "service-account@mycompany.com"
      }
    }

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ecr-pull-sa
  namespace: production
imagePullSecrets:
  - name: ecr-pull-secret

---
apiVersion: v1
kind: Pod
metadata:
  name: myapp
  namespace: production
spec:
  serviceAccountName: ecr-pull-sa
  containers:
    - name: app
      image: 123456789012.dkr.ecr.us-east-1.amazonaws.com/myapp:latest
      imagePullPolicy: Always

---
# IAM policy for ECR access
apiVersion: iam.aws.amazon.com/v1
kind: IAMPolicy
metadata:
  name: ecr-read-only
spec:
  policyDocument:
    Version: '2012-10-17'
    Statement:
      - Effect: Allow
        Action:
          - ecr:GetDownloadUrlForLayer
          - ecr:BatchGetImage
          - ecr:GetImage
          - ecr:DescribeImages
        Resource: arn:aws:ecr:*:123456789012:repository/myapp
      - Effect: Allow
        Action:
          - ecr:GetAuthorizationToken
        Resource: '*'
```

### 5. **Registry Monitoring**

```yaml
# registry-monitoring.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: registry-monitoring
  namespace: monitoring
data:
  dashboards.json: |
    {
      "dashboard": {
        "title": "Container Registry",
        "panels": [
          {
            "title": "Images by Repository",
            "targets": [
              {
                "expr": "count by (repository) (aws_ecr_repository_images)"
              }
            ]
          },
          {
            "title": "Images with Vulnerabilities",
            "targets": [
              {
                "expr": "sum(aws_ecr_image_scan_findings{severity=~\"HIGH|CRITICAL\"})"
              }
            ]
          },
          {
            "title": "Registry Storage",
            "targets": [
              {
                "expr": "aws_ecr_repository_size_bytes"
              }
            ]
          }
        ]
      }
    }

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: registry-alerts
  namespace: monitoring
data:
  alerts.yaml: |
    groups:
      - name: registry_alerts
        rules:
          - alert: ImageWithCriticalVulnerabilities
            expr: aws_ecr_image_scan_findings{severity="CRITICAL"} > 0
            for: 5m
            labels:
              severity: critical
            annotations:
              summary: "Image has critical vulnerabilities"

          - alert: ImagePushFailure
            expr: aws_ecr_push_failures_total > 0
            for: 1m
            labels:
              severity: warning
            annotations:
              summary: "Image push failed"

          - alert: RegistryStorageHigh
            expr: aws_ecr_repository_size_bytes / 1024 / 1024 / 1024 > 100
            labels:
              severity: warning
            annotations:
              summary: "Registry storage usage is high"
```

## Best Practices

### ✅ DO
- Scan images before deployment
- Use image tag immutability
- Implement retention policies
- Control registry access with IAM
- Sign images for verification
- Replicate across regions
- Monitor registry storage
- Use private registries

### ❌ DON'T
- Push to public registries
- Use `latest` tag in production
- Allow anonymous pulls
- Store secrets in images
- Keep old images indefinitely
- Push without scanning
- Use default credentials
- Share registry credentials

## Registry Options

- **Docker Hub**: Public registry
- **AWS ECR**: AWS-managed
- **Google GCR**: Google Cloud
- **Azure ACR**: Azure-managed
- **Artifactory**: Self-hosted
- **Harbor**: Open-source

## Image Naming Convention

```
[registry]/[organization]/[repository]:[tag]
123456789012.dkr.ecr.us-east-1.amazonaws.com/myapp:v1.2.3
```

## Resources

- [AWS ECR Documentation](https://docs.aws.amazon.com/ecr/)
- [Docker Registry V2 API](https://docs.docker.com/registry/spec/api/)
- [Harbor Documentation](https://goharbor.io/docs/)
- [CNCF Image Signing Standards](https://github.com/notaryproject/notary)
