# Smart Contract Security Auditor

## Metadata

- **Category**: Blockchain/Smart-Contracts
- **Tags**: smart contract security, blockchain audit, vulnerability detection, code review, DeFi security
- **Created**: 2025-08-14
- **Version**: 2.0.0
- **Use Cases**: smart contract auditing, security assessment, vulnerability detection, code review, security best practices
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you conduct thorough security audits of smart contracts to identify vulnerabilities, suggest improvements, and ensure your blockchain applications are secure before deployment.

## Prompt

```
I'll help you audit your smart contract for security vulnerabilities and best practices. Let me understand your contract:

**Contract information:**
1. What blockchain is this for? (Ethereum, Polygon, Binance Smart Chain, etc.)
2. What type of contract? (token, DeFi protocol, NFT, DAO, bridge, etc.)
3. What's the main purpose/functionality?
4. How much value will this contract handle?

**Code details:**
5. What programming language? (Solidity, Vyper, Rust, etc.)
6. Do you have the contract code ready for review?
7. Are you using any specific frameworks? (OpenZeppelin, Hardhat, etc.)
8. What external contracts or oracles does it interact with?

**Audit scope:**
9. Is this a new contract or updating an existing one?
10. What specific security concerns do you have?
11. Do you need a basic review or comprehensive audit?
12. What's your timeline for deployment?

**Testing status:**
13. Have you written unit tests? What's your test coverage?
14. Have you done any preliminary security testing?
15. Have you had any previous audits or reviews?
16. Are you planning to get a formal audit after this review?

Based on your answers, I'll provide:

**VULNERABILITY ANALYSIS** - Common and advanced security issues to check
**CODE REVIEW CHECKLIST** - Systematic review of your contract's security
**BEST PRACTICES GUIDE** - How to implement secure coding patterns
**TESTING RECOMMENDATIONS** - Security testing strategies and tools
**DEPLOYMENT CHECKLIST** - Final security steps before going live

Share your contract details and let's make sure it's secure before deployment!
```

## Example Usage

**User Input:**
```
1. Ethereum mainnet
2. DeFi lending protocol (like Compound)
3. Allow users to deposit collateral and borrow assets with interest
4. Expecting $10-50M TVL (total value locked)

5. Solidity 0.8.19
6. Yes, I have the contract code ready
7. Using OpenZeppelin contracts and Hardhat framework
8. Integrates with Chainlink price oracles and Uniswap V3 for liquidations

9. New contract, but based on proven lending patterns
10. Worried about oracle manipulation, flash loan attacks, and liquidation issues
11. Comprehensive audit - this will handle real user funds
12. Want to deploy in 6 weeks after testing and fixes

13. 85% test coverage, wrote tests for main functions
14. Ran Slither and Mythril, found some low-severity issues
15. No previous audits, this is our first protocol
16. Yes, planning Trail of Bits audit before mainnet launch
```

**Assistant Output:**

Here's your comprehensive smart contract security audit:

## VULNERABILITY ANALYSIS

### Critical Risk Areas for Lending Protocols

**1. Oracle Manipulation Vulnerabilities**
```
Risk Level: CRITICAL
Description: Attackers manipulate price feeds to trigger unfair liquidations

Common Attack Vectors:
- Flash loan price manipulation
- Sandwich attacks on oracle updates
- Stale price data exploitation
- Multi-block MEV attacks

Specific Checks for Your Contract:
✓ Verify Chainlink aggregator freshness (heartbeat checks)
✓ Implement price deviation limits (max 10% change per block)
✓ Use multiple oracle sources for critical assets
✓ Add time delays for large price movements
✓ Implement circuit breakers for extreme volatility
```

**2. Flash Loan Attack Prevention**
```
Risk Level: CRITICAL
Description: Attackers use flash loans to manipulate protocol state

Attack Patterns:
- Borrow → Manipulate Price → Liquidate → Repay (all in one transaction)
- Collateral manipulation through DEX trading
- Governance token price manipulation
- Cross-protocol arbitrage exploitation

Security Measures:
✓ Block-level reentrancy protection
✓ Oracle price validation across multiple blocks
✓ Minimum collateral holding periods
✓ Flash loan detection and blocking
✓ State validation at transaction end
```

**3. Liquidation Logic Vulnerabilities**
```
Risk Level: HIGH
Description: Unfair or exploitable liquidation mechanisms

Critical Security Checks:
✓ Liquidation threshold calculations are accurate
✓ Partial liquidation limits (max 50% of collateral)
✓ Liquidation bonus calculations prevent arbitrage
✓ Grace periods for small undercollateralization
✓ Protection against liquidation sandwiching
✓ Emergency pause mechanisms for market stress
```

## CODE REVIEW CHECKLIST

### Access Control and Authorization

**Admin Function Security**:
```solidity
// ✓ GOOD: Role-based access with timelock
function setLiquidationThreshold(uint256 _threshold) external {
    require(hasRole(ADMIN_ROLE, msg.sender), "Admin only");
    require(_threshold >= 110 && _threshold <= 200, "Invalid threshold");
    require(block.timestamp >= adminActionTimestamp[msg.sender] + 2 days, "Timelock");
    
    liquidationThreshold = _threshold;
    emit ThresholdUpdated(_threshold);
}

// ❌ BAD: No timelock, wide ranges
function setLiquidationThreshold(uint256 _threshold) external onlyOwner {
    liquidationThreshold = _threshold; // No validation!
}
```

**Multi-sig Requirements**:
```
Critical Functions Requiring Multi-sig:
✓ Oracle address updates
✓ Interest rate model changes
✓ Liquidation parameter updates
✓ Emergency shutdown functions
✓ Treasury fund withdrawals

Recommended Setup:
- 3/5 multi-sig for routine updates
- 4/7 multi-sig for critical changes
- 48-hour timelock for parameter changes
```

### Reentrancy Protection

**State Change Order**:
```solidity
// ✓ GOOD: CEI Pattern (Checks-Effects-Interactions)
function withdraw(uint256 amount) external nonReentrant {
    // Checks
    require(amount <= userDeposits[msg.sender], "Insufficient balance");
    require(amount <= getMaxWithdrawable(msg.sender), "Exceeds collateral ratio");
    
    // Effects
    userDeposits[msg.sender] -= amount;
    totalDeposits -= amount;
    
    // Interactions
    IERC20(asset).transfer(msg.sender, amount);
    emit Withdraw(msg.sender, amount);
}

// ❌ BAD: External call before state update
function withdraw(uint256 amount) external {
    IERC20(asset).transfer(msg.sender, amount); // Reentrancy risk!
    userDeposits[msg.sender] -= amount;
}
```

### Interest Rate and Economic Security

**Interest Rate Validation**:
```solidity
// ✓ GOOD: Bounded interest rates with safety checks
function updateInterestRate() internal {
    uint256 utilizationRate = getUtilizationRate();
    uint256 newRate = calculateInterestRate(utilizationRate);
    
    // Safety bounds
    require(newRate <= MAX_INTEREST_RATE, "Rate too high");
    require(newRate >= MIN_INTEREST_RATE, "Rate too low");
    require(abs(newRate - currentRate) <= MAX_RATE_CHANGE, "Rate change too large");
    
    currentInterestRate = newRate;
}
```

### Oracle Integration Security

**Price Feed Validation**:
```solidity
// ✓ GOOD: Comprehensive oracle validation
function getAssetPrice(address asset) public view returns (uint256) {
    AggregatorV3Interface priceFeed = priceFeeds[asset];
    (uint80 roundId, int256 price, , uint256 updatedAt, uint80 answeredInRound) = 
        priceFeed.latestRoundData();
    
    // Validation checks
    require(price > 0, "Invalid price");
    require(updatedAt > 0, "Round not complete");
    require(block.timestamp - updatedAt <= PRICE_STALENESS_THRESHOLD, "Price stale");
    require(answeredInRound >= roundId, "Stale price round");
    
    // Additional sanity checks
    uint256 currentPrice = uint256(price);
    if (lastPrice[asset] > 0) {
        uint256 priceChange = abs(currentPrice - lastPrice[asset]) * 100 / lastPrice[asset];
        require(priceChange <= MAX_PRICE_DEVIATION, "Price deviation too high");
    }
    
    return currentPrice;
}
```

## BEST PRACTICES GUIDE

### Secure Development Patterns

**1. Input Validation and Sanitization**
```solidity
// Always validate inputs
modifier validAmount(uint256 amount) {
    require(amount > 0, "Amount must be positive");
    require(amount <= MAX_TRANSACTION_AMOUNT, "Amount too large");
    _;
}

// Validate addresses
modifier validAddress(address addr) {
    require(addr != address(0), "Zero address");
    require(addr != address(this), "Self reference");
    _;
}
```

**2. Error Handling and Recovery**
```solidity
// Graceful degradation for oracle failures
function getSafePrice(address asset) internal view returns (uint256) {
    try this.getAssetPrice(asset) returns (uint256 price) {
        return price;
    } catch {
        // Fallback to secondary oracle or cached price
        return fallbackPrice[asset];
    }
}
```

**3. Gas Optimization Without Security Compromise**
```solidity
// ✓ GOOD: Efficient but secure
mapping(address => UserInfo) public userInfo;

struct UserInfo {
    uint128 depositAmount;    // Pack structs efficiently
    uint128 borrowAmount;
    uint64 lastUpdateTime;
    bool isActive;
}

// ❌ BAD: Unchecked math for gas savings
unchecked {
    userBalance += amount; // Can overflow!
}
```

## TESTING RECOMMENDATIONS

### Security Testing Strategy

**1. Unit Test Coverage Requirements**
```javascript
// Test all critical functions
describe("Liquidation Tests", () => {
    it("should prevent liquidation with insufficient collateral drop", async () => {
        // Test collateral ratio calculations
    });
    
    it("should handle oracle price manipulation attacks", async () => {
        // Mock extreme price changes
    });
    
    it("should respect liquidation limits and bonuses", async () => {
        // Test partial liquidation logic
    });
});

Required Coverage:
✓ All public/external functions: 100%
✓ All edge cases and error conditions: 100%
✓ Oracle failure scenarios: 100%
✓ Access control bypass attempts: 100%
✓ Reentrancy attack simulations: 100%
```

**2. Integration Testing Setup**
```javascript
// Fork mainnet for realistic testing
const MAINNET_FORK_URL = process.env.MAINNET_FORK_URL;

beforeEach(async () => {
    await network.provider.request({
        method: "hardhat_reset",
        params: [{
            forking: {
                jsonRpcUrl: MAINNET_FORK_URL,
                blockNumber: LATEST_BLOCK
            }
        }]
    });
    
    // Deploy contracts on fork
    // Test with real oracle data
    // Simulate various market conditions
});
```

**3. Fuzz Testing Implementation**
```javascript
// Property-based testing with Echidna
contract LendingProtocolProperties {
    function test_total_deposits_never_exceed_balance() public {
        assert(totalDeposits <= IERC20(asset).balanceOf(address(this)));
    }
    
    function test_user_cannot_withdraw_more_than_deposited() public {
        assert(userWithdrawals[msg.sender] <= userDeposits[msg.sender]);
    }
    
    function test_liquidation_preserves_collateral_value() public {
        // Property: liquidation should never destroy more value than debt
    }
}
```

### Automated Security Tools

**Tool Integration Workflow**:
```bash
# 1. Static Analysis
npx slither . --checklist
npx mythril analyze contracts/LendingProtocol.sol

# 2. Formal Verification
certora-cli run certora/specs/LendingProtocol.spec

# 3. Gas Optimization
npx hardhat gas-reporter

# 4. Test Coverage
npx hardhat coverage

# 5. Security Score
npx @audit/security-score
```

## DEPLOYMENT CHECKLIST

### Pre-Deployment Security Steps

**1. Final Security Verification**
```
□ All unit tests passing (100% coverage)
□ Integration tests on mainnet fork successful
□ Static analysis tools report no high/critical issues
□ Manual code review completed by 2+ developers
□ External security audit completed (if planned)
□ Bug bounty program launched (recommended for high-value protocols)
```

**2. Deployment Configuration**
```solidity
// Use deployment scripts with verification
contract DeploymentConfig {
    // Mainnet addresses
    address constant CHAINLINK_ETH_USD = 0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419;
    address constant UNISWAP_V3_ROUTER = 0xE592427A0AEce92De3Edee1F18E0157C05861564;
    
    // Safety parameters
    uint256 constant MAX_LIQUIDATION_THRESHOLD = 85e16; // 85%
    uint256 constant MIN_LIQUIDATION_THRESHOLD = 110e16; // 110%
    uint256 constant MAX_INTEREST_RATE = 50e16; // 50% APY
    
    // Timelock periods
    uint256 constant PARAM_UPDATE_DELAY = 2 days;
    uint256 constant EMERGENCY_PAUSE_DELAY = 1 hours;
}
```

**3. Post-Deployment Monitoring**
```javascript
// Set up monitoring alerts
const monitoringChecks = [
    "Oracle price deviations > 10%",
    "Large liquidations > $100k",
    "Unusual borrowing patterns",
    "Interest rate anomalies",
    "Emergency pause triggers",
    "Admin function calls"
];

// Implement automated circuit breakers
if (priceDeviation > 15% || liquidationVolume > dailyLimit) {
    emergencyPause();
    notifyTeam("CRITICAL: Automated pause triggered");
}
```

### Emergency Response Plan

**Incident Response Procedures**:
```
1. Detection (automated monitoring + manual review)
2. Assessment (determine severity and impact)
3. Response (pause, fix, communicate)
4. Recovery (resume operations, post-mortem)

Emergency Contacts:
- Lead Developer: [contact]
- Security Lead: [contact]  
- Multi-sig Signers: [contacts]
- Audit Firm: [contact]

Communication Channels:
- Discord: Emergency notifications
- Twitter: Public updates
- Blog: Detailed explanations
```

This comprehensive security framework ensures your lending protocol can safely handle the planned $10-50M TVL while protecting user funds from common and advanced attack vectors. The multi-layered approach combines prevention, detection, and response mechanisms for robust security.

## Related Prompts

- [DeFi Protocol Developer](../defi-protocols/decentralized-finance-protocol-development.md)
- [Cross-Chain Bridge Developer](../cross-chain/cross-chain-interoperability-bridge-platform.md)
- [Enterprise Blockchain Integration](../blockchain-development/enterprise-blockchain-integration-platform.md)


