# AWS Security Groups

## AWS Security Groups

```yaml
# aws-security-groups.yaml
Resources:
  # VPC Security Group
  VPCSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: VPC security group
      VpcId: vpc-12345678
      SecurityGroupIngress:
        # Allow HTTP from anywhere
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
          Description: "HTTP from anywhere"

        # Allow HTTPS from anywhere
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0
          Description: "HTTPS from anywhere"

        # Allow SSH from admin network only
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 10.0.0.0/8
          Description: "SSH from admin network"

      SecurityGroupEgress:
        # Allow all outbound
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0
          Description: "All outbound traffic"

      Tags:
        - Key: Name
          Value: vpc-security-group

  # Database Security Group
  DatabaseSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Database security group
      VpcId: vpc-12345678
      SecurityGroupIngress:
        # Allow PostgreSQL from app tier only
        - IpProtocol: tcp
          FromPort: 5432
          ToPort: 5432
          SourceSecurityGroupId: !Ref AppSecurityGroup
          Description: "PostgreSQL from app tier"

      SecurityGroupEgress:
        - IpProtocol: -1
          CidrIp: 0.0.0.0/0

      Tags:
        - Key: Name
          Value: database-security-group

  # Application Tier Security Group
  AppSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Application tier security group
      VpcId: vpc-12345678
      SecurityGroupIngress:
        # Allow traffic from load balancer
        - IpProtocol: tcp
          FromPort: 8080
          ToPort: 8080
          SourceSecurityGroupId: !Ref LBSecurityGroup
          Description: "App traffic from LB"

      SecurityGroupEgress:
        # Allow to databases
        - IpProtocol: tcp
          FromPort: 5432
          ToPort: 5432
          DestinationSecurityGroupId: !Ref DatabaseSecurityGroup
          Description: "Database access"

        # Allow to external APIs
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0
          Description: "HTTPS external APIs"

      Tags:
        - Key: Name
          Value: app-security-group

  # Load Balancer Security Group
  LBSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Load balancer security group
      VpcId: vpc-12345678
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
        - IpProtocol: tcp
          FromPort: 8080
          ToPort: 8080
          DestinationSecurityGroupId: !Ref AppSecurityGroup

      Tags:
        - Key: Name
          Value: lb-security-group
```
