# DevOps & Infrastructure Skills Library

Complete collection of 20 production-ready DevOps and infrastructure automation skills with practical configurations, code samples, and best practices.

## Skills Overview

### Container & Orchestration

1. **kubernetes-deployment** (357 lines)
   - Deployments, StatefulSets, DaemonSets, rolling updates
   - Resource management, health checks, RBAC
   - HPA, PDB, and pod disruption handling
   - Files: kubernetes-deployment/SKILL.md

2. **service-mesh-implementation** (420 lines)
   - Istio setup and configuration
   - Virtual services, destination rules, traffic policies
   - Security (mTLS, AuthZ, AuthN), observability
   - Files: service-mesh-implementation/SKILL.md

### Infrastructure as Code

3. **terraform-infrastructure** (394 lines)
   - AWS VPC, subnets, security groups, routing
   - Load balancers, databases, auto-scaling groups
   - Modular design, state management, remote backends
   - Files: terraform-infrastructure/SKILL.md

4. **ansible-automation** (367 lines)
   - Playbooks, roles, handlers, and templates
   - Configuration management, application deployment
   - Multi-environment support, error handling
   - Files: ansible-automation/SKILL.md

### Web Servers & Load Balancing

5. **nginx-configuration** (331 lines)
   - Reverse proxy, load balancing, SSL/TLS termination
   - Gzip compression, caching, rate limiting
   - Security headers, health checks, monitoring
   - Files: nginx-configuration/SKILL.md

6. **load-balancer-setup** (415 lines)
   - HAProxy configuration with clustering
   - AWS ALB/NLB with target groups
   - Health checks, sticky sessions, traffic policies
   - Files: load-balancer-setup/SKILL.md

### CI/CD & Deployment

7. **cicd-pipeline-setup** (438 lines)
   - GitHub Actions, GitLab CI, Jenkins pipelines
   - Multi-stage builds, testing, security scanning
   - Artifact management, deployment automation
   - Files: cicd-pipeline-setup/SKILL.md

8. **blue-green-deployment** (403 lines)
   - Zero-downtime deployments with instant switching
   - Traffic switching, health verification
   - Rollback procedures and validation
   - Files: blue-green-deployment/SKILL.md

9. **canary-deployment** (438 lines)
   - Gradual rollouts with automatic rollback
   - Metrics-based promotion decisions
   - Load test integration and validation
   - Files: canary-deployment/SKILL.md

### Monitoring & Observability

10. **infrastructure-monitoring** (407 lines)
    - Prometheus setup and configuration
    - Grafana dashboards and visualization
    - AlertManager rules and notification routing
    - Files: infrastructure-monitoring/SKILL.md

11. **log-aggregation** (456 lines)
    - ELK Stack (Elasticsearch, Logstash, Kibana)
    - Loki for Kubernetes logging
    - Log parsing, filtering, retention policies
    - Files: log-aggregation/SKILL.md

### Data Protection & Security

12. **backup-disaster-recovery** (471 lines)
    - Database backup strategies and automation
    - Cross-region replication and failover
    - Point-in-time recovery, data validation
    - Files: backup-disaster-recovery/SKILL.md

13. **secrets-management** (499 lines)
    - HashiCorp Vault setup and configuration
    - AWS Secrets Manager integration
    - Kubernetes secret management and rotation
    - Files: secrets-management/SKILL.md

14. **ssl-certificate-management** (386 lines)
    - Let's Encrypt with cert-manager
    - AWS ACM certificate provisioning
    - Automated renewal and monitoring
    - Files: ssl-certificate-management/SKILL.md

### Scaling & Performance

15. **autoscaling-configuration** (426 lines)
    - Kubernetes HPA with custom metrics
    - AWS Auto Scaling and scheduled scaling
    - Vertical pod autoscaling for optimization
    - Files: autoscaling-configuration/SKILL.md

### Network & DNS

16. **network-security-groups** (470 lines)
    - AWS security groups with fine-grained rules
    - Kubernetes network policies
    - Network segmentation and zero-trust architecture
    - Files: network-security-groups/SKILL.md

17. **dns-management** (415 lines)
    - AWS Route53 failover and routing policies
    - CloudFlare DNS management
    - Health check-based routing and geolocation
    - Files: dns-management/SKILL.md

### Cost & Optimization

18. **infrastructure-cost-optimization** (438 lines)
    - Reserved instances and spot instance usage
    - Right-sizing and cost tracking
    - AWS cost analysis and reporting
    - Files: infrastructure-cost-optimization/SKILL.md

### Testing & Reliability

19. **disaster-recovery-testing** (407 lines)
    - DR test planning and execution
    - RTO/RPO measurement and validation
    - Automated testing and reporting
    - Files: disaster-recovery-testing/SKILL.md

### Artifact Management

20. **container-registry-management** (522 lines)
    - AWS ECR setup and lifecycle policies
    - Image scanning and vulnerability detection
    - Access control and multi-region replication
    - Files: container-registry-management/SKILL.md

## Skills by Technology Stack

### Cloud Platforms

- **AWS**: Terraform, CloudFormation, Auto Scaling, Route53, ECR, ACM, Secrets Manager
- **Kubernetes**: Deployments, HPA, Network Policies, cert-manager, service-mesh
- **Multi-cloud**: DNS, monitoring, logging (platform-agnostic patterns)

### Languages & Formats

- **YAML**: Kubernetes manifests, Ansible playbooks, Docker Compose
- **HCL/Terraform**: Infrastructure code, AWS resources
- **Bash**: Deployment scripts, automation utilities
- **Python**: Cost analysis, monitoring integrations
- **Groovy**: Jenkins pipeline syntax
- **Jinja2**: Ansible templates
- **Nginx/HAProxy**: Web server configurations

### Tools & Frameworks

- Prometheus + Grafana
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Istio service mesh
- Let's Encrypt / cert-manager
- HashiCorp Vault
- Jenkins, GitHub Actions, GitLab CI
- Flagger for canary deployments
- Karpenter for autoscaling

## How to Use These Skills

### Quick Start

1. Navigate to `/home/user/useful-ai-prompts/skills/<skill-name>/SKILL.md`
2. Read the Overview and When to Use section
3. Review Implementation Examples with code samples
4. Follow Best Practices section
5. Check Resources for additional learning

### Integration

- Copy YAML files and adapt for your infrastructure
- Modify Terraform configurations for your AWS/cloud account
- Adapt shell scripts for your environment
- Use as reference templates and starting points

### Learning Path

1. Start with Kubernetes & basic infrastructure concepts
2. Move to configuration management (Terraform, Ansible)
3. Setup CI/CD pipelines
4. Implement monitoring and logging
5. Add advanced patterns (service mesh, canary deployments)
6. Optimize costs and disaster recovery

## File Statistics

| Metric                  | Value |
| ----------------------- | ----- |
| Total Skills            | 20    |
| Total Lines of Content  | 8,451 |
| Code Examples           | 150+  |
| Shell Scripts           | 40+   |
| Configuration Files     | 200+  |
| Average Lines per Skill | 423   |
| Minimum Lines           | 331   |
| Maximum Lines           | 522   |

## Coverage by Topic

### Deployment Strategies

- Rolling updates (Kubernetes)
- Blue-green deployments
- Canary deployments with automatic rollback
- Shadow traffic testing

### High Availability

- Multi-region failover (DNS + Route53)
- Auto-scaling (HPA, AWS ASG)
- Health checks and circuit breakers
- Distributed backups

### Security

- Network policies and security groups
- RBAC (Role-Based Access Control)
- Secret management and rotation
- SSL/TLS certificates with automation
- Image scanning in registries

### Observability

- Metrics collection (Prometheus)
- Log aggregation (ELK, Loki)
- Distributed tracing
- Custom dashboards

### Cost Optimization

- Reserved instances
- Spot instances
- Resource right-sizing
- Cost analysis and tracking

### Disaster Recovery

- Automated backups
- Cross-region replication
- Failover testing
- RTO/RPO validation

## Key Features

Each skill includes:

- Clear overview and use cases
- Multiple implementation examples
- Production-ready configurations
- Real-world best practices
- Anti-patterns to avoid
- Common commands/operations
- Links to official documentation
- Practical troubleshooting tips

## Directory Structure

```
/skills/
├── kubernetes-deployment/SKILL.md
├── terraform-infrastructure/SKILL.md
├── ansible-automation/SKILL.md
├── cicd-pipeline-setup/SKILL.md
├── nginx-configuration/SKILL.md
├── load-balancer-setup/SKILL.md
├── service-mesh-implementation/SKILL.md
├── infrastructure-monitoring/SKILL.md
├── log-aggregation/SKILL.md
├── backup-disaster-recovery/SKILL.md
├── secrets-management/SKILL.md
├── blue-green-deployment/SKILL.md
├── canary-deployment/SKILL.md
├── autoscaling-configuration/SKILL.md
├── network-security-groups/SKILL.md
├── dns-management/SKILL.md
├── ssl-certificate-management/SKILL.md
├── infrastructure-cost-optimization/SKILL.md
├── disaster-recovery-testing/SKILL.md
├── container-registry-management/SKILL.md
└── DEVOPS_SKILLS_INDEX.md (this file)
```

## Getting Started

1. **Review**: Start with overview section of any skill
2. **Learn**: Study the implementation examples
3. **Practice**: Adapt examples for your environment
4. **Implement**: Deploy using provided scripts/configurations
5. **Monitor**: Track results with provided monitoring setup
6. **Iterate**: Use best practices to optimize

## Additional Resources

- Kubernetes Official Docs: https://kubernetes.io/docs/
- Terraform Registry: https://registry.terraform.io/
- AWS Documentation: https://docs.aws.amazon.com/
- Ansible Galaxy: https://galaxy.ansible.com/
- Prometheus Docs: https://prometheus.io/docs/
- Istio Documentation: https://istio.io/latest/docs/

---

Last Updated: 2025-11-07
Version: 1.0
Coverage: 20 Core DevOps & Infrastructure Skills
