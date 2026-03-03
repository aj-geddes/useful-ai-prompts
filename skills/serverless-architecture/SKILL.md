---
name: serverless-architecture
description: >
  Design and implement serverless applications using AWS Lambda, Azure
  Functions, and GCP Cloud Functions with event-driven patterns and
  orchestration.
---

# Serverless Architecture

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Serverless architecture enables building complete applications without managing servers. Design event-driven, scalable systems using managed compute services, databases, and messaging systems. Pay only for actual usage with automatic scaling.

## When to Use

- Event-driven applications
- API backends and microservices
- Real-time data processing
- Batch jobs and scheduled tasks
- Workflow automation
- IoT data pipelines
- Multi-tenant SaaS applications
- Mobile app backends

## Quick Start

Minimal working example:

```yaml
# serverless.yml - Serverless Framework
service: my-app

frameworkVersion: "3"

provider:
  name: aws
  runtime: nodejs18.x
  region: us-east-1
  stage: ${opt:stage, 'dev'}
  memorySize: 256
  timeout: 30
  environment:
    STAGE: ${self:provider.stage}
    DYNAMODB_TABLE: ${self:service}-users-${self:provider.stage}
    SNS_TOPIC_ARN: arn:aws:sns:${self:provider.region}:${aws:accountId}:my-topic
  httpApi:
    cors: true
  iam:
    role:
      statements:
        - Effect: Allow
          Action:
            - dynamodb:Query
            - dynamodb:Scan
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Serverless Application Architecture](references/serverless-application-architecture.md) | Serverless Application Architecture |
| [Event-Driven Lambda Handler Pattern](references/event-driven-lambda-handler-pattern.md) | Event-Driven Lambda Handler Pattern |
| [Orchestration with Step Functions](references/orchestration-with-step-functions.md) | Orchestration with Step Functions |
| [Monitoring and Observability](references/monitoring-and-observability.md) | Monitoring and Observability |

## Best Practices

### ✅ DO

- Design idempotent functions
- Use event sources efficiently
- Implement proper error handling
- Monitor with CloudWatch/Application Insights
- Use infrastructure as code
- Implement distributed tracing
- Version functions for safe deployments
- Use environment variables for configuration

### ❌ DON'T

- Create long-running functions
- Store state in functions
- Ignore cold start optimization
- Use synchronous chains
- Skip testing
- Hardcode configuration
- Deploy without monitoring
