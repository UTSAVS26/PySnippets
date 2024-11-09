import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def one_hot_encode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    encoder = OneHotEncoder(sparse=False, drop='first')
    encoded = encoder.fit_transform(df[[column]])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out([column]))
    return pd.concat([df.drop(column, axis=1), encoded_df], axis=1)

def label_encode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    return df 