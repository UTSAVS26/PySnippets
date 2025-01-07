import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def one_hot_encode(df: pd.DataFrame, column: str, drop_first: bool = True) -> pd.DataFrame:
    """
    Perform one-hot encoding on a specified column.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name to encode.
    - drop_first (bool): Whether to drop the first category to avoid multicollinearity (default is True).

    Returns:
    - pd.DataFrame: A new DataFrame with the one-hot encoded column(s).
    
    Raises:
    - ValueError: If the column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    encoder = OneHotEncoder(sparse=False, drop='first' if drop_first else None)
    encoded = encoder.fit_transform(df[[column]])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out([column]))
    
    # Concatenate the original dataframe without the encoded column and the encoded DataFrame
    return pd.concat([df.drop(column, axis=1), encoded_df], axis=1)

def label_encode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Perform label encoding on a specified column (converting categories to integer labels).
    
    Args:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name to encode.
    
    Returns:
    - pd.DataFrame: A new DataFrame with the label encoded column.
    
    Raises:
    - ValueError: If the column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    return df