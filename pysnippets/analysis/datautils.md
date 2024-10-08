## Data Analysis Module

### Overview

This Python module is designed to perform various data analysis tasks on datasets. It provides utility functions for loading data, performing basic statistical analysis, handling missing data, detecting outliers, splitting datasets, and visualizing distributions and correlations. This module is helpful for preparing data for machine learning models and conducting exploratory data analysis (EDA).

### Key Features

- **Data Loading and Preview:** Loads a CSV file and displays the first few rows for quick initial exploration.
- **Basic Statistics:** Calculates and presents basic statistics (mean, median, standard deviation, etc.) for numerical features.
- **Missing Data Analysis:** Identifies missing values, displays the percentage of missingness per feature, and visualizes it with a bar chart.
- **Data Distribution Analysis:** Plots the distribution of a specific feature using a histogram with a kernel density estimation for better visualization.
- **Correlation Analysis:** Computes and visualizes the correlation matrix using Pearson's or other correlation methods, revealing potential relationships between features.
- **Outlier Detection:** Identifies outliers using the Z-score method based on a specified threshold.
- **Train-Test Split:** Splits the dataset into training and testing sets for model development and evaluation purposes.
- **Label Encoding:** Encodes categorical features into numerical labels for machine learning algorithms.
- **Feature Scaling:** Applies StandardScaler for normalization of features, improving model performance.
- **Categorical Feature Visualization:** Creates a count plot to explore the distribution of values within a categorical feature.
- **Correlation with Target:** Calculates and visualizes the correlation between each feature and the target variable, providing insights into feature importance.

### Usage

This notebook can be used independently by importing the `DataUtils` class into your project or within a larger pipeline for data exploration and preparation tasks. Here's an example of how to load data and perform basic analysis:

```python
import pandas as pd
from eda_functions import DataUtils  # Assuming the class is defined in a separate file

# Load your data
data = pd.read_csv("your_data.csv")

# Preview the first few rows
DataUtils.load_and_preview_data(data, rows=10)  # Increase rows to see more data

# Get basic statistics
DataUtils.basic_statistics(data.select_dtypes(include=[np.number]))  # Analyze numerical features

# Analyze missing data
missing_info = DataUtils.missing_data_analysis(data)

# Explore the distribution of a specific feature
DataUtils.data_distribution_analysis(data, "feature_name")

# Scale features using StandardScaler
X_train_scaled, X_test_scaled = DataUtils.feature_scaling(X_train, X_test)

# Compute and visualize the correlation matrix using Pearson correlation
correlation_matrix = DataUtils.correlation_analysis(data, method='pearson')

# Calculate and visualize correlation of features with the target variable
correlation_with_target = DataUtils.correlation_with_target(data, target_column='target')

# Plot the distribution of a categorical feature
DataUtils.plot_categorical_feature(data, feature='categorical_column')

# Scale features using StandardScaler
X_train_scaled, X_test_scaled = DataUtils.feature_scaling(X_train, X_test)

# Apply label encoding to categorical columns
data_encoded = DataUtils.label_encoding(data, columns=['category_column1', 'category_column2'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = DataUtils.train_test_split_data(data, target_column='target', test_size=0.2)

# Detect outliers in the dataset using the Z-score method
outliers = DataUtils.detect_outliers_z_score(data, threshold=3)
```

For example of how to use this module , please refer example_usage.py
