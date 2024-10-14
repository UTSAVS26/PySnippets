Here’s the complete documentation based on the provided overview and function information for the **PySnippets** package:

---

# Overview

This documentation provides a guide to using the analysis snippets available in the **PySnippets** package. These snippets cover essential operations for data analysis, including data preprocessing, feature engineering, and model evaluation. The documentation includes examples for data cleaning, outlier detection, feature scaling, and model evaluation using popular machine learning algorithms.

## Table of Contents

- [Data Utilities](#data-utilities)
  - [Data Loading and Preview](#data-loading-and-preview)
  - [Basic Statistics](#basic-statistics)
  - [Missing Data Analysis](#missing-data-analysis)
  - [Data Distribution Analysis](#data-distribution-analysis)
  - [Correlation Analysis](#correlation-analysis)
  - [Outlier Detection](#outlier-detection)
  - [Train-Test Split](#train-test-split)
  - [Label Encoding](#label-encoding)
  - [Feature Scaling](#feature-scaling)
  - [Categorical Feature Visualization](#categorical-feature-visualization)
  - [Correlation with Target](#correlation-with-target)
- [Model Utilities](#model-utilities)
  - [Calculate Inference Speed](#calculate-inference-speed)
  - [Calculate Common Metrics](#calculate-common-metrics)
  - [Calculate Model Size](#calculate-model-size)
  - [Model Summary](#model-summary)
  - [Plot Learning Curves](#plot-learning-curves)
  - [Plot Precision-Recall Curve](#plot-precision-recall-curve)

## Data Utilities

### Data Loading and Preview

Loads a CSV file and displays the first few rows for quick initial exploration.

```python
def load_and_preview_data(file_path: str, rows: int = 5) -> pd.DataFrame
```

- **Parameters:**

  - `file_path`: Path to the CSV file.
  - `rows`: Number of rows to display (default is 5).

- **Returns:**

  - A DataFrame containing the loaded data.

- **Example:**
  ```python
  data = DataUtils.load_and_preview_data('data.csv')
  ```

### Basic Statistics

Calculates and presents basic statistics (mean, median, standard deviation, etc.) for numerical features.

```python
def basic_statistics(data: pd.DataFrame) -> pd.DataFrame
```

- **Parameters:**

  - `data`: The DataFrame for which to calculate statistics.

- **Returns:**

  - A DataFrame containing summary statistics of numerical features.

- **Example:**
  ```python
  stats_summary = DataUtils.basic_statistics(data)
  ```

### Missing Data Analysis

Identifies missing values, displays the percentage of missingness per feature, and visualizes it with a bar chart.

```python
def missing_data_analysis(data: pd.DataFrame) -> pd.DataFrame
```

- **Parameters:**

  - `data`: The DataFrame to analyze for missing data.

- **Returns:**

  - A DataFrame summarizing the missing data information.

- **Example:**
  ```python
  missing_info = DataUtils.missing_data_analysis(data)
  ```

### Data Distribution Analysis

Plots the distribution of a specific feature using a histogram with a kernel density estimation for better visualization.

```python
def data_distribution_analysis(data: pd.DataFrame, feature: str)
```

- **Parameters:**

  - `data`: The DataFrame containing the feature to analyze.
  - `feature`: The name of the feature whose distribution is to be plotted.

- **Returns:**

  - None (displays a plot).

- **Example:**
  ```python
  DataUtils.data_distribution_analysis(data, 'feature_name')
  ```

### Correlation Analysis

Computes and visualizes the correlation matrix using Pearson's or other correlation methods, revealing potential relationships between features.

```python
def correlation_analysis(data: pd.DataFrame, method: str = 'pearson') -> pd.DataFrame
```

- **Parameters:**

  - `data`: The DataFrame to analyze.
  - `method`: The correlation method to use (default is 'pearson').

- **Returns:**

  - A DataFrame representing the correlation matrix.

- **Example:**
  ```python
  correlation_matrix = DataUtils.correlation_analysis(data)
  ```

### Outlier Detection

Identifies outliers using the Z-score method based on a specified threshold.

```python
def detect_outliers_z_score(data: pd.DataFrame, threshold: float = 3) -> np.ndarray
```

- **Parameters:**

  - `data`: The DataFrame to analyze for outliers.
  - `threshold`: The Z-score threshold above which a data point is considered an outlier (default is 3).

- **Returns:**

  - An array of outlier indices.

- **Example:**
  ```python
  outliers = DataUtils.detect_outliers_z_score(data)
  ```

### Train-Test Split

Splits the dataset into training and testing sets for model development and evaluation purposes.

```python
def train_test_split_data(data: pd.DataFrame, target_column: str, test_size: float = 0.2, random_state: int = 42) -> tuple
```

- **Parameters:**

  - `data`: The DataFrame to split.
  - `target_column`: The name of the target variable.
  - `test_size`: The proportion of the dataset to include in the test split (default is 0.2).
  - `random_state`: The random seed used for shuffling the data (default is 42).

- **Returns:**

  - A tuple containing training features, testing features, training labels, and testing labels.

- **Example:**
  ```python
  X_train, X_test, y_train, y_test = DataUtils.train_test_split_data(data, 'target')
  ```

### Label Encoding

Encodes categorical features into numerical labels for machine learning algorithms.

```python
def label_encoding(data: pd.DataFrame, columns: list) -> pd.DataFrame
```

- **Parameters:**

  - `data`: The DataFrame containing categorical features to encode.
  - `columns`: A list of column names to encode.

- **Returns:**

  - The DataFrame with encoded columns.

- **Example:**
  ```python
  encoded_data = DataUtils.label_encoding(data, ['categorical_col1', 'categorical_col2'])
  ```

### Feature Scaling

Applies StandardScaler for normalization of features, improving model performance.

```python
def feature_scaling(X_train: np.ndarray, X_test: np.ndarray) -> tuple
```

- **Parameters:**

  - `X_train`: The training features.
  - `X_test`: The testing features.

- **Returns:**

  - A tuple containing the scaled training and testing features.

- **Example:**
  ```python
  X_train_scaled, X_test_scaled = DataUtils.feature_scaling(X_train, X_test)
  ```

### Categorical Feature Visualization

Creates a count plot to explore the distribution of values within a categorical feature.

```python
def plot_categorical_feature(data: pd.DataFrame, feature: str)
```

- **Parameters:**

  - `data`: The DataFrame containing the categorical feature.
  - `feature`: The name of the categorical feature to visualize.

- **Returns:**

  - None (displays a plot).

- **Example:**
  ```python
  DataUtils.plot_categorical_feature(data, 'categorical_feature_name')
  ```

### Correlation with Target

Calculates and visualizes the correlation between each feature and the target variable, providing insights into feature importance.

```python
def correlation_with_target(data: pd.DataFrame, target_column: str) -> pd.Series
```

- **Parameters:**

  - `data`: The DataFrame to analyze.
  - `target_column`: The name of the target variable.

- **Returns:**

  - A Series containing the correlation of each feature with the target variable.

- **Example:**
  ```python
  target_correlation = DataUtils.correlation_with_target(data, 'target')
  ```

Here’s the completed documentation incorporating your Model Utilities for PyTorch:

---

## Model Utilities

### Requirements

To use this notebook, you need the following Python libraries:

- `torch`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `psutil`

### Calculate Inference Speed

Calculates the average inference time for a given model and input tensor.

```python
ModelUtils.calculate_inference_speed(model, input_tensor, device='cpu', iterations=100)
```

- **model**: The PyTorch model to be evaluated.
- **input_tensor**: The input tensor for the model.
- **device**: The device to run the inference on ('cpu' or 'cuda').
- **iterations**: The number of iterations to calculate average inference time.

### Calculate Common Metrics

Calculates and prints accuracy, precision, recall, F1-score, and the confusion matrix.

```python
ModelUtils.calculate_common_metrics(y_true, y_pred)
```

- **y_true**: True labels.
- **y_pred**: Predicted labels.

### Calculate Model Size

Calculates the memory size of a model in megabytes (MB).

```python
ModelUtils.calculate_model_size(model)
```

- **model**: The PyTorch model for which size is to be calculated.

### Model Summary

Generates a summary of the model including the number of layers, total parameters, trainable parameters, and non-trainable parameters.

```python
ModelUtils.model_summary(model)
```

- **model**: The PyTorch model to summarize.

### Plot Learning Curves

Plots training and validation accuracy/loss over time (epochs).

```python
ModelUtils.plot_learning_curve(train_acc, val_acc, train_loss, val_loss)
```

- **train_acc**: List of training accuracies per epoch.
- **val_acc**: List of validation accuracies per epoch.
- **train_loss**: List of training losses per epoch.
- **val_loss**: List of validation losses per epoch.

### Plot Precision-Recall Curve

Plots the precision-recall curve, useful for imbalanced datasets.

```python
ModelUtils.plot_precision_recall_curve(y_true, y_scores)
```

- **y_true**: True labels.
- **y_scores**: Predicted scores or probabilities.

---
