---
name: Clustering Analysis
description: Identify groups and patterns in data using k-means, hierarchical clustering, and DBSCAN for cluster discovery, customer segmentation, and unsupervised learning
---

# Clustering Analysis

## Overview

Clustering partitions data into groups of similar observations without pre-defined labels, enabling discovery of natural patterns and structures in data.

## When to Use

- Segmenting customers based on purchasing behavior or demographics
- Discovering natural groupings in data without prior knowledge of categories
- Identifying market segments for targeted marketing campaigns
- Organizing large datasets into meaningful categories for further analysis
- Finding patterns in gene expression data or medical imaging
- Grouping documents, products, or users by similarity for recommendation systems

## Clustering Algorithms

- **K-Means**: Partitioning into k clusters
- **Hierarchical**: Dendrograms showing nested clusters
- **DBSCAN**: Density-based arbitrary-shaped clusters
- **Gaussian Mixture**: Probabilistic clustering
- **Agglomerative**: Bottom-up hierarchical approach

## Key Concepts

- **Cluster Validation**: Metrics to evaluate cluster quality
- **Optimal Clusters**: Methods to determine best k
- **Inertia**: Within-cluster sum of squares
- **Silhouette Score**: Measure of cluster separation
- **Dendrogram**: Hierarchical clustering visualization

## Implementation with Python

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    silhouette_score, silhouette_samples, davies_bouldin_score,
    calinski_harabasz_score
)
from scipy.cluster.hierarchy import dendrogram, linkage
import seaborn as sns

# Generate sample data
np.random.seed(42)
n_samples = 300
centers = [[0, 0], [5, 5], [-3, 4]]
X = np.vstack([
    np.random.randn(100, 2) + centers[0],
    np.random.randn(100, 2) + centers[1],
    np.random.randn(100, 2) + centers[2],
])

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means with Elbow method
inertias = []
silhouette_scores = []
k_range = range(2, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

fig, axes = plt.subplots(1, 2, figsize=(14, 4))

axes[0].plot(k_range, inertias, 'bo-')
axes[0].set_xlabel('Number of Clusters (k)')
axes[0].set_ylabel('Inertia')
axes[0].set_title('Elbow Method')
axes[0].grid(True, alpha=0.3)

axes[1].plot(k_range, silhouette_scores, 'go-')
axes[1].set_xlabel('Number of Clusters (k)')
axes[1].set_ylabel('Silhouette Score')
axes[1].set_title('Silhouette Analysis')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Optimal k = 3
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)

# K-Means visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# K-Means clusters
axes[0].scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis', alpha=0.6)
axes[0].scatter(
    kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
    c='red', marker='X', s=200, edgecolors='black', linewidths=2
)
axes[0].set_title(f'K-Means (k={optimal_k})')
axes[0].set_xlabel('Feature 1')
axes[0].set_ylabel('Feature 2')

# Silhouette plot
ax = axes[1]
y_lower = 10
silhouette_vals = silhouette_samples(X_scaled, kmeans_labels)

for i in range(optimal_k):
    cluster_silhouette_vals = silhouette_vals[kmeans_labels == i]
    cluster_silhouette_vals.sort()

    size_cluster_i = cluster_silhouette_vals.shape[0]
    y_upper = y_lower + size_cluster_i

    ax.fill_betweenx(np.arange(y_lower, y_upper),
                      0, cluster_silhouette_vals,
                      alpha=0.7, label=f'Cluster {i}')
    y_lower = y_upper + 10

ax.axvline(x=silhouette_score(X_scaled, kmeans_labels), color="red", linestyle="--")
ax.set_xlabel('Silhouette Coefficient')
ax.set_ylabel('Cluster Label')
ax.set_title('Silhouette Plot')

# Hierarchical clustering
linkage_matrix = linkage(X_scaled, method='ward')
dendrogram(linkage_matrix, ax=axes[2], truncate_mode='lastp', p=10)
axes[2].set_title('Dendrogram (Ward)')
axes[2].set_xlabel('Sample Index')

plt.tight_layout()
plt.show()

# Hierarchical clustering
hierarchical = AgglomerativeClustering(n_clusters=optimal_k, linkage='ward')
hier_labels = hierarchical.fit_predict(X_scaled)

# DBSCAN clustering
dbscan = DBSCAN(eps=0.4, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)
n_clusters_dbscan = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
n_noise = list(dbscan_labels).count(-1)

# Gaussian Mixture Model
gmm = GaussianMixture(n_components=optimal_k, random_state=42)
gmm_labels = gmm.fit_predict(X_scaled)
gmm_proba = gmm.predict_proba(X_scaled)

# Clustering algorithm comparison
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

algorithms = [
    (kmeans_labels, 'K-Means'),
    (hier_labels, 'Hierarchical'),
    (dbscan_labels, 'DBSCAN'),
    (gmm_labels, 'Gaussian Mixture'),
]

for idx, (labels, title) in enumerate(algorithms):
    ax = axes[idx // 2, idx % 2]

    # Skip noise points for DBSCAN
    mask = labels != -1
    scatter = ax.scatter(
        X[mask, 0], X[mask, 1], c=labels[mask], cmap='viridis', alpha=0.6
    )

    if title == 'DBSCAN' and n_noise > 0:
        noise_mask = labels == -1
        ax.scatter(X[noise_mask, 0], X[noise_mask, 1], c='red', marker='x', s=100, label='Noise')
        ax.legend()

    ax.set_title(f'{title} (n_clusters={len(set(labels[mask]))})')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')

plt.tight_layout()
plt.show()

# Cluster validation metrics
validation_metrics = {
    'Algorithm': ['K-Means', 'Hierarchical', 'DBSCAN', 'GMM'],
    'Silhouette Score': [
        silhouette_score(X_scaled, kmeans_labels),
        silhouette_score(X_scaled, hier_labels),
        silhouette_score(X_scaled[dbscan_labels != -1], dbscan_labels[dbscan_labels != -1]) if n_noise < len(X_scaled) else np.nan,
        silhouette_score(X_scaled, gmm_labels),
    ],
    'Davies-Bouldin Index': [
        davies_bouldin_score(X_scaled, kmeans_labels),
        davies_bouldin_score(X_scaled, hier_labels),
        davies_bouldin_score(X_scaled[dbscan_labels != -1], dbscan_labels[dbscan_labels != -1]) if n_noise < len(X_scaled) else np.nan,
        davies_bouldin_score(X_scaled, gmm_labels),
    ],
    'Calinski-Harabasz Index': [
        calinski_harabasz_score(X_scaled, kmeans_labels),
        calinski_harabasz_score(X_scaled, hier_labels),
        calinski_harabasz_score(X_scaled[dbscan_labels != -1], dbscan_labels[dbscan_labels != -1]) if n_noise < len(X_scaled) else np.nan,
        calinski_harabasz_score(X_scaled, gmm_labels),
    ],
}

metrics_df = pd.DataFrame(validation_metrics)
print("Clustering Validation Metrics:")
print(metrics_df)

# Cluster size analysis
sizes_df = pd.DataFrame({
    'K-Means': pd.Series(kmeans_labels).value_counts().sort_index(),
    'Hierarchical': pd.Series(hier_labels).value_counts().sort_index(),
    'GMM': pd.Series(gmm_labels).value_counts().sort_index(),
})

print("\nCluster Sizes:")
print(sizes_df)

# Membership probability (GMM)
fig, ax = plt.subplots(figsize=(10, 6))
membership = gmm_proba.max(axis=1)
scatter = ax.scatter(X[:, 0], X[:, 1], c=membership, cmap='RdYlGn', alpha=0.6, s=50)
ax.set_title('Cluster Membership Confidence (GMM)')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
plt.colorbar(scatter, ax=ax, label='Membership Probability')
plt.show()

# Cluster characteristics
kmeans_centers_original = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_df = pd.DataFrame(X, columns=['Feature 1', 'Feature 2'])
cluster_df['Cluster'] = kmeans_labels

for cluster_id in range(optimal_k):
    cluster_data = cluster_df[cluster_df['Cluster'] == cluster_id]
    print(f"\nCluster {cluster_id} Characteristics:")
    print(cluster_data[['Feature 1', 'Feature 2']].describe())
```

## Cluster Quality Metrics

- **Silhouette Score**: -1 to 1 (higher is better)
- **Davies-Bouldin Index**: Lower is better
- **Calinski-Harabasz Index**: Higher is better
- **Inertia**: Lower is better (KMeans only)

## Algorithm Selection

- **K-Means**: Fast, spherical clusters, k needs specification
- **Hierarchical**: Produces dendrogram, interpretable
- **DBSCAN**: Arbitrary shapes, handles noise
- **GMM**: Probabilistic, soft assignments

## Deliverables

- Optimal cluster count analysis
- Cluster visualizations
- Validation metrics comparison
- Cluster characteristics summary
- Silhouette plots
- Dendrogram for hierarchical clustering
- Membership assignments
