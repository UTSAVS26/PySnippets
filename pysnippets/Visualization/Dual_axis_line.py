import matplotlib.pyplot as plt
import numpy as np

def dual_axis_line_plot(x, y1, y2, color1='blue', color2='green', title="Dual Axis Line Plot"):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()  # instantiate a second y-axis

    ax1.plot(x, y1, color=color1, linewidth=2, label='y1')
    ax2.plot(x, y2, color=color2, linewidth=2, linestyle='--', label='y2')

    ax1.set_xlabel("X Axis")
    ax1.set_ylabel("Y1 Axis", color=color1)
    ax2.set_ylabel("Y2 Axis", color=color2)
    plt.title(title)
    plt.show()

# Test case
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
dual_axis_line_plot(x, y1, y2)
