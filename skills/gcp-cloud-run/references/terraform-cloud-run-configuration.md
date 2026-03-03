# Terraform Cloud Run Configuration

## Terraform Cloud Run Configuration

```hcl
# cloud-run.tf
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

variable "image" {
  description = "Container image URI"
}

# Service account for Cloud Run
resource "google_service_account" "cloud_run_sa" {
  account_id   = "cloud-run-sa"
  display_name = "Cloud Run Service Account"
}

# Grant Cloud Logging role
resource "google_project_iam_member" "cloud_run_logs" {
  project = var.project_id
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.cloud_run_sa.email}"
}

# Cloud SQL Client role (if using Cloud SQL)
resource "google_project_iam_member" "cloud_sql_client" {
  project = var.project_id
  role    = "roles/cloudsql.client"
  member  = "serviceAccount:${google_service_account.cloud_run_sa.email}"
}

# Cloud Run service
resource "google_cloud_run_service" "app" {
  name     = "my-app"
  location = var.region

  template {
    spec {
      service_account_name = google_service_account.cloud_run_sa.email

      containers {
        image = var.image

        resources {
          limits = {
            cpu    = "1"
            memory = "512Mi"
          }
        }

        env {
          name  = "NODE_ENV"
          value = "production"
        }

        env {
          name  = "PORT"
          value = "8080"
        }

        ports {
          container_port = 8080
        }

        # Startup probe
        startup_probe {
          http_get {
            path = "/ready"
            port = 8080
          }
          failure_threshold = 3
          period_seconds    = 10
        }

        # Liveness probe
        liveness_probe {
          http_get {
            path = "/live"
            port = 8080
          }
          failure_threshold     = 3
          period_seconds        = 10
          initial_delay_seconds = 10
        }
      }

      timeout_seconds       = 3600
      service_account_name  = google_service_account.cloud_run_sa.email
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "100"
        "autoscaling.knative.dev/minScale" = "1"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  depends_on = [google_project_iam_member.cloud_run_logs]
}

# Allow public access
resource "google_cloud_run_service_iam_binding" "public" {
  service  = google_cloud_run_service.app.name
  location = google_cloud_run_service.app.location
  role     = "roles/run.invoker"
  members = [
    "allUsers"
  ]
}

# Cloud Load Balancer for global access
resource "google_compute_backend_service" "app" {
  name            = "my-app-backend"
  protocol        = "HTTPS"
  security_policy = google_compute_security_policy.app.id

  backend {
    group = google_compute_network_endpoint_group.app.id
  }

  health_checks = [google_compute_health_check.app.id]

  log_config {
    enable      = true
    sample_rate = 1.0
  }
}

# Network Endpoint Group for Cloud Run
resource "google_compute_network_endpoint_group" "app" {
  name                  = "my-app-neg"
  network_endpoint_type = "SERVERLESS"
  cloud_run_config {
    service = google_cloud_run_service.app.name
  }
  location = var.region
}

# Health check
resource "google_compute_health_check" "app" {
  name = "my-app-health-check"

  https_health_check {
    port         = "8080"
    request_path = "/health"
  }
}

# Cloud Armor security policy
resource "google_compute_security_policy" "app" {
  name = "my-app-policy"

  rules {
    action   = "deny(403)"
    priority = "100"
    match {
      versioned_expr = "CEL_V1"
      expression     = "origin.country_code in ['CN', 'RU']"
    }
  }

  rules {
    action   = "rate_based_ban"
    priority = "200"
    match {
      versioned_expr = "CEL_V1"
      expression     = "true"
    }
    rate_limit_options {
      conform_action = "allow"
      exceed_action  = "deny(429)"
      enforce_on_key = "IP"
      ban_duration_sec = 600
      rate_limit_threshold {
        count        = 100
        interval_sec = 60
      }
      ban_threshold_rule {
        count        = 1000
        interval_sec = 60
      }
    }
  }

  rules {
    action   = "allow"
    priority = "65535"
    match {
      versioned_expr = "CEL_V1"
      expression     = "true"
    }
  }
}

# Global address
resource "google_compute_global_address" "app" {
  name = "my-app-address"
}

# HTTPS redirect
resource "google_compute_url_map" "https_redirect" {
  name = "my-app-https-redirect"

  default_url_redirect {
    https_redirect         = true
    redirect_response_code = "301"
    strip_query            = false
  }
}

# HTTPS target proxy
resource "google_compute_target_https_proxy" "app" {
  name            = "my-app-proxy"
  url_map         = google_compute_url_map.app.id
  ssl_certificates = [google_compute_managed_ssl_certificate.app.id]
}

# Managed SSL certificate
resource "google_compute_managed_ssl_certificate" "app" {
  name = "my-app-cert"

  managed {
    domains = ["example.com"]
  }
}

# URL map
resource "google_compute_url_map" "app" {
  name            = "my-app-url-map"
  default_service = google_compute_backend_service.app.id
}

# Forwarding rule
resource "google_compute_global_forwarding_rule" "app" {
  name                  = "my-app-forwarding-rule"
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL"
  port_range            = "443"
  target                = google_compute_target_https_proxy.app.id
  address               = google_compute_global_address.app.address
}

# Monitoring alert
resource "google_monitoring_alert_policy" "cloud_run_errors" {
  display_name = "Cloud Run High Error Rate"
  combiner     = "OR"

  conditions {
    display_name = "Error rate threshold"

    condition_threshold {
      filter          = "metric.type=\"run.googleapis.com/request_count\" AND resource.label.service_name=\"my-app\" AND metric.label.response_code_class=\"5xx\""
      duration        = "60s"
      comparison      = "COMPARISON_GT"
      threshold_value = 10
      aggregations {
        alignment_period    = "60s"
        per_series_aligner  = "ALIGN_RATE"
      }
    }
  }

  notification_channels = []
}

# Cloud Run job for batch processing
resource "google_cloud_run_v2_job" "batch" {
  name     = "batch-processor"
  location = var.region

  template {
    containers {
      image = var.image
      env {
        name  = "JOB_TYPE"
        value = "batch"
      }
    }
    timeout       = "3600s"
    service_account = google_service_account.cloud_run_sa.email
  }
}

# Cloud Scheduler to trigger job
resource "google_cloud_scheduler_job" "batch_trigger" {
  name             = "batch-processor-trigger"
  schedule         = "0 2 * * *"
  time_zone        = "UTC"
  attempt_deadline = "320s"
  region           = var.region

  http_target {
    http_method = "POST"
    uri         = "https://${var.region}-run.googleapis.com/apis/run.googleapis.com/v1/projects/${var.project_id}/locations/${var.region}/jobs/batch-processor:run"

    headers = {
      "Content-Type" = "application/json"
    }

    oidc_token {
      service_account_email = google_service_account.cloud_run_sa.email
    }
  }
}

output "cloud_run_url" {
  value = google_cloud_run_service.app.status[0].url
}

output "load_balancer_ip" {
  value = google_compute_global_address.app.address
}
```
