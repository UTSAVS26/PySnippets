# Model Utilities for PyTorch

This repository contains utility functions to assist in the evaluation and analysis of PyTorch models. These utilities include functions for calculating inference speed, model size, common evaluation metrics, model summary, and plotting learning curves and precision-recall curves.

## Requirements

To use this notebook, you need the following Python libraries:

- `torch`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `psutil`

You can install the required libraries using the following command:

```bash
pip install torch numpy scikit-learn matplotlib seaborn psutil
```

### Features

#### 1. Calculate Inference Speed

Calculates the average inference time for a given model and input tensor.

```bash
ModelUtils.calculate_inference_speed(model, input_tensor, device='cpu', iterations=100)
```

- model: The PyTorch model to be evaluated.
- input_tensor: The input tensor for the model.
- device: The device to run the inference on ('cpu' or 'cuda').
- iterations: The number of iterations to calculate average inference time.

#### 2. Calculate Common Metrics

Calculates and prints accuracy, precision, recall, F1-score, and the confusion matrix.

```bash
ModelUtils.calculate_common_metrics(y_true, y_pred)
```

- y_true: True labels.
- y_pred: Predicted labels.

#### 3. Calculate Model Size

Calculates the memory size of a model in megabytes (MB).

```bash
ModelUtils.calculate_model_size(model)
```

- model: The PyTorch model for which size is to be calculated.

#### 4. Model Summary

Generates a summary of the model including the number of layers, total parameters, trainable parameters, and non-trainable parameters.

```bash
ModelUtils.model_summary(model)
```

- model: The PyTorch model to summarize.

#### 5. Plot Learning Curves

Plots training and validation accuracy/loss over time (epochs).

```bash
ModelUtils.plot_learning_curve(train_acc, val_acc, train_loss, val_loss)
```

- train_acc: List of training accuracies per epoch.
- val_acc: List of validation accuracies per epoch.
- train_loss: List of training losses per epoch.
- val_loss: List of validation losses per epoch.

#### 6. Plot Precision-Recall Curve

Plots the precision-recall curve, useful for imbalanced datasets.

```bash
ModelUtils.plot_precision_recall_curve(y_true, y_scores)
```

- y_true: True labels.
- y_scores: Predicted scores or probabilities.

#### Example Usage

```bash
import torch
from torch import nn
from ModelUtils import ModelUtils

# Example Model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()
input_tensor = torch.randn(1, 10)

# Inference Speed
ModelUtils.calculate_inference_speed(model, input_tensor)

# Model Size
ModelUtils.calculate_model_size(model)

# Model Summary
ModelUtils.model_summary(model)

# Plotting Learning Curves
train_acc = [0.8, 0.85, 0.9]
val_acc = [0.75, 0.8, 0.83]
train_loss = [0.6, 0.5, 0.4]
val_loss = [0.65, 0.55, 0.45]
ModelUtils.plot_learning_curve(train_acc, val_acc, train_loss, val_loss)

# Plotting Precision-Recall Curve
y_true = [0, 1, 1, 0]
y_scores = [0.1, 0.9, 0.8, 0.4]
ModelUtils.plot_precision_recall_curve(y_true, y_scores)
```
