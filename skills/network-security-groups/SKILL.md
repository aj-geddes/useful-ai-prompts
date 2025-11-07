---
name: network-security-groups
description: Configure network security groups and firewall rules to control inbound/outbound traffic and implement network segmentation.
---

# Network Security Groups

## Overview

Implement network security groups and firewall rules to enforce least privilege access, segment networks, and protect infrastructure from unauthorized access.

## When to Use

- Inbound traffic control
- Outbound traffic filtering
- Network segmentation
- Zero-trust networking
- DDoS mitigation
- Database access restriction
- VPN access control
- Multi-tier application security

## Implementation Examples

### 1. **AWS Security Groups**

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

### 2. **Kubernetes Network Policies**

```yaml
# kubernetes-network-policies.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-ingress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: frontend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: ingress-nginx
      ports:
        - protocol: TCP
          port: 8080

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-backend-to-database
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: database
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              tier: backend
      ports:
        - protocol: TCP
          port: 5432

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-backend-to-cache
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: cache
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              tier: backend
      ports:
        - protocol: TCP
          port: 6379

---
# Egress policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-egress
  namespace: production
spec:
  podSelector:
    matchLabels:
      tier: backend
  policyTypes:
    - Egress
  egress:
    # Allow to database
    - to:
        - podSelector:
            matchLabels:
              tier: database
      ports:
        - protocol: TCP
          port: 5432

    # Allow to cache
    - to:
        - podSelector:
            matchLabels:
              tier: cache
      ports:
        - protocol: TCP
          port: 6379

    # Allow DNS
    - to:
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53

    # Allow external APIs
    - to:
        - namespaceSelector: {}
      ports:
        - protocol: TCP
          port: 443
```

### 3. **GCP Firewall Rules**

```yaml
# gcp-firewall-rules.yaml
apiVersion: compute.cnrm.cloud.google.com/v1beta1
kind: ComputeFirewall
metadata:
  name: allow-http-https
spec:
  network:
    name: default
  direction: INGRESS
  priority: 1000
  sourceRanges:
    - 0.0.0.0/0
  allowed:
    - IPProtocol: tcp
      ports:
        - "80"
        - "443"
  targetTags:
    - http-server
    - https-server

---
apiVersion: compute.cnrm.cloud.google.com/v1beta1
kind: ComputeFirewall
metadata:
  name: allow-ssh-internal
spec:
  network:
    name: default
  direction: INGRESS
  priority: 1000
  sourceRanges:
    - 10.0.0.0/8
  allowed:
    - IPProtocol: tcp
      ports:
        - "22"
  targetTags:
    - allow-ssh

---
apiVersion: compute.cnrm.cloud.google.com/v1beta1
kind: ComputeFirewall
metadata:
  name: deny-all-ingress
spec:
  network:
    name: default
  direction: INGRESS
  priority: 65534
  denied:
    - IPProtocol: all
```

### 4. **Security Group Management Script**

```bash
#!/bin/bash
# manage-security-groups.sh - Security group management utility

set -euo pipefail

ACTION="${1:-list}"
REGION="${2:-us-east-1}"

# List security groups
list_security_groups() {
    echo "Security Groups in $REGION:"
    aws ec2 describe-security-groups \
        --region "$REGION" \
        --query 'SecurityGroups[*].[GroupId,GroupName,VpcId]' \
        --output table
}

# Show security group details
show_security_group() {
    local sg_id="$1"
    echo "Inbound Rules for $sg_id:"
    aws ec2 describe-security-groups \
        --group-ids "$sg_id" \
        --region "$REGION" \
        --query 'SecurityGroups[0].IpPermissions' \
        --output table

    echo -e "\nOutbound Rules for $sg_id:"
    aws ec2 describe-security-groups \
        --group-ids "$sg_id" \
        --region "$REGION" \
        --query 'SecurityGroups[0].IpPermissionsEgress' \
        --output table
}

# Add inbound rule
add_inbound_rule() {
    local sg_id="$1"
    local protocol="$2"
    local port="$3"
    local cidr="$4"
    local description="${5:-}"

    aws ec2 authorize-security-group-ingress \
        --group-id "$sg_id" \
        --protocol "$protocol" \
        --port "$port" \
        --cidr "$cidr" \
        --region "$REGION" \
        ${description:+--description "$description"}

    echo "Rule added to $sg_id"
}

# Audit security groups for overly permissive rules
audit_security_groups() {
    echo "Auditing security groups for overly permissive rules..."

    aws ec2 describe-security-groups \
        --region "$REGION" \
        --query 'SecurityGroups[*].[GroupId,IpPermissions]' \
        --output text | while read sg_id; do

        # Check for 0.0.0.0/0 on sensitive ports
        if aws ec2 describe-security-groups \
            --group-ids "$sg_id" \
            --region "$REGION" \
            --query "SecurityGroups[0].IpPermissions[?FromPort==\`22\` || FromPort==\`3306\` || FromPort==\`5432\`]" \
            --output json | grep -q "0.0.0.0/0"; then
            echo "WARNING: $sg_id has sensitive ports open to 0.0.0.0/0"
        fi
    done
}

# Main
case "$ACTION" in
    list)
        list_security_groups
        ;;
    show)
        show_security_group "$3"
        ;;
    add-rule)
        add_inbound_rule "$3" "$4" "$5" "$6" "${7:-}"
        ;;
    audit)
        audit_security_groups
        ;;
    *)
        echo "Usage: $0 {list|show|add-rule|audit} [args]"
        exit 1
        ;;
esac
```

## Best Practices

### ✅ DO
- Implement least privilege access
- Use security groups for segmentation
- Document rule purposes
- Regularly audit rules
- Separate inbound and outbound rules
- Use security group references
- Monitor rule changes
- Test access before enabling

### ❌ DON'T
- Allow 0.0.0.0/0 for databases
- Open all ports unnecessarily
- Mix environments in single SG
- Ignore egress rules
- Allow all protocols
- Forget to document rules
- Use single catch-all rule
- Deploy without firewall

## Common Rules

| Port | Protocol | Purpose |
|------|----------|---------|
| 22 | TCP | SSH (Admin only) |
| 80 | TCP | HTTP (Public) |
| 443 | TCP | HTTPS (Public) |
| 3306 | TCP | MySQL (App tier only) |
| 5432 | TCP | PostgreSQL (App tier only) |
| 6379 | TCP | Redis (App tier only) |

## Resources

- [AWS Security Groups Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
- [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [GCP Firewall Rules](https://cloud.google.com/vpc/docs/firewalls)
- [Zero Trust Networking](https://www.nist.gov/publications/zero-trust-architecture)
