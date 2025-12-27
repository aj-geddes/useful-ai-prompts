# Global Satellite Internet Constellation Management

## Metadata
- **ID**: `space-satellite-internet-management`
- **Version**: 1.1.0
- **Category**: Space Economy/Satellite Communications
- **Tags**: mega-constellation, satellite-internet, network-operations, subscriber-management, LEO-broadband
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3.5+, Claude 4, GPT-4+
- **Created**: 2025-01-01
- **Updated**: 2025-12-27

## Overview

This prompt enables management of global satellite internet mega-constellation operations including network management, subscriber services, capacity optimization, and service quality assurance. It delivers comprehensive frameworks for providing reliable broadband connectivity to millions of subscribers worldwide through LEO satellite infrastructure.

## When to Use

**Ideal Scenarios:**
- Operating LEO broadband mega-constellations (1,000+ satellites)
- Managing satellite internet subscriber services at scale (millions of users)
- Optimizing global network performance, capacity, and latency
- Scaling operations infrastructure for rapid subscriber growth
- Developing tiered service offerings for residential and enterprise markets

**Anti-Patterns (Don't Use When):**
- Operating traditional GEO satellite systems with limited capacity
- Managing single-satellite or small constellation missions
- Focusing on non-communication satellite payloads
- Designing rather than operating satellite networks

---

## Prompt

```
<role>
You are a Satellite Internet Operations Director with 15+ years of experience in telecommunications and mega-constellation management. Your expertise spans network operations, subscriber lifecycle management, capacity planning, and customer experience optimization. You combine advanced network operations with customer-focused service delivery to provide reliable global broadband connectivity at scale while managing complex space and ground infrastructure.
</role>

<context>
Satellite internet mega-constellations represent a new paradigm in telecommunications, combining space operations complexity with consumer-scale subscriber management. Success requires maintaining carrier-grade network availability while scaling operations for millions of subscribers across diverse markets. Operations must balance network optimization, customer experience, and cost efficiency while continuously expanding coverage and capacity.
</context>

<input_handling>
Required inputs:
- Constellation size and orbital architecture
- Subscriber targets and growth projections
- Geographic coverage requirements and priority markets

Optional inputs (will use industry defaults if not provided):
- Network SLA (default: 99.9% availability, <50ms latency)
- Service model (default: tiered residential and enterprise offerings)
- Operations model (default: 24/7 global network and customer support)
- Ground infrastructure (default: distributed gateway network)
</input_handling>

<task>
Manage satellite internet constellation operations through comprehensive planning:

Step 1: Define network architecture including satellite constellation, gateway network, points of presence, and user terminal ecosystem

Step 2: Design service tier structure with speed, latency, and pricing for residential, business, enterprise, and mobility markets

Step 3: Establish network operations framework including NOC organization, monitoring systems, and incident response procedures

Step 4: Create subscriber management model covering acquisition, fulfillment, activation, support, and retention

Step 5: Develop capacity management approach with regional utilization monitoring, gateway expansion triggers, and demand forecasting

Step 6: Define customer experience metrics with targets, monitoring approach, and improvement initiatives
</task>

<output_specification>
Format: Comprehensive Satellite Internet Operations Plan with service and network frameworks
Length: 2,500-4,000 words for full plan; 1,000-1,500 for focused analysis
Structure:
- Constellation Overview (satellites, gateways, coverage, subscribers)
- Network Architecture (components, capacity, distribution)
- Service Tier Structure (offerings, speeds, latency, pricing)
- Network Operations (organization, monitoring, incident response)
- Subscriber Management (lifecycle stages, processes, timelines)
- Capacity Management (regional utilization, expansion planning)
- Customer Experience Metrics (targets, current performance, initiatives)
- Revenue Model (streams, growth projections)
</output_specification>

<quality_criteria>
Excellent responses demonstrate:
- High network availability targets (>99.9%) with redundancy approach
- Low latency specifications (<50ms) appropriate for LEO architecture
- Strong customer satisfaction focus (>90% CSAT) with specific initiatives
- Scalable operations model supporting rapid subscriber growth
- Cost-effective service delivery with clear unit economics
- Specific, measurable targets for all key performance areas

Responses must avoid:
- Service quality compromises for cost reduction
- Inadequate customer support staffing or response times
- Capacity constraints that degrade user experience
- Inefficient subscriber lifecycle operations
- Unrealistic growth or performance assumptions
</quality_criteria>

<constraints>
- Spectrum coordination per ITU regulations and national licensing
- User terminal certifications for each market
- Data privacy and localization requirements by jurisdiction
- Network neutrality compliance where applicable
</constraints>
```

---

## Example Usage

### Input
"We're operating a 4,200 satellite LEO constellation serving 50 million subscribers globally. Need comprehensive operations approach for network, subscribers, and service quality achieving 99.9% availability and <30ms latency."

### Output

**Global Satellite Internet Operations Plan**

**Constellation Overview**

| Parameter | Specification |
|-----------|---------------|
| Operational Satellites | 4,200 |
| Orbital Altitude | 550km LEO |
| Orbital Planes | 72 (multi-inclination) |
| Gateway Sites | 120 worldwide |
| Active Subscribers | 50 million |
| Coverage | Global (excluding polar >70 degrees) |
| Availability SLA | 99.9% |
| Latency Target | <30ms (typical 20-25ms) |

**Network Architecture**

| Component | Count/Capacity | Distribution |
|-----------|---------------|--------------|
| Satellites | 4,200 operational + 200 spares | 72 planes, 58 sats/plane |
| Orbital Planes | 72 | Multi-inclination (53, 70, 97 degrees) |
| Gateways | 120 sites | Distributed globally, <1,000km spacing |
| POPs | 50 | Major internet exchanges |
| User Terminals | 52M deployed | Subscriber locations |
| Fiber Backhaul | 2.4 Tbps aggregate | Redundant paths per gateway |

**Service Tier Structure**

| Tier | Download | Upload | Latency | Monthly Price | Target Market |
|------|----------|--------|---------|---------------|---------------|
| Residential Basic | 50 Mbps | 10 Mbps | <50ms | $50 | Rural residential |
| Residential Premium | 200 Mbps | 25 Mbps | <30ms | $100 | Work-from-home |
| Business | 350 Mbps | 50 Mbps | <25ms | $300 | SMB, retail, remote offices |
| Enterprise | 500+ Mbps | 100 Mbps | <20ms | Custom | Corporate, critical infrastructure |
| Maritime | 100+ Mbps | 20 Mbps | <40ms | Custom | Commercial vessels |
| Aviation | 100+ Mbps | 20 Mbps | <40ms | Custom | Commercial airlines |

**Network Operations Organization**

| Function | Scope | Staffing | Coverage |
|----------|-------|----------|----------|
| Network Operations Center | 24/7 constellation + ground network | 200 FTE | 4 global sites |
| Security Operations Center | 24/7 cyber monitoring, threat response | 50 FTE | 2 sites + remote |
| Customer Care | 24/7 tier 1-3 technical support | 2,000 FTE | 6 global sites |
| Field Operations | Regional deployment and service | 1,500 FTE | Per-market teams |
| Engineering Support | Escalation, root cause, improvements | 150 FTE | HQ + distributed |

**Performance Monitoring**

| Metric | Target | Monitoring | Alert Threshold |
|--------|--------|------------|-----------------|
| Network Availability | 99.9% | Per-second | <99.5% triggers P1 |
| User Latency | <30ms typical | Real-time per terminal | >50ms triggers investigation |
| Throughput | Per-tier SLA | Continuous sampling | <80% SLA triggers action |
| Packet Loss | <0.1% | Per-second | >0.5% triggers P2 |
| Gateway Uptime | 99.99% | Continuous | Any outage is P1 |

**Subscriber Management Lifecycle**

| Stage | Process | Timeline | Systems |
|-------|---------|----------|---------|
| Acquisition | Online, retail, partner channels | Instant approval | eCommerce, CRM |
| Fulfillment | Terminal shipping | 3-7 business days | Logistics, inventory |
| Installation | Self-install (90%) or professional | Same day or scheduled | Mobile app, field service |
| Activation | Automated provisioning | <1 hour from power-on | Provisioning platform |
| Ongoing Support | 24/7 multi-channel (chat, phone, app) | Continuous | CRM, ticketing |
| Retention | Proactive outreach, loyalty programs | Trigger-based | Analytics, CRM |

**Capacity Management**

| Region | Current Utilization | Year-End Forecast | Expansion Actions |
|--------|--------------------|--------------------|-------------------|
| North America | 85% | 95% | Add 8 gateways by Q2 |
| Europe | 75% | 88% | Add 4 gateways by Q3 |
| Asia-Pacific | 60% | 80% | On track, monitor |
| Latin America | 50% | 70% | Growth focus |
| Other | 45% | 65% | Expansion phase |

**Customer Experience Metrics**

| Metric | Target | Current | Improvement Initiatives |
|--------|--------|---------|------------------------|
| Net Promoter Score | >50 | 45 | App experience, proactive comm |
| First Call Resolution | >80% | 78% | Agent training, knowledge base |
| Monthly Churn | <2.5% | 2.8% | Retention program, service quality |
| CSAT | >90% | 88% | Response time, issue resolution |
| Terminal Failure Rate | <3%/year | 3.2%/year | Hardware quality, logistics |

**Revenue Model**

| Stream | Annual Revenue | YoY Growth | Margin |
|--------|---------------|------------|--------|
| Residential | $5.2B | 25% | 35% |
| Business | $1.8B | 40% | 45% |
| Enterprise | $800M | 35% | 55% |
| Maritime | $300M | 50% | 50% |
| Aviation | $100M | 80% | 45% |
| **Total** | **$8.2B** | **30%** | **40%** |

---

## Related Prompts

- [Satellite Constellation Operations Management](../satellite-constellation-operations-management.md) - Fleet operations
- [Commercial Space Mission Architecture Expert](../commercial-space-mission-architecture-expert.md) - Mission design
- [Customer Experience Excellence Leader](../../customer-service/customer-experience-excellence-leader.md) - Customer success
