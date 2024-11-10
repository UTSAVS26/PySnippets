import pandas as pd

from compress import compress_numeric
from utils import time_my_func

@time_my_func
def backup_df(df, path_clean):
    """
    Writes a dataframe to disk after
     cleaning dates
     imputing categoricals
     compressing numerics
    """
    print("Fixing dates...")
    date_cols = df.columns.map(lambda i: i if 'date' in i else None).dropna().tolist()
    if len(date_cols) >= 1:
        for COL in date_cols:
            df.loc[:, COL] = pd.to_datetime(df[COL])

    print("Fixing categoricals...")
    # categoricals
    catg_cols = df.select_dtypes(include=object).columns.tolist()
    if len(catg_cols) >= 1:
        for COL in catg_cols:
            df.loc[:, COL] = df[COL].fillna('_missing_')

    print("Fixing numerics...")
    df = df.apply(compress_numeric)

    print("Saving cleaned file to {}".format(path_clean))
    df.to_csv(path_clean)
    return None