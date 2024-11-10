# Advanced Data Visualization Snippets in Python

Welcome to the **Advanced Data Visualization Snippets** project! This repository contains Python code snippets for creating a wide range of advanced visualizations using `matplotlib`, `seaborn`, and other popular data visualization libraries. Each visualization function is designed to be reusable, customizable, and suitable for various data science and data analysis needs. 

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Visualization Snippets](#visualization-snippets)
    - [1. Dual-Axis Line Plot](#1-dual-axis-line-plot)
    - [2. Advanced Heatmap](#2-advanced-heatmap)
    - [3. Notched Boxplot](#3-notched-boxplot)
    - [4. Stacked Bar Chart](#4-stacked-bar-chart)
    - [5. Split Violin Plot](#5-split-violin-plot)
    - [6. Scatter Plot with Regression Line](#6-scatter-plot-with-regression-line)
    - [7. Surface Plot](#7-surface-plot)
    - [8. Density Plot](#8-density-plot)
    - [9. Circular Bar Plot](#9-circular-bar-plot)
    - [10. Clustered Heatmap](#10-clustered-heatmap)
    - [11. Filled Area Plot](#11-filled-area-plot)
    - [12. Hexbin Plot](#12-hexbin-plot)
    - [13. Radial Bar Chart](#13-radial-bar-chart)
    - [14. Pair Plot](#14-pair-plot)
    - [15. Histogram with KDE](#15-histogram-with-kde)
4. [Testing](#testing)
5. [Customization Options](#customization-options)

## Overview
This repository provides advanced data visualization techniques to help you analyze and present complex datasets. Each snippet includes configuration options, such as `figsize`, `palette`, and more, allowing for flexible customization.

## Installation
Clone the repository and make sure you have the required libraries installed. Use the following command:

```bash
git clone https://github.com/yourusername/advanced-data-visualizations.git
cd advanced-data-visualizations
pip install -r requirements.txt
```

## Visualization Snippets

### 1. Dual-Axis Line Plot
**Description**: Plots two different y-values on the same x-axis, using two y-axes on either side for better data comparison.

**Example**:
```python
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
dual_axis_line_plot(x, y1, y2)
```

### 2. Advanced Heatmap
**Description**: Visualizes data as a heatmap, allowing for extensive customization options like color palette, annotating cells, and adjusting the color range.

**Example**:
```python
data = np.random.rand(10, 12)
advanced_heatmap(data)
```

### 3. Notched Boxplot
**Description**: Displays a notched boxplot, allowing visualization of medians and the spread of the data, suitable for comparing categories.

**Example**:
```python
data = sns.load_dataset("tips")
notched_boxplot(data, x_col='day', y_col='total_bill')
```

### 4. Stacked Bar Chart
**Description**: Creates a stacked bar chart to visualize the composition of categories over a shared axis.

**Example**:
```python
categories = ['A', 'B', 'C', 'D']
values1 = [3, 6, 9, 12]
values2 = [5, 4, 2, 8]
stacked_bar_chart(categories, values1, values2)
```

### 5. Split Violin Plot
**Description**: Generates a split violin plot, which allows comparison of two distributions on the same axis.

**Example**:
```python
data = sns.load_dataset("tips")
split_violin_plot(data, x="day", y="total_bill", hue="sex")
```

### 6. Scatter Plot with Regression Line
**Description**: Plots a scatter plot with a regression line, ideal for observing trends in bivariate data.

**Example**:
```python
data = sns.load_dataset("tips")
scatter_with_regression(data, x="total_bill", y="tip")
```

### 7. Surface Plot
**Description**: Displays a 3D surface plot, useful for visualizing functions of two variables.

**Example**:
```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
surface_plot(x, y, lambda x, y: np.sin(np.sqrt(x**2 + y**2)))
```

### 8. Density Plot
**Description**: Creates a density plot to show the distribution of a continuous variable.

**Example**:
```python
data = sns.load_dataset("iris")
density_plot(data, col="sepal_length")
```

### 9. Circular Bar Plot
**Description**: Plots data in a circular bar chart format, useful for categorical data with circular representation.

**Example**:
```python
labels = ['A', 'B', 'C', 'D', 'E']
values = [4, 6, 5, 7, 3]
circular_bar_plot(labels, values)
```

### 10. Clustered Heatmap
**Description**: Generates a clustered heatmap, ideal for hierarchical data clustering and analysis.

**Example**:
```python
data = np.random.rand(10, 10)
clustered_heatmap(data)
```

### 11. Filled Area Plot
**Description**: Displays a filled area plot to show quantities over time.

**Example**:
```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
filled_area_plot(x, y)
```

### 12. Hexbin Plot
**Description**: Creates a hexbin plot, suitable for visualizing bivariate data distributions in dense regions.

**Example**:
```python
x = np.random.randn(1000)
y = np.random.randn(1000)
hexbin_plot(x, y)
```

### 13. Radial Bar Chart
**Description**: Plots data in a radial bar chart format, ideal for categorical data with radial distribution.

**Example**:
```python
labels = ['Group A', 'Group B', 'Group C']
values = [20, 35, 30]
radial_bar_chart(labels, values)
```

### 14. Pair Plot
**Description**: Generates pairwise relationships in a dataset, useful for exploratory data analysis.

**Example**:
```python
data = sns.load_dataset("iris")
pairplot(data)
```

### 15. Histogram with KDE
**Description**: Plots a histogram with Kernel Density Estimation (KDE) overlay to visualize the distribution of a single variable.

**Example**:
```python
data = sns.load_dataset("tips")
histogram_with_kde(data, col="total_bill")
```

## Testing

To ensure that each visualization works as expected, we use `unittest` to test each plotting function. These tests confirm that functions run without errors and produce the expected figures.

To run the tests:
```bash
python -m unittest test_visualizations.py
```

## Customization Options
Each function includes options for customization, such as:
- `palette`: Customize color schemes using seaborn and matplotlib palettes.
- `figsize`: Adjust the figure size for each plot to meet specific layout requirements.
- `annotate`: Optionally annotate data points or cells, especially in heatmaps and bar charts.
- `linewidth`, `linestyle`, and `alpha`: Customize line thickness, style, and transparency for finer control.

Each function in this repository provides documentation in the docstring, listing the customizable parameters and their descriptions.
