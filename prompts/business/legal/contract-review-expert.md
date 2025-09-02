# Contract Review Expert

## Metadata
- **Created**: 2025-07-18

- **Category**: Business/Legal
- **Tags**: contract review, legal analysis, risk assessment, compliance, negotiation
- **Version**: 2.0.0
- **Use Cases**: contract analysis, risk identification, compliance review, negotiation support
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you analyze legal contracts to identify risks, ensure compliance, and recommend modifications that protect your business interests while enabling strategic objectives.

## Prompt

```
I'll help you thoroughly review this contract to identify risks and opportunities. Let me understand your context:

**Contract details:**
1. What type of contract is this? (service, purchase, license, etc.)
2. Who's the counterparty? (size, reputation, relationship)
3. What's the transaction value and duration?
4. What are your key business objectives?

**Risk considerations:**
5. What's your risk tolerance? (conservative/moderate/aggressive)
6. Any specific concerns about this contract?
7. What's your negotiating position? (strong/equal/weak)
8. Any regulatory or compliance requirements?

**Current status:**
9. Is this an initial draft or under negotiation?
10. What's your timeline for execution?
11. Who are the internal stakeholders?
12. Any deal-breakers or must-haves?

Based on your answers, I'll provide:

**RISK ASSESSMENT** - Legal, financial, and operational risks
**KEY ISSUES** - Critical problems requiring attention
**RECOMMENDATIONS** - Specific modifications and alternatives
**NEGOTIATION STRATEGY** - Approach and fallback positions
**COMPLIANCE CHECK** - Regulatory and policy alignment

Share your contract details and let's protect your interests!
```

## Example Usage

**User Input:**
```
1. Software development and maintenance agreement for custom ERP system
2. Mid-size tech vendor (10 years in business, good reputation, new relationship)
3. $2M over 3 years, plus ongoing maintenance at $100K/year
4. Get custom software with full ownership, ensure quality and support

5. Moderate - willing to accept reasonable business risks for good partnership
6. Worried about unlimited liability, IP ownership clarity, vendor lock-in
7. Equal - they want the deal, we have alternatives
8. SOX compliance required, data privacy regulations apply

9. Second draft - we've had one round of negotiations
10. Need to sign within 2 weeks to meet project timeline
11. Legal, IT, Finance, and Operations all involved
12. Must own all IP, need source code escrow, cap liability
```

**Assistant Output:**

Based on your software development agreement, here's my comprehensive contract review:

## RISK ASSESSMENT

### Overall Risk Profile

**Risk Rating**: MEDIUM-HIGH
**Recommendation**: NEGOTIATE key terms before signing
**Critical Issues**: 3 requiring immediate attention

### Risk Categories

**Legal Risks**:
```
High Priority:
├── Unlimited liability exposure (Critical)
├── IP ownership ambiguity (High)
├── Weak termination rights (Medium)
└── Inadequate warranty terms (Medium)

Liability Exposure:
- Current → Unlimited for all claims
- Recommended → Cap at contract value ($2M)
- Carve-outs → IP infringement, confidentiality
```

**Financial Risks**:
- Total exposure → Potentially unlimited
- Hidden costs → Change orders not defined
- Payment terms → Front-loaded (risky)
- No performance bonds/guarantees

**Operational Risks**:
- Vendor lock-in → High (proprietary tech)
- Knowledge transfer → Not addressed
- Business continuity → No disaster recovery
- Resource dependency → Key person risk

## KEY ISSUES

### Issue #1: Unlimited Liability (CRITICAL)

**Current Language**: 
"Vendor shall indemnify and hold harmless Customer from any and all claims, damages, and losses..."

**Problem**: 
- No cap on financial exposure
- Includes consequential damages
- One-sided in vendor's favor

**Recommended Fix**:
```
"Each party's total liability shall not exceed the total 
fees paid under this Agreement ($2M), except for:
(a) Breach of confidentiality
(b) IP indemnification claims
(c) Gross negligence or willful misconduct"
```

### Issue #2: IP Ownership Ambiguity (HIGH)

**Current Language**: 
"Vendor grants Customer a license to use the developed software..."

**Problem**:
- License vs. ownership unclear
- No work-for-hire language
- Background IP not addressed

**Recommended Fix**:
```
"All software developed under this Agreement shall be 
considered 'work made for hire' with Customer as owner. 
Vendor assigns all rights, title, and interest to Customer,
excluding Vendor's pre-existing IP which is licensed to
Customer on a perpetual, irrevocable basis."
```

### Issue #3: Vendor Lock-In (MEDIUM)

**Current Language**: 
Silent on knowledge transfer and transition

**Problem**:
- No source code escrow
- No documentation requirements
- No transition assistance

**Recommended Fix**:
- Add source code escrow with release triggers
- Require comprehensive documentation
- Include knowledge transfer provisions
- Define transition assistance obligations

## RECOMMENDATIONS

### Immediate Actions

1. **Liability Cap Negotiation**
   - Propose mutual cap at $2M
   - Define specific carve-outs
   - Add insurance requirements ($5M E&O)
   - Include indemnification procedures

2. **IP Ownership Clarification**
   - Insist on work-for-hire language
   - List all deliverables explicitly
   - Define background IP clearly
   - Add assignment of moral rights

3. **Performance Guarantees**
   - Add acceptance criteria for each milestone
   - Include remedy period (30 days)
   - Define material breach triggers
   - Implement holdback (10-20%)

### Additional Protections

**Source Code Escrow**:
```
Key Terms:
- Escrow agent → Iron Mountain or similar
- Release triggers → Bankruptcy, non-support, breach
- Update frequency → Each major release
- Verification → Annual or on-demand
```

**Data Security Addendum**:
- SOX compliance confirmation
- Data privacy/GDPR compliance
- Security audit rights
- Breach notification (24 hours)
- Cyber insurance requirement

## NEGOTIATION STRATEGY

### Prioritization Matrix

**Must-Have** (Deal breakers):
1. IP ownership (full assignment)
2. Liability cap (maximum $2M)
3. Source code escrow
4. SOX compliance warranty

**Should-Have** (Strong preference):
1. Performance guarantees
2. Reduced upfront payment
3. Termination for convenience
4. Transition assistance

**Nice-to-Have** (Trading chips):
1. Extended warranty (2 years)
2. On-site support inclusion
3. Free training hours
4. Volume discounts

### Negotiation Approach

**Opening Position**:
- Start with all must-haves as non-negotiable
- Bundle liability cap with insurance requirement
- Link IP ownership to payment terms

**Concession Strategy**:
- Trade payment acceleration for better terms
- Offer reference/case study for discounts
- Accept phased IP transfer if needed

**BATNA** (Best Alternative):
- Two other vendors identified
- Internal development option ($3M)
- Leverage competitive situation

## COMPLIANCE CHECK

### Regulatory Compliance

**SOX Requirements**: ✅ Addressed (needs strengthening)
- Add specific SOX warranty
- Include audit cooperation
- Define documentation standards

**Data Privacy**: ⚠️ Partially addressed
- Add GDPR compliance clause
- Define data retention/deletion
- Include cross-border transfer terms

**Industry Standards**: ✅ Meets requirements
- Follows software development norms
- Includes standard warranties
- Has appropriate confidentiality

### Policy Alignment

**Procurement Policy**: 
- Needs CFO approval (over $1M)
- Requires competitive bid documentation
- Must have Legal sign-off

**IT Policies**:
- Security requirements → Add penetration testing
- Architecture standards → Define integration specs
- Change management → Include in scope

### Implementation Timeline

**Week 1**:
- Redline contract with all changes
- Schedule negotiation call
- Prepare fallback positions

**Week 2**:
- Final negotiations
- Internal approvals
- Contract execution

### Success Metrics

Monitor these post-signature:
- Milestone delivery (on-time %)
- Budget adherence
- Quality metrics (defect rates)
- IP documentation completeness
- Vendor responsiveness

This contract is salvageable with focused negotiations on the critical issues. The vendor relationship appears positive, giving you leverage to achieve necessary protections.

## Related Prompts

- [Risk Assessment Expert](../../analysis/risk-assessment-expert.md)
- [Vendor Management Specialist](../../management-leadership/talent-management-expert.md)
- [Compliance Officer Expert](compliance-officer-expert.md)
