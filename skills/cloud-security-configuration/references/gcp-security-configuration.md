# GCP Security Configuration

## GCP Security Configuration

```bash
# Enable Cloud Armor
gcloud compute security-policies create my-policy \
  --description "Security policy"

# Add rules
gcloud compute security-policies rules create 100 \
  --security-policy=my-policy \
  --action "deny-403" \
  --expression "origin.country_code == 'CN'"

# Enable Cloud KMS
gcloud kms keyrings create my-keyring --location us-east1

gcloud kms keys create my-key \
  --location us-east1 \
  --keyring my-keyring \
  --purpose encryption

# Set IAM bindings
gcloud projects add-iam-policy-binding MY_PROJECT \
  --member=serviceAccount:my-sa@MY_PROJECT.iam.gserviceaccount.com \
  --role=roles/container.developer

# Enable Binary Authorization
gcloud container binauthz policy import policy.yaml

# VPC Service Controls
gcloud access-context-manager perimeters create my-perimeter \
  --resources=projects/MY_PROJECT
```
