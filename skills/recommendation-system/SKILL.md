---
name: Recommendation System
description: Build collaborative and content-based recommendation engines for product recommendations, personalization, and improving user engagement
---

# Recommendation System

## Overview

This skill implements collaborative and content-based recommendation systems with matrix factorization techniques to predict user preferences, increase engagement, and drive conversions through personalized item suggestions.

## When to Use

- Developing recommendation features to improve user engagement and retention
- Implementing personalized product suggestions to increase sales and conversion rates
- Building hybrid recommendation systems that combine collaborative and content-based approaches
- Analyzing and optimizing recommendation coverage, diversity, and accuracy
- Handling sparse user-item interaction matrices and cold start scenarios
- Running A/B tests to measure the impact of recommendation algorithms on business metrics

## Approaches

- **Collaborative Filtering**: Users similar to you liked X
- **Content-based**: Items similar to what you liked
- **Hybrid**: Combining multiple approaches
- **Matrix Factorization**: Latent factor models
- **Deep Learning**: Neural networks for embeddings

## Key Metrics

- **Precision@K**: % recommendations relevant
- **Recall@K**: % relevant items found
- **NDCG**: Ranking quality metric
- **Coverage**: % items recommended
- **Diversity**: Variety in recommendations

## Implementation with Python

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import seaborn as sns

# Create sample user-item interaction data
np.random.seed(42)
users = [f'user_{i}' for i in range(100)]
items = [f'item_{i}' for i in range(50)]

# Generate ratings (sparse matrix)
ratings_list = []
for user in users:
    n_items_rated = np.random.randint(5, 20)
    rated_items = np.random.choice(items, n_items_rated, replace=False)
    for item in rated_items:
        rating = np.random.randint(1, 6)
        ratings_list.append({'user': user, 'item': item, 'rating': rating})

ratings_df = pd.DataFrame(ratings_list)
print("Sample Ratings:")
print(ratings_df.head(10))

# Create user-item matrix
user_item_matrix = ratings_df.pivot_table(
    index='user', columns='item', values='rating', fill_value=0
)

print(f"\nUser-Item Matrix Shape: {user_item_matrix.shape}")
print(f"Sparsity: {1 - (user_item_matrix != 0).sum().sum() / (user_item_matrix.shape[0] * user_item_matrix.shape[1]):.2%}")

# 1. User-based Collaborative Filtering
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(
    user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index
)

print("\n1. User Similarity Matrix (Sample):")
print(user_similarity_df.iloc[:5, :5])

# Get recommendations for a user
def get_user_based_recommendations(user_id, user_sim_matrix, user_item_mat, n=5):
    similar_users = user_sim_matrix[user_id].sort_values(ascending=False)[1:11]

    recommendations = {}
    for item in user_item_mat.columns:
        if user_item_mat.loc[user_id, item] == 0:  # Not yet rated
            score = (similar_users * user_item_mat.loc[similar_users.index, item]).sum()
            recommendations[item] = score

    top_recs = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n]
    return [rec[0] for rec in top_recs]

# Example: Get recommendations for user_0
user_recommendations = get_user_based_recommendations('user_0', user_similarity_df, user_item_matrix)
print(f"\nRecommendations for user_0: {user_recommendations}")

# 2. Item-based Collaborative Filtering
item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(
    item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns
)

print("\n2. Item Similarity Matrix (Sample):")
print(item_similarity_df.iloc[:5, :5])

# 3. Content-based Filtering
item_features = np.random.rand(len(items), 10)  # Simulate item features
item_feature_similarity = cosine_similarity(item_features)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# User similarity heatmap
sns.heatmap(user_similarity_df.iloc[:10, :10], annot=True, fmt='.2f', cmap='coolwarm',
            ax=axes[0, 0], cbar_kws={'label': 'Similarity'})
axes[0, 0].set_title('User Similarity Matrix (Sample)')

# Item similarity heatmap
sns.heatmap(item_similarity_df.iloc[:10, :10], annot=True, fmt='.2f', cmap='coolwarm',
            ax=axes[0, 1], cbar_kws={'label': 'Similarity'})
axes[0, 1].set_title('Item Similarity Matrix (Sample)')

# Rating distribution
axes[1, 0].hist(ratings_df['rating'], bins=5, color='steelblue', edgecolor='black', alpha=0.7)
axes[1, 0].set_xlabel('Rating')
axes[1, 0].set_ylabel('Count')
axes[1, 0].set_title('Rating Distribution')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# Sparsity by user
user_rating_counts = user_item_matrix.astype(bool).sum(axis=1)
axes[1, 1].hist(user_rating_counts, bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
axes[1, 1].set_xlabel('Number of Rated Items')
axes[1, 1].set_ylabel('Number of Users')
axes[1, 1].set_title('User Activity Distribution')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# 4. Matrix Factorization (NMF)
nmf = NMF(n_components=10, init='random', random_state=42, max_iter=200)
user_latent = nmf.fit_transform(user_item_matrix)
item_latent = nmf.components_.T

print(f"\n4. Matrix Factorization:")
print(f"User latent factors shape: {user_latent.shape}")
print(f"Item latent factors shape: {item_latent.shape}")

# Reconstruct ratings
reconstructed_ratings = user_latent @ item_latent.T
reconstructed_df = pd.DataFrame(
    reconstructed_ratings, index=user_item_matrix.index, columns=user_item_matrix.columns
)

# Calculate RMSE
original_ratings = user_item_matrix[user_item_matrix > 0]
predicted_ratings = reconstructed_df[user_item_matrix > 0]
rmse = np.sqrt(np.mean((original_ratings - predicted_ratings) ** 2))
print(f"Reconstruction RMSE: {rmse:.4f}")

# 5. Evaluation Metrics
def precision_at_k(actual, predicted, k=5):
    if len(actual) == 0:
        return 0
    return len(set(actual[:k]) & set(predicted)) / k

def recall_at_k(actual, predicted, k=5):
    if len(actual) == 0:
        return 0
    return len(set(actual[:k]) & set(predicted)) / len(actual)

# Simulate test set
test_user = 'user_0'
actual_items = ratings_df[ratings_df['user'] == test_user]['item'].values
predicted_items = get_user_based_recommendations(test_user, user_similarity_df, user_item_matrix, n=10)

p_at_5 = precision_at_k(predicted_items, actual_items, k=5)
r_at_5 = recall_at_k(predicted_items, actual_items, k=5)

print(f"\n5. Evaluation Metrics:")
print(f"Precision@5: {p_at_5:.2%}")
print(f"Recall@5: {r_at_5:.2%}")
print(f"F1@5: {2 * (p_at_5 * r_at_5) / (p_at_5 + r_at_5):.2%}")

# 6. Coverage and Diversity
recommended_items = set()
for user in user_item_matrix.index[:20]:
    recs = get_user_based_recommendations(user, user_similarity_df, user_item_matrix, n=5)
    recommended_items.update(recs)

coverage = len(recommended_items) / len(items)
print(f"\nCoverage: {coverage:.2%}")

# 7. Popularity Analysis
item_popularity = ratings_df['item'].value_counts()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Top items
axes[0].barh(item_popularity.head(10).index, item_popularity.head(10).values,
             color='steelblue', edgecolor='black', alpha=0.7)
axes[0].set_xlabel('Number of Ratings')
axes[0].set_title('Top 10 Most Popular Items')
axes[0].grid(True, alpha=0.3, axis='x')

# Popularity distribution
axes[1].hist(item_popularity, bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
axes[1].set_xlabel('Number of Ratings')
axes[1].set_ylabel('Number of Items')
axes[1].set_title('Item Popularity Distribution')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# 8. Cold Start Problem Analysis
new_user = 'new_user'
new_user_ratings = pd.DataFrame({
    'user': [new_user] * 2,
    'item': ['item_0', 'item_1'],
    'rating': [5, 4]
})

print(f"\n8. Cold Start Problem:")
print(f"New user has rated: {len(new_user_ratings)} items")
print(f"Recommendation challenge: Limited user history")

# 9. Recommendation accuracy over time
k_values = [1, 3, 5, 10]
metrics_over_k = []

for k in k_values:
    precision_scores = []
    for user in user_item_matrix.index[:10]:
        recs = get_user_based_recommendations(user, user_similarity_df, user_item_matrix, n=k)
        actual = ratings_df[ratings_df['user'] == user]['item'].values
        precision_scores.append(precision_at_k(recs, actual, k=k))

    metrics_over_k.append({
        'K': k,
        'Precision': np.mean(precision_scores),
        'Recall': np.mean([recall_at_k(get_user_based_recommendations(user, user_similarity_df, user_item_matrix, n=k),
                          ratings_df[ratings_df['user'] == user]['item'].values, k=k)
                          for user in user_item_matrix.index[:10]])
    })

metrics_df = pd.DataFrame(metrics_over_k)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(metrics_df['K'], metrics_df['Precision'], marker='o', linewidth=2, label='Precision', markersize=8)
ax.plot(metrics_df['K'], metrics_df['Recall'], marker='s', linewidth=2, label='Recall', markersize=8)
ax.set_xlabel('K (Number of Recommendations)')
ax.set_ylabel('Score')
ax.set_title('Precision and Recall vs K')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 10. A/B Test Results (Simulated)
print("\n10. A/B Test Results (Simulated):")
print("Control (No recommendations): 5.2% Conversion Rate")
print("Treatment (Recommendations): 7.8% Conversion Rate")
print("Lift: 50% (Statistically Significant, p < 0.05)")

print("\nRecommendation system complete!")
```

## Algorithm Comparison

- **Collaborative Filtering**: Simple, no content needed
- **Content-based**: Works with cold starts
- **Matrix Factorization**: Scalable, finds latent patterns
- **Deep Learning**: Complex patterns, requires data
- **Hybrid**: Combines strengths of multiple approaches

## Implementation Considerations

- Handling cold start (new users/items)
- Computational efficiency at scale
- Addressing sparsity (most items not rated)
- Diversity vs relevance trade-off
- Real-time vs batch recommendations

## Deliverables

- User-item interaction matrix
- Similarity matrices
- Recommendations for sample users
- Evaluation metrics (precision, recall, NDCG)
- Coverage and diversity analysis
- Visualization of results
- Production implementation code
