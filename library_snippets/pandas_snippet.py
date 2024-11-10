import pandas as pd
from pandas import DataFrame
from typing import Any

def read(file_path: str) -> DataFrame:
    return pd.read_csv(file_path)

def filter(df: DataFrame, column_name: str, value: Any) -> DataFrame:
    return df[df[column_name] == value]

def group(df: DataFrame, column_name: str) -> DataFrame:
    return df.groupby(column_name).mean()

def save(df: DataFrame, file_path: str):
    df.to_csv(file_path, index=False)

def filter_condition(df: DataFrame, condition: Any) -> DataFrame:
    return df[condition]

def filter_multiple_conditions(df: DataFrame, conditions: Any) -> DataFrame:
    return df[conditions]

def filter_column_value(df: DataFrame, column_name: str, value: Any) -> DataFrame:
    return df[df[column_name] == value]

def filter_column_values(df: DataFrame, column_name: str, values: Any) -> DataFrame:
    return df[df[column_name].isin(values)] 

def filter_column_not_value(df: DataFrame, column_name: str, value: Any) -> DataFrame:
    return df[df[column_name] != value]

def filter_column_not_values(df: DataFrame, column_name: str, values: Any) -> DataFrame:
    return df[~df[column_name].isin(values)]

def filter_column_between_values(df: DataFrame, column_name: str, min_value: Any, max_value: Any) -> DataFrame:
    return df[(df[column_name] >= min_value) & (df[column_name] <= max_value)]

def filter_column_outside_values(df: DataFrame, column_name: str, min_value: Any, max_value: Any) -> DataFrame:
    return df[(df[column_name] < min_value) | (df[column_name] > max_value)]

def filter_column_not_between_values(df: DataFrame, column_name: str, min_value: Any, max_value: Any) -> DataFrame:
    return df[(df[column_name] < min_value) | (df[column_name] > max_value)]

def filter_column_contains_string(df: DataFrame, column_name: str, string: str) -> DataFrame:
    return df[df[column_name].str.contains(string)]

def filter_column_not_contains_string(df: DataFrame, column_name: str, string: str) -> DataFrame:
    return df[~df[column_name].str.contains(string)]

def filter_column_startswith(df: DataFrame, column_name: str, string: str) -> DataFrame:
    return df[df[column_name].str.startswith(string)]

def filter_column_not_startswith(df: DataFrame, column_name: str, string: str) -> DataFrame:
    return df[~df[column_name].str.startswith(string)]
