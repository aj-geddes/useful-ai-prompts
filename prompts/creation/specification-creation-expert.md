# Specification Creation Expert

## Metadata
- **Created**: 2025-01-15

- **Category**: Creation
- **Tags**: technical specifications, requirements engineering, system design, documentation, standards
- **Version**: 2.0.0
- **Use Cases**: software specifications, API specs, hardware requirements, system architecture, technical standards
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical specification creation assistant that helps you develop clear, comprehensive technical specifications. Provide your requirements and I'll create detailed specifications with all necessary sections, compliance standards, and implementation guidance.

## Prompt

```
I'll help you create professional technical specifications that clearly define requirements and guide implementation. Let me gather information about your specification needs.

About your specification:
1. What type of specification do you need? (software, API, hardware, system, protocol)
2. What's being specified? (describe the product/system/component)
3. Who will use this specification? (developers, manufacturers, integrators)
4. What standards must it comply with? (IEEE, ISO, industry-specific)

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

Based on your answers, I'll create:

**1. EXECUTIVE OVERVIEW** - Purpose, scope, and key stakeholders
**2. DETAILED REQUIREMENTS** - Functional and non-functional specifications
**3. SYSTEM ARCHITECTURE** - Technical design and interfaces
**4. VALIDATION CRITERIA** - Test cases and acceptance criteria
**5. IMPLEMENTATION GUIDE** - Development approach and best practices

Please provide the information above, and I'll create a comprehensive specification that ensures clear understanding and successful implementation.
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

**Assistant Output:**

Based on your payment processing API requirements, here's your comprehensive specification:

# PAYMENT PROCESSING API SPECIFICATION

**Version:** 1.0.0  
**Date:** January 20, 2025  
**Status:** Draft for Review  

## 1. EXECUTIVE OVERVIEW

### 1.1 Purpose

This specification defines the requirements for a RESTful payment processing API that enables secure, scalable payment operations for e-commerce platforms. The API will handle payment transactions, refunds, payment method management, and provide comprehensive transaction history.

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
- Accounting reconciliation

### 1.3 Stakeholders

| Stakeholder | Interest | Requirements |
|-------------|----------|-------------|
| Frontend Developers | Easy integration | Clear documentation, SDKs |
| Mobile Teams | Optimized for mobile | Lightweight responses, offline support |
| Third-party Partners | Reliable integration | Stable API, versioning |
| Security Team | Compliance | PCI-DSS, data encryption |
| Operations | Monitoring | Logs, metrics, alerts |

## 2. DETAILED REQUIREMENTS

### 2.1 Functional Requirements

#### FR-001: Payment Processing

**Description:** The API shall process payment transactions securely and efficiently.

**Requirements:**
```
- Support authorization and capture (single and two-step)
- Handle multiple payment methods (cards, wallets, bank transfers)
- Implement idempotency for all payment operations
- Support partial captures and multiple captures
- Provide real-time transaction status
```

**API Endpoints:**
```yaml
POST /v1/payments
  request:
    amount: integer (in cents)
    currency: ISO 4217 code
    payment_method_id: string
    reference: string (idempotency key)
    capture: boolean (default: true)
    metadata: object
  response:
    payment_id: uuid
    status: enum [authorized, captured, failed]
    amount: integer
    created_at: timestamp

POST /v1/payments/{id}/capture
  request:
    amount: integer (optional, for partial)
  response:
    capture_id: uuid
    amount_captured: integer
    remaining_amount: integer
```

#### FR-002: Refund Management

**Requirements:**
- Process full and partial refunds
- Track refund status and history
- Support refund reasons and metadata
- Implement refund approval workflow

#### FR-003: Payment Method Management

**Requirements:**
- Tokenize payment methods securely
- Store customer payment preferences
- Support multiple payment methods per customer
- Enable/disable payment methods

### 2.2 Non-Functional Requirements

#### Performance Requirements

| Metric | Requirement | Target |
|--------|-------------|--------|
| Response Time | 95th percentile | <100ms |
| Throughput | Peak capacity | 10,000 TPS |
| Availability | Uptime SLA | 99.99% |
| Scalability | Auto-scaling | 30 seconds |

#### Security Requirements

**PCI-DSS Compliance:**
```yaml
Data Protection:
  - No raw card data storage
  - TLS 1.3 for all communications
  - AES-256 encryption at rest
  - Tokenization for sensitive data
  
Access Control:
  - OAuth 2.0 authentication
  - API key + secret for service accounts
  - Rate limiting per client
  - IP allowlisting available
  
Audit Trail:
  - Log all transactions
  - Immutable audit records
  - 7-year retention
  - Real-time monitoring
```

## 3. SYSTEM ARCHITECTURE

### 3.1 High-Level Architecture

```
┌─────────────────────────────────────────────────┐
│            Client Applications                  │
│     (Web, Mobile, Partner Systems)              │
└─────────────────┬───────────────────────────────┘
                  │ HTTPS/TLS 1.3
┌─────────────────┴───────────────────────────────┐
│            API Gateway                          │
│  (Auth, Rate Limiting, Request Routing)         │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────┴───────────────────────────────┐
│         Payment Processing Service              │
├─────────────┬──────────────┬───────────────────┤
│Transaction  │  Refund      │  Payment Method   │
│Handler      │  Manager     │  Vault            │
└─────────────┴──────────────┴───────────────────┘
                  │
┌─────────────────┴───────────────────────────────┐
│           External Services                     │
├──────────────┬─────────────┬───────────────────┤
│Payment       │Fraud        │Banking            │
│Processors    │Detection    │APIs               │
└──────────────┴─────────────┴───────────────────┘
```

### 3.2 API Design Principles

**RESTful Standards:**
- Resource-based URLs
- HTTP methods for actions
- JSON request/response
- HATEOAS for discoverability

**Error Handling:**
```json
{
  "error": {
    "code": "insufficient_funds",
    "message": "Payment declined due to insufficient funds",
    "request_id": "req_abc123",
    "documentation_url": "https://api.example.com/errors/insufficient_funds"
  }
}
```

### 3.3 Data Models

**Core Entities:**

```sql
-- Payment transaction table
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    amount BIGINT NOT NULL,
    currency CHAR(3) NOT NULL,
    status VARCHAR(20) NOT NULL,
    payment_method_id UUID NOT NULL,
    customer_id UUID NOT NULL,
    reference VARCHAR(100) UNIQUE NOT NULL,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_amount CHECK (amount > 0)
);

-- Payment method vault
CREATE TABLE payment_methods (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL,
    token VARCHAR(100) UNIQUE NOT NULL,
    type VARCHAR(20) NOT NULL,
    last_four VARCHAR(4),
    expiry_month INTEGER,
    expiry_year INTEGER,
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3.4 Integration Specifications

**Webhook Events:**
```yaml
events:
  - payment.authorized
  - payment.captured  
  - payment.failed
  - refund.completed
  - payment_method.created
  - payment_method.deleted

payload:
  event_type: string
  event_id: uuid
  timestamp: ISO8601
  data: object
  signature: HMAC-SHA256
```

## 4. VALIDATION CRITERIA

### 4.1 Test Scenarios

**Functional Tests:**

| Test ID | Scenario | Expected Result | Priority |
|---------|----------|-----------------|----------|
| PAY-001 | Process valid payment | Payment authorized | Critical |
| PAY-002 | Insufficient funds | Decline with reason | Critical |
| PAY-003 | Duplicate transaction | Idempotent response | High |
| REF-001 | Full refund | Amount returned | Critical |
| REF-002 | Partial refund | Correct amount | High |
| TOK-001 | Tokenize card | Token generated | Critical |

**Performance Tests:**
```yaml
Load Test:
  - Concurrent users: 1000
  - Duration: 1 hour
  - Target: 95% < 100ms
  
Stress Test:
  - TPS: Ramp to 15,000
  - Duration: 30 minutes
  - Monitor: CPU, memory, latency
  
Endurance Test:
  - Load: 5,000 TPS
  - Duration: 24 hours
  - Check: Memory leaks, degradation
```

### 4.2 Security Validation

**Security Audit Checklist:**
- [ ] PCI-DSS compliance scan
- [ ] Penetration testing
- [ ] OWASP Top 10 review
- [ ] Encryption verification
- [ ] Access control audit
- [ ] Data retention compliance

### 4.3 Acceptance Criteria

**Go-Live Requirements:**
1. All critical tests passing
2. Performance targets met
3. Security audit passed
4. Documentation complete
5. Monitoring configured
6. Runbook prepared

## 5. IMPLEMENTATION GUIDE

### 5.1 Development Approach

**Phase 1: Foundation (Month 1)**
- Set up development environment
- Implement core payment endpoints
- Basic authentication
- Unit test coverage >80%

**Phase 2: Integration (Month 2)**
- Payment processor integration
- Webhook implementation
- Error handling
- Integration testing

**Phase 3: Security & Compliance (Month 3)**
- PCI compliance implementation
- Security hardening
- Penetration testing
- Audit logging

### 5.2 Best Practices

**API Versioning:**
```
/v1/payments  - Current stable
/v2/payments  - Next version (beta)
/v1.1/payments - Minor updates
```

**Idempotency Implementation:**
```python
def process_payment(request):
    # Check idempotency key
    existing = cache.get(request.reference)
    if existing:
        return existing
    
    # Process payment
    result = payment_processor.charge(request)
    
    # Store result
    cache.set(request.reference, result, ttl=86400)
    return result
```

### 5.3 Monitoring & Operations

**Key Metrics:**
- API response time (p50, p95, p99)
- Transaction success rate
- Error rates by type
- Payment processor latency
- Webhook delivery success

**Alerts:**
```yaml
alerts:
  - name: high_error_rate
    condition: error_rate > 1%
    duration: 5 minutes
    severity: critical
    
  - name: payment_processor_down
    condition: health_check_fails
    duration: 1 minute
    severity: critical
```

### 5.4 Sample Implementation

**Payment Service Example:**
```javascript
class PaymentService {
  async processPayment(request) {
    // Validate request
    const validation = this.validatePaymentRequest(request);
    if (!validation.isValid) {
      throw new ValidationError(validation.errors);
    }
    
    // Check idempotency
    const existing = await this.checkIdempotency(request.reference);
    if (existing) {
      return existing;
    }
    
    // Process with retry logic
    const result = await this.retryableOperation(async () => {
      return await this.paymentProcessor.authorize({
        amount: request.amount,
        currency: request.currency,
        token: request.payment_method_id,
        metadata: request.metadata
      });
    });
    
    // Store result
    await this.storeTransaction(result);
    
    // Emit webhook
    await this.webhookService.emit('payment.authorized', result);
    
    return this.formatResponse(result);
  }
}
```

## 6. APPENDICES

### Appendix A: OpenAPI Specification

```yaml
openapi: 3.0.0
info:
  title: Payment Processing API
  version: 1.0.0
  description: Secure payment processing for e-commerce
  
servers:
  - url: https://api.payments.example.com/v1
    description: Production
  - url: https://sandbox.payments.example.com/v1
    description: Sandbox

components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
    OAuth2:
      type: oauth2
      flows:
        clientCredentials:
          tokenUrl: /oauth/token
          scopes:
            payments:read: Read payment data
            payments:write: Create payments
            refunds:write: Process refunds

paths:
  /payments:
    post:
      summary: Create a payment
      security:
        - OAuth2: [payments:write]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PaymentRequest'
      responses:
        201:
          description: Payment created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentResponse'
```

### Appendix B: Glossary

| Term | Definition |
|------|------------|
| **Idempotency** | Property ensuring repeated requests produce same result |
| **Tokenization** | Replacing sensitive data with non-sensitive tokens |
| **PCI-DSS** | Payment Card Industry Data Security Standard |
| **TPS** | Transactions Per Second |
| **Webhook** | HTTP callback for real-time event notifications |

### Appendix C: Compliance Matrix

| Requirement | Standard | Implementation | Verification |
|-------------|----------|----------------|-------------|
| Card data protection | PCI-DSS 4.0 | Tokenization, no storage | Quarterly scan |
| Data privacy | GDPR | Encryption, retention policy | Annual audit |
| API security | OWASP | Auth, rate limiting | Penetration test |
| Availability | SLA | Multi-region, failover | Monitoring |

### VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|------|
| 1.0.0 | 2025-01-20 | API Team | Initial specification |

This specification provides a complete blueprint for implementing a secure, scalable payment processing API that meets all requirements and compliance standards.

## Related Prompts

- [API Design Expert](./api-design-expert.md)
- [System Architecture Designer](./system-architecture-designer.md)
- [Security Requirements Analyst](./security-requirements-analyst.md)
