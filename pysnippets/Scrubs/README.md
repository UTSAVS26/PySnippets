# Scrubs Directory - Python Code Snippets

This directory contains a collection of Python scripts and modules designed to preprocess, clean, and transform data for further analysis or machine learning tasks. Below is a detailed description of each file and its purpose.

## Files and Descriptions

### `backup.py`
- **Purpose**: Handles the saving of cleaned dataframes to disk.
- **Key Functions**:
  - `backup_df(df, path_clean)`: Saves a DataFrame to a CSV file after performing operations like fixing dates, imputing categoricals, and compressing numeric columns.

### `clean.py`
- **Purpose**: Provides functions to clean and preprocess dataframes by removing unwanted columns and rows based on various criteria.
- **Key Functions**:
  - `drop_unnamed(df)`: Removes columns that are unnamed.
  - `drop_zv(df)`: Drops columns with zero variance.
  - `drop_nzv(df, nzv_threshold)`: Drops near-zero variance categorical columns.
  - `drop_missings(df, NA_threshold)`: Drops columns with missing values exceeding a specified threshold.
  - `remove_zv_missings(df, NA_threshold, nzv_threshold)`: Combines the functionalities of dropping columns based on missing values and near-zero variance.

### `clip.py`
- **Purpose**: Manages categorical variables by reducing the number of levels in categorical features.
- **Key Functions**:
  - `clip_categorical(ser, MIN_LEVELS, MIN_FREQ, COVERAGE)`: Clips categorical variables to reduce their levels based on frequency and coverage thresholds.

### `compress.py`
- **Purpose**: Compresses numeric data types and encodes categorical variables.
- **Key Functions**:
  - `compress_numeric(COL)`: Downcasts numeric columns to the smallest appropriate data type.
  - `compress_categorical(COL)`: Encodes categorical variables with more than two classes and persists the encoder.

### `dummies.py`
- **Purpose**: Handles the creation of dummy variables for categorical data.
- **Key Functions**:
  - `make_dummies(ser, DROP_ONE)`: Creates dummy variables for a categorical series.
  - `create_dummified_df(df, drop_one)`: Applies `make_dummies` to each categorical column in a DataFrame.

### `pipeline.py`
- **Purpose**: Orchestrates the entire data cleaning and preprocessing pipeline.
- **Key Functions**:
  - `engineer_features(df)`: Performs feature engineering on the DataFrame.
  - `aggregate_df(df, df_y, cols_flags)`: Aggregates data based on specified flags and other criteria.
  - `get_aggregated_df(df, aggfunc)`: Applies an aggregation function to the DataFrame grouped by a key.

### `utils.py`
- **Purpose**: Provides utility functions.
- **Key Functions**:
  - `time_my_func(my_func)`: Decorator that measures the execution time of functions.

### `__init__.py`
- **Purpose**: Marks the directory as a Python package module, allowing its contents to be imported elsewhere in Python projects.

## Usage

To use these scripts, ensure that your data meets the expected formats and types as required by each function. Most functions expect a pandas DataFrame as input. You can import these modules into your Python scripts or Jupyter notebooks and use them to preprocess and clean your data effectively.

### Example Usage