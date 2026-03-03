# AWS API Gateway Configuration

## AWS API Gateway Configuration

```yaml
# AWS SAM template for API Gateway
AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31

Resources:
  ApiGateway:
    Type: AWS::Serverless::Api
    Properties:
      StageName: prod
      Auth:
        DefaultAuthorizer: JwtAuthorizer
        Authorizers:
          JwtAuthorizer:
            FunctionArn: !GetAtt AuthorizerFunction.Arn
            Identity:
              Headers:
                - Authorization
      TracingEnabled: true
      MethodSettings:
        - ResourcePath: "/*"
          HttpMethod: "*"
          LoggingLevel: INFO
          DataTraceEnabled: true
          MetricsEnabled: true
          ThrottleSettings:
            BurstLimit: 1000
            RateLimit: 100

  UserServiceFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      Runtime: nodejs18.x
      Environment:
        Variables:
          USER_SERVICE_URL: !Sub "https://${UserServiceAlb}.elb.amazonaws.com"
      Events:
        GetUsers:
          Type: Api
          Properties:
            RestApiId: !Ref ApiGateway
            Path: /api/users
            Method: GET
            Auth:
              Authorizer: JwtAuthorizer
        CreateUser:
          Type: Api
          Properties:
            RestApiId: !Ref ApiGateway
            Path: /api/users
            Method: POST
            Auth:
              Authorizer: JwtAuthorizer

  ApiUsagePlan:
    Type: AWS::ApiGateway::UsagePlan
    Properties:
      UsagePlanName: StandardPlan
      ApiStages:
        - ApiId: !Ref ApiGateway
          Stage: prod
      Quota:
        Limit: 10000
        Period: DAY
      Throttle:
        RateLimit: 100
        BurstLimit: 1000

  ApiKey:
    Type: AWS::ApiGateway::ApiKey
    Properties:
      Name: StandardKey
      Enabled: true
      UsagePlanId: !Ref ApiUsagePlan
```
