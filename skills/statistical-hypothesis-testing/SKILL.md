---
name: Statistical Hypothesis Testing
description: Conduct statistical tests including t-tests, chi-square, ANOVA, and p-value analysis for statistical significance, hypothesis validation, and A/B testing
---

# Statistical Hypothesis Testing

## Overview

Hypothesis testing provides a framework for making data-driven decisions by testing whether observed differences are statistically significant or due to chance.

## Testing Framework

- **Null Hypothesis (H0)**: No effect or difference exists
- **Alternative Hypothesis (H1)**: Effect or difference exists
- **Significance Level (α)**: Threshold for rejecting H0 (typically 0.05)
- **P-value**: Probability of observing data if H0 is true

## Common Tests

- **T-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-square**: Test independence of categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Kruskal-Wallis**: Non-parametric alternative to ANOVA

## Implementation with Python

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Sample data
group_a = np.random.normal(100, 15, 50)  # Mean=100, SD=15
group_b = np.random.normal(105, 15, 50)  # Mean=105, SD=15

# Test 1: Independent samples t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"T-test: t={t_stat:.4f}, p-value={p_value:.4f}")
if p_value < 0.05:
    print("Reject null hypothesis: Groups are significantly different")
else:
    print("Fail to reject null hypothesis: No significant difference")

# Test 2: Paired t-test (same subjects, two conditions)
before = np.array([85, 90, 88, 92, 87, 89, 91, 86, 88, 90])
after = np.array([92, 95, 91, 98, 94, 96, 99, 93, 95, 97])

t_stat, p_value = stats.ttest_rel(before, after)
print(f"\nPaired t-test: t={t_stat:.4f}, p-value={p_value:.4f}")

# Test 3: One-way ANOVA (multiple groups)
group1 = np.random.normal(100, 10, 30)
group2 = np.random.normal(105, 10, 30)
group3 = np.random.normal(102, 10, 30)

f_stat, p_value = stats.f_oneway(group1, group2, group3)
print(f"\nANOVA: F={f_stat:.4f}, p-value={p_value:.4f}")

# Test 4: Chi-square test (categorical variables)
# Create contingency table
contingency = np.array([
    [50, 30],  # Control: success, failure
    [45, 35]   # Treatment: success, failure
])

chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
print(f"\nChi-square: χ²={chi2:.4f}, p-value={p_value:.4f}")

# Test 5: Mann-Whitney U test (non-parametric)
u_stat, p_value = stats.mannwhitneyu(group_a, group_b)
print(f"\nMann-Whitney U: U={u_stat:.4f}, p-value={p_value:.4f}")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Distribution comparison
axes[0, 0].hist(group_a, alpha=0.5, label='Group A', bins=20)
axes[0, 0].hist(group_b, alpha=0.5, label='Group B', bins=20)
axes[0, 0].set_title('Group Distributions')
axes[0, 0].legend()

# Q-Q plot for normality
stats.probplot(group_a, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Q-Q Plot (Group A)')

# Before/After comparison
axes[1, 0].plot(before, 'o-', label='Before', alpha=0.7)
axes[1, 0].plot(after, 's-', label='After', alpha=0.7)
axes[1, 0].set_title('Paired Comparison')
axes[1, 0].legend()

# Effect size (Cohen's d)
cohens_d = (np.mean(group_a) - np.mean(group_b)) / np.sqrt(
    ((len(group_a)-1)*np.var(group_a, ddof=1) +
     (len(group_b)-1)*np.var(group_b, ddof=1)) /
    (len(group_a) + len(group_b) - 2)
)
axes[1, 1].text(0.5, 0.5, f"Cohen's d = {cohens_d:.4f}",
                ha='center', va='center', fontsize=14)
axes[1, 1].axis('off')

plt.tight_layout()
plt.show()

# Normality test (Shapiro-Wilk)
stat, p = stats.shapiro(group_a)
print(f"\nShapiro-Wilk normality test: W={stat:.4f}, p-value={p:.4f}")

# Effect size calculation
def calculate_effect_size(group1, group2):
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    cohens_d = (np.mean(group1) - np.mean(group2)) / pooled_std
    return cohens_d

effect_size = calculate_effect_size(group_a, group_b)
print(f"Effect size (Cohen's d): {effect_size:.4f}")

# Confidence intervals
from scipy.stats import t as t_dist

def calculate_ci(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    se = np.std(data, ddof=1) / np.sqrt(n)
    margin = t_dist.ppf((1 + confidence) / 2, n - 1) * se
    return mean - margin, mean + margin

ci = calculate_ci(group_a)
print(f"95% CI for Group A: ({ci[0]:.2f}, {ci[1]:.2f})")

# Additional tests and visualizations

# Test 6: Levene's test for equal variances
stat_levene, p_levene = stats.levene(group_a, group_b)
print(f"\nLevene's Test for Equal Variance:")
print(f"Statistic: {stat_levene:.4f}, P-value: {p_levene:.4f}")

# Test 7: Welch's t-test (doesn't assume equal variance)
t_stat_welch, p_welch = stats.ttest_ind(group_a, group_b, equal_var=False)
print(f"\nWelch's t-test (unequal variance):")
print(f"t-stat: {t_stat_welch:.4f}, p-value: {p_welch:.4f}")

# Power analysis
from scipy.stats import nct
def calculate_power(effect_size, sample_size, alpha=0.05):
    t_critical = stats.t.ppf(1 - alpha/2, 2*sample_size - 2)
    ncp = effect_size * np.sqrt(sample_size / 2)
    power = 1 - stats.nct.cdf(t_critical, 2*sample_size - 2, ncp)
    return power

power = calculate_power(abs(effect_size), len(group_a))
print(f"\nStatistical Power: {power:.2%}")

# Bootstrap confidence intervals
def bootstrap_ci(data, n_bootstrap=10000, ci=95):
    bootstrap_means = []
    for _ in range(n_bootstrap):
        sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_means.append(np.mean(sample))
    lower = np.percentile(bootstrap_means, (100-ci)/2)
    upper = np.percentile(bootstrap_means, ci + (100-ci)/2)
    return lower, upper

boot_ci = bootstrap_ci(group_a)
print(f"\nBootstrap 95% CI for Group A: ({boot_ci[0]:.2f}, {boot_ci[1]:.2f})")

# Multiple testing correction (Bonferroni)
num_tests = 4
bonferroni_alpha = 0.05 / num_tests
print(f"\nBonferroni Corrected Alpha: {bonferroni_alpha:.4f}")
print(f"Use this threshold for {num_tests} tests")

# Test 8: Kruskal-Wallis test (non-parametric ANOVA)
h_stat, p_kw = stats.kruskal(group1, group2, group3)
print(f"\nKruskal-Wallis Test (non-parametric ANOVA):")
print(f"H-statistic: {h_stat:.4f}, p-value: {p_kw:.4f}")

# Effect size for ANOVA
f_stat, p_anova = stats.f_oneway(group1, group2, group3)
# Calculate eta-squared
grand_mean = np.mean([group1, group2, group3])
ss_between = sum(len(g) * (np.mean(g) - grand_mean)**2 for g in [group1, group2, group3])
ss_total = sum((x - grand_mean)**2 for g in [group1, group2, group3] for x in g)
eta_squared = ss_between / ss_total
print(f"\nEffect Size (Eta-squared): {eta_squared:.4f}")
```

## Interpretation Guidelines

- **p < 0.05**: Statistically significant (reject H0)
- **p ≥ 0.05**: Not statistically significant (fail to reject H0)
- **Effect size**: Magnitude of the difference (small/medium/large)
- **Confidence intervals**: Range of plausible parameter values

## Assumptions Checklist

- Independence of observations
- Normality of distributions (parametric tests)
- Homogeneity of variance
- Appropriate sample size
- Random sampling

## Common Pitfalls

- Misinterpreting p-values
- Multiple testing without correction
- Ignoring effect sizes
- Violating test assumptions
- Confusing correlation with causation

## Deliverables

- Test results with p-values and test statistics
- Effect size calculations
- Visualization of distributions
- Confidence intervals
- Interpretation and business implications
