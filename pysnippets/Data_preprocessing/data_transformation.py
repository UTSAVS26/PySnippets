import pandas as pd
import numpy as np

def log_transform(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column] = np.log1p(df[column])
    return df

def power_transform(df: pd.DataFrame, column: str, power: float = 2.0) -> pd.DataFrame:
    df[column] = np.power(df[column], power)
    return df

def binarize(df: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
    df[column] = (df[column] > threshold).astype(int)
    return df 