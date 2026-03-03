# CloudFront Distribution with AWS CLI

## CloudFront Distribution with AWS CLI

```bash
# Create distribution for S3 origin
aws cloudfront create-distribution \
  --distribution-config '{
    "CallerReference": "myapp-'$(date +%s)'",
    "Enabled": true,
    "Comment": "My application distribution",
    "Origins": {
      "Quantity": 1,
      "Items": [{
        "Id": "myS3Origin",
        "DomainName": "mybucket.s3.us-east-1.amazonaws.com",
        "S3OriginConfig": {
          "OriginAccessIdentity": "origin-access-identity/cloudfront/ABCDEFG1234567"
        }
      }]
    },
    "DefaultCacheBehavior": {
      "AllowedMethods": {
        "Quantity": 3,
        "Items": ["GET", "HEAD", "OPTIONS"]
      },
      "ViewerProtocolPolicy": "redirect-to-https",
      "TargetOriginId": "myS3Origin",
      "ForwardedValues": {
        "QueryString": false,
        "Cookies": {"Forward": "none"},
        "Headers": {"Quantity": 0}
      },
      "TrustedSigners": {
        "Enabled": false,
        "Quantity": 0
      },
      "MinTTL": 0,
      "DefaultTTL": 86400,
      "MaxTTL": 31536000,
      "Compress": true
    },
    "CacheBehaviors": [
      {
        "PathPattern": "/api/*",
        "AllowedMethods": {
          "Quantity": 7,
          "Items": ["GET", "HEAD", "OPTIONS", "PUT", "POST", "PATCH", "DELETE"]
        },
        "ViewerProtocolPolicy": "https-only",
        "TargetOriginId": "myS3Origin",
        "ForwardedValues": {
          "QueryString": true,
          "Cookies": {"Forward": "all"},
          "Headers": {"Quantity": 0}
        },
        "MinTTL": 0,
        "DefaultTTL": 0,
        "MaxTTL": 31536000
      }
    ],
    "WebACLId": "arn:aws:wafv2:us-east-1:123456789012:global/webacl/test/a1234567"
  }'

# List distributions
aws cloudfront list-distributions

# Get distribution config
aws cloudfront get-distribution-config \
  --id E123EXAMPLE123

# Invalidate cache
aws cloudfront create-invalidation \
  --distribution-id E123EXAMPLE123 \
  --paths "/*"
```
