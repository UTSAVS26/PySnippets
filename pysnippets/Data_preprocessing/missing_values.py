import pandas as pd
from sklearn.impute import SimpleImputer

def impute_numeric_with_mean(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    imputer = SimpleImputer(strategy='mean')
    df[columns] = imputer.fit_transform(df[columns])
    return df

def impute_categorical_with_mode(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    imputer = SimpleImputer(strategy='most_frequent')
    df[columns] = imputer.fit_transform(df[columns])
    return df

def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    return df.dropna(thresh=int(df.shape[1] * threshold)) 