# Data Compression and Partitioning Strategy

## Data Compression and Partitioning Strategy

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
