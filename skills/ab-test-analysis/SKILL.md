---
name: A/B Test Analysis
description: Design and analyze A/B tests, calculate statistical significance, and determine sample sizes for conversion optimization and experiment validation
---

# A/B Test Analysis

## Overview

A/B testing is a statistical method to compare two variants and determine which performs better, enabling data-driven optimization decisions.

## When to Use

- Comparing two versions of a product feature, webpage, or marketing campaign
- Optimizing conversion rates, click-through rates, or user engagement metrics
- Making data-driven decisions with statistical confidence about changes
- Determining sample size requirements for experiment validity
- Analyzing treatment effects and measuring lift from interventions
- Evaluating whether observed differences are statistically significant

## Core Components

- **Control Group**: Original version (A)
- **Treatment Group**: New variant (B)
- **Metric**: Outcome being measured
- **Sample Size**: Observations needed for power
- **Significance Level**: Type I error threshold (α = 0.05)
- **Power**: 1 - Type II error (typically 0.80)

## Analysis Steps

1. Define success metric
2. Calculate sample size
3. Run experiment
4. Check assumptions
5. Perform statistical test
6. Calculate effect size
7. Interpret results

## Implementation with Python

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import binom_test, ttest_ind, chi2_contingency
import seaborn as sns

# Sample A/B test data
np.random.seed(42)

# Scenario: Testing new checkout flow
control_conversions = np.random.binomial(1, 0.10, 10000)
treatment_conversions = np.random.binomial(1, 0.12, 10000)

control_revenue = np.random.exponential(50, 10000)
treatment_revenue = np.random.exponential(55, 10000)

# Create dataframes
df_control = pd.DataFrame({
    'group': 'Control',
    'converted': control_conversions,
    'revenue': control_revenue,
})

df_treatment = pd.DataFrame({
    'group': 'Treatment',
    'converted': treatment_conversions,
    'revenue': treatment_revenue,
})

df = pd.concat([df_control, df_treatment], ignore_index=True)

print("A/B Test Data Summary:")
print(df.groupby('group')[['converted', 'revenue']].agg({
    'converted': ['sum', 'count', 'mean'],
    'revenue': ['sum', 'mean', 'std'],
}))

# 1. Conversion Rate Test (Chi-square)
contingency_table = pd.crosstab(df['group'], df['converted'])
print("\nContingency Table:")
print(contingency_table)

chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"\nChi-square Test:")
print(f"Chi2 statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Significant: {'Yes' if p_value < 0.05 else 'No'}")

# 2. Conversion Rate Calculation
control_cr = df[df['group'] == 'Control']['converted'].mean()
treatment_cr = df[df['group'] == 'Treatment']['converted'].mean()
lift = (treatment_cr - control_cr) / control_cr * 100

print(f"\nConversion Rates:")
print(f"Control: {control_cr:.4f} ({control_cr*100:.2f}%)")
print(f"Treatment: {treatment_cr:.4f} ({treatment_cr*100:.2f}%)")
print(f"Lift: {lift:.2f}%")

# 3. Revenue Per User Test (T-test)
control_revenue = df[df['group'] == 'Control']['revenue']
treatment_revenue = df[df['group'] == 'Treatment']['revenue']

t_stat, p_value_revenue = ttest_ind(control_revenue, treatment_revenue)
print(f"\nRevenue Per User T-test:")
print(f"Control Mean: ${control_revenue.mean():.2f}")
print(f"Treatment Mean: ${treatment_revenue.mean():.2f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value_revenue:.4f}")
print(f"Significant: {'Yes' if p_value_revenue < 0.05 else 'No'}")

# 4. Effect Size (Cohen's d)
def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std

effect_size = cohens_d(control_revenue, treatment_revenue)
print(f"\nEffect Size (Cohen's d): {effect_size:.4f}")
print("Interpretation: " + {
    True: "Small effect (|d| < 0.2)",
    False: {
        True: "Medium effect (0.2 <= |d| < 0.8)",
        False: "Large effect (|d| >= 0.8)"
    }[abs(effect_size) < 0.8]
}[abs(effect_size) < 0.2])

# 5. Confidence Intervals
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    se = stats.sem(data)
    margin = se * stats.t.ppf((1 + confidence) / 2, n - 1)
    return mean - margin, mean + margin

ci_control = confidence_interval(control_revenue)
ci_treatment = confidence_interval(treatment_revenue)

print(f"\n95% Confidence Intervals:")
print(f"Control: (${ci_control[0]:.2f}, ${ci_control[1]:.2f})")
print(f"Treatment: (${ci_treatment[0]:.2f}, ${ci_treatment[1]:.2f})")

# 6. Sample Size Calculation
def calculate_sample_size(baseline_cr, target_cr, significance=0.05, power=0.80):
    from scipy.stats import norm
    effect_size = 2 * (np.arcsin(np.sqrt(target_cr)) - np.arcsin(np.sqrt(baseline_cr)))
    z_alpha = norm.ppf(1 - significance/2)
    z_beta = norm.ppf(power)
    n = ((z_alpha + z_beta) / effect_size) ** 2
    return int(np.ceil(n))

sample_size_needed = calculate_sample_size(control_cr, treatment_cr)
print(f"\nSample Size Analysis:")
print(f"Baseline CR: {control_cr:.4f}")
print(f"Target CR: {treatment_cr:.4f}")
print(f"Required per group: {sample_size_needed:,}")
print(f"Actual per group: {len(df[df['group'] == 'Control']):,}")

# 7. Sequential Testing / Running Analysis
fig, axes = plt.subplots(2, 2, figsize=(14, 8))

# Cumulative conversion rates
control_cumsum = df[df['group'] == 'Control']['converted'].cumsum()
treatment_cumsum = df[df['group'] == 'Treatment']['converted'].cumsum()
control_n = np.arange(1, len(control_cumsum) + 1)
treatment_n = np.arange(1, len(treatment_cumsum) + 1)

axes[0, 0].plot(control_n, control_cumsum / control_n, label='Control', alpha=0.7)
axes[0, 0].plot(treatment_n, treatment_cumsum / treatment_n, label='Treatment', alpha=0.7)
axes[0, 0].set_xlabel('Sample Size')
axes[0, 0].set_ylabel('Conversion Rate')
axes[0, 0].set_title('Conversion Rate Over Time')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Distribution comparison
axes[0, 1].hist(control_revenue, bins=50, alpha=0.5, label='Control', density=True)
axes[0, 1].hist(treatment_revenue, bins=50, alpha=0.5, label='Treatment', density=True)
axes[0, 1].set_xlabel('Revenue')
axes[0, 1].set_ylabel('Density')
axes[0, 1].set_title('Revenue Distribution')
axes[0, 1].legend()

# Box plot comparison
data_box = [control_revenue, treatment_revenue]
axes[1, 0].boxplot(data_box, labels=['Control', 'Treatment'])
axes[1, 0].set_ylabel('Revenue')
axes[1, 0].set_title('Revenue Distribution (Box Plot)')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# Conversion comparison
conversion_data = pd.DataFrame({
    'Group': ['Control', 'Treatment'],
    'Converted': [control_conversions.sum(), treatment_conversions.sum()],
    'Not Converted': [len(control_conversions) - control_conversions.sum(),
                      len(treatment_conversions) - treatment_conversions.sum()],
})
conversion_data.set_index('Group')[['Converted', 'Not Converted']].plot(
    kind='bar', ax=axes[1, 1], color=['green', 'red'], edgecolor='black'
)
axes[1, 1].set_title('Conversion Comparison')
axes[1, 1].set_ylabel('Count')
axes[1, 1].legend(title='Status')

plt.tight_layout()
plt.show()

# 8. Bayesian Perspective
print("\n8. Bayesian Analysis (informative):")
from scipy.stats import beta

# Assume prior Beta(1, 1) - uninformative
control_successes = control_conversions.sum()
control_failures = len(control_conversions) - control_successes
treatment_successes = treatment_conversions.sum()
treatment_failures = len(treatment_conversions) - treatment_successes

# Posterior distributions
posterior_control = beta(1 + control_successes, 1 + control_failures)
posterior_treatment = beta(1 + treatment_successes, 1 + treatment_failures)

samples_control = posterior_control.rvs(10000)
samples_treatment = posterior_treatment.rvs(10000)

prob_treatment_better = (samples_treatment > samples_control).mean()
print(f"Probability Treatment > Control: {prob_treatment_better:.4f}")

# Visualization
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(samples_control, bins=50, alpha=0.5, label='Control', density=True)
ax.hist(samples_treatment, bins=50, alpha=0.5, label='Treatment', density=True)
ax.set_xlabel('Conversion Rate')
ax.set_ylabel('Density')
ax.set_title('Bayesian Posterior Distributions')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()

# 9. Summary Report
print("\n" + "="*50)
print("A/B TEST SUMMARY REPORT")
print("="*50)
print(f"Metric: Conversion Rate")
print(f"Control CR: {control_cr*100:.2f}%")
print(f"Treatment CR: {treatment_cr*100:.2f}%")
print(f"Lift: {lift:.2f}%")
print(f"P-value: {p_value:.4f}")
print(f"Result: {'REJECT H0 - Significant Difference' if p_value < 0.05 else 'FAIL TO REJECT H0 - No Significant Difference'}")
print(f"Winner: {f'Treatment (+{lift:.2f}%)' if p_value < 0.05 and lift > 0 else 'Control (No clear winner)'}")
print("="*50)
```

## Sample Size Determination

- **Baseline conversion rate**: Current performance
- **Target effect size**: Minimum detectable difference
- **Significance level (α)**: Usually 0.05
- **Power (1-β)**: Usually 0.80 or 0.90

## Key Metrics

- **Conversion Rate**: Proportion of successes
- **Revenue Per User**: Average transaction value
- **Click-through Rate**: Ad performance
- **Engagement**: Feature adoption

## Deliverables

- Test design document
- Sample size calculations
- Statistical test results
- Effect size measurements
- Confidence intervals
- Visualization of results
- Executive summary with recommendation
