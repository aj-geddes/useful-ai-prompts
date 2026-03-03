# Docker Build and Push

## Docker Build and Push

```bash
# Build image locally
docker build -t my-app:latest .

# Tag for Container Registry
docker tag my-app:latest gcr.io/MY_PROJECT_ID/my-app:latest

# Push to Container Registry
docker push gcr.io/MY_PROJECT_ID/my-app:latest

# Or use Cloud Build
gcloud builds submit \
  --tag gcr.io/MY_PROJECT_ID/my-app:latest \
  --source-dir . \
  --no-cache
```
