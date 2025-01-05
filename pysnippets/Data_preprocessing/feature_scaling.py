from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

def standardize_features(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Standardize the features (scale to zero mean and unit variance) for specified columns.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - columns (list): List of column names to standardize.

    Returns:
    - pd.DataFrame: A new DataFrame with standardized features.

    Raises:
    - ValueError: If any of the columns do not exist in the DataFrame.
    """
    # Check if columns exist in the DataFrame
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Columns {missing_cols} do not exist in the DataFrame.")
    
    # Apply StandardScaler
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def min_max_scale_features(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Apply Min-Max scaling (scale to a [0, 1] range) for specified columns.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - columns (list): List of column names to scale.

    Returns:
    - pd.DataFrame: A new DataFrame with Min-Max scaled features.

    Raises:
    - ValueError: If any of the columns do not exist in the DataFrame.
    """
    # Check if columns exist in the DataFrame
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Columns {missing_cols} do not exist in the DataFrame.")
    
    # Apply MinMaxScaler
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
