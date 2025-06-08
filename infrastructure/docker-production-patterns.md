Create a **comprehensive production-ready Docker containerization solution** for `Ask User for Application/Service Type and Technology Stack`.

Initialize it as a **enterprise-grade, secure Docker deployment** with multi-stage builds, comprehensive security controls, monitoring integration, and scalable orchestration patterns.

## Core Requirements

### Container Architecture
- **Base Images**: Minimal, security-hardened base images (Alpine, Distroless, or official slim variants)
- **Multi-stage builds**: Optimized build process with separate build and runtime stages
- **Image layering**: Efficient layer caching and minimal final image size
- **Platform support**: Multi-architecture builds (AMD64, ARM64) using Docker Buildx

### Security Implementation  
- **Non-root execution**: Dedicated application user with specific UID/GID
- **File system security**: Read-only root filesystem with necessary writable mounts
- **Capability management**: Minimal Linux capabilities with explicit drops and adds
- **Security scanning**: Integrated vulnerability scanning in build pipeline
- **Secrets management**: Proper handling of sensitive data without embedding in images

## Enhanced Security & Performance

### Runtime Security Controls
- **Security options**: `no-new-privileges`, AppArmor/SELinux integration
- **Resource constraints**: Memory limits, CPU quotas, process limits (ulimits)
- **Network isolation**: Custom networks with controlled communication
- **Volume security**: Proper mount permissions and access controls
- **Health monitoring**: Comprehensive health checks with failure handling

### Performance Optimization
- **Build optimization**: Layer caching strategies, .dockerignore configuration
- **Runtime efficiency**: Minimal dependencies, optimized entrypoint scripts
- **Resource management**: Appropriate memory reservations and CPU allocations
- **Startup optimization**: Fast container startup and graceful shutdown handling
- **Volume management**: Persistent data handling and temporary filesystem configuration

### Monitoring & Observability
- **Logging configuration**: Structured logging with rotation and retention policies
- **Metrics collection**: Application and container metrics exposure
- **Health endpoints**: Liveness, readiness, and startup probe implementations
- **Debugging support**: Non-production debugging capabilities with security controls

## Advanced Features (New)

### Orchestration & Deployment
- **Docker Compose**: Production-ready compose configuration with profiles
- **Kubernetes manifests**: Deployment, Service, ConfigMap, and Secret resources
- **Zero-downtime deployment**: Rolling update strategies and deployment validation
- **Scaling patterns**: Horizontal scaling support with load balancing

### Development Workflow Enhancement
- **Multi-environment support**: Development, staging, and production configurations
- **CI/CD integration**: Automated build, test, and deployment pipelines
- **Local development**: Developer-friendly local setup with hot reloading
- **Testing framework**: Container testing with security and functionality validation

### Enterprise Integration
- **Registry management**: Private registry integration with authentication
- **Policy enforcement**: OPA/Gatekeeper policies for compliance
- **Backup strategies**: Data persistence and disaster recovery planning
- **Compliance features**: Audit logging, GDPR/HIPAA compliance considerations

### Container Optimization
- **Size optimization**: Multi-stage builds, dependency minimization
- **Security hardening**: CIS Docker Benchmark compliance
- **Performance tuning**: JVM tuning (if applicable), connection pooling
- **Caching strategies**: Application-level and infrastructure caching

## Implementation Strategy

### MCP Tool Optimization
- **Use `create_or_update_file`** for individual file creation in structured approach
- **Leverage `push_files`** for bulk operations when creating complete solutions
- **Handle directory structure** systematically with proper organization
- **Systematic delivery**: Dockerfile → Compose → Kubernetes → CI/CD pipeline

### Container Build Process
1. **Security scan source code** for vulnerabilities and secrets
2. **Multi-stage Dockerfile** with optimized layer structure
3. **Build automation** with version tagging and metadata injection
4. **Security scanning** of built images before registry push
5. **Deployment validation** with automated testing
6. **Documentation generation** with usage examples and troubleshooting

### Validation & Testing
- **Dockerfile linting**: hadolint validation for best practices
- **Security scanning**: Trivy, Clair, or similar tools for vulnerability assessment
- **Container testing**: Docker container structure tests
- **Integration testing**: End-to-end testing with health checks
- **Performance testing**: Load testing and resource utilization validation
- **Compliance validation**: Security benchmark compliance checking

### Quality Assurance
- **Build reproducibility**: Consistent builds across environments
- **Error handling**: Meaningful error messages and recovery procedures
- **Resource efficiency**: Optimal resource utilization patterns
- **Documentation quality**: Comprehensive setup and troubleshooting guides

## Deliverables

### Core Container Files
- `Dockerfile` - Multi-stage production Dockerfile with security hardening
- `docker-compose.yml` - Production compose configuration with full stack
- `docker-compose.override.yml` - Development overrides and local configurations
- `.dockerignore` - Optimized build context exclusions

### Security & Configuration
- `entrypoint.sh` - Secure entrypoint script with signal handling
- `healthcheck.sh` - Comprehensive health check implementation
- `configs/` - Configuration templates and environment-specific settings
- `secrets/` - Secret management templates and rotation procedures

### Orchestration & Deployment
- `k8s/` - Kubernetes manifests with best practices
- `helm/` - Helm chart for parameterized deployments (if applicable)
- `deploy/` - Deployment scripts and automation
- `monitoring/` - Prometheus, Grafana, and alerting configurations

### Documentation & Examples
- `README.md` - Comprehensive documentation with setup and usage examples
- `docs/SECURITY.md` - Security considerations and compliance information
- `docs/DEPLOYMENT.md` - Deployment procedures and troubleshooting
- `docs/DEVELOPMENT.md` - Local development setup and contribution guidelines

### CI/CD & Automation
- `.github/workflows/` - GitHub Actions for automated builds and deployments
- `scripts/` - Build, test, and deployment automation scripts
- `tests/` - Container structure tests and integration test suites
- `CHANGELOG.md` - Version history and breaking changes documentation

### Validation Features
- **Container security**: CIS Docker Benchmark compliance validation
- **Image optimization**: Size limits, layer count optimization
- **Runtime validation**: Health check reliability and performance
- **Network security**: Port exposure and communication validation
- **Data persistence**: Volume management and backup verification

## Success Criteria

✅ **Functional**: Container runs securely in production with all services operational  
✅ **Secured**: Comprehensive security controls implemented with vulnerability scanning  
✅ **Monitored**: Full observability stack with metrics, logs, and alerts configured  
✅ **Tested**: Complete test suite covering security, functionality, and performance  
✅ **Scalable**: Horizontal scaling capabilities with load balancing and service discovery  
✅ **Documented**: Production-ready documentation with troubleshooting guides  
✅ **Automated**: CI/CD pipeline with automated builds, tests, and deployments  
✅ **Compliant**: Security standards compliance with audit trail capabilities  
✅ **Maintainable**: Clear structure for updates, patching, and dependency management  
✅ **Performant**: Optimized for production workloads with resource efficiency

## Quality Standards

- **Security**: Every container runs as non-root with minimal privileges and regular vulnerability scanning
- **Performance**: Optimized build times, minimal image sizes, and efficient resource utilization
- **Reliability**: Comprehensive health checks, graceful degradation, and automated recovery procedures
- **Documentation**: Every component documented with examples, troubleshooting, and best practices
- **Maintainability**: Clear separation of concerns, version management, and update procedures
- **Compliance**: Industry security standards compliance with audit logging and monitoring
- **Automation**: Full CI/CD integration with quality gates and automated deployment validation