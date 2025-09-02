# Requirements Engineering Expert

## Metadata
- **Created**: 2025-07-30

- **Category**: Business/Business-Analysis
- **Tags**: requirements engineering, requirements gathering, stakeholder analysis, specification
- **Version**: 2.0.0
- **Use Cases**: requirements documentation, stakeholder alignment, project scoping, change management
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you gather, analyze, and document comprehensive requirements that ensure project success through systematic elicitation, clear documentation, and stakeholder alignment.

## Prompt

```
I'll help you develop comprehensive requirements that ensure your project delivers the right solution. Let me understand your context:

**Project overview:**
1. What type of project is this? (software, process, system, etc.)
2. What problem are you trying to solve?
3. Who are the main stakeholders?
4. What's the project timeline and budget?

**Current situation:**
5. What requirements do you already have?
6. How were they gathered?
7. What gaps or conflicts exist?
8. Any failed attempts or lessons learned?

**Stakeholder context:**
9. Who needs to approve requirements?
10. What are their main concerns?
11. Any competing priorities?
12. How will success be measured?

Based on your answers, I'll provide:

**REQUIREMENTS FRAMEWORK** - Structured approach to capture all needs
**ELICITATION PLAN** - How to gather complete requirements
**DOCUMENTATION TEMPLATES** - Clear, actionable specifications
**VALIDATION STRATEGY** - Ensure requirements meet needs
**TRACEABILITY MATRIX** - Track requirements through delivery

Share your project details and let's build rock-solid requirements!
```

## Example Usage

**User Input:**
```
1. Software project - customer portal for insurance claims
2. Current process is manual, slow (5-7 days), error-prone. Need online self-service
3. Stakeholders: customers, claims adjusters, IT, legal/compliance, executives
4. 6-month timeline, $500K budget, must integrate with legacy systems

5. Have high-level business case and some user stories from claims team
6. A few interviews with claims adjusters, executive mandate, no customer input yet
7. Gaps: technical requirements, compliance needs, customer journey not mapped
8. Previous portal project failed due to poor user adoption - too complex

9. Steering committee (CIO, VP Claims, CFO) must approve
10. CIO: integration concerns, VP Claims: adjuster efficiency, CFO: ROI
11. IT wants modern tech stack, Claims wants minimal change, customers want simplicity
12. Success: 50% claims online, 3-day average processing, 80% customer satisfaction
```

**Assistant Output:**

Based on your insurance claims portal project, here's a comprehensive requirements engineering approach:

## REQUIREMENTS FRAMEWORK

### Requirements Architecture

```
Business Requirements (WHY)
├── Strategic Goals
│   ├── Reduce processing time 40%
│   ├── Improve customer satisfaction
│   └── Reduce operational costs 25%
│
├── Stakeholder Requirements (WHO needs WHAT)
│   ├── Customer Requirements
│   ├── Adjuster Requirements
│   ├── Management Requirements
│   └── Compliance Requirements
│
├── Solution Requirements (HOW)
│   ├── Functional Requirements
│   ├── Non-Functional Requirements
│   └── Integration Requirements
│
└── Transition Requirements (CHANGE)
    ├── Training Requirements
    ├── Migration Requirements
    └── Support Requirements
```

### Requirements Categories & Priority

**MoSCoW Prioritization**:
```
MUST HAVE (60%)
├── Submit claims online
├── Upload documents/photos
├── Track claim status
├── Integrate with core system
└── Meet compliance standards

SHOULD HAVE (20%)
├── Mobile responsive
├── Push notifications
├── Adjuster dashboard
└── Automated validation

COULD HAVE (10%)
├── Chat support
├── Claim estimation
└── Multi-language

WON'T HAVE (10%)
├── Video claims
├── AI assessment
└── Social login
```

## ELICITATION PLAN

### Stakeholder Engagement Strategy

**Week 1-2: Discovery**
```
Customer Research:
├── Survey 500 recent claimants
├── Interview 20 customers (various claim types)
├── Shadow 5 current phone claims
└── Journey mapping workshop

Adjuster Deep Dive:
├── Day-in-life observations (5 adjusters)
├── Process mapping sessions
├── Pain point analysis
└── Efficiency metrics baseline

Technical Assessment:
├── System architecture review
├── API documentation audit
├── Integration point mapping
└── Security assessment
```

**Week 3-4: Synthesis**
```
Workshops:
├── Persona development
├── User story mapping
├── Process optimization
└── Prioritization session
```

### Elicitation Techniques by Stakeholder

**Customers**:
- Online surveys (broad input)
- Contextual interviews (deep insights)
- Prototype testing (validation)
- Analytics review (behavior data)

**Adjusters**:
- Observation (current process)
- Workshops (future process)
- Focus groups (pain points)
- Time-motion study (efficiency)

**Executives**:
- Structured interviews (goals)
- Business case review (ROI)
- Risk assessment (concerns)
- Success metrics workshop

## DOCUMENTATION TEMPLATES

### User Story Template

```markdown
**Title**: Submit Simple Auto Claim

**As a** policyholder who had a minor accident
**I want to** submit my claim online with photos
**So that** I can start the process immediately without calling

**Acceptance Criteria**:
- [ ] Can select claim type from dropdown
- [ ] Can describe incident in 500 characters
- [ ] Can upload up to 10 photos (50MB total)
- [ ] Receive confirmation with claim number
- [ ] Get estimated timeline for next steps

**Business Rules**:
- Only active policies can file claims
- Claims must be filed within 30 days
- Minimum 3 photos required for auto claims

**Technical Notes**:
- Integrate with Policy API for validation
- Store photos in secure S3 bucket
- Queue for adjuster assignment
```

### Functional Requirement Template

```markdown
**REQ-F-001**: Claim Submission

**Description**: System shall allow authenticated policyholders to submit new claims through web portal

**Rationale**: Enables 24/7 self-service reducing call center load

**Priority**: MUST HAVE

**Acceptance Criteria**:
1. User can access claim form after authentication
2. Form validates all required fields
3. System assigns unique claim number
4. Confirmation displayed and emailed
5. Claim appears in adjuster queue within 5 minutes

**Dependencies**: 
- REQ-T-001 (Authentication)
- REQ-I-001 (Core system integration)

**Assumptions**: 
- Users have active email
- Core system available 99.9%

**Test Scenarios**:
- Happy path: Complete valid claim
- Edge case: Network interruption
- Error case: Invalid policy number
```

### Non-Functional Requirement Template

```markdown
**REQ-NF-001**: Page Load Performance

**Category**: Performance

**Description**: All portal pages shall load within 3 seconds on 4G mobile connection

**Measurement**: 
- Tool: Google Lighthouse
- Target: Performance score >90
- Test conditions: Average 4G (10 Mbps)

**Rationale**: User research shows >3 seconds causes 40% abandonment

**Implementation Notes**:
- Use CDN for static assets
- Implement lazy loading
- Optimize images
- Cache API responses
```

## VALIDATION STRATEGY

### Requirements Review Process

**Level 1: Peer Review**
```
Reviewers: Business analyst team
Focus: Completeness, clarity, consistency
Method: Checklist review
Duration: 2 hours per module
```

**Level 2: Stakeholder Validation**
```
Customers:
├── Prototype walkthrough (10 users)
├── Usability testing
└── Feedback incorporation

Adjusters:
├── Process simulation
├── Efficiency calculation
└── Workflow approval

IT Team:
├── Technical feasibility
├── Integration assessment
└── Security review
```

**Level 3: Executive Approval**
```
Steering Committee Presentation:
├── Requirements summary
├── Risk assessment
├── Cost-benefit analysis
├── Implementation roadmap
└── Success metrics
```

### Validation Checklist

```markdown
□ Complete - All sections filled
□ Clear - Unambiguous language
□ Consistent - No conflicts
□ Testable - Measurable criteria
□ Feasible - Within constraints
□ Necessary - Adds value
□ Traceable - Linked to goals
□ Approved - Stakeholder sign-off
```

## TRACEABILITY MATRIX

### Requirements Mapping

```
Business Goal → Stakeholder Need → Feature → Requirement → Test Case

Example:
"Reduce processing time 40%" 
    → "Submit claims without calling"
        → "Online claim submission"
            → "REQ-F-001: Claim form"
                → "TC-001: Submit valid claim"
```

### Traceability Table Template

| ID | Requirement | Business Goal | Stakeholder | Priority | Status | Test Case |
|----|-------------|---------------|-------------|----------|---------|-----------|
| REQ-F-001 | Claim submission | Reduce time 40% | Customer | MUST | Approved | TC-001-010 |
| REQ-F-002 | Document upload | Reduce callbacks | Customer | MUST | In Review | TC-011-015 |
| REQ-NF-001 | 3-second load | Satisfaction 80% | Customer | MUST | Draft | TC-016-020 |

### Change Management

**Change Request Process**:
1. Submit impact analysis
2. Assess against project constraints
3. Stakeholder review
4. Approval/rejection
5. Update all artifacts
6. Communicate changes

### Implementation Roadmap

**Phase 1: Foundation (Months 1-2)**
- Core claim submission
- Basic authentication
- Document upload
- Status tracking

**Phase 2: Enhancement (Months 3-4)**
- Adjuster dashboard
- Automated validation
- Notifications
- Reporting

**Phase 3: Optimization (Months 5-6)**
- Performance tuning
- Usability improvements
- Advanced features
- Training rollout

### Success Metrics

**Launch + 30 days**:
- 10% claims online
- 95% system uptime
- <5% error rate

**Launch + 90 days**:
- 30% claims online
- 4-day average processing
- 75% satisfaction

**Launch + 180 days**:
- 50% claims online
- 3-day average processing
- 80% satisfaction

This comprehensive requirements approach addresses your previous failure points while ensuring all stakeholder needs are met within constraints.

## Related Prompts

- [Business Analysis Expert](../../problem-solving/performance-bottleneck-analysis-expert.md)
- [User Story Creator](../../analysis/user-behavior-analysis-expert.md)
- [Process Mapping Specialist](../operations/process-optimization-expert.md)
