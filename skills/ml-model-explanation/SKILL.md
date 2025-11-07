---
name: ML Model Explanation
description: Interpret machine learning models using SHAP, LIME, feature importance, partial dependence, and attention visualization for explainability
---

# ML Model Explanation

Model explainability makes machine learning decisions transparent and interpretable, enabling trust, compliance, debugging, and actionable insights from predictions.

## Explanation Techniques

- **Feature Importance**: Global feature contribution to predictions
- **SHAP Values**: Game theory-based feature attribution
- **LIME**: Local linear approximations for individual predictions
- **Partial Dependence Plots**: Feature relationship with predictions
- **Attention Maps**: Visualization of model focus areas
- **Surrogate Models**: Simpler interpretable approximations

## Explainability Types

- **Global**: Overall model behavior and patterns
- **Local**: Explanation for individual predictions
- **Feature-Level**: Which features matter most
- **Model-Level**: How different components interact

## Python Implementation

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.inspection import partial_dependence, permutation_importance
import warnings
warnings.filterwarnings('ignore')

print("=== 1. Feature Importance Analysis ===")

# Create dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10,
                          n_redundant=5, random_state=42)
feature_names = [f'Feature_{i}' for i in range(20)]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
gb_model.fit(X_train, y_train)

# Feature importance methods
print("\n=== Feature Importance Comparison ===")

# 1. Impurity-based importance (default)
impurity_importance = rf_model.feature_importances_

# 2. Permutation importance
perm_importance = permutation_importance(rf_model, X_test, y_test, n_repeats=10, random_state=42)

# Create comparison dataframe
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Impurity': impurity_importance,
    'Permutation': perm_importance.importances_mean
}).sort_values('Impurity', ascending=False)

print("\nTop 10 Most Important Features (by Impurity):")
print(importance_df.head(10)[['Feature', 'Impurity']])

# 2. SHAP-like Feature Attribution
print("\n=== SHAP-like Feature Attribution ===")

class SimpleShapCalculator:
    def __init__(self, model, X_background):
        self.model = model
        self.X_background = X_background
        self.baseline = model.predict_proba(X_background.mean(axis=0).reshape(1, -1))[0]

    def predict_difference(self, X_sample):
        """Get prediction difference from baseline"""
        pred = self.model.predict_proba(X_sample)[0]
        return pred - self.baseline

    def calculate_shap_values(self, X_instance, n_iterations=100):
        """Approximate SHAP values"""
        shap_values = np.zeros(X_instance.shape[1])
        n_features = X_instance.shape[1]

        for i in range(n_iterations):
            # Random feature subset
            subset_mask = np.random.random(n_features) > 0.5

            # With and without feature
            X_with = X_instance.copy()
            X_without = X_instance.copy()
            X_without[0, ~subset_mask] = self.X_background[0, ~subset_mask]

            # Marginal contribution
            contribution = (self.predict_difference(X_with)[1] -
                          self.predict_difference(X_without)[1])

            shap_values[~subset_mask] += contribution / n_iterations

        return shap_values

shap_calc = SimpleShapCalculator(rf_model, X_train)

# Calculate SHAP values for a sample
sample_idx = 0
shap_vals = shap_calc.calculate_shap_values(X_test[sample_idx:sample_idx+1], n_iterations=50)

print(f"\nSHAP Values for Sample {sample_idx}:")
shap_df = pd.DataFrame({
    'Feature': feature_names,
    'SHAP_Value': shap_vals
}).sort_values('SHAP_Value', key=abs, ascending=False)

print(shap_df.head(10)[['Feature', 'SHAP_Value']])

# 3. Partial Dependence Analysis
print("\n=== 3. Partial Dependence Analysis ===")

# Calculate partial dependence for top features
top_features = importance_df['Feature'].head(3).values
top_feature_indices = [feature_names.index(f) for f in top_features]

pd_data = {}
for feature_idx in top_feature_indices:
    pd_result = partial_dependence(rf_model, X_test, [feature_idx])
    pd_data[feature_names[feature_idx]] = pd_result

print(f"Partial dependence calculated for features: {list(pd_data.keys())}")

# 4. LIME - Local Interpretable Model-agnostic Explanations
print("\n=== 4. LIME (Local Surrogate Model) ===")

class SimpleLIME:
    def __init__(self, model, X_train):
        self.model = model
        self.X_train = X_train
        self.scaler = StandardScaler()
        self.scaler.fit(X_train)

    def explain_instance(self, instance, n_samples=1000, n_features=10):
        """Explain prediction using local linear model"""
        # Generate perturbed samples
        scaled_instance = self.scaler.transform(instance.reshape(1, -1))
        perturbations = np.random.normal(scaled_instance, 0.3, (n_samples, instance.shape[0]))

        # Get predictions
        predictions = self.model.predict_proba(perturbations)[:, 1]

        # Train local linear model
        distances = np.sum((perturbations - scaled_instance) ** 2, axis=1)
        weights = np.exp(-distances)

        # Linear regression weights
        local_model = LogisticRegression()
        local_model.fit(perturbations, predictions, sample_weight=weights)

        # Get feature importance
        feature_weights = np.abs(local_model.coef_[0])
        top_indices = np.argsort(feature_weights)[-n_features:]

        return {
            'features': [feature_names[i] for i in top_indices],
            'weights': feature_weights[top_indices],
            'prediction': self.model.predict(instance.reshape(1, -1))[0]
        }

lime = SimpleLIME(rf_model, X_train)
lime_explanation = lime.explain_instance(X_test[0])

print(f"\nLIME Explanation for Sample 0:")
for feat, weight in zip(lime_explanation['features'], lime_explanation['weights']):
    print(f"  {feat}: {weight:.4f}")

# 5. Decision Tree Visualization
print("\n=== 5. Decision Tree Interpretation ===")

# Train small tree for visualization
small_tree = DecisionTreeClassifier(max_depth=3, random_state=42)
small_tree.fit(X_train, y_train)

print(f"Decision Tree (depth=3) trained")
print(f"Tree accuracy: {small_tree.score(X_test, y_test):.4f}")

# 6. Model-agnostic global explanations
print("\n=== 6. Global Model Behavior ===")

class GlobalExplainer:
    def __init__(self, model):
        self.model = model

    def get_prediction_distribution(self, X):
        """Analyze prediction distribution"""
        predictions = self.model.predict_proba(X)
        return {
            'class_0_mean': predictions[:, 0].mean(),
            'class_1_mean': predictions[:, 1].mean(),
            'class_1_std': predictions[:, 1].std()
        }

    def feature_sensitivity(self, X, feature_idx, n_perturbations=10):
        """Measure sensitivity to feature changes"""
        original_pred = self.model.predict_proba(X)[:, 1].mean()
        sensitivities = []

        for perturbation_level in np.linspace(0.1, 1.0, n_perturbations):
            X_perturbed = X.copy()
            X_perturbed[:, feature_idx] = np.random.normal(
                X[:, feature_idx].mean(),
                X[:, feature_idx].std() * perturbation_level,
                len(X)
            )
            perturbed_pred = self.model.predict_proba(X_perturbed)[:, 1].mean()
            sensitivities.append(abs(perturbed_pred - original_pred))

        return np.array(sensitivities)

explainer = GlobalExplainer(rf_model)
pred_dist = explainer.get_prediction_distribution(X_test)
print(f"\nPrediction Distribution:")
print(f"  Class 0 mean probability: {pred_dist['class_0_mean']:.4f}")
print(f"  Class 1 mean probability: {pred_dist['class_1_mean']:.4f}")

# 7. Visualization
print("\n=== 7. Explanability Visualizations ===")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# 1. Feature Importance Comparison
top_features_plot = importance_df.head(10)
axes[0, 0].barh(top_features_plot['Feature'], top_features_plot['Impurity'], color='steelblue')
axes[0, 0].set_xlabel('Importance Score')
axes[0, 0].set_title('Feature Importance (Random Forest)')
axes[0, 0].invert_yaxis()

# 2. Permutation vs Impurity Importance
axes[0, 1].scatter(importance_df['Impurity'], importance_df['Permutation'], alpha=0.6)
axes[0, 1].set_xlabel('Impurity Importance')
axes[0, 1].set_ylabel('Permutation Importance')
axes[0, 1].set_title('Feature Importance Methods Comparison')
axes[0, 1].grid(True, alpha=0.3)

# 3. SHAP Values
shap_sorted = shap_df.head(10).sort_values('SHAP_Value')
colors = ['red' if x < 0 else 'green' for x in shap_sorted['SHAP_Value']]
axes[0, 2].barh(shap_sorted['Feature'], shap_sorted['SHAP_Value'], color=colors)
axes[0, 2].set_xlabel('SHAP Value')
axes[0, 2].set_title('SHAP Values for Sample 0')
axes[0, 2].axvline(x=0, color='black', linestyle='--', linewidth=0.8)

# 4. Partial Dependence
feature_0_idx = top_feature_indices[0]
feature_0_values = np.linspace(X_test[:, feature_0_idx].min(), X_test[:, feature_0_idx].max(), 50)
predictions_pd = []
for val in feature_0_values:
    X_temp = X_test.copy()
    X_temp[:, feature_0_idx] = val
    pred = rf_model.predict_proba(X_temp)[:, 1].mean()
    predictions_pd.append(pred)

axes[1, 0].plot(feature_0_values, predictions_pd, linewidth=2, color='purple')
axes[1, 0].set_xlabel(feature_names[feature_0_idx])
axes[1, 0].set_ylabel('Average Prediction (Class 1)')
axes[1, 0].set_title('Partial Dependence Plot')
axes[1, 0].grid(True, alpha=0.3)

# 5. Model Prediction Distribution
pred_proba = rf_model.predict_proba(X_test)[:, 1]
axes[1, 1].hist(pred_proba, bins=30, color='coral', edgecolor='black', alpha=0.7)
axes[1, 1].set_xlabel('Predicted Probability (Class 1)')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Prediction Distribution')
axes[1, 1].grid(True, alpha=0.3, axis='y')

# 6. Feature Sensitivity Analysis
sensitivities = []
for feat_idx in range(min(5, X_test.shape[1])):
    sensitivity = explainer.feature_sensitivity(X_test, feat_idx, n_perturbations=5)
    sensitivities.append(sensitivity.mean())

axes[1, 2].bar(range(min(5, X_test.shape[1])), sensitivities, color='lightgreen', edgecolor='black')
axes[1, 2].set_xticks(range(min(5, X_test.shape[1])))
axes[1, 2].set_xticklabels([f'F{i}' for i in range(min(5, X_test.shape[1]))])
axes[1, 2].set_ylabel('Average Sensitivity')
axes[1, 2].set_title('Feature Sensitivity to Perturbations')
axes[1, 2].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('model_explainability.png', dpi=100, bbox_inches='tight')
print("\nVisualization saved as 'model_explainability.png'")

# 8. Summary
print("\n=== Explainability Summary ===")
print(f"Total Features Analyzed: {len(feature_names)}")
print(f"Most Important Feature: {importance_df.iloc[0]['Feature']}")
print(f"Importance Score: {importance_df.iloc[0]['Impurity']:.4f}")
print(f"Model Accuracy: {rf_model.score(X_test, y_test):.4f}")
print(f"Average Prediction Confidence: {pred_proba.mean():.4f}")

print("\nML model explanation setup completed!")
```

## Explanation Techniques Comparison

- **Feature Importance**: Fast, global, model-specific
- **SHAP**: Theoretically sound, game-theory based, computationally expensive
- **LIME**: Model-agnostic, local explanations, interpretable
- **PDP**: Shows feature relationships, can be misleading with correlations
- **Attention**: Works for neural networks, interpretable attention weights

## Interpretability vs Accuracy Trade-off

- Linear models: Highly interpretable, lower accuracy
- Tree models: Interpretable, moderate accuracy
- Neural networks: High accuracy, less interpretable
- Ensemble models: High accuracy, need explanation techniques

## Regulatory Compliance

- GDPR: Right to explanation for automated decisions
- Fair Lending: Explainability for credit decisions
- Insurance: Transparency in underwriting
- Healthcare: Medical decision explanation

## Deliverables

- Feature importance rankings
- Local explanations for predictions
- Partial dependence plots
- Global behavior analysis
- Model interpretation report
- Explanation dashboard
