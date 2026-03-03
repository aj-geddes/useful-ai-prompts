# AWS ECR Setup and Management

## AWS ECR Setup and Management

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
