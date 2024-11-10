import pandas as pd
import json
from sklearn.preprocessing import LabelEncoder
from .clip import clip_categorical

def compress_numeric(COL):
    """
    If the passed COL is numeric,
    downcast it to the lowest size.
    Else,
    Return as-is.
    Parameters
    -----------
    COL: pandas.Series
        The Series to shrink
    Returns
    -------
    if numeric, a compressed series
    """
    if 'float' in str(COL.dtype):
        print("Downcasting {} to float".format(COL.name))
        result = pd.to_numeric(COL, downcast='float', errors='ignore')
    elif 'int' in str(COL.dtype):
        print("Downcasting {} to int".format(COL.name))
        result = pd.to_numeric(COL, downcast='integer', errors='ignore')
    else:
        print("{} is not numeric. Returning as-is".format(COL.name))
        result = COL
    return result

def compress_categorical(COL):
    """
    Encode categorical variables with >2 classes
    Persist the encoder as JSON
    """
    if COL.nunique() > 8:
        print("{} has too many levels, clipping it.")
        COL_clipped = clip_categorical(COL, MIN_LEVELS=8)
    else:
        COL_clipped = COL.copy()

    le = LabelEncoder()
    lookup = pd.Series(le.classes_).to_dict()
    COL_encoded = pd.Series(le.transform(COL_clipped), index=COL.index, name=COL.name)

    path_persist = "data/interim/{}_lookup.json".format(COL.name)
    print("Persisting encoder at {}".format(path_persist))
    with open(path_persist, 'w') as fp:
        json.dump(lookup, fp)
    return COL_encoded