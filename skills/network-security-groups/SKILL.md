---
name: network-security-groups
description: >
  Configure network security groups and firewall rules to control
  inbound/outbound traffic and implement network segmentation.
---

# Network Security Groups

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [AWS Security Groups](references/aws-security-groups.md) | AWS Security Groups |
| [Kubernetes Network Policies](references/kubernetes-network-policies.md) | Kubernetes Network Policies |
| [GCP Firewall Rules](references/gcp-firewall-rules.md) | GCP Firewall Rules |
| [Security Group Management Script](references/security-group-management-script.md) | Security Group Management Script |

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
