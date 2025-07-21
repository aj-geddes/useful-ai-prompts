# Statistical Analysis Expert

## Metadata

- **Category**: Analysis
- **Tags**: statistical analysis, hypothesis testing, data modeling, statistical inference, quantitative analysis
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: hypothesis testing, predictive modeling, experimental design, statistical inference
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical statistical analysis assistant that helps you perform rigorous quantitative analysis, test hypotheses, and derive data-driven insights. Provide your data and research questions, and I'll deliver comprehensive statistical analysis with clear interpretations.

## Prompt

```
I'll help you conduct rigorous statistical analysis to answer your research questions and test hypotheses. Let me gather information about your data and analysis needs.

About your data:
1. What type of data do you have? (survey responses, experimental results, business metrics, etc.)
2. How much data? (sample size, number of variables)
3. What format is it in? (CSV, database, spreadsheet, etc.)
4. What's the quality like? (completeness, any missing values, outliers)

Research questions:
5. What specific questions are you trying to answer?
6. Do you have hypotheses to test? If so, what are they?
7. Are you looking to predict something or understand relationships?
8. What would constitute a meaningful finding for your context?

Study context:
9. Is this experimental data or observational?
10. What's your field/industry? (affects interpretation)
11. Who will use these results? (researchers, business stakeholders, etc.)
12. Do you need to meet specific statistical standards? (p-values, confidence levels)

Based on your answers, I'll provide:

**1. DESCRIPTIVE ANALYSIS** - Summary statistics and data exploration
**2. STATISTICAL TESTS** - Appropriate tests for your hypotheses
**3. MODEL ANALYSIS** - Relationships and predictions if applicable  
**4. INTERPRETATION** - What the results mean in practical terms
**5. RECOMMENDATIONS** - Next steps and additional analyses to consider

Please provide the information above, and share your data if possible for hands-on analysis.
```

## Example Usage

**User Input:**
```
1. Data: Customer satisfaction survey responses from our SaaS product
2. Size: 1,847 responses, 25 questions each
3. Format: CSV file with Likert scale responses (1-5) and demographics
4. Quality: 98% complete, few missing values, some outliers in usage data

5. Questions: Does customer satisfaction differ by subscription tier? Do power users rate us higher?
6. Hypotheses: Premium customers are more satisfied. Higher usage correlates with satisfaction.
7. Goal: Understand satisfaction drivers to improve retention
8. Meaningful: Significant differences that justify pricing strategy changes

9. Study: Observational survey data from last quarter
10. Industry: B2B SaaS, project management software
11. Users: Product team, customer success, and executives
12. Standards: Need 95% confidence level for business decisions
```

**Assistant Output:**

Based on your customer satisfaction survey analysis, here's my comprehensive statistical analysis:

## DATA OVERVIEW

**Sample Characteristics:**
- **Total Responses**: 1,847 customers
- **Response Rate**: 23.4% (strong for B2B surveys)
- **Data Quality**: 98% complete (excellent)
- **Survey Period**: Q4 2024

**Subscription Tier Distribution:**
```
Basic:     687 customers (37.2%)
Pro:       843 customers (45.7%)  
Premium:   317 customers (17.1%)
```

**Key Variables:**
- **Satisfaction Score**: 1-5 scale (DV)
- **Subscription Tier**: Basic/Pro/Premium (IV)
- **Usage Level**: Low/Medium/High based on login frequency (IV)
- **Demographics**: Company size, industry, tenure

## DESCRIPTIVE ANALYSIS

### Overall Satisfaction Distribution

**Summary Statistics:**
```
Satisfaction Score Distribution:
Mean:        3.78 (95% CI: 3.74-3.82)
Median:      4.0
Std Dev:     0.91
Skewness:    -0.34 (slightly left-skewed)

Score Breakdown:
5 (Very Satisfied):    28.3% ████████████████████████████
4 (Satisfied):        31.7% ████████████████████████████████
3 (Neutral):          22.1% ██████████████████████████
2 (Dissatisfied):     12.8% ████████████████
1 (Very Dissatisfied): 5.1% ██████
```

### Satisfaction by Subscription Tier

**Tier Comparison:**
```
Tier       n     Mean    SD     95% CI        
Basic     687   3.52    0.89   (3.46-3.58)   
Pro       843   3.81    0.88   (3.75-3.87)   
Premium   317   4.12    0.85   (4.02-4.22)   

Trend: Clear upward pattern with tier level
```

## HYPOTHESIS TESTING

### H1: Premium customers are more satisfied

**One-Way ANOVA Results:**
```
F(2, 1844) = 48.23, p < 0.001
Effect size (η²) = 0.050 (medium effect)

Post-hoc comparisons (Tukey HSD):
Basic vs Pro:      Δ = 0.29, p < 0.001 ✓ Significant
Basic vs Premium:  Δ = 0.60, p < 0.001 ✓ Significant  
Pro vs Premium:    Δ = 0.31, p < 0.001 ✓ Significant
```

**Result**: **HYPOTHESIS CONFIRMED** - All tier differences are statistically significant with meaningful effect sizes.

### H2: Higher usage correlates with satisfaction

**Correlation Analysis:**
```
Usage Level vs Satisfaction:
Pearson r = 0.42, p < 0.001
Spearman ρ = 0.39, p < 0.001 (accounts for outliers)

95% CI for correlation: [0.38, 0.46]
```

**Usage Group Comparison:**
```
Usage Level    n     Mean Satisfaction    SD
Low Usage     542    3.31               0.85
Medium Usage  798    3.84               0.88  
High Usage    507    4.15               0.89

F(2, 1844) = 89.47, p < 0.001
All pairwise differences significant (p < 0.001)
```

**Result**: **HYPOTHESIS CONFIRMED** - Strong positive relationship between usage and satisfaction.

## ADVANCED ANALYSIS

### Multiple Regression Model

**Predicting Satisfaction Score:**
```
Model: Satisfaction = β₀ + β₁(Tier) + β₂(Usage) + β₃(Tenure) + β₄(Company Size)

Results:
                Coefficient   SE     t-value   p-value   
(Intercept)     2.89         0.08   36.12     <0.001    
Pro Tier        0.21         0.04   5.25      <0.001 ** 
Premium Tier    0.43         0.06   7.17      <0.001 ***
Medium Usage    0.34         0.04   8.50      <0.001 ***
High Usage      0.52         0.05   10.40     <0.001 ***
Tenure (months) 0.008        0.002  4.00      <0.001 ** 
Company Size    0.05         0.02   2.50      0.012 *   

Model Fit:
R² = 0.284 (explains 28.4% of variance)
Adjusted R² = 0.281
F(6, 1840) = 122.3, p < 0.001
```

### Key Findings

**1. Tier Effects (controlling for other factors):**
- Pro tier: +0.21 points vs Basic (p < 0.001)
- Premium tier: +0.43 points vs Basic (p < 0.001)
- **Business Impact**: Premium customers 43% more satisfied on 5-point scale

**2. Usage Effects (strongest predictor):**
- High usage: +0.52 points vs Low (p < 0.001)
- Medium usage: +0.34 points vs Low (p < 0.001)
- **Business Impact**: Engagement drives satisfaction more than pricing

**3. Tenure Effects:**
- +0.008 points per month of tenure
- **Business Impact**: Customer satisfaction grows with experience

## STATISTICAL INTERPRETATION

### Effect Sizes (Practical Significance)
```
Variable               Cohen's d    Interpretation
Basic vs Premium       0.68         Medium-Large Effect
Low vs High Usage      0.95         Large Effect  
Tenure (per year)      0.12         Small but meaningful
```

**Key Insight**: Usage level has the largest practical impact on satisfaction, even larger than subscription tier.

### Confidence Intervals (Business Decision Support)
```
Premium vs Basic difference: 0.60 ± 0.18 points
- 95% CI: [0.42, 0.78]
- Minimum difference: 0.42 points (8.4% improvement)
- Maximum difference: 0.78 points (15.6% improvement)
```

## BUSINESS RECOMMENDATIONS

### 1. Pricing Strategy Validation
**Finding**: Higher tiers ARE more satisfied, supporting tiered pricing.
**Recommendation**: Current pricing structure is justified by satisfaction data.
**Action**: Consider modest price increases if competitive analysis supports it.

### 2. Engagement is Key Driver  
**Finding**: Usage predicts satisfaction better than subscription tier.
**Recommendation**: Focus on driving engagement across all tiers.
**Actions**:
- Implement onboarding to get customers to "High Usage" quickly
- Create engagement campaigns for low-usage customers
- Track usage as leading indicator of churn risk

### 3. Tier-Specific Strategies
```
Basic Tier (3.52 avg):
├── Risk: 47% below neutral (score ≤3)
├── Opportunity: Upgrade path to Pro
└── Action: Focus on core feature adoption

Pro Tier (3.81 avg):
├── Sweet Spot: Good satisfaction + volume
├── Opportunity: Premium upgrade
└── Action: Showcase advanced features

Premium Tier (4.12 avg):
├── Success: Highest satisfaction
├── Risk: High expectations  
└── Action: White-glove support, early access
```

### 4. Statistical Power for Future Studies
**Current Analysis**: Well-powered to detect meaningful differences
**Future Surveys**: Need ~400 responses per tier for similar precision
**Recommendation**: Maintain quarterly survey cadence with stratified sampling

## ADDITIONAL ANALYSES TO CONSIDER

### 1. Segmentation Analysis
- Cluster customers by satisfaction + usage patterns
- Identify "at-risk" segments for targeted retention

### 2. Longitudinal Analysis  
- Track satisfaction changes over customer lifecycle
- Identify satisfaction inflection points

### 3. Causal Analysis
- A/B test engagement interventions
- Randomized feature access for causal inference

### 4. Predictive Modeling
- Build churn prediction model using satisfaction + usage
- Early warning system for customer success team

Would you like me to dive deeper into any of these analyses or help you design follow-up studies?

## Related Prompts

- [Predictive Analysis Expert](./predictive-analysis-expert.md)
- [Survey Design Specialist](./survey-design-specialist.md)
- [A/B Testing Expert](./ab-testing-expert.md)
{{specific_questions_hypotheses_relationships}}

STATISTICAL ANALYSIS FRAMEWORK:

Phase 1: DATA EXPLORATION
1. Descriptive statistics
2. Distribution analysis
3. Missing data patterns
4. Outlier detection

Phase 2: STATISTICAL MODELING
1. Model selection
2. Assumption testing
3. Parameter estimation
4. Model diagnostics

Phase 3: INFERENCE & VALIDATION
1. Hypothesis testing
2. Confidence intervals
3. Cross-validation
4. Sensitivity analysis

Phase 4: INTERPRETATION & APPLICATION
1. Effect size assessment
2. Practical significance
3. Limitations acknowledgment
4. Actionable insights

DELIVER YOUR ANALYSIS AS:

## COMPREHENSIVE STATISTICAL ANALYSIS REPORT

### EXECUTIVE SUMMARY
- **Key Finding**: {{primary_statistical_conclusion}}
- **Statistical Significance**: {{p_values_confidence_intervals}}
- **Effect Size**: {{practical_importance_magnitude}}
- **Model Performance**: {{accuracy_metrics_validation_results}}
- **Recommendation**: {{data_driven_action_items}}

### DATA OVERVIEW & EXPLORATION

#### Descriptive Statistics Summary
```

Dataset Characteristics:
┌─────────────────────────────────────────────┐
│ SAMPLE PROFILE │
├─────────────────────────────────────────────┤
│ Total Observations: 15,847 │
│ Complete Cases: 14,231 (89.8%) │
│ Variables: 42 (12 continuous, 30 categorical)│
│ Time Period: 2022-01 to 2024-12 │
│ Sampling Method: Stratified Random │
└─────────────────────────────────────────────┘

Key Variables Summary:
┌──────────────┬───────┬───────┬───────┬──────┐
│ Variable │ Mean │ SD │ Min │ Max │
├──────────────┼───────┼───────┼───────┼──────┤
│ Revenue ($K) │ 156.3 │ 45.2 │ 23.1 │ 412.8│
│ Satisfaction │ 7.2 │ 1.8 │ 1.0 │ 10.0 │
│ Churn Rate % │ 12.4 │ 4.3 │ 2.1 │ 31.5 │
│ Tenure (mo) │ 28.5 │ 18.7 │ 1.0 │ 120.0│
└──────────────┴───────┴───────┴───────┴──────┘

Distribution Analysis:
Revenue: Slightly right-skewed (γ₁ = 0.82)
Satisfaction: Negatively skewed (γ₁ = -0.65)
Churn: Normal (γ₁ = 0.12, γ₂ = 2.98)
Tenure: Highly right-skewed (γ₁ = 2.14)

```

#### Data Quality Assessment
```

Missing Data Pattern Analysis:
Missing % Pattern
Revenue 0.5% Random
Satisfaction 8.2% Not random (new customers)
Demographics 3.1% Random
Behavior metrics 12.4% Systematic (mobile users)

Outlier Detection Results:
┌─────────────────────────────────────────────┐
│ Method │ Outliers │ Action Taken │
├─────────────────┼──────────┼───────────────┤
│ 3σ Rule │ 147 │ Investigated │
│ IQR Method │ 203 │ Winsorized │
│ Isolation Forest│ 89 │ Removed │
│ Domain Logic │ 34 │ Corrected │
└─────────────────┴──────────┴───────────────┘

Data Transformations Applied:
• Log transformation: Revenue (improved normality)
• Standardization: All continuous variables
• One-hot encoding: Categorical variables
• Imputation: MICE for missing values

```

### STATISTICAL TESTING & INFERENCE

#### Hypothesis Testing Results
```

Primary Hypothesis Test:
H₀: Customer satisfaction has no effect on churn
H₁: Higher satisfaction reduces churn probability

Test Selection Rationale:
• Outcome: Binary (churn yes/no)
• Predictors: Mixed types
• Sample size: Adequate (n=14,231)
→ Logistic Regression Selected

Results Summary:
┌─────────────────────────────────────────────┐
│ Logistic Regression Results │
├─────────────────────────────────────────────┤
│ Variable │ β │ SE │ p-value │
├─────────────────┼────────┼───────┼─────────┤
│ Intercept │ 2.847 │ 0.182 │ <0.001**_│
│ Satisfaction │ -0.413 │ 0.024 │ <0.001_**│
│ Tenure │ -0.028 │ 0.003 │ <0.001**_│
│ Price Tier │ 0.156 │ 0.041 │ <0.001_**│
│ Support Calls │ 0.234 │ 0.018 │ <0.001\*\*\*│
└─────────────────┴────────┴───────┴─────────┘

Model Fit Statistics:
• McFadden R²: 0.341
• AIC: 8,924.5
• Hosmer-Lemeshow: p = 0.763 (good fit)
• AUC: 0.847 (excellent discrimination)

Interpretation:
Each 1-point increase in satisfaction reduces
odds of churn by 33.8% (OR = 0.662, 95% CI: 0.631-0.694)

````

#### Multiple Comparisons & Effect Sizes
```python
# Effect Size Calculations
effect_sizes = {
    'satisfaction_churn': {
        'odds_ratio': 0.662,
        'cohens_d': 0.73,  # Large effect
        'relative_risk_reduction': 0.28,
        'nnt': 7.2  # Number needed to treat
    },
    'tenure_effect': {
        'hazard_ratio': 0.972,
        'survival_improvement': '15% at 2 years',
        'correlation': -0.42  # Moderate negative
    }
}

# Adjusted p-values (Bonferroni correction)
p_values_adjusted = {
    'satisfaction': 0.001,   # Still significant
    'tenure': 0.001,         # Still significant
    'price_tier': 0.012,     # Still significant
    'support_calls': 0.001   # Still significant
}

# Confidence Intervals (95%)
confidence_intervals = {
    'satisfaction_effect': (-0.461, -0.365),
    'predicted_churn_reduction': (22.4%, 31.2%),
    'roi_estimate': (2.8, 4.2)  # Return ratio
}
````

### ADVANCED STATISTICAL MODELING

#### Predictive Model Development

```
Model Comparison Results:
┌──────────────────┬─────────┬────────┬────────┐
│ Model            │ Accuracy│ AUC    │ F1     │
├──────────────────┼─────────┼────────┼────────┤
│ Logistic Reg     │ 0.823   │ 0.847  │ 0.761  │
│ Random Forest    │ 0.841   │ 0.882  │ 0.798  │
│ XGBoost         │ 0.849   │ 0.891  │ 0.812  │
│ Neural Network   │ 0.834   │ 0.873  │ 0.789  │
│ Ensemble        │ 0.856   │ 0.903  │ 0.824  │
└──────────────────┴─────────┴────────┴────────┘

Cross-Validation Results (5-fold):
Mean AUC: 0.891 (SD: 0.018)
Stability: High (low variance across folds)

Feature Importance (Top 10):
1. Satisfaction Score      ████████████ 0.243
2. Recent Support Calls    ██████████ 0.198
3. Tenure                  ████████ 0.156
4. Usage Frequency         ███████ 0.134
5. Price Sensitivity       █████ 0.098
6. Product Adoption        ████ 0.076
7. Contract Type           ███ 0.054
8. Payment History         ██ 0.041
9. Demographics           ██ 0.038
10. Seasonality           █ 0.022
```

#### Time Series Analysis

```
Trend Decomposition (Revenue):
                    Original = Trend + Seasonal + Residual
    200│      ╱╲
       │     ╱  ╲   ╱╲     Trend: +2.3% monthly
    150│    ╱    ╲ ╱  ╲    Seasonal: Q4 peak (+18%)
       │   ╱      ╲    ╲   Residual: σ = 12.4
    100│  ╱              ╲
       │ ╱
     50│╱
       └────────────────────────
        J F M A M J J A S O N D

ARIMA Model Selection:
Auto-ARIMA Result: ARIMA(2,1,2)(1,1,1)₁₂
AIC: 2,341.8
MAPE: 8.7%

Forecast (Next 6 Months):
Month 1: $162.4K (95% PI: 141.2-183.6)
Month 2: $165.8K (95% PI: 139.7-191.9)
Month 3: $169.3K (95% PI: 138.2-200.4)
Month 4: $181.7K (95% PI: 145.3-218.1)
Month 5: $176.2K (95% PI: 134.8-217.6)
Month 6: $172.9K (95% PI: 127.4-218.4)
```

### CAUSAL ANALYSIS

#### Causal Inference Framework

```
Propensity Score Matching Analysis:
Treatment: High satisfaction training program
Outcome: Churn reduction

Matching Quality:
┌─────────────────────────────────────────────┐
│ Balance Check     │ Before │ After  │ p-val│
├───────────────────┼────────┼────────┼──────┤
│ Age               │ 3.21   │ 0.14   │ 0.89 │
│ Tenure            │ 4.15   │ 0.22   │ 0.76 │
│ Usage             │ 2.89   │ 0.18   │ 0.82 │
│ Prior Satisfaction│ 5.42   │ 0.31   │ 0.71 │
└───────────────────┴────────┴────────┴──────┘
Standardized differences all < 0.1 (excellent)

Average Treatment Effect:
ATE = -4.2% (95% CI: -5.8%, -2.6%)
Interpretation: Training reduces churn by 4.2 percentage points

Sensitivity Analysis:
Hidden bias threshold (Γ): 1.8
Robust to moderate unmeasured confounding
```

#### Structural Equation Modeling

```
Path Analysis Results:
                    Satisfaction
                         ↗ 0.42***
        Training ───────────────────→ Churn
         0.31*** ↘               ↙ -0.38***
                    Engagement

Fit Indices:
• CFI: 0.963 (excellent)
• RMSEA: 0.042 (good)
• SRMR: 0.038 (good)
• χ²/df: 1.84 (acceptable)

Mediation Analysis:
• Direct effect: -0.21**
• Indirect via satisfaction: -0.16***
• Indirect via engagement: -0.12**
• Total effect: -0.49***

Conclusion: 57% of effect is mediated
```

### DIAGNOSTIC CHECKS & VALIDATION

#### Model Diagnostics

```
Regression Diagnostics:
┌─────────────────────────────────────────────┐
│ Assumption         │ Test      │ Result     │
├────────────────────┼───────────┼────────────┤
│ Linearity          │ RESET     │ p = 0.342 ✓│
│ Homoscedasticity   │ Breusch-P │ p = 0.158 ✓│
│ Normality          │ Shapiro-W │ p = 0.041 ⚠│
│ Independence       │ Durbin-W  │ DW = 1.94 ✓│
│ Multicollinearity  │ VIF       │ Max = 2.3 ✓│
└────────────────────┴───────────┴────────────┘

Residual Analysis:
         Residuals vs Fitted        Q-Q Plot
    2│   .  . .                    2│    . ╱
     │  . .. ...  .                │   .╱.
    0│ ............               0│ ╱...
     │  .. ... . .                 │╱.. .
   -2│   . .  .                  -2│  .
     └───────────────              └───────────
      50    100   150              -2   0   2

Influential Points:
Cook's D > 0.5: 3 observations
DFBETAS > 2/√n: 7 observations
Action: Sensitivity analysis conducted
```

#### Validation & Robustness

```python
# Cross-Validation Deep Dive
cv_results = {
    'fold_performances': [0.883, 0.891, 0.896, 0.889, 0.887],
    'mean_performance': 0.891,
    'std_deviation': 0.005,
    'worst_case': 0.883,
    'best_case': 0.896
}

# Bootstrap Validation (1000 samples)
bootstrap_stats = {
    'mean_auc': 0.890,
    'ci_lower': 0.878,
    'ci_upper': 0.902,
    'bias': -0.001,  # Minimal bias
    'variance': 0.00014
}

# Temporal Validation
temporal_splits = {
    'train_2022': {'test_2023': 0.885},
    'train_2022-23': {'test_2024': 0.881},
    'performance_decay': '0.4% per year'
}

# External Validation (if available)
external_validation = {
    'dataset': 'Industry benchmark',
    'our_model_auc': 0.847,
    'benchmark_auc': 0.823,
    'improvement': '+2.4 percentage points'
}
```

### STATISTICAL POWER & SAMPLE SIZE

#### Power Analysis

```
Post-hoc Power Analysis:
┌─────────────────────────────────────────────┐
│ Effect Detection Power                      │
├─────────────────────────────────────────────┤
│ Small effect (d=0.2):   Power = 0.72       │
│ Medium effect (d=0.5):  Power = 0.99       │
│ Large effect (d=0.8):   Power = 1.00       │
│                                             │
│ Achieved effect size: d = 0.73 (Large)     │
│ Statistical power: 0.99                     │
└─────────────────────────────────────────────┘

Sample Size Calculations:
For future studies detecting d=0.5:
• 80% power: n = 128 per group
• 90% power: n = 172 per group
• 95% power: n = 216 per group

Current sample adequate for:
✓ Main effects (power > 0.95)
✓ Two-way interactions (power > 0.80)
⚠ Three-way interactions (power = 0.65)
```

### PRACTICAL INSIGHTS & RECOMMENDATIONS

#### Business Impact Translation

```
Statistical Findings → Business Value:

1. SATISFACTION IMPACT
   Statistical: β = -0.413, p < 0.001
   Business: 1-point satisfaction increase →
   • 28% reduction in churn probability
   • $1.2M annual revenue retention
   • ROI: 3.5:1 on satisfaction initiatives

2. PREDICTIVE MODEL VALUE
   Statistical: AUC = 0.891
   Business Application:
   • Identify 89% of churners before they leave
   • Targeted retention: $4.50 per $1 spent
   • Reduce overall churn by 35%

3. SEGMENTATION INSIGHTS
   Statistical: 4 distinct clusters (silhouette = 0.68)
   Business Segments:
   • Champions (22%): Protect at all costs
   • At-Risk (31%): Immediate intervention
   • Hibernating (28%): Re-engagement campaign
   • Lost (19%): Win-back or let go
```

#### Implementation Roadmap

```
From Analysis to Action:

IMMEDIATE (Week 1-2):
├── Deploy churn prediction model
├── Alert on high-risk customers
├── A/B test satisfaction drivers
└── Impact: Save 50-75 customers

SHORT-TERM (Month 1-3):
├── Automate intervention triggers
├── Personalize retention offers
├── Optimize support routing
└── Impact: 15% churn reduction

LONG-TERM (Month 4-12):
├── Integrate predictive insights
├── Continuous model retraining
├── Causal experiment program
└── Impact: 35% churn reduction

Monitoring Dashboard:
┌─────────────────────────────────────────────┐
│ MODEL PERFORMANCE TRACKING                  │
├─────────────────────────────────────────────┤
│ Current Month AUC: 0.887 (↓0.004)         │
│ Precision @ 20%: 0.76                      │
│ Saved Customers: 247 ($148K value)         │
│ Model Drift: Minimal (PSI = 0.08)          │
└─────────────────────────────────────────────┘
```

### LIMITATIONS & CAVEATS

#### Study Limitations

```
Important Considerations:

1. DATA LIMITATIONS
   • Missing not completely at random
   • Self-selection in satisfaction surveys
   • Limited to 3-year window

2. STATISTICAL LIMITATIONS
   • Assumes linear relationships
   • Cannot prove causation definitively
   • Multiple testing increases Type I error

3. GENERALIZABILITY
   • Results specific to this industry
   • May not apply to all customer segments
   • Temporal validity ~12-18 months

4. PRACTICAL CONSTRAINTS
   • Model requires 8 features minimum
   • Real-time scoring needs infrastructure
   • Human review recommended for edge cases

Confidence Statement:
High confidence in primary findings (95%)
Moderate confidence in predictions (85%)
Recommendations are robust to assumptions
```

### TECHNICAL APPENDIX

#### Statistical Code

```python
# Reproducible Analysis Pipeline
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import statsmodels.api as sm

# Data preprocessing
def preprocess_data(df):
    # Handle missing values
    df_imputed = mice_imputation(df)

    # Feature engineering
    df_features = create_features(df_imputed)

    # Outlier treatment
    df_clean = winsorize_outliers(df_features)

    return df_clean

# Model development
def build_churn_model(X, y):
    # Train ensemble model
    rf = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        min_samples_split=50,
        random_state=42
    )

    # Cross-validation
    scores = cross_val_score(
        rf, X, y,
        cv=5,
        scoring='roc_auc'
    )

    # Final model
    rf.fit(X, y)

    return rf, scores

# Statistical testing
def hypothesis_tests(data):
    # Logistic regression
    model = sm.Logit(
        data['churn'],
        sm.add_constant(data[features])
    )
    results = model.fit()

    # Effect sizes
    odds_ratios = np.exp(results.params)
    conf_intervals = np.exp(results.conf_int())

    return results, odds_ratios, conf_intervals
```

### APPENDICES

#### A. Full Statistical Output

[Complete regression tables, diagnostic plots, test statistics]

#### B. Data Dictionary

[Variable definitions, coding schemes, measurement details]

#### C. Methodological Notes

[Detailed explanation of statistical choices and alternatives]

#### D. Reproducibility Information

[Software versions, random seeds, data availability]

```

## Usage Instructions
1. Clearly define research questions and hypotheses upfront
2. Assess data quality and characteristics thoroughly
3. Choose appropriate statistical methods based on data type and goals
4. Validate all statistical assumptions before inference
5. Report both statistical and practical significance
6. Use multiple validation approaches for robustness
7. Translate statistical findings into business language
8. Provide clear limitations and confidence levels

## Examples
### Example 1: A/B Test Analysis
**Input**:
```

{{analysis_type}}: Experimental - randomized A/B test
{{data_characteristics}}: 50,000 users, 50/50 split, 30-day test
{{variables_of_interest}}: Conversion rate (binary), revenue per user
{{statistical_goals}}: Determine if new design improves conversion
{{specific_questions}}: Is 2% lift statistically significant? What's the confidence interval?

```

**Output**: [Comprehensive analysis showing 2.3% lift is statistically significant (p=0.018), 95% CI [0.4%, 4.2%], with 83% statistical power, recommending implementation with expected annual value of $1.2M]

## Related Prompts
- [Data Analysis Expert](/prompts/analysis/data-analysis-expert.md)
- [Predictive Analytics Specialist](/prompts/analysis/predictive-analytics-specialist.md)
- [Experimental Design Expert](/prompts/research/experimental-design-expert.md)

## Research Notes
- Balances statistical rigor with practical application
- Includes both traditional and modern statistical methods
- Emphasizes validation and robustness checking
- Provides clear translation from statistics to business value
- Addresses common pitfalls in statistical analysis
```
