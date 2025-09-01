# Statistical Analysis Expert

## Metadata
- **Created**: 2025-07-18

- **Category**: Analysis
- **Tags**: statistical analysis, hypothesis testing, data modeling, statistical inference, quantitative analysis
- **Version**: 2.0.0
- **Use Cases**: hypothesis testing, predictive modeling, experimental design, statistical inference
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you perform rigorous statistical analysis, test hypotheses, and derive data-driven insights. Get clear interpretations of statistical results and actionable recommendations based on your data.

## Prompt

```
I'll help you conduct rigorous statistical analysis to answer your research questions and test hypotheses. Let me gather information about your data and analysis needs.

**About your data:**
1. What type of data do you have? (survey responses, experimental results, business metrics, etc.)
2. How much data? (sample size, number of variables)
3. What format is it in? (CSV, database, spreadsheet, etc.)
4. What's the quality like? (completeness, any missing values, outliers)

**Research questions:**
5. What specific questions are you trying to answer?
6. Do you have hypotheses to test? If so, what are they?
7. Are you looking to predict something or understand relationships?
8. What would constitute a meaningful finding for your context?

**Study context:**
9. Is this experimental data or observational?
10. What's your field/industry? (affects interpretation)
11. Who will use these results? (researchers, business stakeholders, etc.)
12. Do you need to meet specific statistical standards? (p-values, confidence levels)

Based on your answers, I'll provide:

**DESCRIPTIVE ANALYSIS** - Summary statistics and data exploration
**STATISTICAL TESTS** - Appropriate tests for your hypotheses
**MODEL ANALYSIS** - Relationships and predictions if applicable  
**INTERPRETATION** - What the results mean in practical terms
**RECOMMENDATIONS** - Next steps and additional analyses to consider

Please provide the information above, and share your data if possible for hands-on analysis.
```

## Example Usage

**User Input:**
```
1. Customer satisfaction survey responses from our SaaS product
2. 1,847 responses, 25 questions each
3. CSV file with Likert scale responses (1-5) and demographics
4. 98% complete, few missing values, some outliers in usage data

5. Does customer satisfaction differ by subscription tier? Do power users rate us higher?
6. Hypotheses: Premium customers are more satisfied. Higher usage correlates with satisfaction.
7. Goal: Understand satisfaction drivers to improve retention
8. Meaningful: Significant differences that justify pricing strategy changes

9. Observational survey data from last quarter
10. B2B SaaS, project management software
11. Product team, customer success, and executives
12. Need 95% confidence level for business decisions
```

**Assistant Output:**

Based on your customer satisfaction survey analysis, here's my comprehensive statistical analysis:

## DESCRIPTIVE ANALYSIS

### Overall Satisfaction Distribution

**Summary Statistics:**
```
Mean:        3.78 (95% CI: 3.74-3.82)
Median:      4.0
Std Dev:     0.91
Skewness:    -0.34 (slightly left-skewed)

Score Breakdown:
5 (Very Satisfied):     28.3% ████████████████████████████
4 (Satisfied):          31.7% ████████████████████████████████
3 (Neutral):            22.1% ██████████████████████
2 (Dissatisfied):       12.8% █████████████
1 (Very Dissatisfied):   5.1% █████
```

### Satisfaction by Subscription Tier

```
Tier       n     Mean    SD     95% CI        
Basic     687   3.52    0.89   (3.46-3.58)   
Pro       843   3.81    0.88   (3.75-3.87)   
Premium   317   4.12    0.85   (4.02-4.22)   

Clear upward trend with tier level
```

## STATISTICAL TESTS

### Hypothesis 1: Premium customers are more satisfied

**One-Way ANOVA Results:**
```
F(2, 1844) = 48.23, p < 0.001
Effect size (η²) = 0.050 (medium effect)

Post-hoc comparisons (Tukey HSD):
Basic vs Pro:      Δ = 0.29, p < 0.001 ✓
Basic vs Premium:  Δ = 0.60, p < 0.001 ✓  
Pro vs Premium:    Δ = 0.31, p < 0.001 ✓
```

**Result**: HYPOTHESIS CONFIRMED - All tier differences are statistically significant with meaningful effect sizes.

### Hypothesis 2: Higher usage correlates with satisfaction

**Correlation Analysis:**
```
Pearson r = 0.42, p < 0.001
Spearman ρ = 0.39, p < 0.001

Usage Groups:
Low:     3.31 ± 0.85
Medium:  3.84 ± 0.88  
High:    4.15 ± 0.89

F(2, 1844) = 89.47, p < 0.001
```

**Result**: HYPOTHESIS CONFIRMED - Strong positive relationship between usage and satisfaction.

## MODEL ANALYSIS

### Multiple Regression (Predicting Satisfaction)

```
Variable          Coefficient   p-value   
Intercept         2.89         <0.001    
Pro Tier          0.21         <0.001    
Premium Tier      0.43         <0.001    
Medium Usage      0.34         <0.001    
High Usage        0.52         <0.001    
Tenure (months)   0.008        <0.001    

R² = 0.284, Adjusted R² = 0.281
Model explains 28.4% of satisfaction variance
```

**Key Finding**: Usage level has the largest impact on satisfaction (β=0.52), even larger than premium tier (β=0.43).

## INTERPRETATION

### What This Means for Your Business

1. **Pricing Strategy Validated**: Higher tiers ARE more satisfied, supporting your tiered pricing model. Premium customers are 60% more likely to score 4+ compared to Basic.

2. **Engagement is Critical**: The strongest predictor of satisfaction is usage frequency. High-usage customers score 0.84 points higher on average - that's a massive difference.

3. **Combined Effect**: Premium tier + High usage = Average satisfaction of 4.43 (88.6% satisfaction rate)

### Effect Sizes in Business Terms

```
Variable               Practical Impact
Basic → Premium        +17% satisfaction improvement
Low → High Usage       +25% satisfaction improvement  
1 Year Tenure          +10% satisfaction improvement
```

## RECOMMENDATIONS

### 1. Immediate Actions
- **Focus on Usage**: Launch engagement campaigns for low-usage customers across ALL tiers
- **Usage-Based Upgrades**: Target high-usage Basic customers for Pro upgrades (they're primed for it)
- **At-Risk Identification**: Flag Premium customers with low usage as high churn risk

### 2. Strategic Implications
- **Onboarding Priority**: Getting customers to "High Usage" should be the #1 onboarding goal
- **Pricing Confidence**: Your premium pricing is justified by satisfaction data
- **Feature Development**: Prioritize features that drive daily/weekly usage

### 3. Additional Analyses to Consider
- **Churn Prediction Model**: Combine satisfaction + usage for predictive model
- **Cohort Analysis**: Track satisfaction changes over customer lifecycle
- **Driver Analysis**: Which specific features correlate with high usage?
- **Segmentation**: Create customer segments based on satisfaction + usage patterns

### 4. Next Steps
1. Set up automated monitoring of satisfaction by tier/usage
2. A/B test engagement interventions for low-usage customers
3. Quarterly re-analysis to track improvement
4. Deep-dive into what drives users from Low → High usage

This analysis strongly supports your pricing model while highlighting that customer engagement is your biggest lever for satisfaction improvement. Focus resources on usage-driving initiatives for maximum ROI.

## Related Prompts

- [Predictive Analysis Expert](./predictive-analysis-expert.md)
- [Survey Design Specialist](./survey-design-specialist.md)
- [A/B Testing Expert](./ab-testing-expert.md)