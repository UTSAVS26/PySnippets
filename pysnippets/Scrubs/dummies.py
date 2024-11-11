import pandas as pd
from utils import time_my_func

def make_dummies(ser, DROP_ONE=True):
    """
    Create dummies for different levels of a clipped categorical
    Drop one to avoid the trap
    Parameters
    ----------
    ser: input categorical series
        pandas.Series
    Returns
    -------
    df_dum: dummy variables with one level dropped
        pandas.DataFrame
    """
    if ser.nunique() > 10:
        print("Categorical has too many levels, consider clipping")
        df_dum = None
    else:
        PREFIX = 'flag_' + ser.name + '_'
        df_dum = pd.get_dummies(ser, prefix=PREFIX)
        if DROP_ONE:
            other_col = [c for c in df_dum if 'Other' in c]
            to_drop_ = other_col if other_col else df_dum.mean().idxmin()
            print("Dropping {}".format(to_drop_))
            df_dum.drop(to_drop_, axis=1, inplace=True)
    return df_dum

@time_my_func
def create_dummified_df(df, drop_one=True):
    """
    For each (clipped) categorical column
    * Create dummmy DataFrame
    * Concat to input df
    * Drop the categorical

    Returns
    -------
        Passed df with flag_* columns replacing categoricals
    """
    df_ = df.copy()

    cols_dummies = \
    (df_
    .select_dtypes(include=object)
    .columns
    .tolist())
    print("Creating dummies for \n{}".format(cols_dummies))

    list_dummies_df = \
    [make_dummies(df_[COL], DROP_ONE=drop_one) for COL in cols_dummies]

    df_2 = \
    pd.concat([
        df_.drop(cols_dummies, axis=1),
        pd.concat(list_dummies_df, axis=1)
    ], axis=1)

    return df_2