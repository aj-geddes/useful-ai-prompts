---
name: Correlation Analysis
description: Measure relationships between variables using correlation coefficients, correlation matrices, and association tests for correlation measurement, relationship analysis, and multicollinearity detection
---

# Correlation Analysis

## Overview

Correlation analysis measures the strength and direction of relationships between variables, helping identify which features are related and detect multicollinearity.

## When to Use

- Identifying relationships between numerical variables
- Detecting multicollinearity before regression modeling
- Exploratory data analysis to understand feature dependencies
- Feature selection and dimensionality reduction
- Validating assumptions about variable relationships
- Comparing linear and non-linear associations

## Correlation Types

- **Pearson**: Linear correlation (continuous variables)
- **Spearman**: Rank-based correlation (ordinal/non-linear)
- **Kendall**: Rank correlation (robust alternative)
- **Cramér's V**: Association for categorical variables
- **Mutual Information**: Non-linear dependencies

## Key Concepts

- **Correlation Coefficient**: Ranges from -1 to +1
- **Positive Correlation**: Variables move together
- **Negative Correlation**: Variables move oppositely
- **Multicollinearity**: High correlations between predictors

## Implementation with Python

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, kendalltau

# Sample data
np.random.seed(42)
n = 200
age = np.random.uniform(20, 70, n)
income = age * 2000 + np.random.normal(0, 10000, n)
education_years = age / 2 + np.random.normal(0, 3, n)
satisfaction = income / 50000 + np.random.normal(0, 0.5, n)

df = pd.DataFrame({
    'age': age,
    'income': income,
    'education_years': education_years,
    'satisfaction': satisfaction,
    'years_employed': age - education_years - 6
})

# Pearson correlation (linear)
corr_matrix = df.corr(method='pearson')
print("Pearson Correlation Matrix:")
print(corr_matrix)

# Individual correlation with p-value
corr_coef, p_value = pearsonr(df['age'], df['income'])
print(f"\nPearson correlation (age vs income): r={corr_coef:.4f}, p-value={p_value:.4f}")

# Spearman correlation (rank-based)
spearman_matrix = df.corr(method='spearman')
print("\nSpearman Correlation Matrix:")
print(spearman_matrix)

spearman_coef, p_value = spearmanr(df['age'], df['income'])
print(f"Spearman correlation (age vs income): rho={spearman_coef:.4f}, p-value={p_value:.4f}")

# Kendall tau correlation
kendall_coef, p_value = kendalltau(df['age'], df['income'])
print(f"Kendall correlation (age vs income): tau={kendall_coef:.4f}, p-value={p_value:.4f}")

# Correlation heatmap
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Pearson heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, ax=axes[0], vmin=-1, vmax=1)
axes[0].set_title('Pearson Correlation Heatmap')

# Spearman heatmap
sns.heatmap(spearman_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, ax=axes[1], vmin=-1, vmax=1)
axes[1].set_title('Spearman Correlation Heatmap')

plt.tight_layout()
plt.show()

# Correlation with significance testing
def correlation_with_pvalue(df):
    rows, cols = [], []
    for col1 in df.columns:
        for col2 in df.columns:
            if col1 < col2:  # Avoid duplicates
                r, p = pearsonr(df[col1], df[col2])
                rows.append({
                    'Variable 1': col1,
                    'Variable 2': col2,
                    'Correlation': r,
                    'P-value': p,
                    'Significant': 'Yes' if p < 0.05 else 'No'
                })
    return pd.DataFrame(rows)

corr_table = correlation_with_pvalue(df)
print("\nCorrelation with P-values:")
print(corr_table)

# Scatter plots with regression lines
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

pairs = [('age', 'income'), ('age', 'education_years'),
         ('income', 'satisfaction'), ('education_years', 'years_employed')]

for idx, (var1, var2) in enumerate(pairs):
    ax = axes[idx // 2, idx % 2]
    ax.scatter(df[var1], df[var2], alpha=0.5)

    # Add regression line
    z = np.polyfit(df[var1], df[var2], 1)
    p = np.poly1d(z)
    x_line = np.linspace(df[var1].min(), df[var1].max(), 100)
    ax.plot(x_line, p(x_line), "r--", linewidth=2)

    r, p_val = pearsonr(df[var1], df[var2])
    ax.set_title(f'{var1} vs {var2}\nr={r:.4f}, p={p_val:.4f}')
    ax.set_xlabel(var1)
    ax.set_ylabel(var2)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Multicollinearity detection (VIF)
from statsmodels.stats.outliers_influence import variance_inflation_factor

X = df[['age', 'education_years', 'years_employed']]
vif_data = pd.DataFrame()
vif_data['Variable'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print("\nVariance Inflation Factor (VIF):")
print(vif_data)
print("\nVIF > 10: High multicollinearity")
print("VIF > 5: Moderate multicollinearity")

# Partial correlation (controlling for confounding)
def partial_correlation(df, x, y, control_vars):
    from scipy.stats import linregress

    # Residuals of x after removing control variables
    x_residuals = df[x] - np.poly1d(
        np.polyfit(df[control_vars].values, df[x], deg=1)
    )(df[control_vars].values)

    # Residuals of y after removing control variables
    y_residuals = df[y] - np.poly1d(
        np.polyfit(df[control_vars].values, df[y], deg=1)
    )(df[control_vars].values)

    return pearsonr(x_residuals, y_residuals)[0]

partial_corr = partial_correlation(df, 'income', 'satisfaction', ['age'])
print(f"\nPartial correlation (income vs satisfaction, controlling for age): {partial_corr:.4f}")

# Distance correlation (non-linear relationships)
try:
    from dcor import distance_correlation
    dist_corr = distance_correlation(df['age'], df['income'])
    print(f"Distance correlation (age vs income): {dist_corr:.4f}")
except ImportError:
    print("dcor library not installed for distance correlation")

# Correlation stability over time
fig, ax = plt.subplots(figsize=(12, 5))

rolling_corr = df['age'].rolling(window=50).corr(df['income'])
ax.plot(rolling_corr.index, rolling_corr.values)
ax.set_title('Rolling Correlation (age vs income, window=50)')
ax.set_ylabel('Correlation Coefficient')
ax.grid(True, alpha=0.3)
plt.show()
```

## Interpretation Guidelines

- **|r| = 0.0-0.3**: Weak correlation
- **|r| = 0.3-0.7**: Moderate correlation
- **|r| = 0.7-1.0**: Strong correlation
- **p < 0.05**: Statistically significant
- **High VIF (>10)**: Multicollinearity problem

## Important Notes

- Correlation ≠ Causation
- Non-linear relationships missed by Pearson
- Outliers can distort correlations
- Sample size affects significance
- Temporal trends can create spurious correlations

## Visualization Strategies

- Heatmaps for overview
- Scatter plots for relationships
- Pair plots for multivariate analysis
- Rolling correlations for time-varying relationships

## Deliverables

- Correlation matrices (Pearson, Spearman)
- Correlation heatmaps with annotations
- Statistical significance table
- Scatter plots with regression lines
- Multicollinearity assessment (VIF)
- Partial correlation analysis
- Relationship interpretation report
