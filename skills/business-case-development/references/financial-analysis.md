# Financial Analysis

## Financial Analysis

```python
# Business case financial calculations

class FinancialAnalysis:
    def calculate_npv(self, cash_flows, discount_rate=0.10):
        """Calculate Net Present Value"""
        npv = 0
        for year, cash_flow in enumerate(cash_flows):
            npv += cash_flow / ((1 + discount_rate) ** year)
        return round(npv, 2)

    def calculate_irr(self, cash_flows):
        """Calculate Internal Rate of Return"""
        # Approximate IRR calculation
        for irr_guess in range(0, 100):
            npv = self.calculate_npv(cash_flows, irr_guess / 100)
            if npv <= 0:
                return irr_guess / 100

    def calculate_payback_period(self, initial_investment, annual_cash_flows):
        """Calculate months to break even"""
        cumulative = 0
        for year, cash_flow in enumerate(annual_cash_flows):
            cumulative += cash_flow
            if cumulative >= initial_investment:
                remaining = initial_investment - (cumulative - cash_flow)
                months = (remaining / cash_flow) * 12
                return year + (months / 12)
        return None

    def create_financial_summary(self, investment, benefits, costs):
        """Create comprehensive financial analysis"""
        cash_flows = [-investment]  # Year 0

        for year in range(1, 6):  # 5-year projection
            annual_benefit = sum(benefits.values()) * (year / 2) if year < 2 else sum(benefits.values())
            annual_cost = costs['annual']
            cash_flows.append(annual_benefit - annual_cost)

        return {
            'investment': investment,
            'annual_benefit_year_1': cash_flows[1] + costs['annual'],
            'annual_cost': costs['annual'],
            'net_benefit_year_1': cash_flows[1],
            'payback_months': self.calculate_payback_period(investment, cash_flows[1:]),
            'npv_5_year': self.calculate_npv(cash_flows),
            'irr': self.calculate_irr(cash_flows),
            'roi_percent': ((sum(cash_flows[1:]) - investment) / investment) * 100
        }
```
