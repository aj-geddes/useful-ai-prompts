# Cloud Run Deployment with gcloud CLI

## Cloud Run Deployment with gcloud CLI

```bash
# Build container image
gcloud builds submit --tag gcr.io/MY_PROJECT_ID/my-app:latest

# Deploy to Cloud Run
gcloud run deploy my-app \
  --image gcr.io/MY_PROJECT_ID/my-app:latest \
  --platform managed \
  --region us-central1 \
  --memory 512Mi \
  --cpu 1 \
  --timeout 3600 \
  --max-instances 100 \
  --min-instances 1 \
  --no-allow-unauthenticated \
  --set-env-vars NODE_ENV=production,DATABASE_URL=postgresql://...

# Allow public access
gcloud run services add-iam-policy-binding my-app \
  --platform managed \
  --region us-central1 \
  --member=allUsers \
  --role=roles/run.invoker

# Get service URL
gcloud run services describe my-app \
  --platform managed \
  --region us-central1 \
  --format 'value(status.url)'

# View logs
gcloud run services logs read my-app --limit 50

# Update service with new image
gcloud run deploy my-app \
  --image gcr.io/MY_PROJECT_ID/my-app:v2 \
  --platform managed \
  --region us-central1 \
  --update-env-vars VERSION=2
```
