import pandas as pd

def read(file_path):
    return pd.read_csv(file_path)

def filter(df, column_name, value):
    return df[df[column_name] == value]

def group(df, column_name):
    return df.groupby(column_name).mean()

def save(df, file_path):
    df.to_csv(file_path, index=False)
    
def filter_condition(df, condition):
    return df[condition]

def filter_multiple_conditions(df, conditions):
    return df[conditions]

def filter_column_value(df, column_name, value):
    return df[df[column_name] == value]

def filter_column_values(df, column_name, values):
    return df[df[column_name].isin(values)] 

def filter_column_not_value(df, column_name, value):
    return df[df[column_name] != value]

def filter_column_not_values(df, column_name, values):
    return df[~df[column_name].isin(values)]

def filter_column_between_values(df, column_name, min_value, max_value):
    return df[(df[column_name] >= min_value) & (df[column_name] <= max_value)]

def filter_column_outside_values(df, column_name, min_value, max_value):
    return df[(df[column_name] < min_value) | (df[column_name] > max_value)]

def filter_column_not_between_values(df, column_name, min_value, max_value):
    return df[(df[column_name] < min_value) | (df[column_name] > max_value)]

def filter_column_contains_string(df, column_name, string):
    return df[df[column_name].str.contains(string)]

def filter_column_not_contains_string(df, column_name, string):
    return df[~df[column_name].str.contains(string)]

def filter_column_startswith(df, column_name, string):
    return df[df[column_name].str.startswith(string)]

def filter_column_not_startswith(df, column_name, string):
    return df[~df[column_name].str.startswith(string)]
