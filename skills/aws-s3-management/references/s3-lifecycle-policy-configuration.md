# S3 Lifecycle Policy Configuration

## S3 Lifecycle Policy Configuration

```bash
# Create lifecycle policy
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-app-bucket \
  --lifecycle-configuration '{
    "Rules": [
      {
        "Id": "archive-old-logs",
        "Status": "Enabled",
        "Prefix": "logs/",
        "Transitions": [
          {
            "Days": 30,
            "StorageClass": "STANDARD_IA"
          },
          {
            "Days": 90,
            "StorageClass": "GLACIER"
          }
        ],
        "Expiration": {
          "Days": 365
        }
      },
      {
        "Id": "cleanup-incomplete-uploads",
        "Status": "Enabled",
        "AbortIncompleteMultipartUpload": {
          "DaysAfterInitiation": 7
        }
      }
    ]
  }'

# Get bucket lifecycle
aws s3api get-bucket-lifecycle-configuration \
  --bucket my-app-bucket
```
