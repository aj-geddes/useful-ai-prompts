# AWS S3 Storage Optimization

## AWS S3 Storage Optimization

```bash
# Enable Intelligent-Tiering
aws s3api put-bucket-intelligent-tiering-configuration \
  --bucket my-bucket \
  --id OptimizedStorage \
  --intelligent-tiering-configuration '{
    "Id": "OptimizedStorage",
    "Filter": {"Prefix": "data/"},
    "Status": "Enabled",
    "Tierings": [
      {
        "Days": 90,
        "AccessTier": "ARCHIVE_ACCESS"
      },
      {
        "Days": 180,
        "AccessTier": "DEEP_ARCHIVE_ACCESS"
      }
    ]
  }'

# Analyze storage usage
aws s3api list-bucket-metrics-configurations --bucket my-bucket

# Enable S3 Select for cost optimization
aws s3api put-bucket-metrics-configuration \
  --bucket my-bucket \
  --id EntireBucket \
  --metrics-configuration '{
    "Id": "EntireBucket",
    "Filter": {"Prefix": ""}
  }'

# Use S3 Batch Operations for bulk tagging
aws s3control create-job \
  --account-id ACCOUNT_ID \
  --operation LambdaInvoke \
  --manifest '{
    "Spec": {"Format": "S3BatchOperations_CSV_20180820"},
    "Location": "s3://my-bucket/manifest.csv"
  }' \
  --report '{
    "Bucket": "s3://my-bucket/reports/",
    "Prefix": "batch-operation-",
    "Format": "Report_CSV_20180820",
    "Enabled": true,
    "ReportScope": "AllTasks"
  }'
```
