import matplotlib.pyplot as plt

def stacked_bar_chart(categories, values1, values2, title="Stacked Bar Chart", colors=("skyblue", "lightgreen")):
    plt.figure(figsize=(10, 6))
    bar_width = 0.5
    plt.bar(categories, values1, color=colors[0], label="Value 1", width=bar_width)
    plt.bar(categories, values2, bottom=values1, color=colors[1], label="Value 2", width=bar_width)
    plt.legend()
    plt.title(title)
    plt.show()

# Test case
categories = ['A', 'B', 'C', 'D']
values1 = [3, 6, 9, 12]
values2 = [5, 4, 2, 8]
stacked_bar_chart(categories, values1, values2)
