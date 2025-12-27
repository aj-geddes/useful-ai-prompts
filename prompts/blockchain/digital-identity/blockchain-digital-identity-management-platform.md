# Blockchain Digital Identity Management Platform

## Metadata
- **ID**: `blockchain-digital-identity-management-platform`
- **Version**: 3.0.0
- **Category**: Blockchain/Digital-Identity
- **Tags**: digital identity, self-sovereign identity, verifiable credentials, privacy, KYC, DID, zero-knowledge proofs
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview
Designs secure blockchain-based digital identity management systems with self-sovereign identity (SSI), verifiable credentials, and privacy-preserving authentication. Covers DID architecture, zero-knowledge proofs, wallet integration, and regulatory compliance for enterprise and government deployments.

## When to Use
- Building employee or customer identity verification systems
- Implementing self-sovereign identity for credential management
- Creating privacy-preserving authentication with selective disclosure
- Integrating digital identity with HR, CRM, or government systems
- Meeting GDPR compliance requirements for identity data

**Don't use for**: Simple authentication flows, password management, non-blockchain identity solutions, single-application login systems

---

## Prompt

<role>
You are a digital identity architect with 12+ years designing blockchain-based identity systems for enterprises, governments, and consortiums. Your expertise spans W3C DID standards, verifiable credentials, zero-knowledge proof implementations, and privacy regulation compliance across GDPR, CCPA, and sector-specific requirements.
</role>

<context>
Digital identity management requires balancing user privacy with verification needs. Modern SSI systems give users control over their credentials while enabling cryptographic verification. Key considerations include blockchain selection, privacy protocols, wallet UX, and integration with existing enterprise systems.
</context>

<input_handling>
Required:
- Identity types to manage (employee, customer, citizen, student)
- Credentials requiring verification (education, employment, licenses)
- Verifier ecosystem (employers, institutions, government, banks)
- Privacy requirements (selective disclosure, zero-knowledge, anonymous)

Optional (with defaults):
- Blockchain platform (default: Ethereum with L2 scaling)
- Organization size (default: mid-market enterprise)
- Compliance scope (default: GDPR)
- Integration needs (default: standard HR/CRM systems)
</input_handling>

<task>
Design a comprehensive digital identity management platform.

1. Define identity architecture with DID structure and credential schemas
2. Design privacy framework with zero-knowledge proofs and selective disclosure
3. Plan wallet integration for mobile and web credential management
4. Create compliance automation for GDPR and regulatory requirements
5. Architect verification network with trusted verifier ecosystem and APIs
6. Develop implementation roadmap with phased deployment milestones
</task>

<output_specification>
**Digital Identity Platform Design**
- Format: Technical architecture with implementation details
- Length: 1500-2500 words
- Must include: DID architecture, privacy framework, wallet specs, compliance system, API design, timeline, cost breakdown
</output_specification>

<quality_criteria>
Excellent outputs:
- DID and credential schemas follow W3C standards
- Privacy controls provide granular user consent management
- Wallet UX enables simple credential presentation
- Compliance automation handles right-to-erasure and consent tracking
- Verification APIs support real-time credential validation

Avoid:
- Storing personal data on-chain without encryption
- Ignoring gas cost optimization for transactions
- Overlooking user experience in credential presentation flows
- Missing disaster recovery for identity systems
</quality_criteria>

<constraints>
- Follow W3C DID Core and Verifiable Credentials specifications
- Ensure GDPR Article 17 (right to erasure) compatibility
- Design for credential revocation without compromising privacy
- Support offline credential verification where possible
</constraints>

---

## Example Usage

### Input
Building digital identity for global consulting firm with 50K employees and 20K contractors. Need to verify education credentials, certifications, and security clearances. Verifiers include clients, government agencies, and certification bodies. Require high privacy with selective disclosure. Using Ethereum/Polygon, integrating with Workday and Salesforce. $2M budget, 12-month deployment.

### Output

## Identity Architecture

**DID Structure**
```
Format: did:ethr:0x...employee_address
Document contains:
- Public keys for verification
- Service endpoints for credential retrieval
- Authentication methods
- Capability invocation rights
```

**Credential Schema - Education Example**
```json
{
  "type": ["VerifiableCredential", "EducationCredential"],
  "issuer": "did:ethr:0x...university",
  "credentialSubject": {
    "id": "did:ethr:0x...employee",
    "degree": "Master of Computer Science",
    "institution": "Stanford University",
    "graduationDate": "2020-06-15"
  },
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "verificationMethod": "did:ethr:0x...university_key"
  }
}
```

## Privacy Framework

**Selective Disclosure Levels**
- Level 1: Credential validity only (no personal data)
- Level 2: Boolean attribute verification ("has security clearance")
- Level 3: Specific field disclosure with user consent
- Level 4: Zero-knowledge proofs (range proofs, set membership)

**GDPR Compliance**
- Off-chain encrypted credential storage
- On-chain commitment hashes only
- User-controlled encryption keys
- Automated data deletion workflows

## Wallet Integration

**Mobile Wallet Features**
- DID management with biometric auth
- QR code credential presentation
- Selective disclosure interface
- Cross-device synchronization

**Verification Flow**
1. Verifier generates request with required credentials
2. Employee scans QR, reviews request, selects disclosure level
3. Wallet creates verifiable presentation with privacy filters
4. Verifier validates signatures, checks revocation status

## System Integration

**Workday Integration**
- Employee onboarding triggers DID generation
- Role changes update credentials automatically
- Offboarding revokes active credentials

**Verification API**
```javascript
GET /api/verify/credential
POST /api/verify/batch
GET /api/status/employee/{did}
```

## Implementation Timeline

**Phase 1 (Months 1-4):** Blockchain deployment, core credentials, privacy framework, wallet MVP

**Phase 2 (Months 5-8):** Workday/Salesforce integration, verifier network, 1000-employee pilot

**Phase 3 (Months 9-12):** Full rollout, contractor integration, analytics, global expansion

## Cost Breakdown

- Smart contracts & security audit: $300K
- Mobile/web applications: $400K
- Enterprise integration: $350K
- Privacy & compliance: $150K
- Ongoing (annual): $300K

**Success Metrics:** 99.9% uptime, <2s verification, 80% manual verification reduction, 100% GDPR compliance

---

## Related Prompts
- [Smart Contract Security Audit Platform](../smart-contracts/smart-contract-security-audit-platform.md)
- [Enterprise Blockchain Integration Platform](../blockchain-development/enterprise-blockchain-integration-platform.md)
- [Cross-Chain Interoperability Bridge Platform](../cross-chain/cross-chain-interoperability-bridge-platform.md)
