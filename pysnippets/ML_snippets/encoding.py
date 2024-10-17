import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def one_hot_encode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Performs one-hot encoding on a specified column.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column (str): The column to one-hot encode.

    Returns:
        pd.DataFrame: The DataFrame with one-hot encoded column.
    """
    encoder = OneHotEncoder(sparse=False)
    encoded_data = encoder.fit_transform(df[[column]])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out([column]))
    return pd.concat([df.drop(columns=[column]), encoded_df], axis=1)

def label_encode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Performs label encoding on a specified column.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column (str): The column to label encode.

    Returns:
        pd.DataFrame: The DataFrame with label encoded column.
    """
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    return df
