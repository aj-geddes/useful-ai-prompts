---
name: cloud-storage-optimization
description: Optimize cloud storage across AWS S3, Azure Blob, and GCP Cloud Storage with compression, partitioning, lifecycle policies, and cost management.
---

# Cloud Storage Optimization

## Overview

Optimize cloud storage costs and performance across multiple cloud providers using compression, intelligent tiering, data partitioning, and lifecycle management. Reduce storage costs while maintaining accessibility and compliance requirements.

## When to Use

- Reducing storage costs
- Optimizing data access patterns
- Implementing tiered storage strategies
- Archiving historical data
- Improving data retrieval performance
- Managing compliance requirements
- Organizing large datasets
- Optimizing data lakes and data warehouses

## Implementation Examples

### 1. **AWS S3 Storage Optimization**

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

### 2. **Data Compression and Partitioning Strategy**

```python
# Python data optimization
import boto3
import gzip
import json
from datetime import datetime
import pandas as pd

class StorageOptimizer:
    def __init__(self, bucket_name):
        self.s3_client = boto3.client('s3')
        self.bucket = bucket_name

    def compress_and_upload(self, file_path, key):
        """Compress file and upload to S3"""
        with open(file_path, 'rb') as f_in:
            with gzip.open(f_in, 'rb') as f_out:
                self.s3_client.put_object(
                    Bucket=self.bucket,
                    Key=f'{key}.gz',
                    Body=f_out.read(),
                    ContentEncoding='gzip',
                    ServerSideEncryption='AES256'
                )

    def partition_csv_data(self, csv_path, partition_columns):
        """Partition CSV by date and other columns"""
        df = pd.read_csv(csv_path)

        # Partition by date
        df['date'] = pd.to_datetime(df['date'])

        for date, date_group in df.groupby(df['date'].dt.date):
            for partition_val, partition_group in date_group.groupby(partition_columns[0]):
                # Parquet format (more efficient than CSV)
                file_key = f"data/date={date}/category={partition_val}/data.parquet"

                partition_group.to_parquet(
                    f"/tmp/{partition_val}.parquet",
                    compression='snappy',
                    index=False
                )

                self.upload_parquet_file(f"/tmp/{partition_val}.parquet", file_key)

    def upload_parquet_file(self, local_path, s3_key):
        """Upload Parquet file with optimization"""
        with open(local_path, 'rb') as data:
            self.s3_client.put_object(
                Bucket=self.bucket,
                Key=s3_key,
                Body=data.read(),
                ContentType='application/octet-stream',
                ServerSideEncryption='AES256',
                StorageClass='INTELLIGENT_TIERING'
            )

    def analyze_storage_patterns(self):
        """Analyze and recommend storage optimizations"""
        response = self.s3_client.list_objects_v2(
            Bucket=self.bucket,
            Prefix='data/'
        )

        stats = {
            'total_size': 0,
            'file_count': 0,
            'by_extension': {},
            'old_files': []
        }

        for obj in response.get('Contents', []):
            size = obj['Size']
            key = obj['Key']
            modified = obj['LastModified']

            stats['total_size'] += size
            stats['file_count'] += 1

            ext = key.split('.')[-1]
            stats['by_extension'][ext] = stats['by_extension'].get(ext, 0) + 1

            # Files older than 90 days
            days_old = (datetime.now(modified.tzinfo) - modified).days
            if days_old > 90:
                stats['old_files'].append({
                    'key': key,
                    'size': size,
                    'days_old': days_old
                })

        return stats

    def implement_lifecycle_optimization(self):
        """Implement comprehensive lifecycle policy"""
        lifecycle_config = {
            'Rules': [
                # Recent data - standard
                {
                    'Id': 'KeepRecentStandard',
                    'Status': 'Enabled',
                    'Filter': {'Prefix': 'data/'},
                    'NoncurrentVersionTransition': {
                        'NoncurrentDays': 30,
                        'StorageClass': 'STANDARD_IA'
                    }
                },
                # Archive old data
                {
                    'Id': 'ArchiveOldData',
                    'Status': 'Enabled',
                    'Filter': {'Prefix': 'archive/'},
                    'Transitions': [
                        {
                            'Days': 30,
                            'StorageClass': 'STANDARD_IA'
                        },
                        {
                            'Days': 90,
                            'StorageClass': 'GLACIER'
                        },
                        {
                            'Days': 180,
                            'StorageClass': 'DEEP_ARCHIVE'
                        }
                    ],
                    'Expiration': {
                        'Days': 2555  # 7 years
                    }
                },
                # Delete incomplete multipart uploads
                {
                    'Id': 'CleanupIncompleteUploads',
                    'Status': 'Enabled',
                    'AbortIncompleteMultipartUpload': {
                        'DaysAfterInitiation': 7
                    }
                }
            ]
        }

        self.s3_client.put_bucket_lifecycle_configuration(
            Bucket=self.bucket,
            LifecycleConfiguration=lifecycle_config
        )
```

### 3. **Terraform Multi-Cloud Storage Configuration**

```hcl
# storage-optimization.tf

# AWS S3 with tiering
resource "aws_s3_bucket" "data_lake" {
  bucket = "my-data-lake-${data.aws_caller_identity.current.account_id}"
}

resource "aws_s3_bucket_intelligent_tiering_configuration" "archive" {
  bucket = aws_s3_bucket.data_lake.id
  name   = "archive-tiering"

  tiering {
    access_tier = "ARCHIVE_ACCESS"
    days        = 90
  }

  tiering {
    access_tier = "DEEP_ARCHIVE_ACCESS"
    days        = 180
  }

  status = "Enabled"
}

# Azure Blob storage with lifecycle
resource "azurerm_storage_account" "data_lake" {
  name                     = "mydatalake"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  access_tier = "Hot"
}

resource "azurerm_storage_management_policy" "data_lifecycle" {
  storage_account_id = azurerm_storage_account.data_lake.id

  rule {
    name    = "ArchiveOldBlobs"
    enabled = true

    filters {
      prefix_match       = ["data/"]
      blob_index_match {
        name      = "age-days"
        operation = "=="
        value     = "90"
      }
    }

    actions {
      base_blob {
        tier_to_cool_after_days_since_modification_greater_than       = 30
        tier_to_archive_after_days_since_modification_greater_than     = 90
        delete_after_days_since_modification_greater_than              = 2555
      }

      snapshot {
        delete_after_days_since_creation_greater_than = 90
      }

      version {
        tier_to_cool_after_days_since_creation_greater_than       = 30
        tier_to_archive_after_days_since_creation_greater_than     = 90
        delete_after_days_since_creation_greater_than              = 365
      }
    }
  }
}

# GCP Cloud Storage with lifecycle
resource "google_storage_bucket" "data_lake" {
  name     = "my-data-lake-${data.google_client_config.current.project}"
  location = "US"

  uniform_bucket_level_access = true
  storage_class               = "STANDARD"

  lifecycle_rule {
    action {
      type          = "SetStorageClass"
      storage_class = "NEARLINE"
    }

    condition {
      age = 30
    }
  }

  lifecycle_rule {
    action {
      type          = "SetStorageClass"
      storage_class = "COLDLINE"
    }

    condition {
      age = 90
    }
  }

  lifecycle_rule {
    action {
      type          = "Delete"
    }

    condition {
      age = 2555
    }
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }

    condition {
      num_newer_versions = 3
      is_live            = false
    }
  }
}

data "aws_caller_identity" "current" {}
data "google_client_config" "current" {}
```

### 4. **Data Lake Partitioning Strategy**

```python
# Optimized partitioning for data lakes
def create_partitioned_data_lake(source_file, bucket, format='parquet'):
    import pyarrow.parquet as pq
    import pyarrow as pa

    # Read data
    table = pq.read_table(source_file)
    df = table.to_pandas()

    # Create partitions
    partitions = {
        'year': df['date'].dt.year,
        'month': df['date'].dt.month,
        'day': df['date'].dt.day,
        'region': df['region']
    }

    # Group by partitions
    for year, year_group in df.groupby(partitions['year']):
        for month, month_group in year_group.groupby(partitions['month']):
            for day, day_group in month_group.groupby(partitions['day']):
                for region, region_group in day_group.groupby(partitions['region']):
                    # Create partition path
                    path = f"s3://{bucket}/data/year={year}/month={month:02d}/day={day:02d}/region={region}"

                    # Save as Parquet with compression
                    table = pa.Table.from_pandas(region_group)
                    pq.write_table(
                        table,
                        f"{path}/data.parquet",
                        compression='snappy',
                        use_dictionary=True
                    )
```

## Best Practices

### ✅ DO
- Use Parquet or ORC formats for analytics
- Implement tiered storage strategy
- Partition data by time and queryable dimensions
- Enable versioning for critical data
- Use compression (gzip, snappy, brotli)
- Monitor storage costs regularly
- Implement data lifecycle policies
- Archive infrequently accessed data

### ❌ DON'T
- Store uncompressed data
- Keep raw logs long-term
- Ignore storage optimization
- Use only hot storage tier
- Store duplicate data
- Forget to delete old test data

## Cost Optimization Tips

- Use Intelligent-Tiering for variable access patterns
- Archive data older than 90 days
- Use equivalent cold storage across cloud providers
- Delete incomplete multipart uploads
- Monitor usage with cloud tools
- Estimate costs before large uploads

## Resources

- [AWS Storage Optimization](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-optimization.html)
- [Azure Storage Lifecycle](https://docs.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)
- [GCP Cloud Storage Lifecycle](https://cloud.google.com/storage/docs/lifecycle)
