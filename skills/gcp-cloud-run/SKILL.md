---
name: gcp-cloud-run
description: >
  Deploy containerized applications on Google Cloud Run with automatic scaling,
  traffic management, and service mesh integration. Use for container-based
  serverless computing.
---

# GCP Cloud Run

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Google Cloud Run enables deployment of containerized applications at scale without managing infrastructure. Run stateless HTTP containers with automatic scaling from zero to thousands of instances, paying only for compute time consumed.

## When to Use

- Microservices and APIs
- Web applications and backends
- Batch processing jobs
- Long-running background workers
- CI/CD pipeline integration
- Data processing pipelines
- WebSocket applications
- Multi-language services

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Cloud Run Deployment with gcloud CLI](references/cloud-run-deployment-with-gcloud-cli.md) | Cloud Run Deployment with gcloud CLI |
| [Containerized Application (Node.js)](references/containerized-application-nodejs.md) | Containerized Application (Node.js) |
| [Terraform Cloud Run Configuration](references/terraform-cloud-run-configuration.md) | Terraform Cloud Run Configuration |
| [Docker Build and Push](references/docker-build-and-push.md) | Docker Build and Push |

## Best Practices

### ✅ DO

- Use container health checks
- Set appropriate CPU and memory
- Implement graceful shutdown
- Use service accounts with least privilege
- Monitor with Cloud Logging
- Enable Cloud Armor for protection
- Use revision management for blue-green deployments
- Implement startup and liveness probes

### ❌ DON'T

- Store secrets in code
- Use default service account
- Create stateful applications
- Ignore health checks
- Deploy without testing
- Use excessive resource limits
- Store files in container filesystem
