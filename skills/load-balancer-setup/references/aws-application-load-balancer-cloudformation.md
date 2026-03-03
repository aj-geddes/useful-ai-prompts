# AWS Application Load Balancer (CloudFormation)

## AWS Application Load Balancer (CloudFormation)

```yaml
# aws-alb-cloudformation.yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Application Load Balancer with Target Groups"

Parameters:
  VpcId:
    Type: AWS::EC2::VPC::Id
    Description: VPC ID
  SubnetIds:
    Type: List<AWS::EC2::Subnet::Id>
    Description: Public subnet IDs for ALB
  Environment:
    Type: String
    Default: production
    AllowedValues: [dev, staging, production]

Resources:
  # Security Group for ALB
  LoadBalancerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Security group for ALB
      VpcId: !Ref VpcId
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0
      Tags:
        - Key: Name
          Value: !Sub "${Environment}-alb-sg"

  # Application Load Balancer
  ApplicationLoadBalancer:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Name: !Sub "${Environment}-alb"
      Type: application
      Scheme: internet-facing
      SecurityGroups:
        - !Ref LoadBalancerSecurityGroup
      Subnets: !Ref SubnetIds
      Tags:
        - Key: Environment
          Value: !Ref Environment

  # HTTP Listener (redirect to HTTPS)
  HttpListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      DefaultActions:
        - Type: redirect
          RedirectConfig:
            Protocol: HTTPS
            Port: "443"
            StatusCode: HTTP_301
      LoadBalancerArn: !Ref ApplicationLoadBalancer
      Port: 80
      Protocol: HTTP

  # HTTPS Listener
  HttpsListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref WebTargetGroup
      LoadBalancerArn: !Ref ApplicationLoadBalancer
      Port: 443
      Protocol: HTTPS
      Certificates:
        - CertificateArn: !Sub "arn:aws:acm:${AWS::Region}:${AWS::AccountId}:certificate/xxxxxxxx"

  # Target Group for Web Servers
  WebTargetGroup:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      Name: !Sub "${Environment}-web-tg"
      Port: 8080
      Protocol: HTTP
      VpcId: !Ref VpcId
      TargetType: instance

      # Health Check
      HealthCheckEnabled: true
      HealthCheckPath: /health
      HealthCheckProtocol: HTTP
      HealthCheckIntervalSeconds: 30
      HealthCheckTimeoutSeconds: 5
      HealthyThresholdCount: 2
      UnhealthyThresholdCount: 3

      # Stickiness
      TargetGroupAttributes:
        - Key: deregistration_delay.timeout_seconds
          Value: "30"
        - Key: stickiness.enabled
          Value: "true"
        - Key: stickiness.type
          Value: "lb_cookie"
        - Key: stickiness.lb_cookie.duration_seconds
          Value: "86400"

  # Target Group for API
  ApiTargetGroup:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      Name: !Sub "${Environment}-api-tg"
      Port: 3000
      Protocol: HTTP
      VpcId: !Ref VpcId
      TargetType: instance

      HealthCheckPath: /api/health
      HealthCheckIntervalSeconds: 15
      HealthCheckTimeoutSeconds: 5
      HealthyThresholdCount: 2
      UnhealthyThresholdCount: 2

  # Listener Rule for API routing
  ApiListenerRule:
    Type: AWS::ElasticLoadBalancingV2::ListenerRule
    Properties:
      Actions:
        - Type: forward
          TargetGroupArn: !Ref ApiTargetGroup
      Conditions:
        - Field: path-pattern
          Values: ["/api/*"]
      ListenerArn: !Ref HttpsListener
      Priority: 1

Outputs:
  LoadBalancerDNS:
    Description: DNS name of the ALB
    Value: !GetAtt ApplicationLoadBalancer.DNSName
  LoadBalancerArn:
    Description: ARN of the ALB
    Value: !Ref ApplicationLoadBalancer
  WebTargetGroupArn:
    Description: ARN of Web Target Group
    Value: !Ref WebTargetGroup
  ApiTargetGroupArn:
    Description: ARN of API Target Group
    Value: !Ref ApiTargetGroup
```
