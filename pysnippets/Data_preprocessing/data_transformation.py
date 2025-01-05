import pandas as pd
import numpy as np

def log_transform(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Apply a logarithmic transformation (log1p) to a specified column.
    The transformation is log(1 + x) to handle zero and positive values.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name to transform.

    Returns:
    - pd.DataFrame: A new DataFrame with the transformed column.

    Raises:
    - ValueError: If the column does not exist in the DataFrame or contains non-positive values.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    # Ensure that the values are positive before applying log transformation
    if (df[column] <= 0).any():
        raise ValueError(f"Log transformation cannot be applied to non-positive values in column '{column}'.")

    df[column] = np.log1p(df[column])
    return df

def power_transform(df: pd.DataFrame, column: str, power: float = 2.0) -> pd.DataFrame:
    """
    Apply a power transformation to a specified column.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name to transform.
    - power (float): The power to raise the values to (default is 2.0).

    Returns:
    - pd.DataFrame: A new DataFrame with the transformed column.

    Raises:
    - ValueError: If the column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    df[column] = np.power(df[column], power)
    return df

def binarize(df: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
    """
    Binarize a specified column based on a threshold. Values greater than the threshold
    are set to 1, and values less than or equal to the threshold are set to 0.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name to binarize.
    - threshold (float): The threshold for binarization.

    Returns:
    - pd.DataFrame: A new DataFrame with the binarized column.

    Raises:
    - ValueError: If the column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    df[column] = (df[column] > threshold).astype(int)
    return df
