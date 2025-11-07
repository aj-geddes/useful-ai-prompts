---
name: serverless-architecture
description: Design and implement serverless applications using AWS Lambda, Azure Functions, and GCP Cloud Functions with event-driven patterns and orchestration.
---

# Serverless Architecture

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

## Implementation Examples

### 1. **Serverless Application Architecture**

```yaml
# serverless.yml - Serverless Framework
service: my-app

frameworkVersion: '3'

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
            - dynamodb:GetItem
            - dynamodb:PutItem
            - dynamodb:UpdateItem
            - dynamodb:DeleteItem
          Resource: "arn:aws:dynamodb:${self:provider.region}:${aws:accountId}:table/${self:provider.environment.DYNAMODB_TABLE}"
        - Effect: Allow
          Action:
            - sns:Publish
          Resource: ${self:provider.environment.SNS_TOPIC_ARN}

functions:
  # HTTP API endpoints
  getUser:
    handler: src/handlers/getUser.handler
    events:
      - httpApi:
          path: /api/users/{id}
          method: GET

  listUsers:
    handler: src/handlers/listUsers.handler
    events:
      - httpApi:
          path: /api/users
          method: GET

  createUser:
    handler: src/handlers/createUser.handler
    events:
      - httpApi:
          path: /api/users
          method: POST

  # Event-driven functions
  processUserCreated:
    handler: src/handlers/processUserCreated.handler
    events:
      - sns:
          arn: arn:aws:sns:${self:provider.region}:${aws:accountId}:user-created
          topicName: user-created

  processPendingOrders:
    handler: src/handlers/processPendingOrders.handler
    timeout: 300
    events:
      - schedule:
          rate: cron(0 2 * * ? *)
          enabled: true

  # S3 event handler
  processImageUpload:
    handler: src/handlers/processImageUpload.handler
    events:
      - s3:
          bucket: my-uploads-${self:provider.stage}
          event: s3:ObjectCreated:*
          rules:
            - prefix: uploads/
            - suffix: .jpg

  # SQS queue processor
  processQueue:
    handler: src/handlers/processQueue.handler
    events:
      - sqs:
          arn: arn:aws:sqs:${self:provider.region}:${aws:accountId}:my-queue
          batchSize: 10
          batchWindow: 5

resources:
  Resources:
    UsersTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: ${self:provider.environment.DYNAMODB_TABLE}
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: S
          - AttributeName: createdAt
            AttributeType: N
        KeySchema:
          - AttributeName: id
            KeyType: HASH
          - AttributeName: createdAt
            KeyType: RANGE
        BillingMode: PAY_PER_REQUEST
        StreamSpecification:
          StreamViewType: NEW_AND_OLD_IMAGES

    UserNotificationTopic:
      Type: AWS::SNS::Topic
      Properties:
        TopicName: user-created-${self:provider.stage}

    ProcessingQueue:
      Type: AWS::SQS::Queue
      Properties:
        QueueName: my-queue-${self:provider.stage}
        VisibilityTimeout: 300
        MessageRetentionPeriod: 1209600

plugins:
  - serverless-python-requirements
  - serverless-plugin-tracing
  - serverless-offline
  - serverless-dynamodb-local
```

### 2. **Event-Driven Lambda Handler Pattern**

```javascript
// src/handlers/processUserCreated.js
const AWS = require('aws-sdk');
const dynamodb = new AWS.DynamoDB.DocumentClient();

const userService = require('../services/userService');
const emailService = require('../services/emailService');

exports.handler = async (event, context) => {
  console.log('Processing user created event:', JSON.stringify(event));

  try {
    // Parse SNS message
    const records = event.Records;

    for (const record of records) {
      const message = JSON.parse(record.Sns.Message);
      const userId = message.userId;

      // Get user details
      const user = await userService.getUser(userId);

      // Send welcome email
      await emailService.sendWelcomeEmail(user);

      // Initialize user preferences
      await dynamodb.put({
        TableName: process.env.DYNAMODB_TABLE,
        Item: {
          id: userId,
          preferences: {
            newsletter: true,
            notifications: true
          },
          createdAt: Date.now()
        }
      }).promise();

      // Log success
      console.log(`Successfully processed user creation for ${userId}`);
    }

    return {
      statusCode: 200,
      body: JSON.stringify({ message: 'Processed' })
    };
  } catch (error) {
    console.error('Error processing event:', error);
    throw error; // SNS will retry
  }
};

// src/handlers/processImageUpload.js
const AWS = require('aws-sdk');
const s3 = new AWS.S3();
const rekognition = new AWS.Rekognition();

exports.handler = async (event, context) => {
  try {
    for (const record of event.Records) {
      const bucket = record.s3.bucket.name;
      const key = record.s3.object.key;

      console.log(`Processing image: s3://${bucket}/${key}`);

      // Analyze image with Rekognition
      const labels = await rekognition.detectLabels({
        Image: {
          S3Object: {
            Bucket: bucket,
            Name: key
          }
        },
        MaxLabels: 10,
        MinConfidence: 70
      }).promise();

      // Create thumbnail
      await createThumbnail(bucket, key);

      // Index metadata
      await indexMetadata(bucket, key, labels);

      console.log(`Completed processing ${key}`);
    }
  } catch (error) {
    console.error('Error processing S3 event:', error);
    throw error;
  }
};

async function createThumbnail(bucket, key) {
  // Implementation
  return true;
}

async function indexMetadata(bucket, key, labels) {
  // Implementation
  return true;
}
```

### 3. **Orchestration with Step Functions**

```json
{
  "Comment": "Order processing workflow",
  "StartAt": "ValidateOrder",
  "States": {
    "ValidateOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:validateOrder",
      "Next": "CheckInventory",
      "Catch": [
        {
          "ErrorEquals": ["InvalidOrder"],
          "Next": "OrderFailed"
        }
      ]
    },
    "CheckInventory": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:checkInventory",
      "Next": "InventoryDecision"
    },
    "InventoryDecision": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.inStock",
          "BooleanEquals": true,
          "Next": "ProcessPayment"
        }
      ],
      "Default": "OutOfStock"
    },
    "ProcessPayment": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:processPayment",
      "Next": "PaymentDecision",
      "Retry": [
        {
          "ErrorEquals": ["PaymentError"],
          "IntervalSeconds": 2,
          "MaxAttempts": 3,
          "BackoffRate": 2.0
        }
      ]
    },
    "PaymentDecision": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.paymentApproved",
          "BooleanEquals": true,
          "Next": "ShipOrder"
        }
      ],
      "Default": "PaymentFailed"
    },
    "ShipOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:shipOrder",
      "Next": "NotifyCustomer"
    },
    "NotifyCustomer": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "arn:aws:sns:region:account:order-updates",
        "Message": {
          "orderId.$": "$.orderId",
          "status": "shipped"
        }
      },
      "Next": "OrderSuccess"
    },
    "OrderSuccess": {
      "Type": "Succeed"
    },
    "OutOfStock": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:notifyOutOfStock",
      "Next": "OrderFailed"
    },
    "PaymentFailed": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:handlePaymentFailure",
      "Next": "OrderFailed"
    },
    "OrderFailed": {
      "Type": "Fail",
      "Error": "OrderFailed",
      "Cause": "Order processing failed"
    }
  }
}
```

### 4. **Monitoring and Observability**

```python
# Monitoring helper
import json
import logging
from aws_lambda_powertools import Logger, Tracer, Metrics
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
tracer = Tracer()
metrics = Metrics()

@logger.inject_lambda_context
@tracer.capture_lambda_handler
def handler(event: dict, context: LambdaContext) -> dict:
    try:
        logger.info("Processing event", extra={"event": event})

        # Add custom metrics
        metrics.add_metric(
            name="OrderProcessed",
            unit="Count",
            value=1
        )
        metrics.add_metric(
            name="OrderAmount",
            unit="None",
            value=event.get('amount', 0)
        )

        # Business logic
        result = process_order(event)

        logger.info("Order processed successfully", extra={"orderId": result['orderId']})
        return result

    except Exception as e:
        logger.exception("Error processing order")
        metrics.add_metric(
            name="OrderFailed",
            unit="Count",
            value=1
        )
        raise

    finally:
        metrics.flush()

def process_order(event):
    return {"orderId": event.get("id"), "status": "completed"}
```

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

## Architecture Patterns

- Event sourcing for audit trails
- CQRS for read-write optimization
- Saga pattern for distributed transactions
- Dead letter queues for failure handling
- Fan-out/fan-in for parallel processing
- Circuit breaker for resilience

## Resources

- [AWS Serverless Architecture](https://aws.amazon.com/serverless/)
- [Serverless Framework Documentation](https://www.serverless.com/framework/docs)
- [Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
