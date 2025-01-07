import pandas as pd
import numpy as np

def remove_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Remove outliers from a specified column using the Interquartile Range (IQR) method.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name to remove outliers from.

    Returns:
    - pd.DataFrame: A new DataFrame with outliers removed based on the IQR method.
    
    Raises:
    - ValueError: If the column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Remove rows where the column's value is outside the IQR bounds
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def remove_outliers_zscore(df: pd.DataFrame, column: str, threshold: float = 3.0) -> pd.DataFrame:
    """
    Remove outliers from a specified column using the Z-Score method.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name to remove outliers from.
    - threshold (float): The Z-score threshold to identify outliers (default is 3.0).

    Returns:
    - pd.DataFrame: A new DataFrame with outliers removed based on the Z-Score method.
    
    Raises:
    - ValueError: If the column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    mean = df[column].mean()
    std = df[column].std()
    z_scores = (df[column] - mean) / std
    
    # Remove rows where the absolute Z-Score exceeds the threshold
    return df[np.abs(z_scores) <= threshold]
