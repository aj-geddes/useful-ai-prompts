# Cloud Migration Expert

## Metadata
- **Created**: 2025-07-28

- **Category**: Technical/Architecture
- **Tags**: cloud migration, AWS, Azure, GCP, infrastructure, migration strategy
- **Version**: 2.0.0
- **Use Cases**: cloud assessment, migration planning, architecture design, cost optimization
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you plan and execute cloud migrations with minimal risk, optimal architecture, and cost efficiency while ensuring business continuity.

## Prompt

```
I'll help you plan a successful cloud migration that minimizes risk and maximizes value. Let me understand your current situation:

**Current environment:**
1. What's your current infrastructure? (on-premise, hybrid, specific platforms)
2. What are the main applications/workloads to migrate?
3. What's the size/scale? (servers, storage, databases)
4. Any compliance or regulatory requirements?

**Migration goals:**
5. Why migrate to cloud? (cost, scalability, modernization, etc.)
6. Which cloud provider(s) are you considering?
7. What's your timeline and budget constraints?
8. What's your team's cloud experience level?

**Technical context:**
9. What are your critical dependencies? (integrations, legacy systems)
10. Any specific performance requirements?
11. What's your current disaster recovery/backup strategy?
12. How much downtime can you tolerate during migration?

Based on your answers, I'll provide:

**MIGRATION STRATEGY** - Phased approach with risk mitigation
**ARCHITECTURE DESIGN** - Cloud-native architecture recommendations
**COST ANALYSIS** - TCO comparison and optimization strategies
**IMPLEMENTATION ROADMAP** - Step-by-step migration plan
**RISK MITIGATION** - Common pitfalls and how to avoid them

Share your infrastructure details and let's build a solid migration plan!
```

## Example Usage

**User Input:**
```
1. On-premise VMware environment, 200 VMs, mix of Windows/Linux
2. Main apps: E-commerce platform (20 microservices), ERP system, data warehouse, internal tools
3. 200 VMs, 500TB storage, 10 SQL Server databases, 5 PostgreSQL
4. PCI-DSS for e-commerce, GDPR for customer data, SOC2 compliance needed

5. Reduce costs (30% target), improve scalability for seasonal peaks, modernize infrastructure
6. Primary: AWS, but open to multi-cloud for DR
7. 12-month migration window, $2M budget including first year run costs
8. 2 cloud architects, 5 engineers with basic AWS knowledge

9. Dependencies: On-prem Active Directory, legacy ERP needs specific OS versions, real-time data sync with partners
10. E-commerce needs <100ms response time, 99.99% uptime
11. Current: Tape backup, manual failover to secondary DC (4-hour RTO)
12. E-commerce: 2-hour maintenance windows monthly, ERP: 8-hour window quarterly
```

**Assistant Output:**

Based on your infrastructure and requirements, here's a comprehensive cloud migration strategy:

## MIGRATION STRATEGY

### 7R Migration Approach

**Wave 1 (Months 1-3): Rehost**
- Development/test environments (low risk)
- Internal tools and non-critical apps
- **Method**: VMware Cloud on AWS for lift-and-shift

**Wave 2 (Months 4-7): Replatform**
- Data warehouse → Amazon Redshift
- SQL Server databases → RDS with read replicas
- Static content → S3 + CloudFront

**Wave 3 (Months 8-10): Refactor**
- E-commerce microservices → EKS + Fargate
- Implement auto-scaling for seasonal peaks
- API Gateway for partner integrations

**Wave 4 (Months 11-12): Retain/Retire**
- Keep ERP on VMware Cloud (specific OS requirements)
- Decommission redundant systems
- Establish hybrid connectivity

### Migration Pattern by Workload

```
E-commerce Platform:
└── Blue-Green Deployment
    ├── Build parallel environment in AWS
    ├── Sync data continuously
    ├── Test thoroughly
    └── Switch traffic with Route 53

ERP System:
└── VMware Cloud on AWS
    ├── vMotion migration (no downtime)
    ├── Maintain OS compatibility
    └── Gradual modernization later

Databases:
└── AWS Database Migration Service
    ├── Continuous replication
    ├── Minimal downtime cutover
    └── Fallback plan ready
```

## ARCHITECTURE DESIGN

### Target Architecture

**Multi-Account Strategy**:
```
Organization Root
├── Production Account
│   ├── E-commerce VPC (10.0.0.0/16)
│   ├── ERP VPC (10.1.0.0/16)
│   └── Shared Services VPC (10.2.0.0/16)
├── Non-Production Account
├── Security/Audit Account
└── Disaster Recovery Account
```

### E-commerce Architecture (Cloud-Native)

```
CloudFront (CDN)
    ↓
WAF + Shield (DDoS Protection)
    ↓
Application Load Balancer
    ↓
EKS Cluster (3 AZs)
├── Service Mesh (App Mesh/Istio)
├── Auto-scaling Groups
└── Fargate for Batch Jobs
    ↓
RDS Multi-AZ (PostgreSQL)
ElastiCache (Redis)
    ↓
S3 (Object Storage)
```

### Compliance Architecture

**PCI-DSS Compliance**:
- Dedicated subnets for cardholder data
- AWS Network Firewall for segmentation
- CloudTrail + Config for audit logs
- Secrets Manager for credentials

**GDPR Compliance**:
- Data residency in EU regions
- Encryption at rest (KMS) and transit
- DynamoDB for consent management
- Automated data lifecycle policies

## COST ANALYSIS

### Current vs. Cloud TCO (Annual)

**Current On-Premise Costs**:
```
Hardware refresh:     $400K
Software licenses:    $300K
Data center:         $200K
Staff (maintenance): $300K
Total:             $1,200K
```

**Projected AWS Costs**:
```
Compute (EC2/EKS):   $380K
Storage (S3/EBS):    $120K
Database (RDS):      $140K
Network/Transfer:     $60K
Support (Business):   $50K
VMware Cloud:        $180K
Total:               $930K (22.5% savings)

With Reserved Instances: $750K (37.5% savings)
```

### Cost Optimization Strategy

1. **Right-sizing**: Start 20% smaller, scale up as needed
2. **Reserved Instances**: 3-year commits for stable workloads
3. **Spot Instances**: Development/test environments
4. **S3 Lifecycle**: Archive old data to Glacier
5. **Auto-scaling**: Pay only for what you use

## IMPLEMENTATION ROADMAP

### Phase 1: Foundation (Months 1-2)

**Week 1-2: Setup**
- [ ] AWS Organization structure
- [ ] Landing Zone deployment
- [ ] Network architecture (Transit Gateway)
- [ ] Security baseline (GuardDuty, SecurityHub)

**Week 3-4: Connectivity**
- [ ] Direct Connect ordering (10Gbps)
- [ ] Site-to-Site VPN (backup)
- [ ] Active Directory integration
- [ ] DNS/DHCP configuration

**Week 5-8: Pilot Migration**
- [ ] Development environment migration
- [ ] Validate tools and processes
- [ ] Team training on AWS
- [ ] Refine runbooks

### Phase 2: Data Migration (Months 3-5)

**Database Migration**:
```
1. Setup DMS replication instances
2. Create target RDS instances  
3. Initial data load (weekends)
4. Continuous replication
5. Application testing
6. Cutover planning
```

**Storage Migration**:
- AWS DataSync for file servers
- S3 Transfer Acceleration for large datasets
- Snowball Edge for 500TB initial transfer

### Phase 3: Application Migration (Months 6-10)

**E-commerce Migration Plan**:
1. Containerize microservices (if needed)
2. Deploy to EKS in non-prod
3. Performance testing and optimization
4. Set up blue-green deployment
5. Migrate 10% traffic, monitor
6. Gradual traffic shift over 2 weeks

### Phase 4: Optimization (Months 11-12)

- [ ] Performance tuning
- [ ] Cost optimization review
- [ ] Disaster recovery testing
- [ ] Documentation update
- [ ] Knowledge transfer

## RISK MITIGATION

### Top Risks & Mitigation

**1. Data Transfer Bottleneck**
- **Risk**: 500TB transfer could take months
- **Mitigation**: AWS Snowball Edge + parallel transfers
- **Fallback**: Extend timeline if needed

**2. Application Dependencies**
- **Risk**: Hidden dependencies cause failures
- **Mitigation**: Dependency mapping tools, extensive testing
- **Fallback**: Hybrid operation capability

**3. Performance Degradation**
- **Risk**: Latency increases affect user experience
- **Mitigation**: CloudFront, ElastiCache, performance testing
- **Fallback**: Quick rollback procedures

**4. Cost Overruns**
- **Risk**: Unexpected charges exceed budget
- **Mitigation**: Cost alerts, weekly reviews, FinOps practices
- **Fallback**: Reserved capacity buffer

### Testing Strategy

**Pre-Migration Testing**:
- Proof of concepts for each workload type
- Performance benchmarking
- Security assessment
- Disaster recovery drills

**Migration Testing**:
- Smoke tests after each migration
- Load testing at 2x expected traffic
- Failover testing
- Rollback procedures

### Training Plan

**Month 1-2**: AWS Fundamentals
**Month 3-4**: Service-specific deep dives
**Month 5-6**: Security and compliance
**Ongoing**: Weekly knowledge sharing sessions

### Success Metrics

- **Migration**: 100% workloads migrated on schedule
- **Performance**: <100ms response time maintained
- **Availability**: 99.99% uptime achieved
- **Cost**: 30% reduction target met
- **Compliance**: All audits passed

This phased approach minimizes risk while delivering immediate value through quick wins and cost savings.

## Related Prompts

- [Cloud Cost Optimizer](./cloud-cost-expert.md)
- [Infrastructure as Code Expert](./iac-terraform-expert.md)
- [Cloud Security Architect](./cloud-security-expert.md)