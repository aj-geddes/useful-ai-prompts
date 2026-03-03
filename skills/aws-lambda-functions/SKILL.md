---
name: aws-lambda-functions
description: >
  Create and deploy serverless functions using AWS Lambda with event sources,
  permissions, layers, and environment configuration. Use for event-driven
  computing without managing servers.
---

# AWS Lambda Functions

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

AWS Lambda enables you to run code without provisioning or managing servers. Build serverless applications using event-driven triggers, pay only for compute time consumed, and scale automatically with workload.

## When to Use

- API endpoints and webhooks
- Scheduled batch jobs and data processing
- Real-time file processing (S3 uploads)
- Event-driven workflows (SNS, SQS)
- Microservices and backend APIs
- Data transformations and ETL jobs
- IoT and sensor data processing
- WebSocket connections

## Quick Start

Minimal working example:

```bash
# Create Lambda execution role
aws iam create-role \
  --role-name lambda-execution-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Service": "lambda.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }]
  }'

# Attach basic execution policy
aws iam attach-role-policy \
  --role-name lambda-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Create function from ZIP
zip function.zip index.js
aws lambda create-function \
  --function-name my-function \
  --runtime nodejs18.x \
  --role arn:aws:iam::ACCOUNT:role/lambda-execution-role \
  --handler index.handler \
  --zip-file fileb://function.zip \
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Basic Lambda Function with AWS CLI](references/basic-lambda-function-with-aws-cli.md) | Basic Lambda Function with AWS CLI |
| [Lambda Function with Node.js](references/lambda-function-with-nodejs.md) | Lambda Function with Node.js |
| [Terraform Lambda Deployment](references/terraform-lambda-deployment.md) | Terraform Lambda Deployment |
| [Lambda with SAM (Serverless Application Model)](references/lambda-with-sam-serverless-application-model.md) | Lambda with SAM (Serverless Application Model) |
| [Lambda Layers for Code Sharing](references/lambda-layers-for-code-sharing.md) | Lambda Layers for Code Sharing |

## Best Practices

### ✅ DO

- Use environment variables for configuration
- Implement proper error handling and logging
- Optimize package size and dependencies
- Set appropriate timeout and memory
- Use Lambda Layers for shared code
- Implement concurrency limits
- Enable X-Ray tracing for debugging
- Use reserved concurrency for critical functions

### ❌ DON'T

- Store sensitive data in code
- Create long-running operations (>15 min)
- Ignore cold start optimization
- Forget to handle concurrent executions
- Ignore CloudWatch metrics
- Use too much memory unnecessarily
