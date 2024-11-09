from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

def standardize_features(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def min_max_scale_features(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df 