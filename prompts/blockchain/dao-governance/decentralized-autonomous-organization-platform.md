# Decentralized Autonomous Organization Platform

## Metadata
- **ID**: `blockchain-dao-governance-platform`
- **Version**: 1.0.0
- **Category**: Blockchain/DAO Governance
- **Tags**: DAO, governance, decentralized organization, community management, token voting
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3.5+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-01-15

## Overview

Designs and implements DAOs with governance frameworks, treasury management, and community coordination systems. Combines smart contract architecture with organizational design principles for effective decentralized governance at scale.

## When to Use

**Ideal Scenarios:**
- Creating new DAOs for protocols, communities, or investment groups
- Designing governance frameworks and voting mechanisms
- Building treasury management and fund allocation systems
- Planning token-based governance with participation incentives
- Structuring legal wrappers for DAO operations

**Anti-patterns (When NOT to Use):**
- Centralized organization management without decentralization need
- Traditional corporate governance structures
- Simple multi-signature wallets without governance
- Projects without genuine community participation

---

## Prompt

```xml
<role>
You are a DAO architect with 10+ years in organizational design and blockchain governance. You have designed governance systems for DAOs managing $1B+ in assets, with expertise in token economics, voting mechanisms, legal structures, and community coordination at scale.
</role>

<context>
The user needs to design or implement a DAO with effective governance, treasury management, and community participation. This requires balancing decentralization ideals with practical decision-making needs, designing appropriate voting mechanisms, protecting treasury assets, and creating sustainable participation incentives.
</context>

<input_handling>
Required inputs:
- DAO purpose (protocol governance, investment, community, charity)
- Member profile and expected community size
- Decision types and frequency

Optional inputs (inferred if not provided):
- Platform: OpenZeppelin Governor or Aragon based on complexity
- Voting mechanism: Token-weighted with delegation
- Treasury: Gnosis Safe with governance timelock
- Legal structure: LLC wrapper recommended for liability
</input_handling>

<task>
Design a comprehensive DAO governance system following these steps:

1. **Define Governance Structure**: Establish decision-making hierarchy, committees, and authority levels appropriate for the DAO purpose

2. **Design Voting Mechanisms**: Select voting method (token-weighted, quadratic, conviction) with anti-whale protections and participation incentives

3. **Create Treasury Framework**: Design multi-signature custody, spending authorities, and asset management policies

4. **Plan Member Experience**: Establish onboarding, participation incentives, delegation systems, and communication channels

5. **Establish Safety Mechanisms**: Define dispute resolution, emergency procedures, and guardian functions

6. **Address Legal Structure**: Recommend appropriate legal wrapper and compliance considerations
</task>

<output_specification>
Format: Organizational blueprint with technical specifications
Length: 600-900 words

Required sections:
- Governance structure with decision authority
- Voting mechanisms and participation design
- Treasury management and spending controls
- Member onboarding and incentives
- Emergency procedures and dispute resolution
- Legal structure recommendations

Structure: Use code blocks for governance parameters and treasury specifications
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- Balanced power distribution preventing capture
- Clear decision-making processes with reasonable timelines
- Robust treasury protection with appropriate controls
- Practical operational procedures for ongoing management

Common pitfalls to avoid:
- Over-centralized governance defeating DAO purpose
- Complex voting without clear benefit
- Unprotected treasury access or weak controls
- Ignoring legal and regulatory considerations
</quality_criteria>

<constraints>
- Design for the specific jurisdiction and regulatory environment
- Include appropriate checks and balances on all authorities
- Plan for governance evolution and upgrade paths
- Consider attack vectors (governance attacks, treasury drains)
- Address member privacy and compliance requirements
</constraints>
```

---

## Example Usage

### Input
Creating investment DAO for DeFi project funding. Members: 50-100 crypto investors, minimum $50K contribution. Decisions: investment allocation, exit strategies, fund operations. Want token-weighted voting but protection against whale dominance. Starting treasury: $5M. Need clear legal structure for US investors.

### Output

**DeFi Investment DAO Governance Design**

**Governance Structure**
```
Three-Tier Decision Architecture:

General Assembly (All Token Holders):
- Major decisions (>$500K investments)
- Constitutional changes
- Committee elections (annual)
- Annual strategy approval
- Quorum: 30% of tokens

Investment Committee (7 members):
- 4 elected by token vote
- 3 largest contributors (automatic seats)
- Due diligence and recommendations
- Fast-track investments (<$100K)
- Term: 1 year with re-election

Operations Team (3 compensated roles):
- Treasury Manager: Execution and custody
- Legal Counsel: Compliance oversight
- Community Lead: Member relations
- Compensation: Set by governance vote
```

**Voting Mechanism**
```
Token Distribution:
- Total Supply: 1,000,000 INVEST tokens
- Member allocation: 1 token per $100 contributed
- Treasury reserve: 300,000 tokens
- Team/advisor: 200,000 tokens (2-year vest)

Anti-Whale Protections:
- Quadratic voting for major decisions (reduces large holder power)
- Maximum vote weight: 5% of quorum regardless of holdings
- Delegation enabled with same caps
- Conviction voting for ongoing proposals

Voting Parameters:
- Quorum: 30% of circulating supply
- Majority: 60% for standard decisions
- Supermajority: 75% for constitutional changes
- Duration: 7 days standard, 3 days fast-track
- Timelock: 48 hours before execution

Delegation System:
- Any holder can delegate to another member
- Delegations are public (transparency)
- Self-delegation default
- Revocable at any time
```

**Treasury Management**
```
Multi-Sig Structure:
- Gnosis Safe: 4-of-7 signatures required
- Signers: 5 elected + 2 committee appointees
- Hardware wallet required for all signers
- Quarterly signer rotation

Asset Allocation Policy:
- Active investments: 60% ($3M max deployed)
- Liquid reserves: 25% ($1.25M in stables)
- Operating budget: 10% ($500K annual)
- Insurance fund: 5% ($250K)

Spending Authority Levels:
- <$10K: Operations team (2-of-3)
- $10K-$100K: Committee approval (4-of-7)
- $100K-$500K: Committee + 50% token vote
- >$500K: Full governance vote (60% approval)

Investment Process:
1. Sourcing: Any member can submit opportunity
2. Screening: Operations team (48h response)
3. Due diligence: Committee (2-week process)
4. Proposal: Standardized template to members
5. Vote: Based on investment size thresholds
6. Execution: Treasury manager implements
```

**Member Experience**
```
Onboarding Requirements:
- Minimum contribution: $50,000
- KYC/AML verification (required for US legal)
- Accredited investor status (SEC compliance)
- Governance agreement signature
- 30-day onboarding period

Participation Incentives:
- Voting rewards: 0.1% of treasury annually (distributed to voters)
- Active participation bonus: 1.5x for 80%+ vote participation
- Deal sourcing: 1% of profits on sourced investments
- Committee compensation: $2,000/month

Communication:
- Governance forum: Discourse-based discussion
- Real-time: Discord with role-based channels
- Updates: Weekly newsletter + monthly calls
- Voting: Snapshot for gas-free voting, on-chain execution
```

**Legal Structure**
```
Entity: Delaware Series LLC with DAO Addendum
- Operating agreement: Incorporates DAO governance
- Member rights: Defined by token holdings
- Liability: Limited to contribution
- Tax treatment: K-1 pass-through to members

Compliance Requirements:
- Accredited investor verification (506(c))
- AML/KYC for all members (US requirement)
- Quarterly financial reporting
- Annual audit (required above $10M AUM)
- SEC Form D filing

Regulatory Considerations:
- Investment Company Act exemption (3(c)(1) or 3(c)(7))
- Maximum 100 members for 3(c)(1) exemption
- No general solicitation without 506(c) compliance
- State blue sky filings as required
```

**Emergency Procedures**
```
Guardian Council (5-of-9 multi-sig):
- Pause all treasury operations
- Block suspicious transactions
- Emergency fund recovery (confirmed exploit)
- CANNOT modify governance rules
- CANNOT access funds for personal use

Trigger Conditions:
- Smart contract exploit detected
- >30% single-day portfolio loss
- Regulatory enforcement action
- Multi-sig key compromise

Recovery Process:
1. Guardian pause (immediate)
2. Community notification (within 1 hour)
3. Investigation (24-48 hours)
4. Governance vote on resolution
5. Execution with enhanced oversight
```

**Dispute Resolution**
```
Internal Process:
1. Community discussion (7 days)
2. Committee mediation (if needed)
3. Token holder vote (binding)

External Arbitration:
- Binding arbitration clause in member agreement
- JAMS arbitration for disputes >$50K
- Delaware courts for legal matters
- Legal reserve fund for proceedings
```

---

## Related Prompts

- [DeFi Protocol Development](../defi-protocols/decentralized-finance-protocol-development.md) - Building DeFi governance
- [Smart Contract Security](../smart-contracts/smart-contract-security-audit-platform.md) - Governance contract security
- [Token Economics Expert](../tokenization/real-world-asset-tokenization-platform.md) - Token design for governance
