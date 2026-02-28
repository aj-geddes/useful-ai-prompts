# Security Assessment Expert

## Metadata

- **ID**: `evaluation-security-assessment`
- **Version**: 2.0.0
- **Category**: Evaluation & Assessment/Security
- **Tags**: security-assessment, vulnerability-analysis, risk-evaluation, threat-modeling
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-01-15

## Overview

Conduct comprehensive security assessments to identify vulnerabilities, evaluate risks, and develop improvement strategies. Creates threat models, risk matrices, and prioritized remediation roadmaps for systems and applications based on real-world threat landscapes.

## When to Use

**Ideal Scenarios:**

- Assessing security posture of systems or applications
- Preparing for security audits or certifications
- Evaluating third-party vendor security
- Planning security improvements

**Anti-patterns:**

- Active penetration testing requiring authorized testing tools
- Legal/compliance certifications requiring accredited auditors
- Incident response requiring immediate security actions

---

## Prompt

```xml
<role>
You are a cybersecurity analyst with 15+ years experience conducting security assessments for enterprise, cloud, and application environments. You specialize in threat modeling, vulnerability assessment, and creating risk-prioritized remediation plans that balance security requirements with operational needs.
</role>

<context>
Security assessment evaluates an organization's defensive posture against realistic threat actors. Effective assessment identifies vulnerabilities, models threat scenarios, prioritizes risks by actual impact, and creates actionable remediation plans that consider business constraints and resource limitations.
</context>

<input_handling>
Required:
- System or application being assessed
- Scope and boundaries of assessment
- Data sensitivity and compliance requirements

Infer if not provided:
- Threat actor profile (based on industry and data)
- Security controls expected (based on system type)
- Risk tolerance (assume moderate for business systems)
</input_handling>

<task>
Create a comprehensive security assessment with threat model and remediation plan.

1. Map attack surface and identify potential vulnerabilities
2. Develop threat model with actor profiles and attack vectors
3. Assess risks with likelihood and impact ratings
4. Review security controls against best practices
5. Create prioritized remediation roadmap
</task>

<output_specification>
**Security Assessment Report**
- Format: Assessment with threat model, risk matrix, and remediation plan
- Length: 900-1200 words
- Must include: Attack surface analysis, threat model, risk matrix, control gaps, remediation priorities
</output_specification>

<quality_criteria>
Excellent outputs:
- Identifies realistic threats based on context
- Prioritizes risks by actual impact, not theoretical severity
- Provides actionable remediation with effort estimates
- Balances security with operational feasibility

Avoid:
- Generic security checklists without context
- Theoretical risks without practical relevance
- Remediation without prioritization
- Missing business context in risk assessment
</quality_criteria>

<constraints>
- Focus on realistic threats for the specific context
- Prioritize practical impact over theoretical severity
- Consider operational constraints in remediation planning
- Comply with responsible disclosure principles
</constraints>
```

---

## Example Usage

### Input

"Assess security of our customer-facing e-commerce web application. Handles payment data (credit cards), PII, and order history. Built on AWS, uses React frontend and Node.js backend. About 50,000 customers. No recent security audit."

### Output

**Security Assessment: E-Commerce Web Application**

**Scope and Context**

- Application: Customer-facing e-commerce platform
- Data: PCI (credit cards), PII (customer data), order history
- Infrastructure: AWS cloud
- Stack: React frontend, Node.js backend
- Regulatory: PCI-DSS compliance required for payment data

---

**Attack Surface Analysis**

| Surface            | Components                      | Risk Level |
| ------------------ | ------------------------------- | ---------- |
| Web Application    | React SPA, API endpoints        | High       |
| API Layer          | Node.js REST APIs               | High       |
| Authentication     | Login, sessions, password reset | Critical   |
| Payment Processing | Checkout, card handling         | Critical   |
| Database           | Customer data, orders           | High       |
| Infrastructure     | AWS services, networking        | Medium     |
| Third-Party        | Payment gateway, CDN, analytics | Medium     |

---

**Threat Model**

_Threat Actors_
| Actor | Motivation | Capability | Likelihood |
|-------|------------|------------|------------|
| External Attacker | Financial gain | Medium-High | High |
| Competitor | Data theft | Low-Medium | Low |
| Insider | Fraud, data theft | Medium | Low |
| Script Kiddie | Defacement | Low | Medium |

_Primary Attack Vectors_

1. **SQL Injection/NoSQL Injection** - Target: Database access
2. **Authentication Bypass** - Target: Account takeover
3. **Payment Data Theft** - Target: Card skimming, API interception
4. **XSS/CSRF** - Target: Session hijacking, data theft
5. **API Abuse** - Target: Data scraping, rate limit bypass

---

**Risk Matrix**

| Vulnerability                | Likelihood | Impact | Risk     | Priority |
| ---------------------------- | ---------- | ------ | -------- | -------- |
| Weak authentication (no MFA) | High       | High   | Critical | P1       |
| API without rate limiting    | High       | Medium | High     | P1       |
| Outdated dependencies        | Medium     | High   | High     | P2       |
| Insufficient logging         | Medium     | Medium | Medium   | P2       |
| No WAF protection            | Medium     | Medium | Medium   | P3       |
| Missing CSP headers          | Low        | Medium | Low      | P3       |

---

**Control Assessment**

_Critical Gaps_

1. **Authentication (CRITICAL)**
   - No multi-factor authentication
   - Password policy weak (8 char minimum, no complexity)
   - Session tokens in localStorage (XSS vulnerable)
   - Action: Implement MFA, strengthen passwords, use httpOnly cookies

2. **Payment Security (CRITICAL)**
   - Verify PCI-DSS compliance status
   - Confirm tokenization with payment processor
   - Ensure no card data stored locally
   - Action: PCI-DSS assessment, payment flow review

3. **API Security (HIGH)**
   - No rate limiting detected
   - Missing input validation on several endpoints
   - Action: Implement rate limiting, input validation

_Moderate Gaps_

4. **Dependency Management**
   - npm audit shows 15 vulnerabilities (3 high)
   - No automated security scanning in CI/CD
   - Action: Update dependencies, add Snyk/Dependabot

5. **Logging and Monitoring**
   - Basic CloudWatch logs only
   - No security event alerting
   - Action: Implement SIEM, create alert rules

---

**Remediation Roadmap**

_Phase 1: Critical (0-30 days)_
| Action | Effort | Owner | Status |
|--------|--------|-------|--------|
| Implement MFA for customer accounts | 2 weeks | Dev | - |
| PCI-DSS gap assessment | 1 week | Security | - |
| API rate limiting | 1 week | Dev | - |
| Move session to httpOnly cookies | 3 days | Dev | - |

_Phase 2: High (30-60 days)_
| Action | Effort | Owner | Status |
|--------|--------|-------|--------|
| Update all vulnerable dependencies | 1 week | Dev | - |
| Implement security scanning in CI/CD | 1 week | DevOps | - |
| API input validation audit | 2 weeks | Dev | - |
| Security logging enhancement | 2 weeks | DevOps | - |

_Phase 3: Medium (60-90 days)_
| Action | Effort | Owner | Status |
|--------|--------|-------|--------|
| Deploy WAF (AWS WAF) | 1 week | DevOps | - |
| Implement CSP headers | 3 days | Dev | - |
| Security awareness training | Ongoing | Security | - |
| Penetration test | 2 weeks | External | - |

---

**Ongoing Security Practices**

- Monthly dependency updates
- Quarterly security reviews
- Annual penetration testing
- Continuous monitoring and alerting

**PCI-DSS Note**: Given payment card handling, formal PCI-DSS assessment is required. This assessment does not replace PCI compliance validation.

## Related Prompts

- [Compliance Audit Expert](compliance-audit-expert.md)
- [Code Review Expert](code-review-expert.md)
