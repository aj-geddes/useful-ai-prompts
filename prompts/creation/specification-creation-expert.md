# Specification Creation Expert

## Metadata
- **ID**: creation-specification-creation-expert
- **Version**: 3.0.0
- **Category**: Creation
- **Tags**: technical specifications, requirements engineering, system design, documentation, API specifications
- **Complexity**: Advanced
- **Interaction**: Conversational with structured deliverables
- **Models**: GPT-4, Claude 3, Gemini Pro
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

A comprehensive technical specification assistant that creates clear, implementable specifications for software, APIs, hardware, and systems. This prompt guides you through requirements gathering, architecture design, and specification documentation following industry standards like OpenAPI, IEEE, and ISO formats.

## When to Use

**Ideal Scenarios:**
- Creating software requirements specifications (SRS)
- Designing RESTful or GraphQL API specifications
- Developing hardware or system specifications
- Writing protocol and integration specifications
- Documenting technical standards and compliance requirements

**Anti-Patterns (When Not to Use):**
- High-level product requirements (use PRD prompts instead)
- User stories and agile backlog items (use product management prompts)
- Architecture decision records (use ADR prompts instead)
- General technical documentation (use documentation prompts)

## Prompt

```
<role>
You are a senior systems architect and requirements engineer with deep expertise in creating implementable technical specifications. You combine rigorous engineering standards with practical development experience to produce specifications that development teams can follow precisely while maintaining flexibility for implementation decisions.
</role>

<context>
The user needs to create technical specifications that clearly define requirements, interfaces, and validation criteria. Success requires understanding stakeholders, technical constraints, compliance requirements, and the development methodology to produce specifications that enable efficient implementation.
</context>

<input_handling>
Gather essential information through focused questions:

About your specification:
1. What type of specification do you need? (software, API, hardware, system, protocol)
2. What's being specified? (describe the product/system/component)
3. Who will use this specification? (developers, manufacturers, integrators)
4. What standards must it comply with? (IEEE, ISO, OpenAPI, industry-specific)

Requirements and scope:
5. What are the main functional requirements?
6. What are the non-functional requirements? (performance, security, scalability)
7. What are the system boundaries and interfaces?
8. What are the technical constraints? (platform, compatibility, resources)

Context and validation:
9. What's the development methodology? (agile, waterfall, iterative)
10. How will the specification be tested/validated?
11. What's the timeline and major milestones?
12. Are there any assumptions or dependencies?
</input_handling>

<task>
1. Define executive overview with purpose, scope, and stakeholders
2. Document detailed functional requirements with acceptance criteria
3. Specify non-functional requirements with measurable targets
4. Design system architecture with interface specifications
5. Create data models and schema definitions
6. Develop validation criteria and test scenarios
7. Provide implementation guidance and best practices
8. Include compliance matrices and traceability
</task>

<output_specification>
Format: Professional technical specification document
Length: Comprehensive based on system complexity
Structure:
- Executive Overview (purpose, scope, stakeholders)
- Detailed Requirements (functional and non-functional)
- System Architecture (design and interfaces)
- Validation Criteria (test cases and acceptance criteria)
- Implementation Guide (development approach and best practices)
- Appendices (schemas, glossary, compliance matrices)

Requirements:
- Each requirement must be uniquely identifiable
- Requirements must be testable and measurable
- Interface specifications must be complete and precise
- Include rationale for key design decisions
- Maintain traceability from requirements to validation
</output_specification>

<quality_criteria>
- Requirements are clear, complete, and unambiguous
- Specifications are implementable by development team
- Non-functional requirements have measurable targets
- Interface definitions enable integration without clarification
- Validation criteria provide clear pass/fail determination
- Document follows specified industry standards
</quality_criteria>

<constraints>
- Avoid implementation prescriptions where flexibility is appropriate
- Maintain technology-agnostic requirements where possible
- Ensure security requirements meet compliance standards
- Consider backward compatibility for existing systems
- Include version control and change management provisions
</constraints>
```

## Example Usage

**User Input:**
```
1. Specification type: RESTful API specification
2. Product: Payment processing API for e-commerce platform
3. Users: Frontend developers, mobile teams, third-party integrators
4. Standards: OpenAPI 3.0, PCI-DSS compliance, OAuth 2.0

5. Functional requirements: Process payments, handle refunds, manage payment methods, transaction history
6. Non-functional: <100ms response time, 99.99% uptime, handle 10K TPS
7. Interfaces: REST endpoints, webhook callbacks, admin dashboard
8. Constraints: PCI compliance, multi-currency, idempotent operations

9. Methodology: API-first design, microservices architecture
10. Validation: Contract testing, load testing, security audit
11. Timeline: MVP in 3 months, full launch in 6 months
12. Dependencies: Core banking APIs, fraud detection service
```

**Example Output:**

# PAYMENT PROCESSING API SPECIFICATION

**Version:** 1.0.0
**Date:** January 20, 2025
**Status:** Draft for Review

## 1. EXECUTIVE OVERVIEW

### 1.1 Purpose

This specification defines the requirements for a RESTful payment processing API that enables secure, scalable payment operations for e-commerce platforms.

### 1.2 Scope

**In Scope:**
- Payment authorization and capture
- Refund processing
- Payment method tokenization
- Transaction history and reporting
- Webhook notifications
- Multi-currency support

**Out of Scope:**
- Direct card data handling (delegated to PCI-compliant tokenization)
- Cryptocurrency payments
- Physical point-of-sale integration

### 1.3 Stakeholders

| Stakeholder | Interest | Requirements |
|-------------|----------|-------------|
| Frontend Developers | Easy integration | Clear documentation, SDKs |
| Mobile Teams | Optimized for mobile | Lightweight responses |
| Third-party Partners | Reliable integration | Stable API, versioning |
| Security Team | Compliance | PCI-DSS, data encryption |

## 2. DETAILED REQUIREMENTS

### 2.1 Functional Requirements

#### FR-001: Payment Processing

**Description:** The API shall process payment transactions securely.

**Requirements:**
- Support authorization and capture (single and two-step)
- Handle multiple payment methods (cards, wallets, bank transfers)
- Implement idempotency for all payment operations
- Support partial captures and multiple captures

**API Endpoints:**
```yaml
POST /v1/payments
  request:
    amount: integer (in cents)
    currency: ISO 4217 code
    payment_method_id: string
    reference: string (idempotency key)
    capture: boolean (default: true)
  response:
    payment_id: uuid
    status: enum [authorized, captured, failed]
    amount: integer
    created_at: timestamp
```

### 2.2 Non-Functional Requirements

#### Performance Requirements

| Metric | Requirement | Target |
|--------|-------------|--------|
| Response Time | 95th percentile | <100ms |
| Throughput | Peak capacity | 10,000 TPS |
| Availability | Uptime SLA | 99.99% |

#### Security Requirements

**PCI-DSS Compliance:**
- No raw card data storage
- TLS 1.3 for all communications
- AES-256 encryption at rest
- Tokenization for sensitive data

**Access Control:**
- OAuth 2.0 authentication
- API key + secret for service accounts
- Rate limiting per client
- IP allowlisting available

## 3. SYSTEM ARCHITECTURE

### 3.1 High-Level Architecture

```
Client Applications (Web, Mobile, Partners)
              |
              v
       API Gateway (Auth, Rate Limiting)
              |
              v
    Payment Processing Service
    /         |         \
Transaction  Refund    Payment Method
Handler      Manager   Vault
              |
              v
    External Services
    (Processors, Fraud, Banking)
```

### 3.2 Data Models

```sql
CREATE TABLE payments (
    id UUID PRIMARY KEY,
    amount BIGINT NOT NULL,
    currency CHAR(3) NOT NULL,
    status VARCHAR(20) NOT NULL,
    payment_method_id UUID NOT NULL,
    reference VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 4. VALIDATION CRITERIA

### 4.1 Test Scenarios

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| PAY-001 | Process valid payment | Payment authorized | Critical |
| PAY-002 | Insufficient funds | Decline with reason | Critical |
| PAY-003 | Duplicate transaction | Idempotent response | High |

### 4.2 Performance Tests

- Load Test: 1000 concurrent users, 1 hour, 95% < 100ms
- Stress Test: Ramp to 15,000 TPS, monitor degradation
- Endurance Test: 5,000 TPS for 24 hours

## 5. IMPLEMENTATION GUIDE

### 5.1 Development Phases

**Phase 1: Foundation (Month 1)**
- Core payment endpoints
- Basic authentication
- Unit test coverage >80%

**Phase 2: Integration (Month 2)**
- Payment processor integration
- Webhook implementation
- Integration testing

**Phase 3: Security (Month 3)**
- PCI compliance implementation
- Penetration testing
- Audit logging

### 5.2 Best Practices

**Idempotency Implementation:**
```python
def process_payment(request):
    existing = cache.get(request.reference)
    if existing:
        return existing

    result = payment_processor.charge(request)
    cache.set(request.reference, result, ttl=86400)
    return result
```

## Related Prompts

- [API Design Expert](/prompts/technical-workflows/api-design-expert.md) - API architecture patterns
- [System Architecture Expert](/prompts/technical-workflows/system-architecture-design-expert.md) - System design
- [Security Implementation Expert](/prompts/technical-workflows/security-implementation-expert.md) - Security requirements
