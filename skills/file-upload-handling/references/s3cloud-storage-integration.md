# S3/Cloud Storage Integration

## S3/Cloud Storage Integration

```python
# s3_service.py
import boto3
from datetime import timedelta
import os

class S3FileService:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        self.bucket_name = os.getenv('S3_BUCKET_NAME')

    def upload_file(self, file, user_id, file_key):
        """Upload file to S3"""
        try:
            self.s3_client.upload_fileobj(
                file,
                self.bucket_name,
                file_key,
                ExtraArgs={
                    'ContentType': file.content_type,
                    'Metadata': {'user_id': user_id}
                }
            )
            return {'success': True, 'key': file_key}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def get_signed_url(self, file_key, expires_in=3600):
        """Generate signed URL for download"""
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': file_key},
                ExpiresIn=expires_in
            )
            return {'success': True, 'url': url}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def delete_file(self, file_key):
        """Delete file from S3"""
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_key)
            return {'success': True}
        except Exception as e:
            return {'success': False, 'error': str(e)}
```
