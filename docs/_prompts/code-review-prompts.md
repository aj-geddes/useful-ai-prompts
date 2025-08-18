---
category: technical
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for technical optimization and expert consultation
layout: prompt
slug: code-review-prompts
tags:
- technical
title: Code Review Prompts
use_cases:
- technical optimization
- professional workflow enhancement
version: 3.0.0
---

Create a **comprehensive automated code review system** for `Ask User for Programming Language and Project Type` with enterprise-grade analysis capabilities.

Initialize it as a **production-ready code review automation platform** with AI-powered analysis, security scanning, quality metrics, and team collaboration workflows.

## Core Requirements

### Review Framework Architecture

- **Multi-layer analysis**: Syntax, semantics, security, performance, and architectural review
- **Language-specific rules**: Tailored analysis patterns for the specified programming language
- **Customizable rulesets**: Configurable review criteria and severity levels
- **Integration support**: CI/CD pipeline integration and IDE plugin compatibility

### Analysis Categories

- **Code quality**: Structure, readability, maintainability, and complexity analysis
- **Security scanning**: OWASP compliance, vulnerability detection, and threat modeling
- **Performance optimization**: Algorithm efficiency, resource usage, and bottleneck identification
- **Best practices compliance**: Language-specific conventions and industry standards
- **Documentation analysis**: Code comments, API documentation, and inline help quality

## Enhanced Security & Quality Assessment

### Advanced Security Analysis

- **Static Application Security Testing (SAST)**: Comprehensive vulnerability scanning
- **Dependency analysis**: Third-party library security assessment and license compliance
- **Secrets detection**: API keys, passwords, and sensitive data exposure prevention
- **Injection attack prevention**: SQL, NoSQL, command, and script injection vulnerability detection
- **Authentication & authorization**: Access control and permission validation

### Quality Metrics & Standards

- **Code complexity metrics**: Cyclomatic complexity, cognitive complexity, and maintainability index
- **Test coverage analysis**: Unit test coverage, integration test gaps, and quality assessment
- **Technical debt measurement**: Code smells, refactoring opportunities, and legacy code assessment
- **Performance profiling**: Memory usage patterns, execution time analysis, and optimization opportunities
- **Architectural compliance**: Design pattern usage, SOLID principles, and modularity assessment

### Team Collaboration Features

- **Review workflow automation**: Automated reviewer assignment and escalation protocols
- **Knowledge sharing**: Code explanation generation and learning resource recommendations
- **Progress tracking**: Review completion metrics, team performance analytics, and improvement trends
- **Communication integration**: Slack, Teams, and email notification systems

## Advanced Features (New)

### AI-Powered Enhancement

- **Intelligent code suggestions**: Context-aware improvement recommendations
- **Automated fix generation**: Security patch suggestions and code optimization proposals
- **Natural language explanations**: Plain English descriptions of complex code issues
- **Learning system**: Adaptive rules based on team preferences and historical decisions

### Enterprise Integration

- **LDAP/SSO integration**: Enterprise authentication and user management
- **Compliance reporting**: SOC 2, ISO 27001, and industry-specific compliance validation
- **Audit trail management**: Complete review history and decision tracking
- **Custom dashboard creation**: Executive and team-level reporting interfaces

### Development Workflow Optimization

- **Pre-commit hooks**: Automated quality checks before code submission
- **IDE integration**: Real-time feedback and inline suggestions
- **Continuous monitoring**: Production code quality tracking and alerting
- **Training module**: Developer education and best practices guidance

### Advanced Analytics

- **Predictive analysis**: Bug probability assessment and maintenance cost prediction
- **Team performance insights**: Individual and team productivity metrics
- **Code evolution tracking**: Codebase health trends and improvement recommendations
- **Benchmark comparisons**: Industry standard comparisons and competitive analysis

## Implementation Strategy

### MCP Tool Optimization

- **Use `create_or_update_file`** for individual configuration files and rule definitions
- **Leverage `push_files`** for bulk creation of analysis scripts and documentation
- **Handle integration setup** systematically with proper API configurations
- **Systematic deployment**: Core engine → Rules → Integrations → Dashboard → Training

### Development Process

1. **Requirements analysis** for specific language and project type characteristics
2. **Rule engine development** with customizable analysis patterns
3. **Integration framework** setup for CI/CD and development tools
4. **Dashboard and reporting** system implementation
5. **Testing and validation** with sample codebases
6. **Documentation and training** material creation

### Quality Assurance Process

- **Rule validation**: Testing analysis rules against known code patterns
- **Performance benchmarking**: System performance under various codebase sizes
- **Integration testing**: CI/CD pipeline and IDE plugin functionality verification
- **User acceptance testing**: Team workflow validation and usability assessment
- **Security validation**: Review system security and access control testing

### Deployment Strategy

- **Phased rollout**: Gradual team adoption with feedback integration
- **Training program**: Developer onboarding and system usage education
- **Support system**: Documentation, troubleshooting guides, and help desk setup
- **Maintenance planning**: Update procedures and rule refinement processes

## Deliverables

### Core Analysis Engine

- `review-engine/` - Main analysis engine with language-specific processors
- `rules/` - Configurable rule definitions and severity mappings
- `plugins/` - Language-specific analysis plugins and extensions
- `config/` - System configuration templates and environment settings

### Security & Quality Modules

- `security-scanner/` - SAST implementation and vulnerability detection
- `quality-metrics/` - Code quality analysis and measurement tools
- `dependency-analyzer/` - Third-party library security and license scanning
- `performance-profiler/` - Performance analysis and optimization detection

### Integration Components

- `ci-cd-integration/` - Jenkins, GitHub Actions, GitLab CI integration scripts
- `ide-plugins/` - VS Code, IntelliJ, and other IDE extension implementations
- `api/` - REST API for external tool integration and data access
- `webhooks/` - Event-driven integration for real-time notifications

### User Interface & Reporting

- `dashboard/` - Web-based review dashboard and analytics interface
- `reports/` - Automated report generation and customizable templates
- `notifications/` - Email, Slack, and Teams notification systems
- `mobile/` - Mobile application for review management and approval

### Documentation & Training

- `docs/` - Comprehensive setup, configuration, and usage documentation
- `training/` - Developer training materials and best practices guides
- `examples/` - Sample configurations and integration examples
- `troubleshooting/` - Common issues and resolution procedures

### Testing & Validation

- `tests/` - Comprehensive test suite for all system components
- `benchmarks/` - Performance testing and validation scripts
- `sample-projects/` - Test codebases for validation and demonstration
- `compliance-tests/` - Security and compliance validation tools

## Success Criteria

✅ **Comprehensive**: Covers all aspects of code quality, security, and performance analysis  
✅ **Automated**: Seamless integration with development workflows and CI/CD pipelines  
✅ **Actionable**: Provides specific, implementable recommendations for code improvement  
✅ **Scalable**: Handles codebases from small projects to enterprise-scale applications  
✅ **Secure**: Implements robust security scanning and vulnerability detection  
✅ **Collaborative**: Enables effective team review workflows and knowledge sharing  
✅ **Measurable**: Provides quantifiable metrics for code quality and team performance  
✅ **Compliant**: Meets industry standards and regulatory compliance requirements  
✅ **Educational**: Helps developers learn and improve their coding practices  
✅ **Maintainable**: Easy to update, configure, and extend for evolving requirements

## Quality Standards

- **Accuracy**: Review analysis must achieve >95% accuracy with minimal false positives
- **Performance**: System must handle review requests within 30 seconds for typical code changes
- **Reliability**: 99.9% uptime with comprehensive error handling and recovery procedures
- **Security**: All code analysis performed in secure, isolated environments with audit trails
- **Usability**: Intuitive interface requiring minimal training for developer adoption
- **Extensibility**: Modular architecture supporting custom rules and third-party integrations
- **Compliance**: Full audit trail and documentation meeting enterprise compliance requirements
- **Scalability**: Support for teams from 5 to 500+ developers with consistent performance
