# Serverless Application Architecture

## Serverless Application Architecture

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
