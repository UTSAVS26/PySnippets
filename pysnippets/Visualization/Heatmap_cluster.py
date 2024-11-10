import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def clustered_heatmap(data, cmap="coolwarm", title="Clustered Heatmap"):
    sns.clustermap(data, cmap=cmap, figsize=(10, 8))
    plt.title(title)
    plt.show()

# Test case
data = np.random.rand(10, 10)
clustered_heatmap(data)
