import seaborn as sns
import matplotlib.pyplot as plt

def split_violin_plot(data, x, y, hue, split=True, title="Split Violin Plot", palette="Set2"):
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=data, x=x, y=y, hue=hue, split=split, palette=palette)
    plt.title(title)
    plt.show()

# Test case
data = sns.load_dataset("tips")
split_violin_plot(data, x="day", y="total_bill", hue="sex")
