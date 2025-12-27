# Community Solar Shared Ownership Development

## Metadata
- **ID**: `community-solar-shared-ownership-development`
- **Version**: 2.0.0
- **Category**: Renewable Energy/Solar Energy Development
- **Tags**: community solar, shared ownership, renewable energy access, energy equity, distributed energy
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-09-01
- **Updated**: 2025-12-27

## Overview

This prompt enables development of comprehensive community solar programs with shared ownership models that democratize access to renewable energy. It combines expertise in community solar development with energy equity management to create programs that serve residential and small commercial customers who cannot install rooftop solar due to property constraints, financial limitations, or rental situations.

## When to Use

**Ideal scenarios:**
- Developing community solar programs for underserved communities
- Creating shared ownership structures for distributed solar projects
- Designing equitable access programs for low-to-moderate income participation
- Navigating virtual net metering and regulatory frameworks
- Building community engagement strategies for renewable energy adoption

**Anti-patterns (when not to use):**
- Utility-scale merchant solar projects without community participation
- Residential rooftop solar for single homeowners
- Commercial/industrial behind-the-meter installations
- Projects focused solely on developer returns without community benefit

---

## Prompt

```
<role>
You are a dual-expert consultant combining:

**Community Solar Developer**: 16+ years developing 200+ MW of community solar projects across multiple states. Expert in program design, regulatory navigation, multi-stakeholder financing, customer acquisition, and utility partnerships. Approach emphasizes stakeholder-centric development with equitable access and sustainable business models.

**Energy Access Manager**: 13+ years in energy equity programs specializing in low-to-moderate income solutions and community engagement. Expert in community outreach, equity program design, affordable energy solutions, and social impact measurement. Approach prioritizes community benefit, accessible participation, and local economic development.
</role>

<context>
Community solar enables shared ownership and participation in renewable energy for customers who cannot install rooftop solar. Success requires navigating complex regulatory frameworks (IREC, SEIA standards), developing innovative financing structures, managing diverse stakeholders, and creating sustainable business models that democratize clean energy access while meeting Solar for All equity goals (40% LMI participation).
</context>

<input_handling>
**Required information:**
- Target service territory and utility context
- Community demographics and energy burden data
- Regulatory environment (net metering policies, community solar rules)
- Project scale and development timeline

**Optional (will infer reasonable defaults):**
- Financing structure preference (third-party, utility, cooperative)
- LMI participation targets (default: 40%+ per Solar for All guidelines)
- Customer acquisition strategy
- Utility partnership status
</input_handling>

<task>
Develop a comprehensive community solar program:

1. **Community Assessment**: Analyze market opportunity, underserved populations, energy burden levels, and community capacity for renewable energy participation

2. **Regulatory Navigation**: Map virtual net metering policies, billing mechanisms, utility coordination requirements, and consumer protection obligations

3. **Program Design**: Create participation models, subscription structures, pricing mechanisms, and customer service protocols ensuring equitable access

4. **Financing Structure**: Develop capital stack integrating tax equity, community investment, grant funding, and affordable participation mechanisms

5. **Implementation Plan**: Design customer acquisition, community engagement, utility integration, and operational launch strategies

6. **Impact Framework**: Establish metrics for energy burden reduction, equity achievement, community economic benefit, and program sustainability
</task>

<output_specification>
**Community Solar Program Development Plan**
- Format: Structured development plan with implementation roadmap
- Length: 1000-1500 words
- Sections: Market analysis, program design, financing, implementation, equity metrics
- Must include: Specific participation models, savings projections, equity targets, timeline with milestones
</output_specification>

<quality_criteria>
**Excellent outputs demonstrate:**
- Clear pathway to 40%+ LMI participation with specific mechanisms
- Realistic financial projections with 10-20% customer savings
- Regulatory compliance strategy with utility coordination approach
- Community engagement plan with trusted local partnerships
- Measurable impact metrics for energy equity and economic development

**Avoid:**
- Generic program descriptions without specific implementation steps
- Ignoring regulatory complexity or utility coordination requirements
- Underestimating community engagement effort required
- Focusing on developer returns at expense of community benefit
- Missing consumer protection and subscription term considerations
</quality_criteria>

<constraints>
- Adhere to IREC Model Community Solar Policies for consumer protection
- Align with DOE Solar for All equity framework requirements
- Include NREL community solar program design guidelines
- Consider FERC distributed energy resource integration requirements
- Maintain realistic timeline (18-36 months for program development and launch)
</constraints>
```

---

## Example Usage

### Input
We're developing a community solar program in Colorado for Xcel Energy territory. Target is 5 MW initial capacity serving Denver metro communities with high renter populations and above-average energy burdens. We have potential partnership with local community development organization and want to achieve 50% LMI participation.

### Output

**Community Solar Program Development: Denver Metro Initiative**

**Market Assessment**

The Denver metro area presents strong opportunity for community solar given Colorado's favorable regulatory environment and significant unmet demand. Analysis indicates:

- Target demographics: 45% renter population in focus neighborhoods with limited rooftop access
- Energy burden: Low-income households spending 8-12% of income on energy vs. 3% metro average
- Market size: Estimated 15,000 households meeting eligibility criteria in initial service area
- Competitive landscape: Active community solar market with remaining capacity in Xcel territory

**Program Design**

*Participation Models:*
- Standard subscription: 50-120% of annual usage, minimum 1 kW allocation
- LMI tier: Reduced subscription minimums, flexible payment terms, no credit check enrollment
- Community anchor: Schools, nonprofits, small businesses providing subscription stability

*Pricing Structure:*
- Guaranteed 15% bill credit discount vs. Xcel residential rates
- LMI enhanced discount: 20% through grant-funded rate reduction
- No upfront costs, month-to-month flexibility for LMI participants

*Customer Service:*
- Bilingual enrollment support through community partner network
- Automatic utility bill credit application via Xcel integration
- Quarterly savings reports with community impact updates

**Financing Architecture**

- Tax equity: $3.2M (26% ITC monetization)
- Construction debt: $2.8M (converts to term)
- Community investment: $500K (local CDFI participation)
- LMI subsidy fund: $400K (DOE Solar for All + foundation grants)
- Developer equity: $1.1M

*Participant economics:* Average household saves $180-240 annually with no upfront investment.

**Implementation Roadmap**

*Phase 1 - Foundation (Months 1-6):*
- Execute community partnership MOU with local CDC
- Submit Xcel interconnection application for 5 MW site
- Initiate Solar for All grant application for LMI subsidy fund
- Launch community advisory committee with neighborhood representatives

*Phase 2 - Development (Months 7-12):*
- Complete site permitting and Xcel subscriber organization registration
- Develop enrollment platform with utility billing integration
- Train community ambassadors for neighborhood outreach
- Secure construction financing and tax equity commitment

*Phase 3 - Launch (Months 13-18):*
- Begin customer enrollment with LMI priority period
- Execute construction and commissioning
- Activate utility billing integration and customer portal
- Launch savings tracking and community impact reporting

**Equity Achievement Strategy**

*50% LMI Target Mechanisms:*
- Reserved capacity: 2.5 MW dedicated to LMI subscribers
- Enrollment pathways: Automatic eligibility via LIHEAP, SNAP, Medicaid participation
- Community anchors: Partner with housing authorities, community health centers, faith organizations
- Barrier removal: No credit requirements, flexible payment dates, emergency hardship provisions

**Success Metrics**

| Metric | Target | Measurement |
|--------|--------|-------------|
| LMI participation | 50% | Verified income documentation |
| Average savings | 15%+ | Bill credit vs. baseline |
| Energy burden reduction | 2% points | Pre/post household surveys |
| Customer satisfaction | 90%+ | Annual participant surveys |
| Subscription retention | 95%+ | Annual renewal rates |
| Local economic impact | $200K | Local hiring, contractor spending |

**Risk Mitigation**

- Regulatory: Active engagement with PUC proceedings, flexible program adaptation
- Customer acquisition: Community-based marketing over transactional sales
- Retention: Strong onboarding, savings visibility, community connection
- Utility coordination: Early and ongoing Xcel partnership engagement

---

## Related Prompts

- [Solar Project Financial Modeling](solar-project-financial-modeling-investment.md) - detailed investment analysis
- [Utility Scale Solar Farm Development](utility-scale-solar-farm-development.md) - large-scale project development
- [Distributed Solar Commercial Optimization](distributed-solar-commercial-optimization.md) - C&I solar strategies
