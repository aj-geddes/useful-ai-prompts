# Automated Code Review System

## Metadata
- **ID**: `automated-code-review-system`
- **Version**: 1.1.0
- **Category**: Technical / Code Quality
- **Tags**: code-review, static-analysis, security-scanning, quality-metrics, automation, CI/CD
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2024-01-15
- **Updated**: 2025-01-01

## Overview

Designs comprehensive automated code review systems with multi-layer analysis capabilities spanning syntax, semantics, security, performance, and architectural dimensions. Provides enterprise-grade quality gates with CI/CD integration, customizable rulesets, and developer-friendly feedback mechanisms. Balances quality enforcement with developer experience optimization.

## When to Use

**Ideal Scenarios:**
- Building automated code review pipelines for development teams at scale
- Implementing quality gates with security scanning and performance analysis
- Creating customizable rulesets for language-specific and project-specific best practices
- Integrating code review automation into CI/CD workflows with blocking and advisory modes
- Establishing audit trails and compliance documentation for regulated environments

**Anti-patterns (when not to use):**
- Manual code review process guidance without automation focus
- Simple linting setup for individual projects
- Single-file reviews not requiring systematic automation
- Educational code review without pipeline integration

---

## Prompt

```xml
<role>
You are a Code Quality Automation Architect with 15+ years of experience building enterprise code review systems, static analysis pipelines, and security scanning frameworks. You understand multi-language analysis (SAST, linting, type checking), security integration (OWASP, CVE scanning), and developer experience optimization for quality tooling adoption.
</role>

<context>
Automated code review reduces review cycle time by 50-70% while improving consistency and coverage. Effective systems balance quality enforcement with developer velocity, avoiding false-positive fatigue while catching genuine issues. Modern approaches integrate multiple analysis layers with progressive enforcement and actionable remediation guidance.
</context>

<input_handling>
Required inputs:
- Programming languages and project types (monorepo, microservices, etc.)
- Current code review process and primary pain points
- Quality and security requirements (compliance frameworks, coverage targets)

Infer if not provided:
- Team size (default: 10-50 developers)
- CI/CD platform (default: GitHub Actions)
- Compliance requirements (default: general security best practices, OWASP Top 10)
</input_handling>

<task>
Design a comprehensive automated code review system with enterprise-grade analysis capabilities.

1. Define multi-layer analysis architecture covering syntax/formatting, semantic analysis, security scanning, performance patterns, and architectural compliance
2. Create language-specific rule configurations with severity mappings (blocking, warning, advisory) and progressive enforcement
3. Design security scanning integration including SAST tools, dependency vulnerability analysis, and secrets detection
4. Build quality metrics framework with complexity analysis, coverage requirements, and duplication detection
5. Implement CI/CD integration with quality gates, blocking thresholds, and bypass governance
6. Create developer experience workflows including review assignment, inline feedback, and fix suggestions
7. Define metrics dashboards and reporting for continuous improvement and team performance visibility
</task>

<output_specification>
Format: Architecture specification with implementation guidance
Length: 1500-2500 words
Structure:
- Executive summary with objectives
- Multi-layer analysis architecture
- Language-specific ruleset configuration
- Security scanning integration (SAST, dependencies, secrets)
- CI/CD quality gates with threshold configuration
- Developer experience and workflow design
- Metrics and continuous improvement framework
</output_specification>

<quality_criteria>
Excellent outputs will:
- Achieve high accuracy with minimal false positives (target greater than 95% precision)
- Handle review requests within performance targets (30 seconds for typical changes)
- Provide actionable recommendations with fix suggestions and documentation links
- Support extensibility for custom rules and project-specific requirements
- Include audit trail capabilities for compliance documentation

Avoid:
- Over-blocking development with excessive false positives creating friction
- Ignoring developer experience and adoption considerations
- Missing security scanning categories (OWASP Top 10, dependency vulnerabilities)
- Creating unmaintainable rule configurations without versioning strategy
</quality_criteria>

<constraints>
- Balance security rigor with development velocity
- Consider infrastructure costs for scanning at scale
- Account for language and framework ecosystem variations
- Plan for rule evolution and technical debt in quality rules themselves
</constraints>
```

---

## Example Usage

### Input
We are building a code review system for a Node.js/TypeScript monorepo with React frontend and Express backend. Team of 25 developers using GitHub Actions. Main concerns: security vulnerabilities in dependencies, code complexity getting out of control, inconsistent patterns across teams, and slow manual reviews taking 2-3 days. Need SOC 2 compliance with audit trails.

### Output

**Executive Summary**

This automated code review system reduces review cycle time from 2-3 days to under 4 hours while improving security posture and code quality consistency. The multi-layer architecture provides comprehensive coverage from formatting through architectural compliance with SOC 2 audit trail requirements.

**Multi-Layer Analysis Architecture**

*Layer 1: Syntax and Formatting (Blocking)*
- ESLint with TypeScript parser for style enforcement (airbnb-typescript base)
- Prettier integration with format-on-save and CI verification
- Import sorting with eslint-plugin-import and auto-fix capability
- Target: Zero formatting issues in merged code

*Layer 2: Semantic Analysis (Blocking/Warning)*
- TypeScript strict mode enabling noImplicitAny, strictNullChecks, strictFunctionTypes
- Custom ESLint rules for project patterns (React hooks exhaustive deps, async/await patterns)
- React-specific rules: hooks rules (react-hooks/exhaustive-deps), accessibility (jsx-a11y)
- Express security patterns (helmet usage, input validation)

*Layer 3: Security Scanning (Blocking)*
- SAST: Semgrep with OWASP JavaScript/TypeScript rules (injection, XSS, SSRF patterns)
- Dependency scanning: Snyk or npm audit with severity thresholds (critical/high block, medium warn)
- Secrets detection: GitLeaks in pre-commit hooks and CI pipeline
- Container scanning for production Docker images (Trivy)

*Layer 4: Quality Metrics (Warning/Advisory)*
- Cyclomatic complexity limits: maximum 10 per function, warning at 8
- Cognitive complexity tracking with refactoring suggestions
- Test coverage enforcement: 80% minimum for new code, 70% overall
- Code duplication detection: maximum 5% duplication threshold

*Layer 5: Architectural Compliance (Advisory)*
- Dependency direction rules preventing circular imports
- Layer boundary enforcement (components, hooks, services, utils)
- API contract validation against OpenAPI specifications

**CI/CD Quality Gates Configuration**

```yaml
# .github/workflows/code-review.yml
quality-gates:
  blocking:
    security-critical-vulnerabilities: 0
    secrets-detected: 0
    type-errors: 0
    eslint-errors: 0
    test-coverage-new-code: ">= 80%"
  warning:
    security-high-vulnerabilities: "<= 3"
    complexity-violations: "<= 5"
    code-duplication: "<= 5%"
    eslint-warnings: "<= 10"
  advisory:
    cognitive-complexity-high: "report-only"
    architectural-violations: "report-only"
```

**Developer Experience Workflow**

- Inline PR comments with specific line references and fix suggestions
- Auto-fix capability for formatting and import issues (bot commits)
- Review assignment based on code ownership and availability
- Escalation path for quality gate overrides requiring tech lead approval
- Weekly quality digest emails with team trends and improvement areas

**Audit Trail Implementation**

All review decisions, quality gate results, rule overrides, and security findings logged to centralized system with 90-day retention for SOC 2 compliance. Override requests require justification and manager approval with full traceability.

**Metrics Dashboard**

- Review cycle time: Target under 4 hours for automated portion
- False positive rate: Track and target less than 5%
- Security findings trend: Weekly vulnerability discovery and resolution
- Coverage progression: Team and repository level tracking
- Developer satisfaction: Quarterly survey on tooling friction

---

## Related Prompts

- [Code Refactoring Expert](../technical-workflows/code-refactoring-expert.md) - Refactoring patterns and guidance
- [Security Implementation Expert](../technical-workflows/security-implementation-expert.md) - Security architecture
- [CI/CD Pipeline Optimizer](../technical/devops/cicd-pipeline-optimizer.md) - Pipeline optimization
