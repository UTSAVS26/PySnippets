import seaborn as sns
import matplotlib.pyplot as plt

def density_plot(data, col, title="Density Plot with Shade"):
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=data, x=col, shade=True)
    plt.title(title)
    plt.show()

# Test case
data = sns.load_dataset("iris")
density_plot(data, col="sepal_length")
