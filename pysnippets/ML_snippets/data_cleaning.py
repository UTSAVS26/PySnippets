import pandas as pd

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows from a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame without duplicates.
    """
    return df.drop_duplicates()

def handle_missing_values(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """
    Handles missing values in a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        strategy (str): The strategy to use for handling missing values ('mean', 'median', 'drop').

    Returns:
        pd.DataFrame: The DataFrame with missing values handled.
    """
    if strategy == "mean":
        return df.fillna(df.mean())
    elif strategy == "median":
        return df.fillna(df.median())
    elif strategy == "drop":
        return df.dropna()
    else:
        raise ValueError("Invalid strategy. Choose from 'mean', 'median', or 'drop'.")
