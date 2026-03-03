# Three-Point Estimation (PERT)

## Three-Point Estimation (PERT)

```python
# Three-point estimation technique for uncertainty

class ThreePointEstimation:
    @staticmethod
    def calculate_pert_estimate(optimistic, most_likely, pessimistic):
        """
        PERT formula: (O + 4M + P) / 6
        Weighted toward most likely estimate
        """
        pert = (optimistic + 4 * most_likely + pessimistic) / 6
        return round(pert, 2)

    @staticmethod
    def calculate_standard_deviation(optimistic, pessimistic):
        """Standard deviation for risk analysis"""
        sigma = (pessimistic - optimistic) / 6
        return round(sigma, 2)

    @staticmethod
    def calculate_confidence_interval(pert_estimate, std_dev, confidence=0.95):
        """
        Calculate confidence interval for estimate
        95% confidence ≈ ±2 sigma
        """
        z_score = 1.96 if confidence == 0.95 else 2.576
        margin = z_score * std_dev

        return {
            'estimate': pert_estimate,
            'lower_bound': round(pert_estimate - margin, 2),
            'upper_bound': round(pert_estimate + margin, 2),
            'range': f"{pert_estimate - margin:.1f} - {pert_estimate + margin:.1f}"
        }

# Example
optimistic = 10  # best case
most_likely = 20  # expected
pessimistic = 40  # worst case

pert = ThreePointEstimation.calculate_pert_estimate(optimistic, most_likely, pessimistic)
std_dev = ThreePointEstimation.calculate_standard_deviation(optimistic, pessimistic)
confidence = ThreePointEstimation.calculate_confidence_interval(pert, std_dev)

print(f"PERT Estimate: {pert} days")
print(f"Standard Deviation: {std_dev}")
print(f"95% Confidence Range: {confidence['range']}")
```
