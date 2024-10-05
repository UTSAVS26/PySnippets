import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_distribution(df: pd.DataFrame, column: str):
    """
    Plots the distribution of a specified column.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column (str): The column to plot.

    Returns:
        None
    """
    sns.histplot(df[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

def plot_correlation_matrix(df: pd.DataFrame):
    """
    Plots the correlation matrix of the DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        None
    """
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()
