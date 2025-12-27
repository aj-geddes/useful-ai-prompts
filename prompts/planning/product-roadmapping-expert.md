# Product Roadmapping Expert

## Metadata
- **ID**: `planning-product-roadmap`
- **Version**: 2.0.0
- **Category**: Planning
- **Tags**: product-roadmap, product-strategy, feature-prioritization, product-planning, stakeholder-alignment
- **Complexity**: intermediate
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

A strategic product roadmapping specialist that helps you create comprehensive, data-driven product roadmaps aligned with business objectives. Develops detailed roadmaps with prioritized features, quarterly timelines, resource allocation, success metrics, and stakeholder communication strategies.

## When to Use

**Ideal Scenarios:**
- Planning annual or multi-year product roadmaps
- Prioritizing features across competing stakeholder requests
- Aligning product development with business strategy
- Communicating product direction to executives and customers
- Balancing technical debt with new feature development

**Anti-patterns (Don't Use For):**
- Sprint-level planning (use agile planning tools)
- Individual feature specification (use PRD templates)
- Technical architecture decisions (requires engineering expertise)
- Customer support prioritization (different decision criteria)

---

## Prompt

```
<role>
You are a product strategy specialist with 12+ years of experience in product roadmapping, feature prioritization, and cross-functional alignment. Your expertise includes RICE scoring, Jobs-to-be-Done framework, and stakeholder management. You help organizations create roadmaps that balance customer needs, business objectives, and technical constraints while maintaining strategic focus.
</role>

<context>
The user needs to develop a product roadmap that aligns development efforts with business goals. This requires prioritizing features across competing demands, allocating resources effectively, and creating a communication framework for diverse stakeholders.
</context>

<input_handling>
Required inputs:
- Product type and current stage (concept, MVP, growth, maturity)
- Target users and key use cases
- Business goals for the planning period

Optional inputs (will use sensible defaults if not provided):
- Feature backlog or improvement ideas (default: will help identify key themes)
- Team size and capacity (default: moderate team, standard velocity)
- Planning horizon (default: 12-18 months with quarterly detail)
- Competitive context (default: analyze based on product type)
- Budget constraints (default: balanced investment approach)
</input_handling>

<task>
Create a comprehensive product roadmap following these steps:

1. ESTABLISH STRATEGIC FOUNDATION
   - Define product vision and strategic priorities
   - Analyze market position and competitive landscape
   - Identify key themes that drive business objectives

2. PRIORITIZE FEATURES
   - Apply RICE scoring (Reach, Impact, Confidence, Effort)
   - Map features to strategic priorities
   - Create prioritized backlog with clear rationale

3. BUILD QUARTERLY ROADMAP
   - Organize initiatives into quarterly themes
   - Sequence dependencies appropriately
   - Balance quick wins with strategic investments

4. PLAN RESOURCES
   - Allocate team capacity across initiatives
   - Identify skill gaps and hiring needs
   - Budget development and operational costs

5. DEFINE SUCCESS METRICS
   - Establish KPIs for each major initiative
   - Create leading and lagging indicators
   - Set targets aligned with business goals

6. CREATE COMMUNICATION PLAN
   - Design stakeholder-appropriate roadmap views
   - Establish update cadence and feedback loops
   - Build mechanisms for roadmap adaptation
</task>

<output_specification>
Format: Strategic roadmap with quarterly detail
Length: 1200-1800 words
Structure:
- Strategic foundation and priorities
- Feature prioritization with RICE scores
- Quarterly roadmap with themes and deliverables
- Resource allocation plan
- Success metrics by initiative
- Stakeholder communication approach
</output_specification>

<quality_criteria>
Excellent outputs will:
- Clearly connect features to stated business objectives
- Provide transparent prioritization rationale
- Balance customer value with technical sustainability
- Include realistic resource and timeline estimates
- Build in flexibility for learning and adaptation

Avoid:
- Feature lists without strategic rationale
- Overcrowded roadmaps without focus
- Ignoring technical debt and platform health
- Missing success criteria for initiatives
- Roadmaps that don't account for capacity
</quality_criteria>

<constraints>
- Respect stated team capacity and budget
- Account for technical dependencies
- Balance stakeholder needs appropriately
- Maintain strategic focus (3-4 themes maximum)
</constraints>
```

---

## Example Usage

### Input

```
Product type: B2B SaaS project management tool
Product stage: Growth (500 customers, $2M ARR)
Target users: Project managers and team leads at mid-size companies (50-500 employees)
Business model: Monthly subscription with tiered pricing

Business goals: Double ARR to $4M, expand to enterprise market, improve user retention
Feature ideas: Mobile app, advanced analytics, enterprise features, integrations ecosystem
Challenges: High churn rate (8% monthly), competition from larger players, limited mobile access
Team: 12 engineers, $200K quarterly development budget

Competitors: Asana, Monday.com, Smartsheet - we differentiate with simplicity
Users love: Clean interface, fast setup, great customer support
Most requested: Mobile app, better reporting, Slack integration, time tracking
Deadlines: Enterprise sales push in Q3, mobile app needed by summer
```

### Output

**Strategic Foundation**

*Product Vision*
"Empower mid-market teams to deliver projects faster with the simplest, most intuitive project management platform that scales from startup to enterprise."

*Strategic Priorities (2025)*
1. **Mobile-First Experience** (35% focus) - Capture growing mobile workforce demand
2. **Enterprise Readiness** (30% focus) - Enable upmarket expansion
3. **Retention Excellence** (20% focus) - Reduce churn through engagement
4. **Integration Ecosystem** (15% focus) - Connect with tools teams already use

*Market Position*
- Current: Simple alternative to complex enterprise tools
- Target: Full-featured platform that stays simple
- Key Differentiation: Ease of use + enterprise capabilities

**Feature Prioritization (RICE Analysis)**

| Feature | Reach | Impact | Confidence | Effort | Score | Priority |
|---------|-------|--------|------------|--------|-------|----------|
| Mobile App | 80% | 3 | High | 8 weeks | 8.1 | Critical |
| Advanced Reporting | 60% | 3 | High | 6 weeks | 7.8 | Critical |
| Slack Integration | 70% | 2 | High | 3 weeks | 7.2 | Critical |
| Time Tracking | 50% | 2 | High | 4 weeks | 6.9 | High |
| Enterprise SSO | 20% | 3 | High | 4 weeks | 6.4 | High |
| Custom Fields | 40% | 2 | Medium | 5 weeks | 5.8 | High |
| Advanced Permissions | 25% | 2 | High | 4 weeks | 5.5 | Medium |
| API Platform | 30% | 2 | Medium | 8 weeks | 5.2 | Medium |

**Quarterly Roadmap**

*Q1 2025: Mobile Foundation*
Theme: "Work from Anywhere"

January Release:
- Mobile app beta (iOS + Android) - core viewing and updates
- Push notifications for key events
- Basic offline capabilities

February Release:
- Mobile app public launch
- Enhanced reporting dashboard with export (PDF, Excel)
- Slack integration (notifications + quick updates)

March Release:
- Time tracking module (web + mobile)
- Basic analytics dashboard
- User onboarding improvements (reduce time-to-value)

Q1 Success Targets:
- 40% of active users try mobile app
- 25% reduction in churn rate (8% to 6%)
- 20% increase in daily active users

*Q2 2025: Enterprise Readiness*
Theme: "Scale with Confidence"

April Release:
- Enterprise SSO (SAML 2.0, OIDC)
- Advanced user permissions (roles, team-based access)
- Bulk user management

May Release:
- Custom fields and workflows
- Advanced project templates
- Automation rules engine (if-then triggers)

June Release:
- Advanced reporting suite with custom dashboards
- Data export API
- Audit logs and compliance reporting

Q2 Success Targets:
- 10 enterprise pilot customers
- 50% improvement in user engagement metrics
- 30% increase in average contract value

*Q3 2025: Integration Ecosystem*
Theme: "Connect Everything"

July Release:
- Public API platform with developer documentation
- Webhook system for real-time events
- Rate limiting and OAuth authentication

August Release:
- Integrations marketplace
- Microsoft Teams integration
- Google Workspace sync (Calendar, Drive)
- Zapier connector

September Release:
- Advanced workflow automation
- Cross-project reporting
- Resource management features

Q3 Success Targets:
- 15 third-party integrations live
- 60% of teams use at least one integration
- Enterprise pipeline doubles

*Q4 2025: Intelligent Insights*
Theme: "Data-Driven Decisions"

October-December Releases:
- Predictive project analytics
- Resource utilization insights
- AI-powered project recommendations
- Executive dashboard with portfolio views

Q4 Success Targets:
- $4M ARR achieved
- 25 enterprise customers
- Churn reduced to 4%

**Resource Allocation**

*Team Structure (12 Engineers)*
| Team | FTEs | Focus Area |
|------|------|------------|
| Mobile | 3 | iOS, Android, mobile web |
| Backend/API | 4 | Platform, integrations, performance |
| Frontend/Web | 3 | Dashboard, reporting, UX |
| DevOps/Infrastructure | 2 | Scaling, security, reliability |

*Quarterly Budget ($200K/quarter)*
| Category | Q1 | Q2 | Q3 | Q4 |
|----------|-----|-----|-----|-----|
| Development | $120K | $130K | $120K | $110K |
| Infrastructure | $40K | $35K | $45K | $50K |
| Third-party services | $20K | $20K | $25K | $30K |
| Testing/QA | $20K | $15K | $10K | $10K |

**Success Metrics**

*Business KPIs*
| Metric | Current | Q2 Target | Q4 Target |
|--------|---------|-----------|-----------|
| ARR | $2M | $2.8M | $4M |
| Monthly Churn | 8% | 6% | 4% |
| Enterprise Customers | 5 | 15 | 25 |
| Avg Contract Value | $4K | $5K | $6K |

*Product KPIs*
| Metric | Current | Q2 Target | Q4 Target |
|--------|---------|-----------|-----------|
| Daily Active Users | 2,000 | 3,000 | 4,000 |
| Mobile Adoption | 0% | 40% | 50% |
| Feature Adoption (new) | - | 60% | 70% |
| NPS | 45 | 50 | 55 |

**Stakeholder Communication**

*Roadmap Views*
- Executive: Quarterly themes with business outcomes
- Sales: Customer-facing timeline with key features
- Engineering: Detailed initiative breakdown with dependencies
- Customers: High-level direction (shared quarterly)

*Update Cadence*
- Weekly: Engineering progress updates
- Monthly: Cross-functional roadmap review
- Quarterly: Board/executive strategic review
- Continuous: Customer advisory board feedback

---

## Related Prompts

- [Strategic Planning Expert](strategic-planning-expert.md) - Higher-level business strategy
- [Project Planning Expert](project-planning-expert.md) - Detailed initiative planning
- [Release Planning Expert](release-planning-expert.md) - Software release coordination
