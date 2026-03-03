---
name: aws-cloudfront-cdn
description: >
  Distribute content globally using CloudFront with caching, security headers,
  WAF integration, and origin configuration. Use for low-latency content
  delivery.
---

# AWS CloudFront CDN

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Amazon CloudFront is a fast, globally distributed content delivery network (CDN). Cache content at edge locations worldwide to reduce latency, improve performance, and provide high availability with DDoS protection.

## When to Use

- Static website hosting and assets
- API acceleration and dynamic content
- Video and media streaming
- Mobile application content
- Large file downloads
- Real-time data distribution
- DDoS protection for origins
- Origin isolation and security

## Quick Start

Minimal working example:

```bash
# Create distribution for S3 origin
aws cloudfront create-distribution \
  --distribution-config '{
    "CallerReference": "myapp-'$(date +%s)'",
    "Enabled": true,
    "Comment": "My application distribution",
    "Origins": {
      "Quantity": 1,
      "Items": [{
        "Id": "myS3Origin",
        "DomainName": "mybucket.s3.us-east-1.amazonaws.com",
        "S3OriginConfig": {
          "OriginAccessIdentity": "origin-access-identity/cloudfront/ABCDEFG1234567"
        }
      }]
    },
    "DefaultCacheBehavior": {
      "AllowedMethods": {
        "Quantity": 3,
        "Items": ["GET", "HEAD", "OPTIONS"]
      },
      "ViewerProtocolPolicy": "redirect-to-https",
      "TargetOriginId": "myS3Origin",
      "ForwardedValues": {
        "QueryString": false,
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [CloudFront Distribution with AWS CLI](references/cloudfront-distribution-with-aws-cli.md) | CloudFront Distribution with AWS CLI |
| [Terraform CloudFront Configuration](references/terraform-cloudfront-configuration.md) | Terraform CloudFront Configuration |
| [Custom Headers and Security Configuration](references/custom-headers-and-security-configuration.md) | Custom Headers and Security Configuration |

## Best Practices

### ✅ DO

- Use Origin Access Identity (OAI) for S3
- Enable HTTPS only for viewers
- Compress content at CloudFront
- Set appropriate cache TTLs
- Use cache invalidation cautiously
- Enable WAF for protection
- Monitor CloudWatch metrics
- Use multiple origins for redundancy

### ❌ DON'T

- Make S3 buckets public
- Cache sensitive data
- Use HTTP for production
- Ignore cache headers
- Create excessive invalidations
- Skip WAF protection
