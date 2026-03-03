# Terraform Cloud Functions Configuration

## Terraform Cloud Functions Configuration

```hcl
# cloud-functions.tf
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

variable "project_id" {
  description = "GCP Project ID"
}

variable "region" {
  default = "us-central1"
}

# Service account for functions
resource "google_service_account" "function_sa" {
  account_id   = "cloud-function-sa"
  display_name = "Cloud Function Service Account"
}

# Grant invoker role
resource "google_project_iam_member" "function_invoker" {
  project = var.project_id
  role    = "roles/cloudfunctions.invoker"
  member  = "serviceAccount:${google_service_account.function_sa.email}"
}

# Grant Cloud Logging role
resource "google_project_iam_member" "function_logs" {
  project = var.project_id
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.function_sa.email}"
}

# Source archive bucket
resource "google_storage_bucket" "function_source" {
  name     = "${var.project_id}-function-source"
  location = var.region
}

# Upload function code
resource "google_storage_bucket_object" "function_zip" {
  name   = "function-${data.archive_file.function.output_md5}.zip"
  bucket = google_storage_bucket.function_source.name
  source = data.archive_file.function.output_path
}

# Archive function code
data "archive_file" "function" {
  type        = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/function.zip"
}

# HTTP Cloud Function
resource "google_cloudfunctions2_function" "http_function" {
  name        = "my-http-function"
  location    = var.region
  description = "HTTP trigger function"

  build_config {
    runtime           = "nodejs18"
    entry_point       = "httpHandler"
    source {
      storage_source {
        bucket = google_storage_bucket.function_source.name
        object = google_storage_bucket_object.function_zip.name
      }
    }
  }

  service_config {
    max_instance_count = 100
    available_memory_mb = 256
    timeout_seconds = 60
    service_account_email = google_service_account.function_sa.email

    environment_variables = {
      NODE_ENV = "production"
      API_KEY  = "your-api-key"
    }
  }

  labels = {
    env = "production"
  }
}

# Allow public HTTP access
resource "google_cloudfunctions2_function_iam_member" "http_public" {
  cloud_function = google_cloudfunctions2_function.http_function.name
  role           = "roles/cloudfunctions.invoker"
  member         = "allUsers"
}

# Pub/Sub topic
resource "google_pubsub_topic" "messages" {
  name = "message-topic"
}

# Pub/Sub Cloud Function
resource "google_cloudfunctions2_function" "pubsub_function" {
  name        = "my-pubsub-function"
  location    = var.region
  description = "Pub/Sub trigger function"

  build_config {
    runtime           = "nodejs18"
    entry_point       = "pubsubHandler"
    source {
      storage_source {
        bucket = google_storage_bucket.function_source.name
        object = google_storage_bucket_object.function_zip.name
      }
    }
  }

  service_config {
    max_instance_count = 100
    available_memory_mb = 256
    timeout_seconds = 300
    service_account_email = google_service_account.function_sa.email
  }

  event_trigger {
    trigger_region = var.region
    event_type     = "google.cloud.pubsub.topic.publish"
    pubsub_topic   = google_pubsub_topic.messages.id
  }
}

# Cloud Storage bucket
resource "google_storage_bucket" "uploads" {
  name     = "${var.project_id}-uploads"
  location = var.region
}

# Cloud Storage trigger function
resource "google_cloudfunctions2_function" "storage_function" {
  name        = "my-storage-function"
  location    = var.region
  description = "Cloud Storage trigger function"

  build_config {
    runtime           = "nodejs18"
    entry_point       = "storageHandler"
    source {
      storage_source {
        bucket = google_storage_bucket.function_source.name
        object = google_storage_bucket_object.function_zip.name
      }
    }
  }

  service_config {
    max_instance_count = 50
    available_memory_mb = 256
    timeout_seconds = 60
    service_account_email = google_service_account.function_sa.email
  }

  event_trigger {
    trigger_region = var.region
    event_type     = "google.storage.object.finalize"
    resource       = google_storage_bucket.uploads.name
  }
}

# Cloud Scheduler job (CRON)
resource "google_cloud_scheduler_job" "batch_job" {
  name             = "batch-job-scheduler"
  description      = "Scheduled batch job"
  schedule         = "0 2 * * *" # Daily at 2 AM
  time_zone        = "UTC"
  attempt_deadline = "320s"
  region           = var.region

  retry_config {
    retry_count = 1
  }

  http_target {
    uri        = google_cloudfunctions2_function.http_function.service_config[0].uri
    http_method = "POST"

    headers = {
      "Content-Type" = "application/json"
    }

    body = base64encode(jsonencode({
      job_type = "batch"
    }))

    oidc_token {
      service_account_email = google_service_account.function_sa.email
    }
  }
}

# Cloud Logging sink
resource "google_logging_project_sink" "function_logs" {
  name        = "cloud-function-logs"
  destination = "logging.googleapis.com/projects/${var.project_id}/logs/my-http-function"

  filter = "resource.type=\"cloud_function\" AND resource.labels.function_name=\"my-http-function\""
}

# Monitoring alert
resource "google_monitoring_alert_policy" "function_errors" {
  display_name = "Cloud Function Error Rate"
  combiner     = "OR"

  conditions {
    display_name = "Error rate threshold"

    condition_threshold {
      filter          = "metric.type=\"cloudfunctions.googleapis.com/function/error_count\" AND resource.type=\"cloud_function\""
      duration        = "60s"
      comparison      = "COMPARISON_GT"
      threshold_value = 10
      aggregations {
        alignment_period    = "60s"
        per_series_aligner  = "ALIGN_RATE"
      }
    }
  }
}

output "http_function_url" {
  value = google_cloudfunctions2_function.http_function.service_config[0].uri
}
```
