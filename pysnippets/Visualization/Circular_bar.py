import matplotlib.pyplot as plt
import numpy as np

def circular_bar_plot(labels, values, title="Circular Bar Plot", color="skyblue"):
    N = len(labels)
    theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
    values = np.concatenate((values,[values[0]]))  # Closing the circle
    theta = np.concatenate((theta,[theta[0]]))

    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)
    ax.fill(theta, values, color=color, alpha=0.3)
    ax.plot(theta, values, color=color)
    plt.title(title)
    plt.show()

# Test case
labels = ['A', 'B', 'C', 'D', 'E']
values = [4, 6, 5, 7, 3]
circular_bar_plot(labels, values)
