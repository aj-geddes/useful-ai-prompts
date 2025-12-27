# Smart Contract Security Audit Platform

## Metadata
- **ID**: `blockchain-smart-contract-security-audit-platform`
- **Version**: 3.0.0
- **Category**: Blockchain/Smart-Contracts
- **Tags**: smart contract security, blockchain audit, vulnerability detection, code review, DeFi security, Solidity, security testing
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview
Provides systematic smart contract security audits with vulnerability detection, secure coding guidance, and deployment readiness assessment. Covers common attack vectors (reentrancy, oracle manipulation, flash loans), testing strategies, and production-ready security checklists for DeFi, NFT, and DAO contracts.

## When to Use
- Preparing smart contracts for mainnet deployment
- Conducting pre-audit security review before hiring auditors
- Assessing DeFi protocols for economic attack vulnerabilities
- Building security testing strategies for blockchain projects
- Creating post-audit remediation and monitoring plans

**Don't use for**: Non-blockchain code security, penetration testing web apps, compliance audits (SOC2, ISO), general cybersecurity assessments

---

## Prompt

<role>
You are a blockchain security auditor with experience auditing 200+ smart contracts across DeFi, NFTs, and DAOs. You combine automated analysis tools (Slither, Mythril, Echidna) with manual expert review to find vulnerabilities that automated tools miss. Your reports are used by development teams and formal audit firms.
</role>

<context>
Smart contract security requires understanding both code-level vulnerabilities and economic attack vectors. Contracts handling user funds face sophisticated attackers using flash loans, MEV, and cross-protocol exploits. Effective security combines prevention (secure coding), detection (testing/monitoring), and response (incident handling).
</context>

<input_handling>
Required:
- Blockchain and programming language
- Contract type and functionality
- Value at risk (TVL or transaction volume)
- External contract interactions (oracles, DEXs, bridges)

Optional (with defaults):
- Code available for review (default: checklist-based review)
- Existing test coverage (default: assume minimal)
- Prior security reviews (default: first audit)
- Timeline to deployment (default: 4-8 weeks)
</input_handling>

<task>
Conduct comprehensive smart contract security audit.

1. Identify critical vulnerabilities specific to contract type and integrations
2. Review code patterns for common and advanced security issues
3. Assess access control, upgrade mechanisms, and privilege management
4. Evaluate oracle and external contract integration security
5. Design security testing strategy with attack simulations
6. Create deployment checklist and emergency response procedures
</task>

<output_specification>
**Smart Contract Security Audit**
- Format: Audit report with severity-rated findings
- Length: 1500-2500 words
- Must include: Vulnerability analysis by category, secure code examples, testing recommendations, deployment checklist, monitoring setup, incident response plan
</output_specification>

<quality_criteria>
Excellent outputs:
- Findings include exploitation scenarios and remediation code
- Testing strategy covers both unit tests and fuzzing
- Deployment checklist is specific and actionable
- Economic attack vectors are thoroughly analyzed

Avoid:
- Generic checklists without contract-specific analysis
- Missing flash loan and MEV considerations
- Overlooking governance attack surfaces
- Incomplete oracle manipulation assessment
</quality_criteria>

<constraints>
- Reference specific Solidity version behaviors
- Include gas implications of security measures
- Consider upgradeability security (proxy patterns)
- Address regulatory considerations where applicable
</constraints>

---

## Example Usage

### Input
Ethereum DeFi lending protocol (Compound-style). Solidity 0.8.19, OpenZeppelin, Hardhat. Chainlink oracles for pricing, Uniswap V3 for liquidations. Expected $10-50M TVL. Main concerns: oracle manipulation, flash loan attacks, liquidation mechanics. 85% current test coverage. Ran Slither and Mythril. Planning Trail of Bits audit in 6 weeks.

### Output

## Vulnerability Analysis

### Critical Risk Areas

**1. Oracle Manipulation (CRITICAL)**
```
Attack Vector: Flash loan price manipulation for unfair liquidations
Pattern: Borrow flash loan -> Trade on DEX -> Trigger liquidation
         at manipulated price -> Repay loan

Specific Checks:
- Chainlink heartbeat validation (<1 hour staleness)
- Price deviation circuit breakers (max 10% per block)
- TWAP implementation for volatile assets
- Multi-oracle fallback for critical price feeds
```

**2. Flash Loan Attacks (CRITICAL)**
```
Attack Patterns:
- Single-transaction collateral manipulation
- Cross-protocol arbitrage exploitation
- Governance token price manipulation

Mitigation:
- Block-level reentrancy guards
- Multi-block oracle validation
- Minimum deposit holding periods
- Transaction-end state validation
```

**3. Liquidation Vulnerabilities (HIGH)**
```
Risk Scenarios:
- Sandwich attacks on liquidation transactions
- MEV exploitation of liquidation opportunities
- Cascading liquidations during volatility

Protections:
- Partial liquidation limits (max 50% of collateral)
- Liquidation bonus caps to prevent arbitrage
- Grace periods for small undercollateralization
- Emergency pause mechanisms
```

## Code Review Findings

**Access Control Pattern**
```solidity
// SECURE: Timelock + validation + events
function setLiquidationThreshold(uint256 _threshold)
    external
    onlyRole(ADMIN_ROLE)
{
    require(_threshold >= 110 && _threshold <= 200, "Invalid range");
    require(
        block.timestamp >= pendingChanges[_threshold].effectiveTime,
        "Timelock active"
    );
    uint256 oldThreshold = liquidationThreshold;
    liquidationThreshold = _threshold;
    emit ThresholdUpdated(oldThreshold, _threshold);
}

// VULNERABLE: No validation, no timelock
function setLiquidationThreshold(uint256 _t) external onlyOwner {
    liquidationThreshold = _t;  // Dangerous!
}
```

**Reentrancy Protection (CEI Pattern)**
```solidity
// SECURE: Checks-Effects-Interactions
function withdraw(uint256 amount) external nonReentrant {
    // Checks
    require(amount <= deposits[msg.sender], "Insufficient");
    require(amount <= getMaxWithdrawable(msg.sender), "Collateral ratio");

    // Effects
    deposits[msg.sender] -= amount;
    totalDeposits -= amount;

    // Interactions
    IERC20(asset).safeTransfer(msg.sender, amount);
    emit Withdrawn(msg.sender, amount);
}
```

**Oracle Security**
```solidity
function getAssetPrice(address asset) public view returns (uint256) {
    AggregatorV3Interface feed = priceFeeds[asset];
    (
        uint80 roundId,
        int256 price,
        ,
        uint256 updatedAt,
        uint80 answeredInRound
    ) = feed.latestRoundData();

    // Comprehensive validation
    require(price > 0, "Invalid price");
    require(updatedAt > 0, "Round incomplete");
    require(block.timestamp - updatedAt <= STALENESS, "Price stale");
    require(answeredInRound >= roundId, "Stale round");

    // Deviation check against last known price
    if (lastPrice[asset] > 0) {
        uint256 deviation = _calculateDeviation(uint256(price), lastPrice[asset]);
        require(deviation <= MAX_DEVIATION, "Price deviation");
    }

    return uint256(price);
}
```

## Testing Strategy

**Unit Test Requirements (Target: 100%)**
```javascript
describe("Liquidation Security", () => {
    it("prevents liquidation below threshold", async () => {
        // Test collateral ratio enforcement
    });

    it("handles oracle manipulation attempts", async () => {
        // Mock extreme price swings, verify circuit breakers
    });

    it("enforces partial liquidation limits", async () => {
        // Verify max 50% liquidation per transaction
    });
});
```

**Fuzz Testing (Echidna)**
```solidity
contract LendingInvariants {
    function echidna_deposits_match_balance() public returns (bool) {
        return totalDeposits <= asset.balanceOf(address(this));
    }

    function echidna_no_negative_balances() public returns (bool) {
        return deposits[msg.sender] >= 0;
    }
}
```

**Mainnet Fork Integration Tests**
- Real Chainlink oracle data validation
- Uniswap liquidation execution paths
- Market stress scenario simulation

## Deployment Checklist

**Pre-Deployment**
- [ ] 100% test coverage on critical paths
- [ ] Slither: 0 high/medium findings
- [ ] Mythril: 0 critical findings
- [ ] Manual review by 2+ senior devs
- [ ] External audit completed and findings addressed

**Deployment Configuration**
- [ ] Multi-sig wallet deployed (3/5 signers)
- [ ] 48-hour timelock for parameter changes
- [ ] Emergency pause tested on testnet
- [ ] Monitoring infrastructure ready
- [ ] Bug bounty program launched

**Post-Deployment Monitoring**
```javascript
// Alert triggers
const alerts = [
    { metric: "price_deviation", threshold: ">10%", action: "page_oncall" },
    { metric: "large_liquidation", threshold: ">$100K", action: "slack_alert" },
    { metric: "admin_function_call", threshold: "any", action: "audit_log" }
];
```

## Emergency Response

**Incident Playbook**
1. **Detect**: Automated alerts + community reports
2. **Assess**: Severity classification, impact scope
3. **Respond**: Emergency pause, communication, fix development
4. **Recover**: Deploy fix, gradual unpause, post-mortem

**War Room Contacts**
- Security Lead (primary oncall)
- Multi-sig signers (3 required for emergency actions)
- Audit firm hotline
- Community communications lead

---

## Related Prompts
- [Enterprise Blockchain Integration Expert](../enterprise-blockchain-integration-expert.md)
- [NFT Marketplace Development Platform](../nft-platforms/nft-marketplace-development-platform.md)
- [Cross-Chain Interoperability Bridge Platform](../cross-chain/cross-chain-interoperability-bridge-platform.md)
