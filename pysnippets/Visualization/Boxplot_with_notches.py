import seaborn as sns
import matplotlib.pyplot as plt

def notched_boxplot(data, x_col, y_col, palette='muted', notch=True, title="Notched Box Plot"):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x=x_col, y=y_col, palette=palette, notch=notch)
    plt.title(title)
    plt.show()

# Test case
data = sns.load_dataset("tips")
notched_boxplot(data, x_col='day', y_col='total_bill')


