import numpy as np
from advanced_graphing import (
    set_config, line_plot, bar_chart, scatter_plot, pie_chart, 
    subplot, heatmap, normalize_data, moving_average, 
    set_color_palette, annotate_point, qq_plot, safe_plot,
    get_available_styles
)

# Print available styles
available_styles = get_available_styles()
print("Available styles:", available_styles)

# Set global configuration
preferred_style = 'seaborn-v0_8-darkgrid' if 'seaborn-v0_8-darkgrid' in available_styles else 'ggplot'
set_config(style=preferred_style, figsize=(12, 8), color_palette='Set2')

# Generate some example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
safe_plot(line_plot, x, y, title="Sine Wave", xlabel="X", ylabel="sin(x)")

# Bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.rand(5) * 10
safe_plot(bar_chart, categories, values, title="Random Bar Chart")

# Scatter plot
x_scatter = np.random.rand(50)
y_scatter = x_scatter + np.random.normal(0, 0.1, 50)
safe_plot(scatter_plot, x_scatter, y_scatter, title="Scatter Plot with Noise")

# Pie chart
sizes = [35, 30, 20, 15]
labels = ['A', 'B', 'C', 'D']
safe_plot(pie_chart, labels, sizes, title="Sample Pie Chart")

# Heatmap
data = np.random.rand(10, 10)
safe_plot(heatmap, data, title="Random Heatmap")

# Subplots
def plot1():
    line_plot(x, np.sin(x), title="Sin(x)")

def plot2():
    line_plot(x, np.cos(x), title="Cos(x)")

safe_plot(subplot, [plot1, plot2], 1, 2, ["Sin(x)", "Cos(x)"])

# Data preprocessing
normalized_data = normalize_data(y)
safe_plot(line_plot, x, normalized_data, title="Normalized Sine Wave")

moving_avg = moving_average(y, 10)
safe_plot(line_plot, x[9:], moving_avg, title="Moving Average of Sine Wave")

# Color palette
set_color_palette("Set3")
safe_plot(scatter_plot, x, y, title="Sine Wave with New Color Palette")

# Annotation
def annotated_plot():
    line_plot(x, y, title="Annotated Sine Wave")
    annotate_point(np.pi, 0, "y = 0 at π")

safe_plot(annotated_plot)

# Statistical plot
data = np.random.normal(0, 1, 1000)
safe_plot(qq_plot, data, title="Q-Q Plot of Normal Distribution")

print("All plots have been generated and displayed.")