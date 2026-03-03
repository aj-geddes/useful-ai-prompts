# Terraform Multi-Cloud Storage Configuration

## Terraform Multi-Cloud Storage Configuration

```hcl
# storage-optimization.tf

# AWS S3 with tiering
resource "aws_s3_bucket" "data_lake" {
  bucket = "my-data-lake-${data.aws_caller_identity.current.account_id}"
}

resource "aws_s3_bucket_intelligent_tiering_configuration" "archive" {
  bucket = aws_s3_bucket.data_lake.id
  name   = "archive-tiering"

  tiering {
    access_tier = "ARCHIVE_ACCESS"
    days        = 90
  }

  tiering {
    access_tier = "DEEP_ARCHIVE_ACCESS"
    days        = 180
  }

  status = "Enabled"
}

# Azure Blob storage with lifecycle
resource "azurerm_storage_account" "data_lake" {
  name                     = "mydatalake"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  access_tier = "Hot"
}

resource "azurerm_storage_management_policy" "data_lifecycle" {
  storage_account_id = azurerm_storage_account.data_lake.id

  rule {
    name    = "ArchiveOldBlobs"
    enabled = true

    filters {
      prefix_match       = ["data/"]
      blob_index_match {
        name      = "age-days"
        operation = "=="
        value     = "90"
      }
    }

    actions {
      base_blob {
        tier_to_cool_after_days_since_modification_greater_than       = 30
        tier_to_archive_after_days_since_modification_greater_than     = 90
        delete_after_days_since_modification_greater_than              = 2555
      }

      snapshot {
        delete_after_days_since_creation_greater_than = 90
      }

      version {
        tier_to_cool_after_days_since_creation_greater_than       = 30
        tier_to_archive_after_days_since_creation_greater_than     = 90
        delete_after_days_since_creation_greater_than              = 365
      }
    }
  }
}

# GCP Cloud Storage with lifecycle
resource "google_storage_bucket" "data_lake" {
  name     = "my-data-lake-${data.google_client_config.current.project}"
  location = "US"

  uniform_bucket_level_access = true
  storage_class               = "STANDARD"

  lifecycle_rule {
    action {
      type          = "SetStorageClass"
      storage_class = "NEARLINE"
    }

    condition {
      age = 30
    }
  }

  lifecycle_rule {
    action {
      type          = "SetStorageClass"
      storage_class = "COLDLINE"
    }

    condition {
      age = 90
    }
  }

  lifecycle_rule {
    action {
      type          = "Delete"
    }

    condition {
      age = 2555
    }
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }

    condition {
      num_newer_versions = 3
      is_live            = false
    }
  }
}

data "aws_caller_identity" "current" {}
data "google_client_config" "current" {}
```
