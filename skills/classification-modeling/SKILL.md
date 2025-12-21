---
name: Classification Modeling
description: Build binary and multiclass classification models using logistic regression, decision trees, and ensemble methods for categorical prediction and classification
---

# Classification Modeling

## Overview

Classification modeling predicts categorical target values, assigning observations to discrete classes or categories based on input features.

## When to Use

- Predicting binary outcomes like customer churn, loan default, or email spam
- Classifying items into multiple categories such as product types or sentiment
- Building credit scoring models or risk assessment systems
- Identifying disease diagnosis or medical condition from patient data
- Predicting customer purchase likelihood or response to marketing
- Detecting fraud, anomalies, or quality defects in production systems

## Classification Types

- **Binary Classification**: Two classes (yes/no, success/failure)
- **Multiclass**: More than two classes
- **Multi-label**: Multiple classes per observation

## Common Algorithms

- **Logistic Regression**: Linear classification
- **Decision Trees**: Rule-based non-linear
- **Random Forest**: Ensemble of decision trees
- **Gradient Boosting**: Sequential tree building
- **SVM**: Support Vector Machines
- **Naive Bayes**: Probabilistic classifier

## Key Metrics

- **Accuracy**: Overall correct predictions
- **Precision**: True positives / (true + false positives)
- **Recall**: True positives / (true + false negatives)
- **F1-Score**: Harmonic mean of precision/recall
- **AUC-ROC**: Area under receiver operating characteristic curve

## Implementation with Python

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    confusion_matrix, classification_report, roc_auc_score, roc_curve,
    precision_recall_curve, f1_score, accuracy_score
)
import seaborn as sns

# Generate sample binary classification data
np.random.seed(42)
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=1000, n_features=20, n_informative=10,
    n_redundant=5, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_scaled, y_train)
y_pred_lr = lr_model.predict(X_test_scaled)
y_proba_lr = lr_model.predict_proba(X_test_scaled)[:, 1]

print("Logistic Regression:")
print(classification_report(y_test, y_pred_lr))
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba_lr):.4f}\n")

# Decision Tree
dt_model = DecisionTreeClassifier(max_depth=10, random_state=42)
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)
y_proba_dt = dt_model.predict_proba(X_test)[:, 1]

print("Decision Tree:")
print(classification_report(y_test, y_pred_dt))
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba_dt):.4f}\n")

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
y_proba_rf = rf_model.predict_proba(X_test)[:, 1]

print("Random Forest:")
print(classification_report(y_test, y_pred_rf))
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba_rf):.4f}\n")

# Gradient Boosting
gb_model = GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42)
gb_model.fit(X_train, y_train)
y_pred_gb = gb_model.predict(X_test)
y_proba_gb = gb_model.predict_proba(X_test)[:, 1]

print("Gradient Boosting:")
print(classification_report(y_test, y_pred_gb))
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba_gb):.4f}\n")

# Confusion matrices
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

models = [
    (y_pred_lr, 'Logistic Regression'),
    (y_pred_dt, 'Decision Tree'),
    (y_pred_rf, 'Random Forest'),
    (y_pred_gb, 'Gradient Boosting'),
]

for idx, (y_pred, title) in enumerate(models):
    cm = confusion_matrix(y_test, y_pred)
    ax = axes[idx // 2, idx % 2]
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_title(title)
    ax.set_ylabel('True Label')
    ax.set_xlabel('Predicted Label')

plt.tight_layout()
plt.show()

# ROC Curves
plt.figure(figsize=(10, 8))

probas = [
    (y_proba_lr, 'Logistic Regression'),
    (y_proba_dt, 'Decision Tree'),
    (y_proba_rf, 'Random Forest'),
    (y_proba_gb, 'Gradient Boosting'),
]

for y_proba, label in probas:
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    auc = roc_auc_score(y_test, y_proba)
    plt.plot(fpr, tpr, label=f'{label} (AUC={auc:.4f})')

plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Precision-Recall Curves
plt.figure(figsize=(10, 8))

for y_proba, label in probas:
    precision, recall, _ = precision_recall_curve(y_test, y_proba)
    f1 = f1_score(y_test, (y_proba > 0.5).astype(int))
    plt.plot(recall, precision, label=f'{label} (F1={f1:.4f})')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curves')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Feature importance
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Tree-based feature importance
feature_importance_rf = pd.Series(
    rf_model.feature_importances_, index=range(X.shape[1])
).sort_values(ascending=False)

axes[0].barh(range(10), feature_importance_rf.values[:10])
axes[0].set_yticks(range(10))
axes[0].set_yticklabels([f'Feature {i}' for i in feature_importance_rf.index[:10]])
axes[0].set_title('Random Forest - Top 10 Features')
axes[0].set_xlabel('Importance')

# Logistic regression coefficients
lr_coef = pd.Series(lr_model.coef_[0], index=range(X.shape[1])).abs().sort_values(ascending=False)
axes[1].barh(range(10), lr_coef.values[:10])
axes[1].set_yticks(range(10))
axes[1].set_yticklabels([f'Feature {i}' for i in lr_coef.index[:10]])
axes[1].set_title('Logistic Regression - Top 10 Features (abs coef)')
axes[1].set_xlabel('Absolute Coefficient')

plt.tight_layout()
plt.show()

# Model comparison
results = pd.DataFrame({
    'Model': ['Logistic Regression', 'Decision Tree', 'Random Forest', 'Gradient Boosting'],
    'Accuracy': [
        accuracy_score(y_test, y_pred_lr),
        accuracy_score(y_test, y_pred_dt),
        accuracy_score(y_test, y_pred_rf),
        accuracy_score(y_test, y_pred_gb),
    ],
    'AUC-ROC': [
        roc_auc_score(y_test, y_proba_lr),
        roc_auc_score(y_test, y_proba_dt),
        roc_auc_score(y_test, y_proba_rf),
        roc_auc_score(y_test, y_proba_gb),
    ],
    'F1-Score': [
        f1_score(y_test, y_pred_lr),
        f1_score(y_test, y_pred_dt),
        f1_score(y_test, y_pred_rf),
        f1_score(y_test, y_pred_gb),
    ]
})

print("Model Comparison:")
print(results)

# Cross-validation
cv_scores = cross_val_score(
    RandomForestClassifier(n_estimators=100, random_state=42),
    X_train, y_train, cv=5, scoring='roc_auc'
)
print(f"\nCross-validation AUC scores: {cv_scores}")
print(f"Mean CV AUC: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

# Probability calibration
from sklearn.calibration import calibration_curve

prob_true, prob_pred = calibration_curve(y_test, y_proba_rf, n_bins=10)

plt.figure(figsize=(8, 6))
plt.plot(prob_pred, prob_true, 'o-', label='Random Forest')
plt.plot([0, 1], [0, 1], 'k--', label='Perfect Calibration')
plt.xlabel('Mean Predicted Probability')
plt.ylabel('Fraction of Positives')
plt.title('Calibration Curve')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## Class Imbalance Handling

- **Oversampling**: Increase minority class samples
- **Undersampling**: Reduce majority class samples
- **SMOTE**: Synthetic minority oversampling
- **Class weights**: Penalize misclassifying minority class

## Threshold Selection

- **Default (0.5)**: Equal misclassification cost
- **Custom threshold**: Based on business requirements
- **Optimal**: Maximizing F1-score or AUC

## Deliverables

- Classification metrics (accuracy, precision, recall, F1)
- Confusion matrices for all models
- ROC and Precision-Recall curves
- Feature importance analysis
- Model comparison table
- Recommendations for best model
- Probability calibration plots
