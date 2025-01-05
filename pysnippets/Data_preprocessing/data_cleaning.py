import pandas as pd

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the DataFrame.
    
    Args:
    - df (pd.DataFrame): The input DataFrame.
    
    Returns:
    - pd.DataFrame: A new DataFrame with duplicates removed.
    """
    if df.empty:
        print("Warning: The DataFrame is empty.")
    return df.drop_duplicates()

def replace_missing_with_mean(df: pd.DataFrame, column: str, default_value: float = None) -> pd.DataFrame:
    """
    Replace missing values in a specified column with the column's mean or a provided default value.
    
    Args:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name where missing values need to be replaced.
    - default_value (float, optional): If provided, will replace missing values with this value.
    
    Returns:
    - pd.DataFrame: A new DataFrame with missing values replaced.
    
    Raises:
    - ValueError: If the column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    if default_value is not None:
        df[column].fillna(default_value, inplace=True)
    else:
        mean_value = df[column].mean()
        df[column].fillna(mean_value, inplace=True)
    
    return df

def standardize_text(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Standardize the text in a specified column by converting it to lowercase and stripping whitespace.
    
    Args:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column to standardize.
    
    Returns:
    - pd.DataFrame: A new DataFrame with standardized text in the specified column.
    
    Raises:
    - ValueError: If the column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    df[column] = df[column].str.lower().str.strip()
    return df
