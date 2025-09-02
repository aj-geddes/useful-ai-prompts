# Contingency Planning Expert

## Metadata
- **Created**: 2025-01-15

- **Category**: Planning
- **Tags**: contingency planning, business continuity, crisis management, disaster recovery, resilience planning
- **Version**: 2.0.0
- **Use Cases**: business continuity, disaster recovery, crisis response, emergency planning, operational resilience
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical contingency planning assistant that helps you prepare for disruptions and ensure business continuity. Provide your organization details and I'll create comprehensive contingency plans with response strategies, recovery procedures, and resilience measures.

## Prompt

```
I'll help you create a robust contingency plan to protect your organization from disruptions and ensure rapid recovery. Let me gather information about your needs.

About your organization:
1. What type of organization are you? (small business, enterprise, nonprofit, government)
2. What industry/sector are you in?
3. How many locations and employees do you have?
4. What are your most critical operations or services?

Risk assessment:
5. What threats are you most concerned about? (natural disasters, cyber attacks, supply chain, etc.)
6. Have you experienced any major disruptions before? What happened?
7. How much downtime can you tolerate? (hours, days, weeks)
8. What would be the impact of losing key systems or facilities?

Current preparedness:
9. Do you have any existing contingency plans or procedures?
10. What backup systems or redundancies are in place?
11. What's your budget for contingency planning?
12. Who would lead crisis response efforts?

Based on your answers, I'll develop:

**1. THREAT ASSESSMENT** - Comprehensive risk analysis and impact evaluation
**2. RESPONSE STRATEGIES** - Tiered response plans for different scenarios
**3. CONTINUITY PROCEDURES** - How to maintain critical operations
**4. RECOVERY PLANS** - Step-by-step restoration procedures
**5. TESTING FRAMEWORK** - How to validate and improve your plans

Please provide the information above, and I'll create a contingency plan tailored to your organization's needs and risks.
```

## Example Usage

**User Input:**
```
1. Organization: Mid-size manufacturing company
2. Industry: Automotive parts supplier
3. Locations: 2 facilities (main plant and warehouse), 350 employees
4. Critical operations: Production lines, customer order fulfillment, quality testing

5. Main threats: Equipment failure, supply chain disruption, cyber attacks, severe weather
6. Past disruptions: 3-day shutdown from equipment failure last year, lost $2M
7. Downtime tolerance: 24 hours max for production, 4 hours for order processing
8. Impact: Would lose $500K/day, risk losing major contracts

9. Existing plans: Basic fire evacuation plan, informal IT backup
10. Current redundancies: Some spare parts inventory, manual backup for some processes
11. Budget: $100K for improvements this year
12. Crisis lead: Operations Director with management team
```

**Assistant Output:**

Based on your automotive parts manufacturing operations, here's your comprehensive contingency plan:

# CONTINGENCY PLAN - AUTOPARTS MANUFACTURING

## 1. THREAT ASSESSMENT

### Risk Priority Matrix

**Critical Risks (High Impact, High Probability):**

**1. Equipment Failure**
- Probability → High (based on last year's incident)
- Impact: $500K/day production loss
- Current vulnerability → Limited spare parts, aging equipment
- Risk score: 9/10

**2. Supply Chain Disruption**
- Probability → Medium-High (global supply issues)
- Impact → Production stoppage within 5 days
- Current vulnerability → Single suppliers for key materials
- Risk score: 8/10

**3. Cyber Attack**
- Probability → Medium (increasing industry targeting)
- Impact → System shutdown, data loss, ransom
- Current vulnerability → Basic IT security only
- Risk score: 7/10

**4. Severe Weather**
- Probability → Medium (seasonal exposure)
- Impact → Facility damage, power loss, access issues
- Current vulnerability → No backup power at main plant
- Risk score: 6/10

### Business Impact Analysis

**Production Line Failure:**
- Revenue loss: $500K/day
- Customer impact → Late deliveries, contract penalties
- Recovery time: 24-72 hours depending on failure
- Cascading effects → Warehouse backup, quality delays

**IT System Failure:**
- Order processing stops: $200K/day impact
- Manufacturing disruption → Can run manually for 8 hours
- Data loss risk → Customer orders, quality records
- Recovery time: 4-24 hours

## 2. RESPONSE STRATEGIES

### Tiered Response Framework

**Level 1: Minor Disruption (Single system/area)**
- Trigger → Localized issue, <4 hour impact
- Response Lead → Department Manager
- Actions → Fix issue, notify Operations Director
- Communication → Internal only

**Level 2: Major Disruption (Multiple systems/departments)**
- Trigger: >4 hour impact or $100K+ loss
- Response Lead → Operations Director
- Team → Department heads, IT, HR
- Actions → Activate backup procedures
- Communication → Notify customers if delays expected

**Level 3: Crisis (Facility-wide or multi-day)**
- Trigger: >24 hour shutdown or $500K+ impact
- Response Lead → CEO/President
- Team → Full leadership + external support
- Actions → Full contingency activation
- Communication → All stakeholders, media if needed

### Scenario-Specific Response Plans

**Equipment Failure Response:**

*Immediate (0-2 hours):*
1. Assess failure scope and safety
2. Notify maintenance and Operations Director
3. Check spare parts availability
4. Begin repair or call service vendor

*Short-term (2-24 hours):*
1. Reroute production if possible
2. Notify affected customers of potential delays
3. Expedite parts delivery if needed
4. Consider overtime to catch up

*Extended (24+ hours):*
1. Activate overflow agreement with sister plant
2. Rent temporary equipment if available
3. Negotiate deadline extensions
4. Daily customer updates

**Cyber Attack Response:**

*Detection (0-1 hour):*
1. Isolate affected systems immediately
2. Activate IT response team
3. Document everything observed
4. Initiate manual backup procedures

*Containment (1-8 hours):*
1. Assess attack scope and type
2. Contact cyber insurance carrier
3. Engage forensics firm if needed
4. Notify law enforcement if criminal

*Recovery (8+ hours):*
1. Restore from clean backups
2. Patch vulnerabilities
3. Monitor for reinfection
4. Implement additional security

## 3. CONTINUITY PROCEDURES

### Critical Operations Maintenance

**Production Continuity:**

*Primary Strategy:*
- Cross-train operators on multiple lines
- Maintain 72-hour raw material buffer
- Pre-qualify overflow manufacturing partners
- Document all critical processes

*Backup Procedures:*
- Manual production capability for 8 hours
- Sister plant can handle 30% capacity
- Approved subcontractors list ready
- Customer priority matrix established

**Order Processing Continuity:**

*Primary Systems:*
- Cloud-based order system (new recommendation)
- Real-time backups every hour
- Redundant internet connections
- Mobile hotspot backup

*Manual Backup:*
- Printed order forms available
- Phone order procedures documented
- Priority customer list maintained
- Daily order logs printed

### Supply Chain Continuity

**Supplier Diversification Plan:**
1. Identify single-source materials (30 days)
2. Qualify alternate suppliers (60 days)
3. Establish backup agreements (90 days)
4. Maintain strategic inventory (ongoing)

**Inventory Strategy:**
- Critical parts: 2-week supply minimum
- High-value items → Just-in-time with backup
- Common items: 1-month buffer
- Review levels quarterly

## 4. RECOVERY PLANS

### Production Recovery Roadmap

**Phase 1: Assessment (0-4 hours)**
- Damage evaluation
- Resource inventory
- Timeline estimation
- Team assignments

**Phase 2: Stabilization (4-24 hours)**
- Safety securing
- Temporary fixes
- Critical operations restart
- Communication plan

**Phase 3: Restoration (1-7 days)**
- Full repairs initiated
- Normal operations resuming
- Backlog processing
- Performance monitoring

**Phase 4: Improvement (1-4 weeks)**
- Root cause analysis
- Process improvements
- Plan updates
- Training reinforcement

### IT System Recovery

**Recovery Priority Order:**
1. Network and communications (1 hour)
2. Order processing system (2 hours)
3. Production planning (4 hours)
4. Quality systems (8 hours)
5. Administrative systems (24 hours)

**Data Recovery Procedures:**
- Backup verification → Test monthly
- Recovery point objective: 1 hour max data loss
- Recovery time objective: 4 hours for critical systems
- Alternative processing → Manual procedures ready

## 5. TESTING FRAMEWORK

### Testing Schedule

**Monthly Tests:**
- Data backup restoration (IT systems)
- Emergency contact list verification
- Critical spare parts inventory check
- Generator/UPS testing (when installed)

**Quarterly Tests:**
- Department-level response drills
- Manual process exercises
- Supplier backup communication
- Customer notification procedures

**Annual Tests:**
- Full facility evacuation
- Complete system failover test
- Multi-scenario tabletop exercise
- Third-party plan review

### Performance Metrics

**Key Performance Indicators:**
- Response time to incidents
- Recovery time achievement
- Test exercise success rate
- Plan update frequency
- Training completion rate

**Success Criteria:**
- Level 1 response: <30 minutes
- Critical system recovery: <4 hours
- Full production recovery: <24 hours
- Zero safety incidents during crisis
- 95% customer satisfaction maintained

### Implementation Roadmap

**Next 30 Days:**
1. Establish crisis response team
2. Document critical procedures
3. Create emergency contact database
4. Begin cross-training program

**Next 60 Days:**
1. Install backup power (generator)
2. Implement cloud backup system
3. Qualify alternate suppliers
4. Conduct first response drill

**Next 90 Days:**
1. Complete all documentation
2. Train all key personnel
3. Execute full test exercise
4. Refine plans based on lessons

### Budget Allocation ($100K)

**Technology Improvements: $45K**
- Backup generator: $25K
- Cloud backup system: $15K
- Cybersecurity upgrades: $5K

**Inventory & Equipment: $30K**
- Critical spare parts: $20K
- Emergency supplies: $5K
- Communication equipment: $5K

**Training & Services: $20K**
- Staff training program: $10K
- Consulting/plan development: $7K
- Testing/drill costs: $3K

**Contingency Reserve: $5K**
- Emergency response costs
- Unexpected needs

### Quick Reference Guide

**Emergency Contacts:**
- Fire/Medical: 911
- Operations Director: [Name/Phone]
- IT Emergency: [24/7 number]
- Key Suppliers: [Contact list]
- Insurance: [Claim number]

**Immediate Actions Checklist:**
□ Ensure personnel safety
□ Assess incident scope
□ Activate response team
□ Begin documentation
□ Notify stakeholders
□ Initiate recovery procedures

This plan provides a solid foundation for protecting your operations. Start with the 30-day priorities and build from there.

## Related Prompts

- [Risk Management Planning Expert](risk-management-expert.md)
- [Crisis Management Expert](../problem-solving/crisis-management-expert.md)
- [Business Continuity Expert](../management-leadership/talent-management-expert.md)

## Usage Instructions

1. Begin with comprehensive threat assessment and business impact analysis
2. Develop tiered response strategies based on incident severity and scope
3. Create detailed contingency procedures for critical business functions
4. Implement robust testing and validation program with regular exercises
5. Build organizational resilience through training and cultural development
6. Establish financial preparedness with emergency funding and insurance
7. Create comprehensive communication plans for all stakeholder groups
8. Maintain continuous improvement through monitoring and plan updates

## Examples

### Example 1: Small Business Continuity Plan

**Input**:

```
{{organization_type}}: Small professional services firm
{{geographic_scope}}: Single office location
{{technology_dependence}}: High dependence on cloud services
{{resource_availability}}: Limited emergency resources
{{recovery_time_objectives}}: 24-48 hours for full operations
```

**Output**: [Streamlined business continuity plan focused on cloud resilience, remote work capability, client communication, and cost-effective recovery strategies]

### Example 2: Healthcare System Emergency Planning

**Input**:

```
{{organization_type}}: Regional healthcare system
{{regulatory_requirements}}: Heavy healthcare compliance requirements
{{stakeholder_complexity}}: Patients, families, staff, community, regulators
{{risk_profile}}: High risk with life safety implications
{{industry_sector}}: Healthcare with critical community services
```

**Output**: [Healthcare-specific contingency plan addressing patient safety, regulatory compliance, community coordination, and medical service continuity]

## Related Prompts

- [Risk Management Expert](/prompts/planning/risk-management.md)
- [Crisis Management Specialist](/prompts/problem-solving/crisis-management.md)
- [Business Continuity Planner](/prompts/planning/business-continuity.md)

## Research Notes

- Based on international standards (ISO 22301, NIST) and best practices
- Integrates business continuity with organizational resilience building
- Emphasizes all-hazards approach with scenario-specific planning
- Focuses on proactive preparation and rapid response capability
- Balances comprehensive planning with practical implementation and testing
