import pandas as pd

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

def replace_missing_with_mean(df: pd.DataFrame, column: str) -> pd.DataFrame:
    mean_value = df[column].mean()
    df[column].fillna(mean_value, inplace=True)
    return df

def standardize_text(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column] = df[column].str.lower().str.strip()
    return df 