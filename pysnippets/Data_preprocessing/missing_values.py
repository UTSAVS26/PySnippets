import pandas as pd
from sklearn.impute import SimpleImputer

def impute_numeric_with_mean(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Impute missing numeric values in specified columns with the mean value of each column.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - columns (list): List of column names to impute.

    Returns:
    - pd.DataFrame: A new DataFrame with missing numeric values imputed with the mean.

    Raises:
    - ValueError: If any of the columns do not exist in the DataFrame.
    """
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Columns {missing_cols} do not exist in the DataFrame.")
    
    imputer = SimpleImputer(strategy='mean')
    df[columns] = imputer.fit_transform(df[columns])
    return df

def impute_categorical_with_mode(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Impute missing categorical values in specified columns with the most frequent value (mode).

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - columns (list): List of column names to impute.

    Returns:
    - pd.DataFrame: A new DataFrame with missing categorical values imputed with the mode.

    Raises:
    - ValueError: If any of the columns do not exist in the DataFrame.
    """
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Columns {missing_cols} do not exist in the DataFrame.")
    
    imputer = SimpleImputer(strategy='most_frequent')
    df[columns] = imputer.fit_transform(df[columns])
    return df

def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Drop rows with missing values if the number of missing values exceeds a given threshold.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - threshold (float): Proportion of non-null values required in a row to keep it. Default is 0.5.

    Returns:
    - pd.DataFrame: A new DataFrame with rows dropped based on the missing value threshold.
    """
    # Drop rows where the number of non-null values is less than the threshold
    return df.dropna(thresh=int(df.shape[1] * threshold))
