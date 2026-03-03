# Lambda with SAM (Serverless Application Model)

## Lambda with SAM (Serverless Application Model)

```yaml
# template.yaml
AWSTemplateFormatVersion: "2010-09-09"
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
      FunctionName: !Sub "${Environment}-my-function"
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
      TableName: !Sub "${Environment}-data"
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
      BucketName: !Sub "${Environment}-data-${AWS::AccountId}"
      VersioningConfiguration:
        Status: Enabled

  # API Gateway
  MyApi:
    Type: AWS::Serverless::Api
    Properties:
      Name: !Sub "${Environment}-api"
      StageName: !Ref Environment
      Cors:
        AllowMethods: "'*'"
        AllowHeaders: "'Content-Type,Authorization'"
        AllowOrigin: "'*'"

Outputs:
  FunctionArn:
    Value: !GetAtt MyFunction.Arn
  ApiEndpoint:
    Value: !Sub "https://${MyApi}.execute-api.${AWS::Region}.amazonaws.com"
```
