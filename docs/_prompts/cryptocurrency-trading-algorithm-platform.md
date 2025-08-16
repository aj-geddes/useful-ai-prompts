---
category: blockchain
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for blockchain optimization and expert consultation
slug: cryptocurrency-trading-bot-builder
tags:
- blockchain
title: Cryptocurrency Trading Bot Builder
use_cases:
- blockchain optimization
- professional workflow enhancement
version: 3.0.0
---

# Cryptocurrency Trading Bot Builder

## Metadata

- **Category**: Blockchain/Crypto-Trading
- **Tags**: crypto trading, trading bot, algorithmic trading, automated trading, cryptocurrency strategy
- **Created**: 2025-08-14
- **Version**: 2.0.0
- **Use Cases**: automated crypto trading, trading strategy development, portfolio management, risk control
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you build cryptocurrency trading bots and automated trading strategies. Whether you're a beginner wanting simple dollar-cost averaging or an experienced trader needing complex algorithms, this will guide you through creating profitable trading systems.

## Prompt

```
I'll help you build a cryptocurrency trading bot tailored to your experience and goals. Let me understand your trading needs:

**Your trading background:**
1. What's your trading experience? (complete beginner, some manual trading, experienced trader)
2. How much capital do you plan to trade with?
3. What's your risk tolerance? (conservative, moderate, aggressive)
4. How much time can you spend monitoring the bot daily?

**Trading strategy goals:**
5. What trading approach interests you? (buy and hold, swing trading, day trading, arbitrage)
6. Which cryptocurrencies do you want to trade? (Bitcoin, Ethereum, altcoins, all)
7. What returns are you hoping for? (steady growth, beat the market, high risk/high reward)
8. How important is avoiding losses vs. maximizing gains?

**Technical setup:**
9. What's your programming experience? (none, basic, intermediate, advanced)
10. Do you prefer no-code solutions or custom development?
11. Which exchanges do you use? (Binance, Coinbase, Kraken, etc.)
12. What's your budget for tools and services?

Based on your answers, I'll provide:

**STRATEGY RECOMMENDATION** - Best trading approach for your situation
**BOT IMPLEMENTATION** - Step-by-step setup guide with specific tools
**RISK MANAGEMENT** - How to protect your capital and manage losses
**PERFORMANCE TRACKING** - How to measure and improve your bot's results
**SCALING PLAN** - How to grow your trading operation over time

Share your trading goals and experience level, and let's build your profitable trading bot!
```

## Example Usage

**User Input:**
```
1. Some manual trading experience - been buying crypto for 2 years, mostly buy and hold
2. Starting with $10,000, can add $2,000 monthly
3. Moderate risk - want growth but can't afford major losses
4. Can check it 2-3 times per day, maybe 30 minutes total

5. Interested in swing trading - hold positions for days to weeks
6. Want to focus on Bitcoin and Ethereum, maybe add 2-3 solid altcoins
7. Hoping for 20-30% annual returns, better than just holding
8. Avoiding big losses is more important than hitting home runs

9. Basic programming - can follow tutorials and modify code
10. Prefer something with a GUI but willing to do some coding
11. Using Binance and Coinbase Pro
12. Can spend $100-200/month on tools and data
```

**Assistant Output:**

Perfect! Here's your cryptocurrency swing trading bot strategy:

## STRATEGY RECOMMENDATION

### Recommended Approach: Multi-Timeframe Momentum Swing Trading

**Why This Fits Your Profile**:
```
Experience Level: Building on your buy/hold knowledge
Capital: $10K start + $2K monthly is perfect for scaling
Risk Tolerance: Moderate risk with structured stop losses
Time Commitment: 30 min/day fits swing trading perfectly
Goals: 20-30% annual returns are achievable with disciplined execution
```

### Core Strategy Framework

```
Trading Style: Swing Trading (3-14 day holds)
Assets: BTC (40%), ETH (40%), 2 rotating altcoins (20%)
Entry Signals: RSI + Moving Average + Volume confirmation
Exit Signals: Take profit targets + trailing stops
Risk Per Trade: 2% maximum capital risk
Win Rate Target: 55-60% with 1.5:1 reward/risk ratio
```

## BOT IMPLEMENTATION

### Option 1: 3Commas (Recommended for You)

**Why 3Commas**:
```
✓ User-friendly interface with advanced features
✓ Direct Binance/Coinbase Pro integration
✓ Built-in backtesting and paper trading
✓ Cost: $29/month (within your budget)
✓ No coding required for basic strategies
```

**Setup Process**:
```
Week 1: Account Setup & Testing
1. Create 3Commas account and connect exchanges
2. Set up paper trading mode
3. Configure basic DCA bot for BTC/ETH
4. Run paper trades for 1 week

Week 2: Strategy Implementation
1. Create swing trading bot with these settings:
   - RSI(14) oversold <30, overbought >70
   - Price above 20-day MA for long entries
   - Volume 1.5x average volume
   - 3% stop loss, 6% take profit

Week 3: Live Trading Start
1. Start with $2,000 (20% of capital)
2. Monitor performance daily
3. Adjust settings based on results
4. Add more capital monthly if profitable
```

### Option 2: Custom Python Bot (If You Want to Learn)

**TradingView + Python Framework**:
```
Tools Needed:
- TradingView Pro account ($15/month)
- Python with CCXT library (free)
- VPS hosting ($20/month)
- Telegram alerts (free)

Strategy Code Structure:
```python
# Simplified strategy logic
def swing_strategy():
    rsi = get_rsi(14)
    price = get_current_price()
    ma20 = get_moving_average(20)
    volume = get_volume_ratio()
    
    # Long entry conditions
    if (rsi < 35 and 
        price > ma20 and 
        volume > 1.5):
        enter_long_position()
    
    # Exit conditions
    if position_profit() > 6%:
        take_profit()
    elif position_loss() > 3%:
        stop_loss()
```

## RISK MANAGEMENT

### Position Sizing Strategy

**Capital Allocation**:
```
Conservative Approach (Recommended):
- Maximum 4 positions at once
- 2% risk per trade = $200 max loss per trade
- Position size = $200 ÷ stop_loss_% = position size

Example for BTC at $45,000 with 3% stop:
Risk per trade: $200
Stop loss: 3% = $1,350
Position size: $200 ÷ 0.03 = $6,667 investment
Shares to buy: $6,667 ÷ $45,000 = 0.148 BTC
```

### Stop Loss Management

**Dynamic Stop Strategy**:
```
Initial Stop: 3% below entry price
Trailing Stop: Once 3% profit, trail stop at breakeven
Progressive Trail: Every 2% gain, raise stop by 1%

Example Trade:
Entry: $45,000
Initial Stop: $43,650 (3% loss)
Breakeven Trigger: $46,350 (3% gain)
New Stop: $45,000 (breakeven)
6% Gain Level: $47,700
Final Stop: $46,350 (3% profit locked)
```

### Risk Controls

**Daily/Weekly Limits**:
```
Maximum Daily Loss: 1% of total capital ($100)
Maximum Weekly Loss: 3% of total capital ($300)
Consecutive Losses: Stop after 3 losing trades
Monthly Review: Adjust strategy if <15% win rate
```

## PERFORMANCE TRACKING

### Key Metrics to Monitor

**Trading Performance**:
```
Daily Metrics:
- Total P&L (profit/loss)
- Win rate percentage
- Average win vs average loss
- Number of trades executed

Weekly Analysis:
- Best performing coin/strategy
- Worst performing setup
- Risk-adjusted returns (Sharpe ratio)
- Maximum drawdown experienced

Monthly Review:
- Compare to buy-and-hold returns
- Analyze major wins and losses
- Adjust position sizing if needed
- Review and update strategy parameters
```

### Tracking Tools

**Performance Dashboard**:
```
Built-in 3Commas Analytics:
- Automatic P&L calculation
- Performance vs benchmarks
- Risk metrics and drawdown
- Trade history and analysis

Manual Tracking Spreadsheet:
- Date, coin, entry/exit prices
- Reason for entry (which signal)
- Profit/loss and percentage
- Market conditions and notes
```

### Benchmark Comparison

**Monthly Performance Targets**:
```
Conservative Success: Beat BTC buy-and-hold by 5%
Moderate Success: 2-3% monthly returns consistently
Strong Success: 30%+ annual returns with <15% max drawdown

Red Flags (Stop Trading Signals):
- 3 consecutive months of losses
- Drawdown exceeding 20% of capital
- Win rate falling below 40% for 30+ trades
- Stress affecting daily life or decisions
```

## SCALING PLAN

### Growth Phases

**Phase 1: Proof of Concept (Months 1-3)**
```
Capital: $2,000 live trading
Goal: Prove strategy works consistently
Success Criteria: 
- Positive returns vs buy-and-hold
- <10% maximum drawdown
- >50% win rate maintained

Learning Focus:
- Master the chosen platform
- Understand your emotional responses
- Refine entry/exit criteria
- Build confidence in the system
```

**Phase 2: Scale Up (Months 4-9)**
```
Capital: Increase to $5,000-8,000
Goal: Optimize for better risk-adjusted returns
Success Criteria:
- 15%+ returns vs 10% max drawdown
- Consistent monthly profitability
- Refined strategy parameters

Improvements:
- Add 1-2 additional altcoins
- Implement more sophisticated signals
- Consider multiple timeframe analysis
- Optimize position sizing algorithms
```

**Phase 3: Advanced Trading (Months 10+)**
```
Capital: Scale to full $10,000+ monthly additions
Goal: Build toward full-time trading income
Success Criteria:
- 25-30% annual returns consistently
- Multiple strategy diversification
- Automated monitoring and alerts

Advanced Features:
- Multi-exchange arbitrage opportunities
- Options/futures hedging strategies
- Market-making in low-cap altcoins
- Research new DeFi yield strategies
```

### Technology Upgrades

**Platform Evolution Path**:
```
Month 1-6: Master 3Commas platform
Month 6-12: Add TradingView advanced alerts
Month 12+: Consider custom Python development
Year 2+: Explore institutional-grade platforms

Cost Scaling:
Current: ~$150/month in tools/data
6 months: ~$300/month (more exchanges, data)
1 year: ~$500/month (professional tools)
```

### Risk Management Evolution

**Sophistication Progression**:
```
Beginner: Fixed 2% position sizing
Intermediate: Kelly criterion position sizing
Advanced: Portfolio optimization with correlation
Expert: Multi-strategy risk parity allocation

Capital Protection:
- Always maintain 6-month living expenses separately
- Never risk more than you can afford to lose
- Take profits regularly to build emergency fund
- Consider partial withdrawals at major milestones
```

This roadmap turns your $10,000 starting capital into a systematic trading operation that can potentially generate 20-30% annual returns while managing downside risk through disciplined money management and proven swing trading techniques.

## Related Prompts

- [DeFi Protocol Developer](../defi-protocols/decentralized-finance-protocol-development.md)
- [Smart Contract Security Auditor](../smart-contracts/smart-contract-security-audit-platform.md)
- [Cross-Chain Bridge Developer](../cross-chain/cross-chain-interoperability-bridge-platform.md)