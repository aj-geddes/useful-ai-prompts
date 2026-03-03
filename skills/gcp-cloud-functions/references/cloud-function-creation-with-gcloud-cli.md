# Cloud Function Creation with gcloud CLI

## Cloud Function Creation with gcloud CLI

```bash
# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Initialize and authenticate
gcloud init
gcloud auth application-default login

# Set project
gcloud config set project MY_PROJECT_ID

# Create service account
gcloud iam service-accounts create cloud-function-sa \
  --display-name "Cloud Function Service Account"

# Grant permissions
gcloud projects add-iam-policy-binding MY_PROJECT_ID \
  --member="serviceAccount:cloud-function-sa@MY_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/cloudfunctions.invoker"

# Deploy HTTP function
gcloud functions deploy my-http-function \
  --gen2 \
  --runtime nodejs18 \
  --region us-central1 \
  --source ./src \
  --entry-point httpHandler \
  --trigger-http \
  --allow-unauthenticated \
  --timeout 60 \
  --memory 256MB \
  --max-instances 100 \
  --set-env-vars NODE_ENV=production,API_KEY=xxx \
  --service-account cloud-function-sa@MY_PROJECT_ID.iam.gserviceaccount.com

# Deploy Pub/Sub function
gcloud functions deploy my-pubsub-function \
  --gen2 \
  --runtime nodejs18 \
  --region us-central1 \
  --source ./src \
  --entry-point pubsubHandler \
  --trigger-topic my-topic \
  --memory 256MB \
  --timeout 300 \
  --service-account cloud-function-sa@MY_PROJECT_ID.iam.gserviceaccount.com

# Deploy Cloud Storage function
gcloud functions deploy my-storage-function \
  --gen2 \
  --runtime nodejs18 \
  --region us-central1 \
  --source ./src \
  --entry-point storageHandler \
  --trigger-bucket my-bucket \
  --trigger-location us-central1 \
  --timeout 60 \
  --service-account cloud-function-sa@MY_PROJECT_ID.iam.gserviceaccount.com

# List functions
gcloud functions list

# Get function details
gcloud functions describe my-http-function --gen2 --region us-central1

# Call function
gcloud functions call my-http-function \
  --region us-central1 \
  --data '{"name":"John"}'

# View logs
gcloud functions logs read my-http-function --limit 50 --gen2 --region us-central1

# Delete function
gcloud functions delete my-http-function --gen2 --region us-central1
```
