import matplotlib.pyplot as plt
import numpy as np

def filled_area_plot(x, y, title="Filled Area Plot", color="skyblue", alpha=0.3):
    plt.figure(figsize=(10, 6))
    plt.fill_between(x, y, color=color, alpha=alpha)
    plt.plot(x, y, color="blue")
    plt.title(title)
    plt.show()

# Test case
x = np.linspace(0, 10, 100)
y = np.sin(x)
filled_area_plot(x, y)
