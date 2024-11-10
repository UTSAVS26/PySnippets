import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def advanced_heatmap(data, cmap='coolwarm', annot=True, fmt=".2f", figsize=(10, 8), title="Heatmap"):
    plt.figure(figsize=figsize)
    sns.heatmap(data, cmap=cmap, annot=annot, fmt=fmt, linewidths=.5)
    plt.title(title)
    plt.show()

# Test case
data = np.random.rand(10, 12)
advanced_heatmap(data)
