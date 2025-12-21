---
name: Data Cleaning Pipeline
description: Build robust processes for data cleaning, missing value imputation, outlier handling, and data transformation for data preprocessing, data quality, and data pipeline automation
---

# Data Cleaning Pipeline

## Overview

Data cleaning pipelines transform raw, messy data into clean, standardized formats suitable for analysis and modeling through systematic handling of missing values, outliers, and data quality issues.

## When to Use

- Preparing raw datasets for analysis or modeling
- Handling missing values and data quality issues
- Removing duplicates and standardizing formats
- Detecting and treating outliers
- Building automated data preprocessing workflows
- Ensuring data integrity and consistency

## Core Components

- **Missing Value Handling**: Imputation and removal strategies
- **Outlier Detection & Treatment**: Identifying and handling anomalies
- **Data Type Standardization**: Ensuring correct data types
- **Duplicate Removal**: Identifying and removing duplicates
- **Normalization & Scaling**: Standardizing value ranges
- **Text Cleaning**: Handling text data

## Cleaning Strategies

- **Deletion**: Removing rows or columns
- **Imputation**: Filling with mean, median, or predictive models
- **Transformation**: Converting between formats
- **Validation**: Ensuring data integrity rules

## Implementation with Python

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer, KNNImputer

# Load raw data
df = pd.read_csv('raw_data.csv')

# Step 1: Identify and handle missing values
print("Missing values:\n", df.isnull().sum())

# Strategy 1: Delete rows with critical missing values
df = df.dropna(subset=['customer_id', 'transaction_date'])

# Strategy 2: Impute numerical columns with median
imputer = SimpleImputer(strategy='median')
df['age'] = imputer.fit_transform(df[['age']])

# Strategy 3: Use KNN imputation for related features
knn_imputer = KNNImputer(n_neighbors=5)
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = knn_imputer.fit_transform(df[numeric_cols])

# Strategy 4: Fill categorical with mode
df['category'] = df['category'].fillna(df['category'].mode()[0])

# Step 2: Handle duplicates
print(f"Duplicate rows: {df.duplicated().sum()}")
df = df.drop_duplicates()

# Duplicate on specific columns
df = df.drop_duplicates(subset=['customer_id', 'transaction_date'])

# Step 3: Outlier detection and handling
Q1 = df['amount'].quantile(0.25)
Q3 = df['amount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df = df[(df['amount'] >= lower_bound) & (df['amount'] <= upper_bound)]

# Alternative: Cap outliers
df['amount'] = df['amount'].clip(lower=lower_bound, upper=upper_bound)

# Step 4: Data type standardization
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['customer_id'] = df['customer_id'].astype('int64')
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Step 5: Text cleaning
df['name'] = df['name'].str.strip().str.lower()
df['name'] = df['name'].str.replace('[^a-z0-9\s]', '', regex=True)

# Step 6: Normalization and scaling
scaler = StandardScaler()
df[['age', 'income']] = scaler.fit_transform(df[['age', 'income']])

# MinMax scaling for bounded range [0, 1]
minmax_scaler = MinMaxScaler()
df[['score']] = minmax_scaler.fit_transform(df[['score']])

# Step 7: Create data quality report
def create_quality_report(df_original, df_cleaned):
    report = {
        'Original rows': len(df_original),
        'Cleaned rows': len(df_cleaned),
        'Rows removed': len(df_original) - len(df_cleaned),
        'Removal percentage': ((len(df_original) - len(df_cleaned)) / len(df_original) * 100),
        'Original missing': df_original.isnull().sum().sum(),
        'Cleaned missing': df_cleaned.isnull().sum().sum(),
    }
    return pd.DataFrame(report, index=[0])

quality = create_quality_report(df, df)
print(quality)

# Step 8: Validation checks
assert df['age'].isnull().sum() == 0, "Age has missing values"
assert df['transaction_date'].dtype == 'datetime64[ns]', "Date not datetime"
assert (df['amount'] >= 0).all(), "Negative amounts detected"

print("Data cleaning pipeline completed successfully!")
```

## Pipeline Architecture

```python
class DataCleaningPipeline:
    def __init__(self):
        self.cleaner_steps = []

    def add_step(self, func, description):
        self.cleaner_steps.append((func, description))
        return self

    def execute(self, df):
        for func, desc in self.cleaner_steps:
            print(f"Executing: {desc}")
            df = func(df)
        return df

# Usage
pipeline = DataCleaningPipeline()
pipeline.add_step(
    lambda df: df.dropna(subset=['customer_id']),
    "Remove rows with missing customer_id"
).add_step(
    lambda df: df.drop_duplicates(),
    "Remove duplicate rows"
).add_step(
    lambda df: df[(df['amount'] > 0) & (df['amount'] < 100000)],
    "Filter invalid amount ranges"
)

df_clean = pipeline.execute(df)
```

## Advanced Cleaning Techniques

```python
# Step 9: Feature-specific cleaning
df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)  # Remove non-digits

# Step 10: Datetime handling
df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
df['days_since_creation'] = (pd.Timestamp.now() - df['created_date']).dt.days

# Step 11: Categorical standardization
df['status'] = df['status'].str.lower().str.strip()
df['status'] = df['status'].replace({
    'active': 'active',
    'inactive': 'inactive',
    'pending': 'pending',
})

# Step 12: Numeric constraint checking
df['age'] = df['age'].where((df['age'] >= 0) & (df['age'] <= 150), np.nan)
df['percentage'] = df['percentage'].where((df['percentage'] >= 0) & (df['percentage'] <= 100), np.nan)

# Step 13: Create data quality score
quality_score = {
    'Missing %': (df.isnull().sum() / len(df) * 100).mean(),
    'Duplicates %': (df.duplicated().sum() / len(df) * 100),
    'Complete Features': (df.notna().sum() / len(df)).mean() * 100,
}

# Step 14: Generate cleaning report
cleaning_report = f"""
DATA CLEANING REPORT
====================
Rows removed: {len(df) - len(df_clean)}
Columns: {len(df_clean.columns)}
Remaining rows: {len(df_clean)}
Completeness: {(df_clean.notna().sum().sum() / (len(df_clean) * len(df_clean.columns)) * 100):.1f}%
"""
print(cleaning_report)
```

## Key Decisions

- How to handle missing values (delete vs impute)?
- Which outliers are legitimate business cases?
- What are acceptable value ranges?
- Which duplicates are true duplicates?
- How to standardize categorical values?

## Validation Steps

- Check for data type consistency
- Verify value ranges are reasonable
- Confirm no unintended data loss
- Document all transformations applied
- Create audit trail of changes

## Deliverables

- Cleaned dataset with quality metrics
- Data cleaning log documenting all steps
- Validation report confirming data integrity
- Before/after comparison statistics
- Cleaning code and pipeline documentation
