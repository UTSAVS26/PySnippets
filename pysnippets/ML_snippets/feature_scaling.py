from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

def standardize_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes the features (mean = 0, standard deviation = 1).

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The standardized DataFrame.
    """
    scaler = StandardScaler()
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

def normalize_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizes the features to a range between 0 and 1.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The normalized DataFrame.
    """
    scaler = MinMaxScaler()
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
