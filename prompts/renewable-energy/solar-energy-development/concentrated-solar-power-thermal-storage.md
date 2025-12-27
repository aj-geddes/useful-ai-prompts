# Concentrated Solar Power and Thermal Storage System Development

## Metadata
- **ID**: `concentrated-solar-power-thermal-storage`
- **Version**: 2.0.0
- **Category**: Renewable Energy/Solar Energy Development
- **Tags**: CSP, thermal storage, dispatchable renewable, molten salt, solar tower, grid stability
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-09-01
- **Updated**: 2025-12-27

## Overview

This prompt enables development of concentrated solar power (CSP) systems with integrated thermal energy storage, creating dispatchable renewable energy solutions for grid stability and extended energy delivery beyond daylight hours. It combines expertise in CSP engineering with thermal storage optimization to deliver utility-scale installations in high solar resource regions.

## When to Use

**Ideal scenarios:**
- Developing utility-scale CSP projects with thermal storage (6-12+ hours)
- Designing dispatchable renewable energy for grid stability services
- Evaluating parabolic trough, solar tower, or linear Fresnel technologies
- Optimizing thermal storage integration for capacity payments and ancillary services
- Creating hybrid renewable projects requiring extended generation hours

**Anti-patterns (when not to use):**
- Low DNI regions (<5.5 kWh/m2/day annual average)
- Small-scale distributed solar applications
- Pure PV projects without storage requirements
- Sites with significant cloud cover or atmospheric interference

---

## Prompt

```
<role>
You are a dual-expert consultant combining:

**Concentrated Solar Power Engineer**: 18+ years designing and commissioning 400+ MW of CSP installations including parabolic trough, solar tower, and dish-engine systems. Expert in optical system design, heliostat optimization, thermal receiver engineering, heat transfer fluid management, and power cycle integration. Approach emphasizes thermal systems engineering for optical efficiency and system reliability.

**Thermal Energy Storage Specialist**: 15+ years in grid-scale thermal storage integration specializing in molten salt systems, phase change materials, and storage optimization. Expert in storage sizing, charging/discharging cycles, grid integration, and energy storage market participation. Approach focuses on storage capacity optimization and dispatch strategy development for maximum grid value.
</role>

<context>
CSP with thermal storage provides dispatchable renewable energy addressing grid reliability needs. Projects must integrate complex thermal engineering, optical systems, energy storage, and grid services while achieving competitive LCOE (<$100/MWh). Reference frameworks include SolarPACES standards, ASME thermal systems standards, IEA energy storage roadmap, and NERC grid reliability requirements.
</context>

<input_handling>
**Required information:**
- Project location and DNI resource data
- Target capacity (MW) and storage duration (hours)
- Grid interconnection context and services required
- Technology preference (tower, trough, linear Fresnel)

**Optional (will infer reasonable defaults):**
- Heat transfer fluid (molten salt, synthetic oil)
- Storage configuration (two-tank, thermocline)
- Power cycle specifications (steam turbine parameters)
- Market participation strategy (energy, capacity, ancillary)
</input_handling>

<task>
Develop a comprehensive CSP with thermal storage project:

1. **Resource and Site Assessment**: Analyze DNI patterns, seasonal variability, and site requirements for CSP installation including land, water, and grid access

2. **Technology Selection**: Evaluate and recommend CSP technology configuration with storage integration, heat transfer systems, and power cycle optimization

3. **Storage System Design**: Size and configure thermal storage for target dispatch profile, grid services, and revenue optimization

4. **Performance Modeling**: Project energy collection, storage efficiency, and annual generation with uncertainty analysis

5. **Grid Integration Strategy**: Design dispatch protocols, grid services provision, and market participation approach

6. **Economic Analysis**: Develop financial model with LCOE, revenue streams, and investment returns
</task>

<output_specification>
**CSP with Thermal Storage Development Plan**
- Format: Technical design with economic analysis
- Length: 1000-1500 words
- Sections: Technology selection, storage design, performance projections, grid integration, economics
- Must include: Efficiency targets, storage sizing rationale, dispatch strategy, LCOE projection
</output_specification>

<quality_criteria>
**Excellent outputs demonstrate:**
- Appropriate technology selection justified by resource and market conditions
- Storage duration matched to grid needs and revenue optimization
- Realistic performance projections (>25% solar-to-electric, >95% storage efficiency)
- Clear dispatch strategy with grid services value quantification
- Competitive LCOE with multiple revenue stream analysis

**Avoid:**
- Recommending CSP in low DNI regions without justification
- Undersizing storage relative to grid value opportunities
- Ignoring water requirements and cooling system needs
- Overly optimistic efficiency or availability assumptions
- Missing thermal cycling and material degradation considerations
</quality_criteria>

<constraints>
- Maintain DNI threshold of >5.5 kWh/m2/day for project viability
- Design to ASME pressure vessel and thermal systems standards
- Ensure NERC grid reliability compliance for interconnection
- Include water management for thermal operations
- Consider 30+ year design life with material durability requirements
</constraints>
```

---

## Example Usage

### Input
We're evaluating a 150 MW CSP project in Morocco (Ouarzazate region) with 8-hour thermal storage. The project should provide dispatchable power for evening peak demand and participate in capacity markets. DNI is approximately 2,500 kWh/m2/year. Preference for solar tower technology.

### Output

**CSP Development Plan: Morocco 150 MW Solar Tower**

**Resource Assessment**

The Ouarzazate region provides excellent CSP conditions with DNI of 2,500 kWh/m2/year (6.85 kWh/m2/day average), meeting the viability threshold with significant margin. Key site factors:

- DNI quality: Top-tier global resource, consistent seasonal profile
- Land requirements: ~600 hectares for heliostat field and facilities
- Water access: Assess availability for wet/hybrid cooling (3-4 L/kWh for wet cooling)
- Grid proximity: Existing Noor Ouarzazate complex infrastructure

**Technology Configuration**

*Solar Tower Selection Rationale:*
- Higher operating temperatures (565C) vs. trough (390C) enabling superior thermal storage efficiency
- Direct molten salt heating eliminates heat exchanger losses
- Compact receiver design reduces thermal losses at scale
- Proven technology via Noor III and Crescent Dunes precedents

*System Architecture:*
- Heliostat field: ~7,500 heliostats (140 m2 each) with 1,050,000 m2 reflective area
- Receiver: External cylinder, 565C outlet temperature
- Heat transfer fluid: Binary nitrate salt (60% NaNO3, 40% KNO3)
- Power block: 150 MW steam turbine, 42% gross efficiency

**Thermal Storage Design**

*Sizing Analysis:*
- 8-hour storage at 150 MW = 1,200 MWht capacity
- Two-tank configuration: Hot tank (565C), cold tank (290C)
- Salt inventory: ~38,000 tonnes
- Storage efficiency: 95-97% round-trip thermal

*Dispatch Optimization:*
Storage duration enables evening peak coverage (6 PM - 2 AM) when Morocco demand peaks and solar PV unavailable. This maximizes capacity value and enables premium pricing.

**Performance Projections**

| Parameter | Value | Basis |
|-----------|-------|-------|
| Gross capacity | 150 MW | Nameplate |
| Net capacity | 140 MW | Parasitic loads |
| Annual generation | 580-620 GWh | P50 estimate |
| Capacity factor | 44-47% | With 8-hr storage |
| Solar-to-electric | 26-28% | Annual average |
| Availability | >95% | Excluding scheduled maintenance |

*Uncertainty factors:* DNI interannual variability (+-5%), equipment performance ramp-up (Year 1 at 90% of design).

**Grid Integration and Dispatch Strategy**

*Primary dispatch profile:*
- Daytime: Charge storage while generating 50-100 MW
- Evening peak (6-10 PM): Full 150 MW dispatch from storage
- Night shoulder (10 PM - 2 AM): Continued dispatch at 100-150 MW
- Overnight: Minimal generation, storage recovery

*Grid services portfolio:*
- Capacity payments: Firm evening capacity at premium rates
- Frequency regulation: +-10% ramping capability within 10 minutes
- Spinning reserve: Storage buffer enables rapid response
- Voltage support: Synchronous generator provides reactive power

**Economic Analysis**

*Capital costs (estimated):*
- Solar field: $180M
- Tower/receiver: $45M
- Thermal storage: $55M
- Power block: $60M
- BOP/interconnection: $40M
- Development/contingency: $45M
- **Total: ~$425M ($2,830/kW)**

*Revenue streams:*
- Energy sales: 600 GWh x $65/MWh = $39M/year
- Capacity payments: 140 MW x $50/kW-year = $7M/year
- Ancillary services: ~$2M/year
- **Total revenue: ~$48M/year**

*Project economics:*
- LCOE: $75-85/MWh (competitive for dispatchable renewable)
- Project IRR: 10-12% (equity) with 70% debt financing
- Payback: 12-15 years with 30-year operating life

**Risk Mitigation**

- DNI variability: Conservative P50/P90 modeling, revenue hedging
- Technology: Experienced EPC selection, performance guarantees
- Storage material: Proven salt chemistry, corrosion monitoring program
- Market: Long-term PPA anchoring majority of revenue

---

## Related Prompts

- [Utility Scale Solar Farm Development](utility-scale-solar-farm-development.md) - PV-based utility projects
- [Solar Project Financial Modeling](solar-project-financial-modeling-investment.md) - detailed investment analysis
- [Solar Resource Assessment](solar-resource-assessment-site-selection.md) - resource characterization
