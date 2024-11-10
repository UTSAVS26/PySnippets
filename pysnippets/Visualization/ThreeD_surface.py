import matplotlib.pyplot as plt
import numpy as np

def surface_plot(x, y, z_func, title="3D Surface Plot"):
    X, Y = np.meshgrid(x, y)
    Z = z_func(X, Y)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(title)
    plt.show()

# Test case
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
surface_plot(x, y, lambda x, y: np.sin(np.sqrt(x**2 + y**2)))
