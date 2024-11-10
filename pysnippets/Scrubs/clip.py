def clip_categorical(ser, MIN_LEVELS=5, MIN_FREQ=0.05, COVERAGE=0.95):
    """
    Manage Categoricals with too many levels
    If the categorical has only 2 levels, it will be returned as-is
    Parameters
    ----------
    SR: pandas.Series
        the input Categorical series with >= MIN_LEVELS
    MIN_FREQ: float
        Levels with at least MIN_FREQ %cases will survive
    COVERAGE: float
        Levels that make up COVERAGE% of the data will survive
    Returns
    -------
    A pandas.Series object with
    retained labels for levels that account for COVERAGE% of the data
    replaced labels (with 'Other') for rare levels
    """
    sr = ser.copy()
    if sr.nunique() >= MIN_LEVELS:
        KEEP_1 = \
        (sr
         .value_counts(normalize=True)
         .where(lambda i: i >= MIN_FREQ)
         .dropna()
         .index
         .tolist()
        )

        KEEP_2 = \
        (sr
         .value_counts(normalize=True)
         .cumsum()
         .where(lambda x: x <= COVERAGE)
         .dropna()
         .index
         .tolist()
        )

        KEEP = set(KEEP_1).union(set(KEEP_2))

        sr[-sr.isin(KEEP)] = 'Other'
        sr = sr.map(lambda x: '_'.join(str(x).split()))
        print("{} now has {} Levels and {} % Coverage".format(sr.name, sr.nunique(), 100 * COVERAGE))
    else:
        print("{} doesn't have more than {} levels. Returning as-is.".format(sr.name, MIN_LEVELS))
    return sr