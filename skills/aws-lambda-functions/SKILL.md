---
name: aws-lambda-functions
description: Create and deploy serverless functions using AWS Lambda with event sources, permissions, layers, and environment configuration. Use for event-driven computing without managing servers.
---

# AWS Lambda Functions

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

## Implementation Examples

### 1. **Basic Lambda Function with AWS CLI**

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
  --timeout 30 \
  --memory-size 256 \
  --environment Variables={ENV=production,DB_HOST=db.example.com}

# Invoke function
aws lambda invoke \
  --function-name my-function \
  --payload '{"name":"John","age":30}' \
  response.json
```

### 2. **Lambda Function with Node.js**

```javascript
// index.js
exports.handler = async (event) => {
  console.log('Event:', JSON.stringify(event));

  try {
    // Parse different event sources
    const body = typeof event.body === 'string'
      ? JSON.parse(event.body)
      : event.body || {};

    // Process S3 event
    if (event.Records && event.Records[0].s3) {
      const bucket = event.Records[0].s3.bucket.name;
      const key = event.Records[0].s3.object.key;
      console.log(`Processing S3 object: ${bucket}/${key}`);
    }

    // Database query simulation
    const results = await queryDatabase(body);

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({
        message: 'Success',
        data: results
      })
    };
  } catch (error) {
    console.error('Error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message })
    };
  }
};

async function queryDatabase(params) {
  // Simulate database call
  return { items: [] };
}
```

### 3. **Terraform Lambda Deployment**

```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Lambda execution role
resource "aws_iam_role" "lambda_role" {
  name = "lambda-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# CloudWatch Logs policy
resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# S3 Lambda Layer (dependencies)
resource "aws_lambda_layer_version" "dependencies" {
  filename            = "layer.zip"
  layer_name          = "nodejs-dependencies"
  compatible_runtimes = ["nodejs18.x"]
}

# Lambda function
resource "aws_lambda_function" "api_handler" {
  filename      = "lambda.zip"
  function_name = "api-handler"
  role          = aws_iam_role.lambda_role.arn
  handler       = "index.handler"
  runtime       = "nodejs18.x"
  timeout       = 30
  memory_size   = 256

  layers = [aws_lambda_layer_version.dependencies.arn]

  environment {
    variables = {
      STAGE = "production"
      DB_HOST = var.database_host
    }
  }

  depends_on = [aws_iam_role_policy_attachment.lambda_logs]
}

# API Gateway trigger
resource "aws_lambda_permission" "api_gateway" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.api_handler.function_name
  principal     = "apigateway.amazonaws.com"
}

# S3 trigger
resource "aws_lambda_permission" "s3_trigger" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.api_handler.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.upload_bucket.arn
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket      = aws_s3_bucket.upload_bucket.id
  depends_on  = [aws_lambda_permission.s3_trigger]

  lambda_function {
    lambda_function_arn = aws_lambda_function.api_handler.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "uploads/"
    filter_suffix       = ".jpg"
  }
}
```

### 4. **Lambda with SAM (Serverless Application Model)**

```yaml
# template.yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Globals:
  Function:
    Timeout: 30
    MemorySize: 256
    Runtime: nodejs18.x
    Tracing: Active

Parameters:
  Environment:
    Type: String
    Default: dev
    AllowedValues: [dev, prod]

Resources:
  # Lambda function
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub '${Environment}-my-function'
      CodeUri: src/
      Handler: index.handler
      Architectures:
        - x86_64
      Environment:
        Variables:
          STAGE: !Ref Environment
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref DataTable
        - S3CrudPolicy:
            BucketName: !Ref DataBucket
      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /api/{proxy+}
            Method: ANY
            RestApiId: !Ref MyApi
        S3Upload:
          Type: S3
          Properties:
            Bucket: !Ref DataBucket
            Events: s3:ObjectCreated:*
            Filter:
              S3Key:
                Rules:
                  - Name: prefix
                    Value: uploads/

  # DynamoDB table
  DataTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub '${Environment}-data'
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH

  # S3 bucket
  DataBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub '${Environment}-data-${AWS::AccountId}'
      VersioningConfiguration:
        Status: Enabled

  # API Gateway
  MyApi:
    Type: AWS::Serverless::Api
    Properties:
      Name: !Sub '${Environment}-api'
      StageName: !Ref Environment
      Cors:
        AllowMethods: "'*'"
        AllowHeaders: "'Content-Type,Authorization'"
        AllowOrigin: "'*'"

Outputs:
  FunctionArn:
    Value: !GetAtt MyFunction.Arn
  ApiEndpoint:
    Value: !Sub 'https://${MyApi}.execute-api.${AWS::Region}.amazonaws.com'
```

### 5. **Lambda Layers for Code Sharing**

```bash
# Create layer directory structure
mkdir -p layer/nodejs/node_modules
cd layer/nodejs

# Install dependencies
npm install lodash axios moment

# Go back and create zip
cd ..
zip -r layer.zip .

# Upload layer
aws lambda publish-layer-version \
  --layer-name shared-utils \
  --zip-file fileb://layer.zip \
  --compatible-runtimes nodejs18.x
```

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

## Monitoring & Troubleshooting

- CloudWatch Logs for application logging
- CloudWatch Metrics for duration, errors, throttles
- X-Ray tracing for performance analysis
- Dead Letter Queues for failed messages
- Alarms for errors and throttling

## Resources

- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/)
- [Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)
