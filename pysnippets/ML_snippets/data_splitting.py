from sklearn.model_selection import train_test_split
import pandas as pd

def split_data(df: pd.DataFrame, target: str, test_size: float = 0.2):
    """
    Splits the data into training and testing sets.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        target (str): The target column for prediction.
        test_size (float): The proportion of the dataset to include in the test split.

    Returns:
        tuple: Training and testing data and target variables.
    """
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test
