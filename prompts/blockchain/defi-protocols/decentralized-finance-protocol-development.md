# DeFi Protocol Builder

## Metadata
- **Created**: 2025-01-15

- **Category**: Blockchain/DeFi-Protocols
- **Tags**: DeFi, automated market maker, yield farming, liquidity pools, smart contracts
- **Version**: 2.0.0
- **Use Cases**: DeFi protocol development, yield farming setup, AMM creation, liquidity management
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro

## Description

This prompt helps you build secure DeFi protocols including automated market makers (AMMs), yield farming systems, and lending platforms with proper tokenomics and risk management.

## Prompt

```
I'll help you build a secure and profitable DeFi protocol. Let me understand your project:

**Protocol concept:**
1. What type of DeFi protocol? (AMM/DEX, lending, yield farming, derivatives)
2. What problem are you solving for users?
3. What's your target market? (retail users, institutions, other protocols)
4. What makes your protocol unique?

**Technical setup:**
5. Which blockchain(s)? (Ethereum, Polygon, BSC, Arbitrum, etc.)
6. What's your development experience level?
7. Do you have smart contract developers?
8. What's your budget for development and audits?

**Tokenomics and incentives:**
9. Will you have a governance token?
10. How will you incentivize liquidity providers?
11. What are your revenue streams?
12. How will you bootstrap initial liquidity?

Based on your answers, I'll provide:

**PROTOCOL ARCHITECTURE** - Smart contract design and implementation plan
**TOKENOMICS MODEL** - Token distribution and incentive mechanisms
**SECURITY FRAMEWORK** - Audit checklist and risk mitigation
**LAUNCH STRATEGY** - Go-to-market plan and liquidity bootstrapping
**RISK MANAGEMENT** - Economic attacks prevention and monitoring

Share your DeFi vision and let's build something secure and profitable!
```

## Example Usage

**User Input:**
```
1. AMM/DEX - Building a concentrated liquidity AMM like Uniswap V3
2. Solving capital efficiency - most AMMs waste 99% of liquidity outside price range
3. Targeting professional traders and large liquidity providers
4. Dynamic fee tiers that adjust based on volatility + MEV protection

5. Ethereum mainnet first, then Arbitrum and Polygon
6. Intermediate - built simple contracts before but not full DeFi
7. Have 2 Solidity developers, need to hire 1 more senior dev
8. $500K budget - $300K development, $200K for multiple audits

9. Yes - governance token for fee distribution and protocol decisions
10. Trading fees + bonus emissions for concentrated positions
11. Trading fees (0.05-1% based on volatility) + potential MEV revenue
12. $2M initial liquidity from team/investors + liquidity mining program
```

**Assistant Output:**

Here's your comprehensive DeFi protocol development plan:

## PROTOCOL ARCHITECTURE

### Smart Contract Design

```
Core Contracts Needed:

1. Pool Factory Contract
   - Creates new trading pairs
   - Manages protocol fees
   - Handles upgrades

2. Pool Contract (per trading pair)  
   - Concentrated liquidity positions
   - Dynamic fee calculation
   - MEV protection mechanisms
   - Price oracle integration

3. Position Manager Contract
   - NFT-based liquidity positions
   - Fee collection and compounding
   - Position visualization

4. Router Contract
   - Multi-hop swaps
   - Slippage protection
   - Gas optimization
```

### Technical Implementation Plan

**Phase 1: Core AMM (Months 1-3)**
```
Week 1-4: Pool Factory + Basic Pool
- Deploy factory contract
- Implement basic swap functionality
- Add liquidity provision

Week 5-8: Concentrated Liquidity
- Range-based positions
- Tick-based math implementation
- Position NFTs

Week 9-12: Advanced Features
- Dynamic fees based on volatility
- MEV protection (commit-reveal)
- Oracle price feeds
```

**Security Considerations:**
- Use OpenZeppelin libraries for standard functions
- Implement reentrancy guards on all external calls
- Add emergency pause functionality
- Comprehensive input validation

## TOKENOMICS MODEL

### Token Distribution (100M total supply)

```
Team & Advisors: 20M (20%) - 4 year vesting
Investors: 15M (15%) - 2 year vesting  
Treasury: 25M (25%) - Protocol development
Liquidity Mining: 30M (30%) - 3 year distribution
Public Sale: 10M (10%) - No vesting
```

### Incentive Mechanisms

**Liquidity Provider Rewards:**
```
Base Trading Fees: 60% to LPs
Bonus Emissions: 
- 2x multiplier for full-range positions
- 4x multiplier for tight ranges (±2%)
- 6x multiplier for active management

Weekly Distribution: 200K tokens
Reduction: 5% every 3 months
```

**Fee Structure:**
```
Stable Pairs (USDC/USDT): 0.05%
Standard Pairs (ETH/USDC): 0.3%  
Exotic Pairs: 1.0%
Dynamic Adjustment: ±50% based on volatility
```

### Revenue Model

**Protocol Revenue Streams:**
1. **Trading Fees**: 40% of all trading fees to protocol
2. **MEV Revenue**: 50% of captured MEV value
3. **Flash Loan Fees**: 0.09% on all flash loans
4. **Governance Token Sales**: Strategic token releases

**Projected Revenue (Year 1):**
- Daily Volume Target: $50M → $18B annually
- Average Fee: 0.25% → $45M fee revenue
- Protocol Share: 40% → $18M protocol revenue

## SECURITY FRAMEWORK

### Smart Contract Security Checklist

**Pre-Audit Development:**
```
✓ Use proven libraries (OpenZeppelin, PRBMath)
✓ Implement comprehensive tests (>95% coverage)
✓ Add overflow/underflow protection
✓ Validate all external inputs
✓ Implement proper access controls
✓ Add emergency pause mechanisms
✓ Document all functions thoroughly
```

**Testing Strategy:**
```
Unit Tests: Individual function testing
Integration Tests: Contract interaction testing  
Fuzzing: Random input testing
Simulation: Large-scale transaction simulation
Formal Verification: Mathematical proof of correctness
```

### Audit Plan ($200K budget)

**Primary Audit: Consensys Diligence ($120K)**
- 6-week comprehensive audit
- Formal verification of core math
- Economic attack vector analysis

**Secondary Audit: Trail of Bits ($60K)**
- 3-week focused audit
- Automated testing tools
- Gas optimization review

**Bug Bounty: $20K ongoing**
- $50K max payout for critical bugs
- $10K for high severity
- $2K for medium severity

### Risk Management

**Economic Attack Vectors:**
```
Flash Loan Attacks: 
- Solution: Time-weighted average prices
- Implementation: TWAP oracle with 10-minute window

Sandwich Attacks:
- Solution: MEV protection with commit-reveal
- Implementation: 2-block confirmation system

Liquidity Drain:
- Solution: Emergency pause + withdrawal limits
- Implementation: 24-hour withdrawal limit per user
```

## LAUNCH STRATEGY

### Pre-Launch (Months 1-4)

**Development & Testing:**
```
Month 1: Core contracts development
Month 2: Frontend + testing
Month 3: Security audits
Month 4: Bug fixes + final testing
```

**Community Building:**
```
Twitter/Discord: DeFi education content
Partnerships: Integrate with wallets/aggregators
KOL Engagement: DeFi influencer partnerships
Beta Testing: Invite 100 power users
```

### Launch Phase (Month 5)

**Liquidity Bootstrapping:**
```
Week 1: Team provides $1M initial liquidity
Week 2: Strategic partners add $500K
Week 3: Public liquidity mining launch
Week 4: Trading competition ($50K prizes)
```

**Marketing Blitz:**
```
Launch Day: Coordinated announcements
Week 1: Podcast tour + AMAs
Week 2: DeFi conference presentations  
Week 3: Integration announcements
Week 4: Metrics and success stories
```

### Growth Phase (Months 6-12)

**Expansion Strategy:**
```
Month 6: Arbitrum deployment
Month 8: Polygon deployment  
Month 10: Additional token pairs
Month 12: Derivatives trading launch
```

**Partnership Pipeline:**
```
Aggregators: 1inch, Paraswap, Matcha
Wallets: MetaMask, Rainbow, Argent
Protocols: Compound, Aave, Yearn
Institutions: Jump, Alameda, Wintermute
```

## DEVELOPMENT ROADMAP

### Team Scaling Plan

**Current Team: 2 Solidity developers**
**Hiring Needs:**
```
Month 1: Senior Smart Contract Lead ($180K)
Month 2: Frontend Developer ($120K)  
Month 3: DevOps Engineer ($140K)
Month 4: Product Manager ($150K)
```

**Development Tools:**
```
Hardhat: Development framework
Foundry: Advanced testing
Slither: Static analysis
Tenderly: Debugging and monitoring
```

### Milestone Timeline

```
Month 1: ✓ Core contracts (Factory + Pool)
Month 2: ✓ Concentrated liquidity + NFTs  
Month 3: ✓ Frontend MVP + testing
Month 4: ✓ Security audits complete
Month 5: 🚀 Mainnet launch
Month 6: ✓ $10M TVL target
Month 9: ✓ Multi-chain deployment
Month 12: ✓ $100M TVL target
```

### Success Metrics

**Technical KPIs:**
- Contract uptime: >99.9%
- Gas efficiency: <80K per swap
- Security: Zero critical bugs

**Business KPIs:**  
- TVL: $10M (Month 6) → $100M (Month 12)
- Daily volume: $1M → $50M
- Active users: 1,000 → 10,000
- Revenue: $1M → $18M annually

This plan balances innovation with proven DeFi patterns. Focus on security first, then scale aggressively once you prove product-market fit.

## Related Prompts

- [Smart Contract Security Auditor](../smart-contracts/smart-contract-security-audit-platform.md)
- [DAO Creator and Management Guide](../dao-governance/decentralized-autonomous-organization-platform.md)
- [Cryptocurrency Trading Bot Builder](../crypto-trading/cryptocurrency-trading-algorithm-platform.md)
