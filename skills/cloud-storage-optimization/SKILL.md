---
name: cloud-storage-optimization
description: >
  Optimize cloud storage across AWS S3, Azure Blob, and GCP Cloud Storage with
  compression, partitioning, lifecycle policies, and cost management.
---

# Cloud Storage Optimization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Optimize cloud storage costs and performance across multiple cloud providers using compression, intelligent tiering, data partitioning, and lifecycle management. Reduce storage costs while maintaining accessibility and compliance requirements.

## When to Use

- Reducing storage costs
- Optimizing data access patterns
- Implementing tiered storage strategies
- Archiving historical data
- Improving data retrieval performance
- Managing compliance requirements
- Organizing large datasets
- Optimizing data lakes and data warehouses

## Quick Start

Minimal working example:

```bash
# Enable Intelligent-Tiering
aws s3api put-bucket-intelligent-tiering-configuration \
  --bucket my-bucket \
  --id OptimizedStorage \
  --intelligent-tiering-configuration '{
    "Id": "OptimizedStorage",
    "Filter": {"Prefix": "data/"},
    "Status": "Enabled",
    "Tierings": [
      {
        "Days": 90,
        "AccessTier": "ARCHIVE_ACCESS"
      },
      {
        "Days": 180,
        "AccessTier": "DEEP_ARCHIVE_ACCESS"
      }
    ]
  }'

# Analyze storage usage
aws s3api list-bucket-metrics-configurations --bucket my-bucket

# Enable S3 Select for cost optimization
aws s3api put-bucket-metrics-configuration \
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [AWS S3 Storage Optimization](references/aws-s3-storage-optimization.md) | AWS S3 Storage Optimization |
| [Data Compression and Partitioning Strategy](references/data-compression-and-partitioning-strategy.md) | Data Compression and Partitioning Strategy |
| [Terraform Multi-Cloud Storage Configuration](references/terraform-multi-cloud-storage-configuration.md) | Terraform Multi-Cloud Storage Configuration |
| [Data Lake Partitioning Strategy](references/data-lake-partitioning-strategy.md) | Data Lake Partitioning Strategy |

## Best Practices

### ✅ DO

- Use Parquet or ORC formats for analytics
- Implement tiered storage strategy
- Partition data by time and queryable dimensions
- Enable versioning for critical data
- Use compression (gzip, snappy, brotli)
- Monitor storage costs regularly
- Implement data lifecycle policies
- Archive infrequently accessed data

### ❌ DON'T

- Store uncompressed data
- Keep raw logs long-term
- Ignore storage optimization
- Use only hot storage tier
- Store duplicate data
- Forget to delete old test data
