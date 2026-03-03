# S3 Bucket Creation and Configuration with AWS CLI

## S3 Bucket Creation and Configuration with AWS CLI

```bash
# Create bucket
aws s3api create-bucket \
  --bucket my-app-bucket-$(date +%s) \
  --region us-east-1

# Enable versioning
aws s3api put-bucket-versioning \
  --bucket my-app-bucket \
  --versioning-configuration Status=Enabled

# Block public access
aws s3api put-public-access-block \
  --bucket my-app-bucket \
  --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,\
    BlockPublicPolicy=true,RestrictPublicBuckets=true

# Enable encryption
aws s3api put-bucket-encryption \
  --bucket my-app-bucket \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }]
  }'

# Upload file with metadata
aws s3 cp index.html s3://my-app-bucket/ \
  --cache-control "max-age=3600" \
  --metadata "author=john,version=1"

# Sync directory to S3
aws s3 sync ./dist s3://my-app-bucket/ \
  --delete \
  --exclude "*.map"

# List objects with metadata
aws s3api list-objects-v2 \
  --bucket my-app-bucket \
  --query 'Contents[].{Key:Key,Size:Size,Modified:LastModified}'
```
