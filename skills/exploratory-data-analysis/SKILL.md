---
name: Exploratory Data Analysis
description: Discover patterns, distributions, and relationships in data through visualization, summary statistics, and hypothesis generation for exploratory data analysis, data profiling, and initial insights
---

# Exploratory Data Analysis (EDA)

## Overview

Exploratory Data Analysis (EDA) is the critical first step in data science projects, systematically examining datasets to understand their characteristics, identify patterns, and assess data quality before formal modeling.

## Core Concepts

- **Data Profiling**: Understanding basic statistics and data types
- **Distribution Analysis**: Examining how variables are distributed
- **Relationship Discovery**: Identifying patterns between variables
- **Anomaly Detection**: Finding outliers and unusual patterns
- **Data Quality Assessment**: Evaluating completeness and consistency

## When to Use

- Starting a new dataset analysis
- Understanding data before modeling
- Identifying data quality issues
- Generating hypotheses for testing
- Communicating insights to stakeholders

## Implementation with Python

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load and explore data
df = pd.read_csv('customer_data.csv')

# Basic profiling
print(f"Shape: {df.shape}")
print(f"Data types:\n{df.dtypes}")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")

# Statistical summary
print(df.describe())
print(df.describe(include='object'))

# Distribution analysis - numerical columns
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
df['age'].hist(bins=30, ax=axes[0, 0])
axes[0, 0].set_title('Age Distribution')

df['income'].hist(bins=30, ax=axes[0, 1])
axes[0, 1].set_title('Income Distribution')

# Box plots for outlier detection
df.boxplot(column='age', by='region', ax=axes[1, 0])
axes[1, 0].set_title('Age by Region')

# Categorical analysis
df['category'].value_counts().plot(kind='bar', ax=axes[1, 1])
axes[1, 1].set_title('Category Distribution')
plt.tight_layout()
plt.show()

# Correlation analysis
numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()

# Multivariate relationships
sns.pairplot(df[['age', 'income', 'education_years']], diag_kind='hist')
plt.show()

# Skewness and kurtosis
print("\nSkewness:")
print(numeric_df.skew())
print("\nKurtosis:")
print(numeric_df.kurtosis())

# Percentile analysis
print("\nPercentiles for Age:")
print(df['age'].quantile([0.25, 0.5, 0.75, 0.95, 0.99]))

# Missing data patterns
missing_pct = (df.isnull().sum() / len(df) * 100)
missing_pct[missing_pct > 0].sort_values(ascending=False)

# Value count analysis
print("\nCustomer Types Distribution:")
print(df['customer_type'].value_counts(normalize=True))

# Advanced EDA: Groupby analysis
print("\nGroupBy Analysis:")
print(df.groupby('region')[['age', 'income']].agg(['mean', 'median', 'std']))

# Correlation with target variable
if 'target' in df.columns:
    target_corr = df.corr()['target'].sort_values(ascending=False)
    print("\nFeature Correlation with Target:")
    print(target_corr)

# Data type breakdown
print("\nData Type Summary:")
print(df.dtypes.value_counts())

# Unique value count
print("\nUnique Value Counts:")
print(df.nunique().sort_values(ascending=False))

# Variance analysis
print("\nVariance per Feature:")
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    variance = df[col].var()
    print(f"  {col}: {variance:.2f}")

# Distribution patterns
for col in df.select_dtypes(include=[np.number]).columns:
    skew = df[col].skew()
    kurt = df[col].kurtosis()
    print(f"{col} - Skew: {skew:.2f}, Kurtosis: {kurt:.2f}")

# Bivariate analysis
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
df.groupby('region')['income'].mean().plot(kind='bar', ax=axes[0])
axes[0].set_title('Average Income by Region')
df.groupby('category')['age'].mean().plot(kind='bar', ax=axes[1])
axes[1].set_title('Average Age by Category')
plt.tight_layout()
plt.show()

# Summary statistics profile
print("\nComprehensive Data Profile:")
profile = {
    'Variable': df.columns,
    'Type': df.dtypes,
    'Non-Null Count': df.count(),
    'Null Count': df.isnull().sum(),
    'Unique Values': df.nunique(),
}
profile_df = pd.DataFrame(profile)
print(profile_df)
```

## Advanced EDA Techniques

```python
# Step 15: Interaction analysis
import itertools

numeric_cols = df.select_dtypes(include=[np.number]).columns
interaction_strengths = []

for col1, col2 in itertools.combinations(numeric_cols[:5], 2):
    interaction_score = abs(df[col1].corr(df[col2]))
    interaction_strengths.append({
        'Pair': f"{col1} × {col2}",
        'Correlation': interaction_score,
    })

interaction_df = pd.DataFrame(interaction_strengths).sort_values('Correlation', ascending=False)
print("\nTop Interactions:")
print(interaction_df.head())

# Step 16: Outlier summary
for col in numeric_cols:
    Q1, Q3 = df[col].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    if len(outliers) > 0:
        print(f"\n{col}: {len(outliers)} outliers detected ({len(outliers)/len(df)*100:.1f}%)")

# Step 17: Generate automated insights
print("\n" + "="*60)
print("AUTOMATED DATA INSIGHTS")
print("="*60)

for col in numeric_cols:
    skewness = df[col].skew()
    mean_val = df[col].mean()
    median_val = df[col].median()

    if abs(skewness) > 1:
        direction = "right" if skewness > 0 else "left"
        print(f"{col}: Highly {direction}-skewed distribution")

    if abs(mean_val - median_val) > 0.1 * median_val:
        print(f"{col}: Mean and median differ significantly")

print("="*60)
```

## Key Questions to Ask

1. What are the data dimensions and types?
2. How are key variables distributed?
3. What patterns exist between variables?
4. Are there obvious data quality issues?
5. What outliers or anomalies exist?
6. What hypotheses can we generate?

## Best Practices

- Start with data profiling before visualization
- Check data types and missing values early
- Visualize distributions before jumping to analysis
- Document interesting findings and anomalies
- Create summaries for stakeholder communication
- Use domain knowledge to interpret patterns

## Common Pitfalls

- Skipping data quality checks
- Over-interpreting patterns in small datasets
- Ignoring domain context
- Insufficient data visualization
- Not documenting findings systematically

## Deliverables

- Data quality report with missing values and duplicates
- Summary statistics and distribution charts
- Correlation and relationship visualizations
- List of notable patterns and anomalies
- Hypotheses for further investigation
- Data cleaning recommendations
