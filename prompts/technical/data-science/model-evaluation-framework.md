# Model Evaluation Framework

## Metadata
- **Created**: 2025-07-26

- **Category**: Technical/Data-Science
- **Tags**: model evaluation, machine learning, performance metrics, validation, model selection
- **Version**: 2.0.0
- **Use Cases**: model comparison, performance validation, production readiness, ML optimization
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you comprehensively evaluate machine learning models using appropriate metrics, validation strategies, and real-world performance considerations.

## Prompt

```
I'll help you evaluate your machine learning model thoroughly to ensure it meets your business needs. Let me understand your model and context:

**About your model:**
1. What type of problem? (classification, regression, clustering, etc.)
2. What's your model architecture? (random forest, neural network, etc.)
3. What's the business use case?
4. What are the consequences of false positives vs false negatives?

**Data context:**
5. How much data do you have? (training/validation/test split)
6. Is your data balanced? Any class imbalance issues?
7. Any data quality concerns? (missing values, outliers, drift)
8. Is this time series data or cross-sectional?

**Current performance:**
9. What metrics have you calculated so far?
10. Do you have baseline model performance to compare against?
11. Any specific performance thresholds required?
12. Have you tested on production-like data?

Based on your answers, I'll provide:

**EVALUATION STRATEGY** - Comprehensive testing approach
**METRIC ANALYSIS** - Which metrics matter most and why
**VALIDATION FRAMEWORK** - Proper validation techniques
**PERFORMANCE INSIGHTS** - Deep dive into model behavior
**PRODUCTION READINESS** - Deployment considerations

Share your model details and let's ensure it's truly ready for deployment!
```

## Example Usage

**User Input:**
```
1. Binary classification - predicting customer churn
2. XGBoost model with 47 features, tuned hyperparameters
3. Identify customers likely to cancel subscription in next 30 days for retention campaigns
4. False negatives worse - missing churners costs ~$200/customer, false positive costs ~$10 campaign cost

5. 100K customers: 70K train, 15K validation, 15K test. 18 months of data
6. Imbalanced - only 8% churn rate in historical data
7. Some features have 10-15% missing values, seeing slight drift in user behavior post-COVID
8. Time-based with monthly snapshots, customer tenure varies 1-60 months

9. Just accuracy (92%) and basic precision/recall
10. Current random targeting gets 8% success rate
11. Need to catch at least 50% of churners, keep campaign costs reasonable
12. Not yet - only tested on historical data splits
```

**Assistant Output:**

Based on your churn prediction model, here's a comprehensive evaluation framework:

## EVALUATION STRATEGY

### Critical Issues to Address
1. **Accuracy is misleading** - At 92% with 8% churn rate, your model might just be predicting everyone stays!
2. **Time-based validation needed** - Random splits don't work for churn
3. **Business metrics missing** - Need to evaluate $ impact, not just ML metrics

### Proper Evaluation Approach
**Time-Based Split**: 
- Train: Months 1-12
- Validate: Months 13-15  
- Test: Months 16-18
- This prevents future data leakage

## METRIC ANALYSIS

### Primary Metrics (Given Business Context)

**1. Recall @ Top 20% (Critical)**
```
Why: If you can only campaign to 20% of customers, 
     how many churners do you catch?
Target: 60%+ (achievable with good model)
Current: Calculate this immediately
```

**2. Precision-Recall AUC**
```
Why: Robust to class imbalance unlike ROC-AUC
Target: 0.35+ (good for 8% base rate)
Interpretation: Area under precision-recall curve
```

**3. Lift @ Deciles**
```
Top 10%: Should show 4-5x lift
Top 20%: Should show 3-4x lift  
Top 30%: Should show 2-3x lift
```

### Business Metrics

**4. Expected Revenue Impact**
```
Per 1000 customers targeted:
True Positives × $200 saved
- False Positives × $10 cost
- False Negatives × $200 lost

Compare to random targeting baseline
```

**5. Campaign Efficiency**
```
Number Needed to Treat (NNT) = 1/Precision
Cost per Saved Customer = NNT × $10
Must be < $200 to be profitable
```

## VALIDATION FRAMEWORK

### 1. Temporal Validation
```python
# Pseudo-code for proper time-based validation
for month in [13, 14, 15, 16, 17, 18]:
    train_data = data[data.month < month - 2]
    val_data = data[data.month == month - 2]
    test_data = data[data.month == month]
    
    # Retrain model monthly
    model.fit(train_data)
    predictions = model.predict_proba(test_data)
    
    # Track metric stability
    metrics[month] = calculate_metrics(predictions)
```

### 2. Stratified Analysis
Evaluate performance by:
- Customer tenure buckets (new vs. established)
- Revenue segments (high vs. low value)
- Product types
- Acquisition channels

### 3. Feature Stability Testing
```
Critical checks:
- Feature importance changes over time
- Prediction drift month-to-month
- Missing value impact analysis
- COVID period vs. normal behavior
```

## PERFORMANCE INSIGHTS

### Detailed Analysis Plan

**1. Probability Calibration**
- Plot: Predicted vs. Actual churn rates by decile
- Test: Hosmer-Lemeshow goodness-of-fit
- Fix: Isotonic/Platt calibration if needed

**2. Error Analysis**
```
False Negatives Profile:
- Which churners are we missing?
- Common characteristics?
- Actionable patterns?

False Positives Profile:  
- Why did model think they'd churn?
- Can we identify systematic errors?
```

**3. Feature Diagnostics**
- SHAP values for top 20% predictions
- Partial dependence plots for key features
- Feature interaction effects
- Missing value impact on predictions

**4. Threshold Optimization**
```
Business-Driven Threshold:
1. Set minimum recall (50% churners)
2. Find threshold that maximizes profit
3. Calculate campaign size needed
4. Validate stability across time
```

## PRODUCTION READINESS

### Performance Monitoring Plan

**1. Data Quality Checks**
- Missing value rates by feature
- Feature distribution shifts (KS test)
- Prediction distribution monitoring
- Business metric tracking

**2. Model Performance Tracking**
```
Weekly Dashboard:
- Precision @ current threshold
- Recall @ current threshold  
- Campaign conversion rate
- Revenue impact vs. baseline
```

**3. Retraining Strategy**
- Monthly performance review
- Quarterly full retrain
- Trigger: 10% performance drop
- A/B test new models

### Deployment Checklist

**Pre-Production Tests:**
- [ ] Inference speed < 100ms per prediction
- [ ] Handle missing values gracefully
- [ ] Prediction logging configured
- [ ] Fallback for model failures
- [ ] Feature pipeline validated

**Business Integration:**
- [ ] CRM integration for campaigns
- [ ] Scoring frequency defined
- [ ] Action thresholds agreed
- [ ] Success metrics dashboarded

### Next Steps

1. **Immediate**: Recalculate metrics with proper time splits
2. **This Week**: Build business impact simulator
3. **Before Deploy**: Run 2-week shadow mode test
4. **Post-Deploy**: Daily monitoring for 2 weeks

### Red Flags to Address
- No discussion of probability calibration
- Single-point time validation insufficient  
- Need customer lifetime value in optimization
- Feature drift requires monitoring

Your 92% accuracy likely hides poor churn detection. Focus on recall at reasonable precision levels and tie everything to business value.

## Related Prompts

- [ML Experimentation Framework](../../management-leadership/delegation-framework-expert.md)
- [Feature Engineering Specialist](../../decision-making/feature-prioritization-expert.md)
- [Model Deployment Strategist](../../technical-workflows/deployment-pipeline-creation-expert.md)
