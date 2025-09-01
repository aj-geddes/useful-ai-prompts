# Support Escalation Process Expert

## Metadata
- **Category**: Customer-Focused/Support Operations
- **Created**: 2025-01-15
- **Version**: 1.0.0
- **Tags**: escalation-management, support-tiers, issue-resolution, incident-response
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description
Design efficient escalation processes that ensure critical customer issues are resolved quickly by the right experts. This prompt helps create clear escalation paths, criteria, and communication protocols.

## Prompt Template

```
I'll help you design an effective support escalation process. Let's understand your needs:

SUPPORT STRUCTURE:
- How many support tiers do you have?
- Team sizes and expertise levels?
- Current escalation challenges?

ISSUE TYPES:
- Common escalation triggers?
- Critical vs non-critical definitions?
- Technical vs non-technical splits?

BUSINESS IMPACT:
- Customer types (enterprise, SMB, consumer)?
- SLA requirements?
- Cost of escalations?

Here's your comprehensive escalation framework:

## 1. ESCALATION HIERARCHY
**Tier Definitions**:
| Tier | Expertise | Issue Types | Resolution Time | Escalation % |
|------|-----------|-------------|-----------------|---------------|
| Tier 1 | General support | Password, billing, basic | 1 hour | 20% escalate |
| Tier 2 | Technical support | Configuration, integrations | 4 hours | 10% escalate |
| Tier 3 | Senior engineers | Bugs, complex technical | 24 hours | 5% escalate |
| Tier 4 | Engineering/Product | Critical bugs, features | 48 hours | Rare |

**Expertise Matrix**:
- Product knowledge requirements
- Technical skill levels
- Customer communication abilities
- Decision-making authority

## 2. ESCALATION CRITERIA
**Automatic Triggers**:
```
IF customer_tier = "Enterprise" AND wait_time > 2 hours
THEN escalate_to_tier_2

IF issue_type = "Data Loss" OR "Security Breach"
THEN escalate_to_tier_3_immediately

IF customer_sentiment = "Extremely Negative" AND attempts > 3
THEN escalate_with_manager_notification
```

**Manual Escalation Guidelines**:
- Customer impact assessment
- Technical complexity evaluation
- Business risk factors
- Time sensitivity analysis

## 3. COMMUNICATION PROTOCOLS
**Internal Handoff Process**:
| Step | Action | Information Required | Tool/Template |
|------|--------|---------------------|---------------|
| 1 | Document issue | Full context, attempts, customer state | Ticket system |
| 2 | Tag and notify | Priority, category, next tier alert | Slack/system |
| 3 | Warm transfer | Brief next tier, stay available | Call/chat |
| 4 | Follow up | Confirm resolution ownership | Ticket update |

**Customer Communication**:
- Escalation acknowledgment template
- Expected timeline setting
- Progress update schedule
- Resolution confirmation

## 4. PRIORITY MANAGEMENT
**Severity Levels**:
| Level | Definition | Response Time | Escalation Path |
|-------|------------|---------------|-----------------|
| P1 | Service down, multiple users | 15 min | Direct to Tier 3 |
| P2 | Major feature broken | 2 hours | Tier 2 → 3 |
| P3 | Minor feature issue | 8 hours | Standard path |
| P4 | Enhancement request | 48 hours | Product team |

**Queue Management**:
- Priority weighting algorithm
- Resource allocation rules
- Overflow procedures
- Weekend/holiday coverage

## 5. QUALITY & IMPROVEMENT
**Escalation Metrics**:
- Volume by type and tier
- Resolution time by level
- Customer satisfaction post-escalation
- First-contact resolution impact

**Prevention Analysis**:
- Root cause tracking
- Knowledge base gaps
- Training needs identification
- Product improvement inputs

**Process Optimization**:
- Monthly escalation reviews
- Tier skill gap analysis
- Automation opportunities
- Feedback implementation
```

## Examples

### Example 1: SaaS Support Escalation
**Input**: "B2B software, 50 support agents in 3 tiers, increasing escalations causing delays"
**Output**: Redesigned criteria reducing unnecessary escalations by 35%, automated routing based on keywords and customer tier, specialist pools for common complex issues, manager dashboard for real-time monitoring.

### Example 2: E-commerce Customer Service
**Input**: "High-volume consumer support, seasonal spikes, need faster resolution for order issues"
**Output**: Dynamic escalation rules based on order value and time-sensitivity, express lanes for shipping issues, automated escalation for social media complaints, achieving 50% reduction in resolution time.

## Usage Instructions
1. Map current escalation patterns before redesigning
2. Define clear criteria that agents can easily follow
3. Build in automatic de-escalation when appropriate
4. Train all tiers on the complete process
5. Monitor and adjust thresholds based on data

## Related Prompts
- Customer Support Process Expert
- Service Design Expert
- Crisis Management Expert