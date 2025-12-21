---
name: Model Hyperparameter Tuning
description: Optimize hyperparameters using grid search, random search, Bayesian optimization, and automated ML frameworks like Optuna and Hyperopt
---

# Model Hyperparameter Tuning

## Overview

Hyperparameter tuning is the process of systematically searching for the best combination of model configuration parameters to maximize performance on validation data.

## When to Use

- When optimizing model performance beyond baseline configurations
- When comparing different parameter combinations systematically
- When fine-tuning complex models with many hyperparameters
- When seeking the best trade-off between bias, variance, and training time
- When improving model generalization on validation and test data
- When exploring parameter spaces for neural networks, tree models, or ensemble methods

## Tuning Methods

- **Grid Search**: Exhaustive search over parameter grid
- **Random Search**: Random sampling from parameter space
- **Bayesian Optimization**: Probabilistic model-based search
- **Hyperband**: Multi-fidelity optimization
- **Evolutionary Algorithms**: Genetic algorithm based search
- **Population-based Training**: Distributed parameter optimization

## Hyperparameters by Model Type

- **Tree Models**: max_depth, min_samples_split, learning_rate
- **Neural Networks**: learning_rate, batch_size, num_layers, dropout
- **SVM**: C, kernel, gamma
- **Ensemble**: n_estimators, max_features, min_samples_leaf

## Python Implementation

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import optuna
from optuna.samplers import TPESampler
import torch
import torch.nn as nn
from torch.optim import Adam
import time

# Create dataset
X, y = make_classification(n_samples=2000, n_features=50, n_informative=30,
                          n_redundant=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Dataset shapes:", X_train_scaled.shape, X_test_scaled.shape)

# 1. Grid Search
print("\n=== 1. Grid Search ===")
start = time.time()

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=0
)

grid_search.fit(X_train_scaled, y_train)
grid_time = time.time() - start

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.4f}")
print(f"Test score: {grid_search.score(X_test_scaled, y_test):.4f}")
print(f"Time taken: {grid_time:.2f}s")

# 2. Random Search
print("\n=== 2. Random Search ===")
start = time.time()

param_dist = {
    'n_estimators': np.arange(50, 300, 10),
    'max_depth': np.arange(5, 30, 1),
    'min_samples_split': np.arange(2, 20, 1),
    'min_samples_leaf': np.arange(1, 10, 1),
    'max_features': ['sqrt', 'log2']
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_dist,
    n_iter=20,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42,
    verbose=0
)

random_search.fit(X_train_scaled, y_train)
random_time = time.time() - start

print(f"Best parameters: {random_search.best_params_}")
print(f"Best CV score: {random_search.best_score_:.4f}")
print(f"Test score: {random_search.score(X_test_scaled, y_test):.4f}")
print(f"Time taken: {random_time:.2f}s")

# 3. Bayesian Optimization with Optuna
print("\n=== 3. Bayesian Optimization (Optuna) ===")

def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 300),
        'max_depth': trial.suggest_int('max_depth', 5, 30),
        'min_samples_split': trial.suggest_int('min_samples_split', 2, 20),
        'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 10),
        'max_features': trial.suggest_categorical('max_features', ['sqrt', 'log2'])
    }

    model = RandomForestClassifier(**params, random_state=42)
    scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='accuracy')
    return scores.mean()

start = time.time()
sampler = TPESampler(seed=42)
study = optuna.create_study(sampler=sampler, direction='maximize')
study.optimize(objective, n_trials=20, show_progress_bar=False)
optuna_time = time.time() - start

best_trial = study.best_trial
print(f"Best parameters: {best_trial.params}")
print(f"Best CV score: {best_trial.value:.4f}")

# Train final model with best params
best_model = RandomForestClassifier(**best_trial.params, random_state=42)
best_model.fit(X_train_scaled, y_train)
print(f"Test score: {best_model.score(X_test_scaled, y_test):.4f}")
print(f"Time taken: {optuna_time:.2f}s")

# 4. Gradient Boosting hyperparameter tuning
print("\n=== 4. Gradient Boosting Tuning ===")

gb_param_grid = {
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7, 9],
    'min_samples_split': [2, 5, 10],
    'subsample': [0.8, 0.9, 1.0]
}

gb_search = GridSearchCV(
    GradientBoostingClassifier(random_state=42),
    gb_param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=0
)

gb_search.fit(X_train_scaled, y_train)

print(f"Best parameters: {gb_search.best_params_}")
print(f"Best CV score: {gb_search.best_score_:.4f}")
print(f"Test score: {gb_search.score(X_test_scaled, y_test):.4f}")

# 5. Learning rate tuning for neural networks
print("\n=== 5. Learning Rate Tuning for Neural Networks ===")

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(50, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.3)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = torch.sigmoid(self.fc3(x))
        return x

learning_rates = [0.0001, 0.001, 0.01, 0.1]
lr_results = {}

device = torch.device('cpu')

for lr in learning_rates:
    model = SimpleNN().to(device)
    optimizer = Adam(model.parameters(), lr=lr)
    criterion = nn.BCELoss()

    X_train_tensor = torch.FloatTensor(X_train_scaled)
    y_train_tensor = torch.FloatTensor(y_train).unsqueeze(1)

    best_loss = float('inf')
    patience = 10
    patience_counter = 0

    for epoch in range(100):
        output = model(X_train_tensor)
        loss = criterion(output, y_train_tensor)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if loss.item() < best_loss:
            best_loss = loss.item()
            patience_counter = 0
        else:
            patience_counter += 1

        if patience_counter >= patience:
            break

    lr_results[lr] = best_loss
    print(f"Learning Rate {lr}: Best Loss = {best_loss:.6f}")

# 6. Comparison visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Search method comparison
methods = ['Grid Search', 'Random Search', 'Bayesian Opt']
times = [grid_time, random_time, optuna_time]
scores = [grid_search.best_score_, random_search.best_score_, study.best_value]

x = np.arange(len(methods))
axes[0, 0].bar(x, times, color='steelblue', alpha=0.7)
axes[0, 0].set_ylabel('Time (seconds)')
axes[0, 0].set_title('Tuning Method Comparison - Time')
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(methods)

axes[0, 1].bar(x, scores, color='coral', alpha=0.7)
axes[0, 1].set_ylabel('CV Accuracy')
axes[0, 1].set_title('Tuning Method Comparison - Accuracy')
axes[0, 1].set_xticks(x)
axes[0, 1].set_xticklabels(methods)
axes[0, 1].set_ylim([0.8, 1.0])

# Hyperparameter importance from Optuna
importance_dict = {}
for param_name in study.best_trial.params.keys():
    trial_values = []
    for trial in study.trials:
        if param_name in trial.params:
            trial_values.append(trial.value)
    if trial_values:
        importance_dict[param_name] = np.std(trial_values)

axes[1, 0].barh(list(importance_dict.keys()), list(importance_dict.values()),
               color='lightgreen', edgecolor='black')
axes[1, 0].set_xlabel('Importance (Std Dev)')
axes[1, 0].set_title('Hyperparameter Importance')

# Learning rate tuning for NN
axes[1, 1].plot(list(lr_results.keys()), list(lr_results.values()), marker='o',
               linewidth=2, markersize=8, color='purple')
axes[1, 1].set_xlabel('Learning Rate')
axes[1, 1].set_ylabel('Best Training Loss')
axes[1, 1].set_title('Learning Rate Impact on Neural Network')
axes[1, 1].set_xscale('log')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('hyperparameter_tuning.png', dpi=100, bbox_inches='tight')
print("\nVisualization saved as 'hyperparameter_tuning.png'")

print("\nHyperparameter tuning completed!")
```

## Tuning Strategy by Model

- **Tree Models**: Focus on depth, min_samples, max_features
- **Boosting**: Learning_rate, n_estimators, subsample
- **Neural Networks**: Learning rate, batch size, regularization
- **SVM**: C and kernel type are most important

## Best Practices

- Scale search space logarithmically for continuous parameters
- Use cross-validation for robust estimates
- Start with random search for initial exploration
- Use Bayesian optimization for final refinement
- Monitor for diminishing returns

## Deliverables

- Optimal hyperparameters found
- Performance metrics for top configurations
- Tuning efficiency analysis
- Visualization of parameter impact
- Tuning report and recommendations
