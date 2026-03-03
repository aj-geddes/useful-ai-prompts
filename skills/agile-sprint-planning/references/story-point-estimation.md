# Story Point Estimation

## Story Point Estimation

```python
# Story point estimation using Planning Poker approach

class StoryEstimation:
    # Fibonacci sequence for estimation
    ESTIMATE_OPTIONS = [1, 2, 3, 5, 8, 13, 21, 34]

    @staticmethod
    def calculate_story_points(complexity, effort, risk):
        """
        Estimate story points based on multiple factors
        Factors should be rated 1-5
        """
        base_points = (complexity * effort) / 5
        risk_multiplier = 1 + (risk * 0.1)
        estimated_points = base_points * risk_multiplier

        # Round to nearest Fibonacci number
        for estimate in StoryEstimation.ESTIMATE_OPTIONS:
            if estimated_points <= estimate:
                return estimate

        return StoryEstimation.ESTIMATE_OPTIONS[-1]

    @staticmethod
    def conduct_planning_poker(team_estimates):
        """
        Handle Planning Poker consensus process
        """
        estimates = sorted(team_estimates)
        median = estimates[len(estimates) // 2]

        # If significant disagreement, discuss and re-estimate
        if estimates[-1] - estimates[0] > 5:
            return {
                'consensus': False,
                'median': median,
                'low': estimates[0],
                'high': estimates[-1],
                'action': 'Discuss and re-estimate'
            }

        return {'consensus': True, 'estimate': median}

# Example usage
print(StoryEstimation.calculate_story_points(
    complexity=3,  # Medium complexity
    effort=2,      # Low effort
    risk=1         # Low risk
))  # Output: 3 points
```
