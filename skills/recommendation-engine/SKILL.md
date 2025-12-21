---
name: Recommendation Engine
description: Build recommendation systems using collaborative filtering, content-based filtering, matrix factorization, and neural network approaches
---

# Recommendation Engine

## Overview

This skill provides comprehensive implementation of recommendation systems using collaborative filtering, content-based filtering, matrix factorization, and hybrid approaches to predict user preferences and deliver personalized suggestions.

## When to Use

- Building personalized product recommendations for e-commerce platforms
- Creating content recommendation systems for streaming services, news platforms, or social media
- Implementing user-user or item-item collaborative filtering based on interaction patterns
- Addressing cold start problems for new users or items with limited interaction history
- Evaluating recommendation quality using precision@k, recall@k, and NDCG metrics
- Scaling recommendation systems to handle millions of users and items efficiently

## Recommendation Approaches

- **Collaborative Filtering**: Using user-item interaction patterns
- **Content-Based**: Recommending similar items based on features
- **Hybrid**: Combining multiple approaches
- **Matrix Factorization**: Decomposing user-item matrix
- **Neural Networks**: Deep learning for embeddings
- **Knowledge-Based**: Using domain knowledge and rules

## Key Techniques

- **User-User Similarity**: Finding similar users
- **Item-Item Similarity**: Finding similar items
- **Latent Factors**: Hidden patterns in data
- **Embeddings**: Vector representations of users/items
- **Graph-Based**: Social networks and item graphs

## Python Implementation

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix
import warnings
warnings.filterwarnings('ignore')

print("=== 1. Collaborative Filtering ===")

# Create sample user-item interaction matrix
np.random.seed(42)
n_users = 50
n_items = 30

# Create sparse interaction matrix (ratings: 0-5)
interaction_matrix = np.random.randint(0, 6, size=(n_users, n_items))
# Make it sparse (many zeros)
interaction_matrix[np.random.random((n_users, n_items)) > 0.3] = 0

print(f"User-Item Matrix Shape: {interaction_matrix.shape}")
print(f"Sparsity: {(interaction_matrix == 0).sum() / interaction_matrix.size:.2%}")

# User-based collaborative filtering
print("\n=== User-Based Collaborative Filtering ===")

# Normalize ratings
user_means = np.nanmean(np.where(interaction_matrix != 0, interaction_matrix, np.nan), axis=1, keepdims=True)
user_means[np.isnan(user_means)] = 0

interaction_normalized = interaction_matrix - user_means

# Convert to sparse matrix
interaction_sparse = csr_matrix(interaction_normalized)

# Compute user-user similarity
user_similarity = cosine_similarity(interaction_sparse)

print(f"User Similarity Matrix Shape: {user_similarity.shape}")
print(f"Sample user similarity [0,1]: {user_similarity[0, 1]:.4f}")

# 2. Item-based collaborative filtering
print("\n=== Item-Based Collaborative Filtering ===")

# Compute item-item similarity
item_similarity = cosine_similarity(interaction_sparse.T)

print(f"Item Similarity Matrix Shape: {item_similarity.shape}")
print(f"Sample item similarity [0,1]: {item_similarity[0, 1]:.4f}")

# 3. Matrix Factorization (SVD)
print("\n=== Matrix Factorization (SVD) ===")

# Apply SVD
svd = TruncatedSVD(n_components=5, random_state=42)
user_factors = svd.fit_transform(interaction_sparse)
item_factors = svd.components_.T

print(f"User Factors Shape: {user_factors.shape}")
print(f"Item Factors Shape: {item_factors.shape}")
print(f"Explained Variance Ratio: {svd.explained_variance_ratio_.sum():.4f}")

# Reconstruct ratings
reconstructed_ratings = user_factors @ item_factors.T + user_means

print(f"Reconstructed Ratings Shape: {reconstructed_ratings.shape}")
print(f"Reconstruction Error: {np.mean((interaction_matrix - reconstructed_ratings) ** 2):.4f}")

# 4. Content-Based Filtering
print("\n=== Content-Based Filtering ===")

# Create item features (e.g., product descriptions)
item_descriptions = [
    "action adventure movie thriller",
    "romantic comedy drama love",
    "sci-fi technology future space",
    "horror scary thriller dark",
    "animation family kids fun",
    "adventure action explosions",
    "documentary educational learning",
    "sports competition championship",
    "musical dance entertainment",
    "historical drama biography"
]

# Expand to 30 items
item_descriptions = (item_descriptions * 4)[:30]

# Create TF-IDF vectors
tfidf = TfidfVectorizer(lowercase=True)
item_features = tfidf.fit_transform(item_descriptions)

# Compute item-item similarity based on content
content_similarity = cosine_similarity(item_features)

print(f"Item Feature Matrix Shape: {item_features.shape}")
print(f"Content-based Item Similarity [0,1]: {content_similarity[0, 1]:.4f}")

# 5. Hybrid Recommendation System
print("\n=== Hybrid Recommendation System ===")

class HybridRecommender:
    def __init__(self, user_similarity, item_similarity, interaction_matrix):
        self.user_similarity = user_similarity
        self.item_similarity = item_similarity
        self.interaction_matrix = interaction_matrix
        self.n_users = interaction_matrix.shape[0]
        self.n_items = interaction_matrix.shape[1]

    def recommend_user_based(self, user_id, n_recommendations=5):
        """User-based collaborative filtering recommendation"""
        # Get similar users
        similar_users = self.user_similarity[user_id]
        similar_indices = np.argsort(similar_users)[-5:-1]  # Top 4 similar users

        # Get items rated highly by similar users
        similar_users_ratings = self.interaction_matrix[similar_indices]
        user_items = self.interaction_matrix[user_id]

        # Items not rated by user but rated by similar users
        recommendations = {}
        for item_id in range(self.n_items):
            if user_items[item_id] == 0:
                avg_rating = np.mean(similar_users_ratings[:, item_id])
                if avg_rating > 2:
                    recommendations[item_id] = avg_rating

        top_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]
        return top_items

    def recommend_item_based(self, user_id, n_recommendations=5):
        """Item-based collaborative filtering recommendation"""
        # Get items rated by user
        user_items = self.interaction_matrix[user_id]
        rated_items = np.where(user_items > 0)[0]

        if len(rated_items) == 0:
            return []

        # Find similar items
        recommendations = {}
        for rated_item in rated_items:
            similar_items = self.item_similarity[rated_item]
            similar_indices = np.argsort(similar_items)[-10:]

            for sim_item in similar_indices:
                if user_items[sim_item] == 0:
                    if sim_item not in recommendations:
                        recommendations[sim_item] = 0
                    recommendations[sim_item] += user_items[rated_item] * similar_items[sim_item]

        top_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]
        return top_items

    def get_hybrid_recommendations(self, user_id, n_recommendations=5, alpha=0.5):
        """Hybrid approach combining user-based and item-based"""
        user_based = dict(self.recommend_user_based(user_id, n_recommendations * 2))
        item_based = dict(self.recommend_item_based(user_id, n_recommendations * 2))

        hybrid = {}
        for item_id in set(list(user_based.keys()) + list(item_based.keys())):
            score = (alpha * user_based.get(item_id, 0) +
                    (1 - alpha) * item_based.get(item_id, 0))
            hybrid[item_id] = score

        top_items = sorted(hybrid.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]
        return top_items

# Create recommender
recommender = HybridRecommender(user_similarity, item_similarity, interaction_matrix)

# Generate recommendations for user 0
print("\nRecommendations for User 0:")
print("User-Based:", recommender.recommend_user_based(0, 5))
print("Item-Based:", recommender.recommend_item_based(0, 5))
print("Hybrid:", recommender.get_hybrid_recommendations(0, 5))

# 6. Evaluation Metrics
print("\n=== Recommendation Metrics ===")

class RecommendationMetrics:
    @staticmethod
    def precision_at_k(actual, predicted, k=5):
        """Precision at K"""
        pred_k = predicted[:k]
        hits = len(set(actual) & set(pred_k))
        return hits / k if k > 0 else 0

    @staticmethod
    def recall_at_k(actual, predicted, k=5):
        """Recall at K"""
        pred_k = predicted[:k]
        hits = len(set(actual) & set(pred_k))
        return hits / len(actual) if len(actual) > 0 else 0

    @staticmethod
    def ndcg_at_k(actual, predicted, k=5):
        """Normalized Discounted Cumulative Gain"""
        pred_k = predicted[:k]
        dcg = sum([1 / np.log2(i + 2) for i, item in enumerate(pred_k) if item in actual])
        idcg = sum([1 / np.log2(i + 2) for i in range(min(len(actual), k))])
        return dcg / idcg if idcg > 0 else 0

# Compute metrics
actual_items = [1, 5, 8, 12]
predicted_items = [1, 3, 5, 7, 9, 12, 15]

p5 = RecommendationMetrics.precision_at_k(actual_items, predicted_items, 5)
r5 = RecommendationMetrics.recall_at_k(actual_items, predicted_items, 5)
ndcg5 = RecommendationMetrics.ndcg_at_k(actual_items, predicted_items, 5)

print(f"Precision@5: {p5:.4f}")
print(f"Recall@5: {r5:.4f}")
print(f"NDCG@5: {ndcg5:.4f}")

# 7. Cold Start Problem Handling
print("\n=== Cold Start Problem ===")

class ColdStartHandler:
    def __init__(self, interaction_matrix):
        self.interaction_matrix = interaction_matrix
        self.item_popularity = interaction_matrix.sum(axis=0)
        self.item_quality = (interaction_matrix > 0).sum(axis=0) / len(interaction_matrix)

    def recommend_for_new_user(self, n_recommendations=5):
        """Recommend popular items for new user"""
        scores = self.item_popularity + self.item_quality * 100
        top_items = np.argsort(scores)[-n_recommendations:][::-1]
        return list(top_items)

    def recommend_for_new_item(self, n_recommendations=5):
        """Recommend new item to users who liked similar items"""
        # Return users most likely to rate new item
        user_activity = (self.interaction_matrix > 0).sum(axis=1)
        active_users = np.argsort(user_activity)[-n_recommendations:][::-1]
        return list(active_users)

cold_start = ColdStartHandler(interaction_matrix)
print("Popular items for new user:", cold_start.recommend_for_new_user(5))

# 8. Visualization
print("\n=== Visualization ===")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# User similarity heatmap
axes[0, 0].imshow(user_similarity[:10, :10], cmap='YlOrRd', aspect='auto')
axes[0, 0].set_title('User Similarity Matrix (First 10 Users)')
axes[0, 0].set_xlabel('User ID')
axes[0, 0].set_ylabel('User ID')
plt.colorbar(axes[0, 0].images[0], ax=axes[0, 0])

# Item similarity heatmap
axes[0, 1].imshow(item_similarity[:10, :10], cmap='YlOrRd', aspect='auto')
axes[0, 1].set_title('Item Similarity Matrix (First 10 Items)')
axes[0, 1].set_xlabel('Item ID')
axes[0, 1].set_ylabel('Item ID')
plt.colorbar(axes[0, 1].images[0], ax=axes[0, 1])

# Interaction matrix
axes[1, 0].imshow(interaction_matrix[:15, :15], cmap='Blues', aspect='auto')
axes[1, 0].set_title('User-Item Interaction Matrix (First 15x15)')
axes[1, 0].set_xlabel('Item ID')
axes[1, 0].set_ylabel('User ID')
plt.colorbar(axes[1, 0].images[0], ax=axes[1, 0])

# Rating distribution
rating_counts = np.bincount(interaction_matrix.flatten(), minlength=6)
axes[1, 1].bar(range(6), rating_counts, color='steelblue', edgecolor='black')
axes[1, 1].set_xlabel('Rating')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Rating Distribution')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('recommendation_analysis.png', dpi=100, bbox_inches='tight')
print("\nVisualization saved as 'recommendation_analysis.png'")

# 9. Summary
print("\n=== Recommendation Summary ===")
print(f"Total Users: {n_users}")
print(f"Total Items: {n_items}")
print(f"Total Interactions: {(interaction_matrix > 0).sum()}")
print(f"Sparsity: {(interaction_matrix == 0).sum() / interaction_matrix.size:.2%}")
print(f"Avg interactions per user: {(interaction_matrix > 0).sum() / n_users:.2f}")
print(f"Avg interactions per item: {(interaction_matrix > 0).sum() / n_items:.2f}")

print("\nRecommendation engine setup completed!")
```

## Algorithm Comparison

- **User-CF**: Good for diverse preferences, but suffers from sparsity
- **Item-CF**: Better for stable preferences, works well with sparse data
- **SVD**: Captures latent factors, computationally efficient
- **Neural Networks**: Captures complex patterns, requires more data

## Common Challenges

- **Cold Start**: New users/items with no interaction history
- **Sparsity**: Sparse interaction matrices
- **Scalability**: Handling millions of users and items
- **Diversity**: Avoiding recommendation bubbles
- **Fairness**: Representing all item types fairly

## Deliverables

- Recommendation model
- Ranked item predictions
- Evaluation metrics
- A/B testing framework
- Deployment code
- Performance analysis
