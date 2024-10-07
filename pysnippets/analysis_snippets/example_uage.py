import pandas as pd
import  DataUtils  # Assuming the class is defined in eda_functions.py
import numpy as np


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

# Detect outliers using Z-score
outliers = DataUtils.detect_outliers_z_score(data, threshold=3)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = DataUtils.train_test_split_data(data, "target_column")

# Apply label encoding to categorical columns
data_encoded = DataUtils.label_encoding(data, ["categorical_column1", "categorical_column2"])

# Scale features using StandardScaler
X_train_scaled, X_test_scaled = DataUtils.feature_scaling(X_train, X_test)

# Plot a count plot for a categorical feature
DataUtils.plot_categorical_feature(data, "categorical_column")

# Calculate and visualize correlation with the target variable
correlation = DataUtils.correlation_with_target(data, "target_column")