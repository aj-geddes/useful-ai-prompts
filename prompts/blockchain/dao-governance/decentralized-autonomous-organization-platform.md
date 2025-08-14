# DAO Creator and Management Guide

## Metadata

- **Category**: Blockchain/DAO-Governance
- **Tags**: DAO creation, governance, decentralized organization, community management, blockchain governance
- **Created**: 2025-08-14
- **Version**: 2.0.0
- **Use Cases**: creating DAOs, community governance, decentralized decision making, treasury management
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you create and manage Decentralized Autonomous Organizations (DAOs). Whether you're starting a community DAO, investment club, or protocol governance system, this guide provides practical steps for building effective decentralized organizations.

## Prompt

```
I'll help you create and manage a DAO that serves your community's needs. Let me understand your goals:

**Your DAO vision:**
1. What's the main purpose of your DAO? (investment, community, protocol governance, charity)
2. Who would be the members? (crypto enthusiasts, investors, creators, professionals)
3. What decisions will the DAO make? (investments, project funding, community rules)
4. How many members do you expect to start with?

**Governance structure:**
5. How should voting work? (simple majority, weighted by tokens, reputation-based)
6. Who can propose ideas? (any member, specific roles, minimum requirements)
7. How long should voting periods last?
8. What happens if votes are close or controversial?

**Treasury and tokens:**
9. Will you have a treasury with funds? How much to start?
10. Do you need governance tokens? How will they be distributed?
11. How will the DAO fund its operations?
12. What spending limits should require votes?

**Technical setup:**
13. What's your technical expertise? (beginner, intermediate, advanced)
14. Do you prefer existing platforms or custom development?
15. Which blockchain do you want to use? (Ethereum, Polygon, etc.)
16. What's your budget for setup and operations?

Based on your answers, I'll provide:

**DAO STRUCTURE** - Governance framework tailored to your community
**PLATFORM RECOMMENDATION** - Best tools and services for your needs
**LAUNCH STRATEGY** - Step-by-step guide to get your DAO running
**MANAGEMENT PLAYBOOK** - How to run effective governance and grow membership
**LEGAL CONSIDERATIONS** - Compliance and risk management guidance

Share your DAO vision and let's build a thriving decentralized community!
```

## Example Usage

**User Input:**
```
1. Investment DAO focused on funding early-stage DeFi projects
2. 50-100 crypto investors and DeFi enthusiasts initially
3. Which projects to fund, investment amounts, exit strategies
4. Starting with 20 founding members

5. Token-weighted voting - bigger investments get more say
6. Any member can propose, but need 10% support to go to vote
7. 7-day voting periods for investment decisions
8. Need 60% majority to pass, re-vote if 50-60%

9. Starting treasury of $1M (members contribute)
10. Yes, governance tokens based on capital contributed
11. 2% management fee plus 20% of profits
12. Investments over $50K need vote, operations under $10K are automatic

13. Intermediate - we have developers but new to DAOs
14. Prefer existing platform for faster launch
15. Polygon for lower gas costs
16. $50K budget for setup and first year operations
```

**Assistant Output:**

Perfect! Here's your DeFi investment DAO structure:

## DAO STRUCTURE

### Recommended Framework: Capital-Weighted Investment DAO

**Why This Works for You**:
```
Investment Focus: Structured for funding decisions and ROI tracking
Member Profile: Sophisticated crypto investors
Capital Base: $1M starting treasury provides good foundation
Governance: Token-weighted voting aligns with investment amounts
```

### Governance Architecture

```
DAO Structure:
┌─────────────────────────────────────────┐
│             General Assembly            │
│        (All Token Holders)             │
└─────────────────────────────────────────┘
                     │
┌─────────────────────────────────────────┐
│          Investment Committee           │
│    (Top 5 token holders + 3 elected)   │
└─────────────────────────────────────────┘
                     │
┌─────────────────────────────────────────┐
│           Execution Team                │
│  (Operations Manager + Legal + Finance) │
└─────────────────────────────────────────┘

Decision Flow:
Proposal → Committee Review → Member Vote → Execution
```

## PLATFORM RECOMMENDATION

### Recommended Platform: Aragon on Polygon

**Why Aragon**:
```
✓ Purpose-built for investment DAOs
✓ Native Polygon support (low gas fees)
✓ Built-in treasury management
✓ Proven track record with 1000+ DAOs
✓ No-code setup for most features
```

**Alternative Options**:
```
DAOstack: Better for complex governance
Snapshot + Gnosis Safe: More customizable but requires more setup
Colony: Good for ongoing project management
Moloch v3: Optimized for investment clubs
```

## LAUNCH STRATEGY

### Phase 1: Foundation Setup (Weeks 1-4)

**Week 1: Legal and Structure**
```
Entity Formation:
- Set up LLC wrapper (recommended for legal protection)
- Draft operating agreement with DAO governance
- Establish bank account for fiat operations
- Consult lawyer on securities compliance

Cost: $15K (legal setup, compliance review)
```

**Week 2: Token Design and Distribution**
```
Governance Token (DEFI_INV):
- Total Supply: 1,000,000 tokens
- Founding Member Allocation: 20 members × 25,000 tokens each (500K)
- Treasury Reserve: 300,000 tokens (future members)
- Team Allocation: 200,000 tokens (vested over 2 years)

Token Distribution Method:
- $50K investment = 25,000 tokens initially
- Future members: $1 = 1 token (adjusted quarterly)
- Voting Power: 1 token = 1 vote
```

**Week 3: Platform Configuration**
```
Aragon DAO Setup:
1. Create DAO on Polygon network
2. Deploy governance token contract
3. Set up voting parameters:
   - Minimum support: 60%
   - Minimum approval: 10%
   - Vote duration: 7 days
4. Configure treasury with multi-sig requirements
5. Set up automatic execution for passed proposals
```

**Week 4: Member Onboarding**
```
Founding Member Process:
1. KYC/AML verification for all members
2. Investment contribution (minimum $50K)
3. Governance token distribution
4. Wallet setup and DAO access training
5. First governance vote (ratify operating procedures)

Launch Event:
- Virtual DAO launch party
- First investment proposal ready
- Media announcement and PR
```

### Phase 2: Operations Launch (Weeks 5-12)

**Investment Process Implementation**:
```
Deal Flow Setup:
Week 5-6: Establish deal sourcing (accelerators, networks, direct)
Week 7-8: Create due diligence framework and templates
Week 9-10: First investment proposal and vote
Week 11-12: Execute first investment and track performance

Investment Committee Responsibilities:
- Screen all proposals before member votes
- Conduct due diligence and risk assessment
- Present investment recommendations with analysis
- Monitor portfolio performance and report monthly
```

### Phase 3: Growth and Optimization (Months 4-12)

**Scaling Strategy**:
```
Month 4-6: Open to new members (cap at 100)
Month 7-9: Launch secondary investment strategies
Month 10-12: Consider launching public fund or token

Growth Targets:
- $5M treasury by end of year 1
- 10-15 portfolio investments
- 20% average ROI across portfolio
- 80+ active DAO members
```

## MANAGEMENT PLAYBOOK

### Monthly Operations Cycle

**Week 1: Portfolio Review**
```
Investment Committee Meeting:
- Review all portfolio companies performance
- Assess any exit opportunities
- Identify companies needing additional support
- Prepare monthly report for members

Member Communication:
- Monthly newsletter with performance updates
- Portfolio company spotlights
- Market analysis and trends
- Upcoming investment opportunities
```

**Week 2: Deal Sourcing and Pipeline**
```
New Opportunities:
- Review incoming deal flow
- Initial screening and filtering
- Schedule founder presentations
- Conduct preliminary due diligence

Pipeline Management:
- Update deal tracker
- Schedule committee deep dives
- Prepare proposal templates
- Coordinate member access to deal materials
```

**Week 3: Member Engagement**
```
Community Activities:
- Weekly AMAs with portfolio founders
- Educational webinars on DeFi trends
- Member networking events
- Expert guest speaker sessions

Governance Activities:
- Process any pending proposals
- Review and update governance parameters
- Address member feedback and concerns
- Plan upcoming votes and decisions
```

**Week 4: Strategic Planning**
```
Long-term Focus:
- Review DAO strategy and performance
- Plan next quarter's investment themes
- Assess need for policy updates
- Prepare quarterly member meeting
```

### Voting and Proposal Management

**Investment Proposal Template**:
```
Standard Investment Proposal Format:

1. Executive Summary (300 words max)
   - Company overview and team
   - Market opportunity and traction
   - Investment terms and amount

2. Investment Committee Recommendation
   - Due diligence summary
   - Risk assessment (1-10 scale)
   - Expected returns and timeline
   - Committee vote (unanimous/majority/split)

3. Financial Details
   - Proposed investment amount
   - Valuation and equity percentage
   - Follow-on rights and anti-dilution
   - Expected hold period and exit strategy

4. Member Discussion Period (48 hours)
   - Q&A with committee members
   - Community discussion thread
   - Founder AMA session

5. Formal Vote (7 days)
   - Clear yes/no decision
   - Minimum 60% approval required
   - Results automatically executed
```

### Treasury Management

**Asset Allocation Strategy**:
```
Treasury Composition:
- 60% Deployed Capital (active investments)
- 25% Liquid Reserves (USDC/ETH for opportunities)
- 10% Operating Capital (DAO expenses, salaries)
- 5% Risk Buffer (insurance, legal reserves)

Monthly Treasury Report:
- Total AUM and performance vs benchmarks
- Investment pipeline value and timeline
- Operating expense breakdown
- Cash flow projections for next quarter
```

## LEGAL CONSIDERATIONS

### Regulatory Compliance

**Securities Law Compliance**:
```
Investment DAO Considerations:
- Structure as investment club vs. fund
- Accredited investor requirements
- Securities registration exemptions
- State and federal compliance requirements

Recommended Legal Structure:
- Delaware LLC with DAO governance
- Operating agreement defining token rights
- Investment policy statement
- Member accreditation verification
```

**Ongoing Compliance Requirements**:
```
Annual Obligations:
- Tax reporting (K-1s for members)
- State registration maintenance
- Investor reporting and transparency
- Audit of investment performance

Risk Management:
- Directors and officers insurance
- Cyber liability coverage
- Professional liability for advisors
- Multi-sig treasury protection
```

### Risk Mitigation Strategies

**Operational Risks**:
```
Smart Contract Risk:
- Use audited contracts only (Aragon/OpenZeppelin)
- Multi-sig requirements for large transactions
- Time delays for major governance changes
- Emergency pause mechanisms

Governance Risks:
- Quorum requirements prevent small group control
- Anti-whale measures (voting caps)
- Transparent decision-making processes
- Member dispute resolution procedures
```

**Investment Risks**:
```
Portfolio Risk Management:
- Maximum 10% of treasury in any single investment
- Diversification across stages and sectors
- Due diligence standards and checklists
- Regular portfolio review and rebalancing

Member Protection:
- Clear investment policy and restrictions
- Regular financial reporting and audits
- Professional investment committee oversight
- Exit mechanisms for dissenting members
```

This comprehensive framework creates a professional investment DAO that balances member democracy with efficient decision-making, providing the structure needed to successfully invest in DeFi projects while protecting member interests and maintaining regulatory compliance.

## Related Prompts

- [DeFi Protocol Developer](../defi-protocols/decentralized-finance-protocol-development.md)
- [Smart Contract Security Auditor](../smart-contracts/smart-contract-security-audit-platform.md)
- [Cryptocurrency Trading Bot Builder](../crypto-trading/cryptocurrency-trading-algorithm-platform.md)

