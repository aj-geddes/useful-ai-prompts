---
name: Neural Network Design
description: Design and architect neural networks with various architectures including CNNs, RNNs, Transformers, and attention mechanisms using PyTorch and TensorFlow
---

# Neural Network Design

## Overview

This skill covers designing and implementing neural network architectures including CNNs, RNNs, Transformers, and ResNets using PyTorch and TensorFlow, with focus on architecture selection, layer composition, and optimization techniques.

## When to Use

- Designing custom neural network architectures for computer vision tasks like image classification or object detection
- Building sequence models for time series forecasting, natural language processing, or video analysis
- Implementing transformer-based models for language understanding or generation tasks
- Creating hybrid architectures that combine CNNs, RNNs, and attention mechanisms
- Optimizing network depth, width, and skip connections for better training and performance
- Selecting appropriate activation functions, normalization layers, and regularization techniques

## Core Architecture Types

- **Feedforward Networks (MLPs)**: Fully connected layers
- **Convolutional Networks (CNNs)**: Image processing
- **Recurrent Networks (RNNs, LSTMs, GRUs)**: Sequence processing
- **Transformers**: Self-attention based architecture
- **Hybrid Models**: Combining multiple architecture types

## Network Design Principles

- **Depth vs Width**: Trade-offs between layers and units
- **Skip Connections**: Residual networks for deeper training
- **Normalization**: Batch norm, layer norm for stability
- **Regularization**: Dropout, L1/L2 preventing overfitting
- **Activation Functions**: ReLU, GELU, Swish for non-linearity

## PyTorch and TensorFlow Implementation

```python
import torch
import torch.nn as nn
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 1. Feedforward Neural Network (MLP)
print("=== 1. Feedforward Neural Network ===")

class MLPPyTorch(nn.Module):
    def __init__(self, input_size, hidden_sizes, output_size):
        super().__init__()
        layers = []
        prev_size = input_size

        for hidden_size in hidden_sizes:
            layers.append(nn.Linear(prev_size, hidden_size))
            layers.append(nn.BatchNorm1d(hidden_size))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(0.3))
            prev_size = hidden_size

        layers.append(nn.Linear(prev_size, output_size))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)

mlp = MLPPyTorch(input_size=784, hidden_sizes=[512, 256, 128], output_size=10)
print(f"MLP Parameters: {sum(p.numel() for p in mlp.parameters()):,}")

# 2. Convolutional Neural Network (CNN)
print("\n=== 2. Convolutional Neural Network ===")

class CNNPyTorch(nn.Module):
    def __init__(self):
        super().__init__()
        # Conv blocks
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.pool1 = nn.MaxPool2d(2, 2)

        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        self.pool2 = nn.MaxPool2d(2, 2)

        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(128)
        self.pool3 = nn.MaxPool2d(2, 2)

        # Fully connected layers
        self.fc1 = nn.Linear(128 * 4 * 4, 256)
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(256, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.pool1(x)
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.pool2(x)
        x = self.relu(self.bn3(self.conv3(x)))
        x = self.pool3(x)
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

cnn = CNNPyTorch()
print(f"CNN Parameters: {sum(p.numel() for p in cnn.parameters()):,}")

# 3. Recurrent Neural Network (LSTM)
print("\n=== 3. LSTM Network ===")

class LSTMPyTorch(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers,
                           batch_first=True, dropout=0.3)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        lstm_out, (h_n, c_n) = self.lstm(x)
        last_hidden = h_n[-1]
        output = self.fc(last_hidden)
        return output

lstm = LSTMPyTorch(input_size=100, hidden_size=128, num_layers=2, output_size=10)
print(f"LSTM Parameters: {sum(p.numel() for p in lstm.parameters()):,}")

# 4. Transformer Block
print("\n=== 4. Transformer Architecture ===")

class TransformerBlock(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.attention = nn.MultiheadAttention(d_model, num_heads, dropout=dropout)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)

        self.feedforward = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model),
            nn.Dropout(dropout)
        )

    def forward(self, x):
        # Self-attention
        attn_out, _ = self.attention(x, x, x)
        x = self.norm1(x + attn_out)

        # Feedforward
        ff_out = self.feedforward(x)
        x = self.norm2(x + ff_out)
        return x

class TransformerPyTorch(nn.Module):
    def __init__(self, vocab_size, d_model, num_heads, num_layers, d_ff):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.transformer_blocks = nn.ModuleList([
            TransformerBlock(d_model, num_heads, d_ff)
            for _ in range(num_layers)
        ])
        self.fc = nn.Linear(d_model, 10)

    def forward(self, x):
        x = self.embedding(x)
        for block in self.transformer_blocks:
            x = block(x)
        x = x.mean(dim=1)  # Global average pooling
        x = self.fc(x)
        return x

transformer = TransformerPyTorch(vocab_size=1000, d_model=256, num_heads=8,
                                 num_layers=3, d_ff=512)
print(f"Transformer Parameters: {sum(p.numel() for p in transformer.parameters()):,}")

# 5. Residual Network (ResNet)
print("\n=== 5. Residual Network ===")

class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, 3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU()

        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, 1, stride=stride),
                nn.BatchNorm2d(out_channels)
            )

    def forward(self, x):
        residual = self.shortcut(x)
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += residual
        out = self.relu(out)
        return out

class ResNetPyTorch(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, 7, stride=2, padding=3)
        self.bn1 = nn.BatchNorm2d(64)
        self.maxpool = nn.MaxPool2d(3, stride=2, padding=1)

        self.layer1 = self._make_layer(64, 64, 3, stride=1)
        self.layer2 = self._make_layer(64, 128, 4, stride=2)
        self.layer3 = self._make_layer(128, 256, 6, stride=2)
        self.layer4 = self._make_layer(256, 512, 3, stride=2)

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(512, 10)

    def _make_layer(self, in_channels, out_channels, blocks, stride):
        layers = [ResidualBlock(in_channels, out_channels, stride)]
        for _ in range(1, blocks):
            layers.append(ResidualBlock(out_channels, out_channels))
        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.maxpool(self.bn1(self.conv1(x)))
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

resnet = ResNetPyTorch()
print(f"ResNet Parameters: {sum(p.numel() for p in resnet.parameters()):,}")

# 6. TensorFlow Keras model with custom layers
print("\n=== 6. TensorFlow Keras Model ===")

tf_model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D((2, 2)),

    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D((2, 2)),

    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.GlobalAveragePooling2D(),

    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation='softmax')
])

print(f"TensorFlow Model Parameters: {tf_model.count_params():,}")
tf_model.summary()

# 7. Model comparison
models_info = {
    'MLP': mlp,
    'CNN': cnn,
    'LSTM': lstm,
    'Transformer': transformer,
    'ResNet': resnet,
}

param_counts = {name: sum(p.numel() for p in model.parameters())
                for name, model in models_info.items()}

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Parameter counts
axes[0].barh(list(param_counts.keys()), list(param_counts.values()), color='steelblue')
axes[0].set_xlabel('Number of Parameters')
axes[0].set_title('Model Complexity Comparison')
axes[0].set_xscale('log')

# Architecture comparison table
architectures = {
    'MLP': 'Feedforward, Dense layers',
    'CNN': 'Conv layers, Pooling',
    'LSTM': 'Recurrent, Long-term memory',
    'Transformer': 'Self-attention, Parallel processing',
    'ResNet': 'Residual connections, Skip paths'
}

y_pos = np.arange(len(architectures))
axes[1].axis('off')
table_data = [[name, architectures[name]] for name in architectures.keys()]
table = axes[1].table(cellText=table_data, colLabels=['Model', 'Architecture'],
                      cellLoc='left', loc='center', bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2)

plt.tight_layout()
plt.savefig('neural_network_architectures.png', dpi=100, bbox_inches='tight')
print("\nVisualization saved as 'neural_network_architectures.png'")

print("\nNeural network design analysis complete!")
```

## Architecture Selection Guide

- **MLP**: Tabular data, simple classification
- **CNN**: Image classification, object detection
- **LSTM/GRU**: Time series, sequential data
- **Transformer**: NLP, long-range dependencies
- **ResNet**: Very deep networks, image tasks

## Key Design Considerations

- Input/output shape compatibility
- Receptive field size for CNNs
- Sequence length for RNNs
- Attention head count for Transformers
- Skip connection placement for ResNets

## Deliverables

- Network architecture definition
- Parameter count analysis
- Layer-by-layer description
- Data flow diagrams
- Performance benchmarks
- Deployment requirements
