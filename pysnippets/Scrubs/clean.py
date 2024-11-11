import numpy as np

from utils import time_my_func

def drop_unnamed(df):
    """
    """
    cols_unnamed = [x for x in df.columns if x.lower().startswith('unnamed')]

    if len(cols_unnamed) >= 1:
        df.drop(cols_unnamed, axis=1, inplace=True)
    else:
        pass
    return df

def drop_zv(df_):
    """
    Drop columns that have zero-variance
    For Categoricals, if nunique == 1
    For Numeric, if std == 0
    """
    cols_catg_zv = \
    (df_
     .select_dtypes(include='object')
     .nunique()
     .where(lambda i: i == 1)
     .dropna()
     .index
     .tolist()
    )

    cols_numeric_zv = \
    (df_
     .select_dtypes(include=np.number)
     .std()
     .where(lambda i: i == 0)
     .dropna()
     .index
     .tolist()
    )

    cols_zv = cols_catg_zv + cols_numeric_zv

    if len(cols_zv) >= 1:
        print("The following columns have zero-variance and will be dropped \n{}".format(cols_zv))
        df_.drop(cols_zv, axis=1, inplace=True)
    else:
        print("No columns with zero-variance.")
    return df_

def drop_nzv(df_, nzv_threshold=0.95):
    """
    Drop categorical columns that have near-zero variance
    Such variables have very little predictive power
    i.e., if frequency of mode > threshold
    """
    cols_catg_nzv = \
    (df_
     .select_dtypes(include='object')
     .apply(lambda c: c.value_counts(normalize=True).agg(['max', 'idxmax']))
     .T
     .query("max > {}".format(nzv_threshold))
     .index
     .tolist()
    )

    if len(cols_catg_nzv) >= 1:
        print("The mode of these columns has a frequency higher than {}. Dropping these. \n{}"
              .format(nzv_threshold, cols_catg_nzv))
        df_.drop(cols_catg_nzv, axis=1, inplace=True)
    else:
        print("No categorical columns with near-zero variance found.")
    return df_

def drop_missings(df_, NA_threshold=0.8):
    """
    Drop columns that have more missings than threshold
    """
    cols_missings = \
    (df_
     .isnull()
     .mean()
     .where(lambda i: i > NA_threshold)
     .dropna()
     .index
     .tolist()
    )

    if len(cols_missings) >= 1:
        print("The following columns have more than {:.2f}% missings and will be dropped...\n{}"
              .format(NA_threshold * 100, cols_missings))
        df_.drop(cols_missings, inplace=True, axis=1)
    else:
        print("No columns have more than {:.2f}% missings.".format(NA_threshold))
    return df_

@time_my_func
def remove_zv_missings(df, NA_threshold=0.85, nzv_threshold=0.95):
    """
    Clean passed dataset by removing columns with
    * gt NA_threshold percentage of missing values
    * gt nzv_threshold frequency of the mode
    * zero variance

    Parameters
    ---------
    df: DataFrame
        The input dataset

    NA_threshold: float
        Acceptable limit for missings

    nzv_threshold: float
        Acceptable limit for frequency of mode

    Returns
    -------
        Cleaned DataFrame
    """
    df_ = \
    (df
     .copy()
     .pipe(drop_unnamed)
     .pipe(drop_missings, NA_threshold=NA_threshold)
     .pipe(drop_zv)
     .pipe(drop_nzv, nzv_threshold=nzv_threshold)
    )
    return df_