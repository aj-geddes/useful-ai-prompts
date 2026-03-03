# S3 Access with Presigned URLs

## S3 Access with Presigned URLs

```bash
# Generate presigned URL (1 hour expiration)
aws s3 presign s3://my-app-bucket/private/document.pdf \
  --expires-in 3600

# Generate presigned URL for PUT (upload)
aws s3 presign s3://my-app-bucket/uploads/file.jpg \
  --expires-in 3600 \
  --region us-east-1 \
  --request-method PUT
```
