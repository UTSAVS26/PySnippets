import seaborn as sns
import matplotlib.pyplot as plt

def scatter_with_regression(data, x, y, title="Scatter Plot with Regression Line"):
    plt.figure(figsize=(10, 6))
    sns.regplot(data=data, x=x, y=y, scatter_kws={"s": 50, "color": "blue"}, line_kws={"color": "red"})
    plt.title(title)
    plt.show()

# Test case
data = sns.load_dataset("tips")
scatter_with_regression(data, x="total_bill", y="tip")
