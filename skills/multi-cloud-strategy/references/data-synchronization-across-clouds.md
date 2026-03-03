# Data Synchronization across Clouds

## Data Synchronization across Clouds

```python
# Multi-cloud data replication
import boto3
from azure.storage.blob import BlobServiceClient
from google.cloud import storage
import hashlib
from datetime import datetime

class MultiCloudDataSync:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.azure_client = BlobServiceClient.from_connection_string(
            "DefaultEndpointsProtocol=https;..."
        )
        self.gcp_client = storage.Client()

    def sync_object_to_all_clouds(self, source_cloud, source_bucket, key, data):
        """Sync object to all cloud providers"""
        try:
            # Calculate checksum
            checksum = hashlib.sha256(data).hexdigest()

            if source_cloud == "aws":
                # Upload to AWS
                self.s3.put_object(
                    Bucket=source_bucket,
                    Key=key,
                    Body=data,
                    Metadata={'checksum': checksum, 'synced-at': datetime.utcnow().isoformat()}
                )
                # Replicate to Azure
                self._sync_to_azure(key, data, checksum)
                # Replicate to GCP
                self._sync_to_gcp(key, data, checksum)

            elif source_cloud == "azure":
                # Upload to Azure
                container_client = self.azure_client.get_container_client("data")
                container_client.upload_blob(
                    key,
                    data,
                    overwrite=True,
                    metadata={'checksum': checksum, 'synced-at': datetime.utcnow().isoformat()}
                )
                # Replicate to AWS
                self._sync_to_aws(key, data, checksum)
                # Replicate to GCP
                self._sync_to_gcp(key, data, checksum)

            elif source_cloud == "gcp":
                # Upload to GCP
                bucket = self.gcp_client.bucket("my-bucket")
                blob = bucket.blob(key)
                blob.upload_from_string(
                    data,
                    metadata={'checksum': checksum, 'synced-at': datetime.utcnow().isoformat()}
                )
                # Replicate to AWS
                self._sync_to_aws(key, data, checksum)
                # Replicate to Azure
                self._sync_to_azure(key, data, checksum)

            return {
                'status': 'success',
                'key': key,
                'checksum': checksum,
                'synced_clouds': ['aws', 'azure', 'gcp']
            }

        except Exception as e:
            print(f"Error syncing data: {e}")
            return {'status': 'failed', 'error': str(e)}

    def _sync_to_aws(self, key, data, checksum):
        """Sync to AWS S3"""
        self.s3.put_object(
            Bucket='my-bucket',
            Key=key,
            Body=data,
            Metadata={'source': 'multi-cloud-sync', 'checksum': checksum}
        )

    def _sync_to_azure(self, key, data, checksum):
        """Sync to Azure Blob Storage"""
        container_client = self.azure_client.get_container_client("data")
        container_client.upload_blob(
            key,
            data,
            overwrite=True,
            metadata={'source': 'multi-cloud-sync', 'checksum': checksum}
        )

    def _sync_to_gcp(self, key, data, checksum):
        """Sync to GCP Cloud Storage"""
        bucket = self.gcp_client.bucket("my-bucket")
        blob = bucket.blob(key)
        blob.upload_from_string(
            data,
            metadata={'source': 'multi-cloud-sync', 'checksum': checksum}
        )

    def verify_consistency(self, key):
        """Verify data consistency across all clouds"""
        checksums = {}

        # Get from AWS
        try:
            aws_obj = self.s3.get_object(Bucket='my-bucket', Key=key)
            aws_data = aws_obj['Body'].read()
            checksums['aws'] = hashlib.sha256(aws_data).hexdigest()
        except Exception as e:
            checksums['aws'] = f'error: {str(e)}'

        # Get from Azure
        try:
            container_client = self.azure_client.get_container_client("data")
            blob_client = container_client.get_blob_client(key)
            azure_data = blob_client.download_blob().readall()
            checksums['azure'] = hashlib.sha256(azure_data).hexdigest()
        except Exception as e:
            checksums['azure'] = f'error: {str(e)}'

        # Get from GCP
        try:
            bucket = self.gcp_client.bucket("my-bucket")
            blob = bucket.blob(key)
            gcp_data = blob.download_as_bytes()
            checksums['gcp'] = hashlib.sha256(gcp_data).hexdigest()
        except Exception as e:
            checksums['gcp'] = f'error: {str(e)}'

        consistent = len(set(v for v in checksums.values() if not v.startswith('error'))) <= 1

        return {
            'key': key,
            'consistent': consistent,
            'checksums': checksums
        }
```
