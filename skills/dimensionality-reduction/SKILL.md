---
name: Dimensionality Reduction
description: Reduce feature dimensionality using PCA, t-SNE, and feature selection for feature reduction, visualization, and computational efficiency
---

# Dimensionality Reduction

## Overview

Dimensionality reduction techniques reduce the number of features while preserving important information, improving model efficiency and enabling visualization of high-dimensional data.

## When to Use

- High-dimensional datasets with many features
- Visualizing complex datasets in 2D or 3D
- Reducing computational complexity and training time
- Removing redundant or highly correlated features
- Preventing overfitting in machine learning models
- Preprocessing data before clustering or classification

## Techniques

- **PCA**: Principal Component Analysis
- **t-SNE**: t-Distributed Stochastic Neighbor Embedding
- **UMAP**: Uniform Manifold Approximation and Projection
- **Feature Selection**: Selecting important features
- **Feature Extraction**: Creating new features

## Benefits

- Reduce computational complexity
- Remove noise and redundancy
- Improve model generalization
- Enable visualization
- Prevent curse of dimensionality

## Implementation with Python

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, TruncatedSVD, FactorAnalysis
from sklearn.manifold import TSNE, MDS
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif
import seaborn as sns

# Load data
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA()
pca.fit(X_scaled)

# Explained variance
explained_variance = np.cumsum(pca.explained_variance_ratio_)
print("Explained Variance Ratio by Component:")
print(pca.explained_variance_ratio_)
print(f"Cumulative Variance (first 2): {explained_variance[1]:.4f}")

# Scree plot
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

axes[0].plot(range(1, len(pca.explained_variance_ratio_) + 1),
             pca.explained_variance_ratio_, 'bo-')
axes[0].set_xlabel('Principal Component')
axes[0].set_ylabel('Explained Variance Ratio')
axes[0].set_title('Scree Plot')
axes[0].grid(True, alpha=0.3)

axes[1].plot(range(1, len(explained_variance) + 1),
             explained_variance, 'go-')
axes[1].axhline(y=0.95, color='r', linestyle='--', label='95% Variance')
axes[1].set_xlabel('Number of Components')
axes[1].set_ylabel('Cumulative Explained Variance')
axes[1].set_title('Cumulative Explained Variance')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# PCA with 2 components
pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X_scaled)

# PCA with 3 components
pca_3d = PCA(n_components=3)
X_pca_3d = pca_3d.fit_transform(X_scaled)

# PCA visualization
fig = plt.figure(figsize=(14, 5))

# 2D PCA
ax1 = fig.add_subplot(131)
scatter = ax1.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=y, cmap='viridis', alpha=0.6)
ax1.set_xlabel(f'PC1 ({pca_2d.explained_variance_ratio_[0]:.2%})')
ax1.set_ylabel(f'PC2 ({pca_2d.explained_variance_ratio_[1]:.2%})')
ax1.set_title('PCA 2D')
plt.colorbar(scatter, ax=ax1)

# 3D PCA
ax2 = fig.add_subplot(132, projection='3d')
scatter = ax2.scatter(X_pca_3d[:, 0], X_pca_3d[:, 1], X_pca_3d[:, 2],
                      c=y, cmap='viridis', alpha=0.6)
ax2.set_xlabel(f'PC1 ({pca_3d.explained_variance_ratio_[0]:.2%})')
ax2.set_ylabel(f'PC2 ({pca_3d.explained_variance_ratio_[1]:.2%})')
ax2.set_zlabel(f'PC3 ({pca_3d.explained_variance_ratio_[2]:.2%})')
ax2.set_title('PCA 3D')

# Loading plot
ax3 = fig.add_subplot(133)
loadings = pca_2d.components_.T
for i, feature in enumerate(feature_names):
    ax3.arrow(0, 0, loadings[i, 0], loadings[i, 1],
             head_width=0.05, head_length=0.05, fc='blue', ec='blue')
    ax3.text(loadings[i, 0]*1.15, loadings[i, 1]*1.15, feature, fontsize=10)
ax3.set_xlim(-1, 1)
ax3.set_ylim(-1, 1)
ax3.set_xlabel(f'PC1 ({pca_2d.explained_variance_ratio_[0]:.2%})')
ax3.set_ylabel(f'PC2 ({pca_2d.explained_variance_ratio_[1]:.2%})')
ax3.set_title('PCA Loadings')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# t-SNE visualization
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='viridis', alpha=0.6)
plt.xlabel('t-SNE Dimension 1')
plt.ylabel('t-SNE Dimension 2')
plt.title('t-SNE Visualization')
plt.colorbar(scatter, label='Class')
plt.show()

# MDS visualization
mds = MDS(n_components=2, random_state=42)
X_mds = mds.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_mds[:, 0], X_mds[:, 1], c=y, cmap='viridis', alpha=0.6)
plt.xlabel('MDS Dimension 1')
plt.ylabel('MDS Dimension 2')
plt.title('MDS Visualization')
plt.colorbar(scatter, label='Class')
plt.show()

# Feature Selection - SelectKBest
selector = SelectKBest(score_func=f_classif, k=2)
X_selected = selector.fit_transform(X, y)
selected_features = np.array(feature_names)[selector.get_support()]
scores = selector.scores_

feature_scores = pd.DataFrame({
    'Feature': feature_names,
    'Score': scores
}).sort_values('Score', ascending=False)

print("\nFeature Selection (F-test):")
print(feature_scores)

plt.figure(figsize=(10, 5))
plt.barh(feature_scores['Feature'], feature_scores['Score'])
plt.xlabel('F-test Score')
plt.title('Feature Importance (SelectKBest)')
plt.tight_layout()
plt.show()

# Mutual Information
selector_mi = SelectKBest(score_func=mutual_info_classif, k=2)
X_selected_mi = selector_mi.fit_transform(X, y)
scores_mi = selector_mi.scores_

feature_scores_mi = pd.DataFrame({
    'Feature': feature_names,
    'Score': scores_mi
}).sort_values('Score', ascending=False)

print("\nFeature Selection (Mutual Information):")
print(feature_scores_mi)

# Tree-based feature importance
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)
importances = rf.feature_importances_

feature_importance = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values('Importance', ascending=False)

print("\nFeature Importance (Random Forest):")
print(feature_importance)

plt.figure(figsize=(10, 5))
plt.barh(feature_importance['Feature'], feature_importance['Importance'])
plt.xlabel('Importance')
plt.title('Feature Importance (Random Forest)')
plt.tight_layout()
plt.show()

# Factor Analysis
fa = FactorAnalysis(n_components=2, random_state=42)
X_fa = fa.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_fa[:, 0], X_fa[:, 1], c=y, cmap='viridis', alpha=0.6)
plt.xlabel('Factor 1')
plt.ylabel('Factor 2')
plt.title('Factor Analysis')
plt.colorbar(scatter, label='Class')
plt.show()

# Model performance comparison
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

models = {
    'Original Features': X_scaled,
    'PCA (2)': X_pca_2d,
    'PCA (3)': X_pca_3d,
    't-SNE': X_tsne,
    'Selected (2 best)': X_selected,
}

scores = {}
for name, X_reduced in models.items():
    clf = LogisticRegression(max_iter=200)
    cv_scores = cross_val_score(clf, X_reduced, y, cv=5, scoring='accuracy')
    scores[name] = {
        'Mean Accuracy': cv_scores.mean(),
        'Std Dev': cv_scores.std(),
        'Features': X_reduced.shape[1],
    }

scores_df = pd.DataFrame(scores).T
print("\nModel Performance with Different Dimensionality:")
print(scores_df)
```

## Algorithm Comparison

- **PCA**: Linear, fast, interpretable
- **t-SNE**: Non-linear, good visualization, computationally expensive
- **UMAP**: Non-linear, preserves local/global structure
- **Feature Selection**: Maintains interpretability
- **Factor Analysis**: Statistical approach

## Choosing Number of Components

- **Explained Variance**: Retain 95% of variance
- **Elbow Method**: Look for "elbow" in scree plot
- **Cross-validation**: Optimize for downstream task

## Deliverables

- Scree plots and cumulative variance
- 2D/3D visualizations
- PCA loadings interpretation
- Feature importance ranking
- Model performance comparison
- Component interpretation
