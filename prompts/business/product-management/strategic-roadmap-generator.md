# Strategic Roadmap Generator

## Metadata
- **Created**: 2025-07-20

- **Category**: Business/Product-Management
- **Tags**: product roadmap, strategic planning, product strategy, roadmap development
- **Version**: 2.0.0
- **Use Cases**: product planning, roadmap creation, feature prioritization, strategic alignment
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you create strategic product roadmaps that balance customer needs, business objectives, and technical constraints while maintaining clear communication with stakeholders.

## Prompt

```
I'll help you create a strategic product roadmap that aligns with your business goals. Let me understand your context:

**Product overview:**
1. What product are you roadmapping?
2. What stage is it in? (early, growth, mature)
3. Who are your primary users/customers?
4. What's your competitive position?

**Strategic context:**
5. What are your key business objectives?
6. What metrics define success?
7. What's your time horizon? (quarterly, annual, multi-year)
8. Any major constraints? (resources, technology, market)

**Current situation:**
9. What are the biggest user pain points?
10. What opportunities are you seeing?
11. What technical debt or limitations exist?
12. How do you currently prioritize features?

Based on your answers, I'll provide:

**STRATEGIC THEMES** - High-level focus areas aligned with goals
**ROADMAP STRUCTURE** - Organized timeline with key deliverables
**PRIORITIZATION FRAMEWORK** - How to decide what to build when
**STAKEHOLDER VIEW** - Different roadmap versions for different audiences
**SUCCESS METRICS** - How to measure roadmap effectiveness

Share your product context and let's build a compelling roadmap!
```

## Example Usage

**User Input:**
```
1. B2B analytics platform for e-commerce companies
2. Growth stage - 2 years old, 200 customers, $5M ARR
3. Primary users: E-commerce analysts, marketing managers at mid-market retailers
4. #3 in market, competing against 2 larger players and several startups

5. Double ARR to $10M, expand to enterprise, reduce churn from 15% to 10%
6. Success: ARR growth, NPS >50, enterprise logos, feature adoption rates
7. Planning 12-month roadmap with quarterly releases
8. Limited engineering (8 devs), legacy codebase areas, GDPR compliance needed

9. Pain points: Slow report generation, limited customization, poor mobile experience
10. Opportunities: AI-powered insights, marketplace integrations, real-time analytics
11. Tech debt: Monolithic architecture, outdated UI framework, scaling issues >1M records
12. Currently using customer requests + revenue impact, but it's ad hoc
```

**Assistant Output:**

Here's your strategic product roadmap for the next 12 months:

## STRATEGIC THEMES

### Theme Architecture

```
North Star: "Become the Intelligence Layer for E-commerce Growth"

Q1: Foundation - "Performance & Reliability"
Q2: Expansion - "Integrate Everywhere"  
Q3: Intelligence - "AI-Powered Insights"
Q4: Enterprise - "Scale & Sophistication"
```

### Theme Rationale

**Q1 - Foundation First**:
- Can't grow with performance issues
- Reduces churn (addresses #1 complaint)
- Enables future features

**Q2 - Ecosystem Play**:
- Marketplace integrations = stickiness
- Competitive differentiator
- Enables richer analytics

**Q3 - AI Advantage**:
- Next-gen capabilities
- Premium pricing opportunity
- Enterprise appeal

**Q4 - Enterprise Ready**:
- Larger deals = faster ARR growth
- Security & compliance
- Advanced features

## ROADMAP STRUCTURE

### Q1: Performance & Reliability Sprint

**Major Deliverables**:

```
1. Report Generation Optimization (Weeks 1-4)
   - Current: 2-5 min for complex reports
   - Target: <30 seconds for 95% of reports
   - Approach: Caching, query optimization, CDN

2. Architecture Modernization Phase 1 (Weeks 5-8)
   - Extract reporting service
   - Implement job queue system
   - Database sharding prep

3. Mobile Experience MVP (Weeks 9-12)
   - Responsive dashboards
   - Key metrics on mobile
   - Push notifications
```

**Outcomes**:
- 70% faster report generation
- Mobile NPS from 20 → 45
- Churn reduction: 15% → 12%

### Q2: Integration Ecosystem

**Major Deliverables**:

```
1. Marketplace Integrations (Weeks 1-6)
   - Shopify Plus (must-have)
   - Amazon Seller Central
   - Google Analytics 4
   - Facebook Ads

2. Custom Fields & Filters (Weeks 7-9)
   - User-defined metrics
   - Saved filter sets
   - Custom dashboards

3. API v2 Launch (Weeks 10-12)
   - RESTful design
   - Webhook support
   - Rate limiting
```

**Outcomes**:
- 30% increase in data sources connected
- API adoption by 50+ customers
- Platform stickiness ↑40%

### Q3: AI-Powered Intelligence

**Major Deliverables**:

```
1. Anomaly Detection (Weeks 1-4)
   - Automatic alerts
   - Revenue anomalies
   - Traffic pattern changes

2. Predictive Analytics Beta (Weeks 5-8)
   - Sales forecasting
   - Inventory predictions
   - Customer LTV modeling

3. Insights Engine (Weeks 9-12)
   - Natural language queries
   - Auto-generated insights
   - Competitive benchmarking
```

**Outcomes**:
- New premium tier at 2x price
- 25% of customers upgrade
- Win first 5 enterprise deals

### Q4: Enterprise Scale

**Major Deliverables**:

```
1. Enterprise Security Suite (Weeks 1-6)
   - SSO/SAML support
   - Role-based access control
   - Audit logging
   - GDPR compliance

2. White-Label Options (Weeks 7-9)
   - Custom branding
   - Embedded analytics
   - Multi-tenant architecture

3. Advanced Analytics (Weeks 10-12)
   - Cohort analysis
   - Attribution modeling
   - A/B test analysis
```

**Outcomes**:
- 10+ enterprise customers
- ARR: $8M → $10M trajectory
- NPS: 45 → 55

## PRIORITIZATION FRAMEWORK

### RICE Scoring Model

```
Reach × Impact × Confidence / Effort = Priority Score

Reach: # of customers affected (1-10)
Impact: Revenue/retention impact (1-10)
Confidence: Success probability (0.1-1.0)
Effort: Developer weeks (1-50)
```

### Feature Evaluation Matrix

| Feature | Reach | Impact | Confidence | Effort | Score | Quarter |
|---------|-------|---------|------------|---------|--------|---------|
| Report Speed | 10 | 9 | 0.9 | 8 | 10.1 | Q1 |
| Mobile App | 7 | 7 | 0.8 | 12 | 3.3 | Q1 |
| Shopify Integration | 8 | 8 | 0.9 | 6 | 9.6 | Q2 |
| AI Insights | 6 | 10 | 0.7 | 20 | 2.1 | Q3 |
| SSO Support | 4 | 9 | 0.9 | 4 | 8.1 | Q4 |

### Decision Criteria

**Must Have**:
- Addresses top 3 customer complaints
- Supports ARR growth goals
- Technically feasible with current team

**Should Have**:
- Competitive differentiation
- Platform extensibility
- Technical debt reduction

**Nice to Have**:
- Experimental features
- Minor UX improvements
- Internal tools

## STAKEHOLDER VIEW

### Executive Roadmap (Board/Leadership)

```
2024 Product Strategy

Q1: Stabilize - Fix performance, reduce churn
Q2: Expand - Ecosystem integrations  
Q3: Innovate - AI capabilities
Q4: Enterprise - Security & scale

Key Metrics:
- Churn: 15% → 10%
- ARR: $5M → $10M
- Enterprise Customers: 0 → 10
- NPS: 35 → 55
```

### Customer Roadmap (Public)

```
Coming Soon:

✓ Next Month:
  • 5x faster reports
  • Mobile dashboards

✓ Spring 2024:
  • Shopify integration
  • Custom metrics
  • New API

✓ Summer 2024:
  • AI-powered insights
  • Anomaly detection
  • Predictive analytics

✓ Fall 2024:
  • Enterprise security
  • Advanced analytics
  • White-label options
```

### Engineering Roadmap (Internal)

```
Technical Priorities:

Q1: Architecture
- Service extraction
- Database optimization  
- Mobile web framework

Q2: Integrations
- API v2 design
- Webhook infrastructure
- OAuth implementations

Q3: ML Pipeline
- Data pipeline upgrade
- Model training infrastructure
- Real-time processing

Q4: Enterprise
- Multi-tenancy
- Security hardening
- Compliance framework
```

## SUCCESS METRICS

### Roadmap KPIs

**Delivery Metrics**:
```
On-Time Delivery: >80%
Scope Creep: <20%
Quality (bugs): <5 critical/quarter
Team Velocity: 20% improvement
```

**Business Impact**:
```
                Q1    Q2    Q3    Q4
ARR ($M)        5.5   6.5   8.0   10.0
Churn %         12%   11%   10%   10%
NPS             40    45    50    55
Enterprise      0     2     5     10
```

### Feature Adoption Tracking

**Success Criteria by Feature**:
- Report Speed: 90% use new engine
- Mobile: 40% MAU on mobile
- Integrations: 2+ per customer
- AI Insights: 60% engagement
- Enterprise: 10 logos signed

### Quarterly Reviews

**Roadmap Retrospective**:
1. What shipped vs. planned?
2. Which bets paid off?
3. What did we learn?
4. How should we adjust?

**Adjustment Triggers**:
- Competitor launches major feature
- Customer feedback pattern emerges
- Technical discovery changes scope
- Market conditions shift

### Communication Cadence

**Internal**:
- Weekly: Engineering standups
- Bi-weekly: Stakeholder updates
- Monthly: Customer advisory board
- Quarterly: Board review

**External**:
- Monthly: Product updates blog
- Quarterly: Roadmap refresh
- Annual: Vision presentation

This roadmap balances fixing current issues while building toward your growth goals. The key is maintaining flexibility while staying focused on the strategic themes.

## Related Prompts

- [Product Strategy Expert](../../communication/email-communication-strategy-expert.md)
- [Feature Prioritization Specialist](../../decision-making/feature-prioritization-expert.md)
- [Product Metrics Analyst](../../creation/product-design-expert.md)
