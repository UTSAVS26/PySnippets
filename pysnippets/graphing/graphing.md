# Advanced Graphing Module

## Overview

The Advanced Graphing Module is a Python library that simplifies the process of creating various types of plots and data visualizations. It builds upon popular libraries like Matplotlib, Seaborn, Plotly and scipy to provide an easy-to-use interface for both basic and advanced plotting needs.

## Features

- **Configurable Defaults**: Set global styles, figure sizes, and color palettes.
- **Multiple Plot Types**: Line plots, bar charts, scatter plots, pie charts, heatmaps, and more.
- **Subplot Support**: Easily create multiple plots in a single figure.
- **Interactive Plots**: Option to create interactive plots using Plotly.
- **Data Preprocessing**: Built-in functions for data normalization and moving averages.
- **Statistical Visualizations**: Includes Q-Q plot functionality.
- **Annotation**: Helper function to annotate specific points on plots.
- **Error Handling**: Safe plotting function with logging for easier debugging.
- **Customization**: Functions to change color palettes and apply different styles.

## Installation

1. Ensure you have Python 3.6 or later installed.
2. Install the required dependencies:

   ```
   pip install matplotlib numpy seaborn plotly scipy
   ```

3. Download `advanced_graphing.py` and place it in your project directory or Python path.

## Usage

1. Import the functions you need from the module:

   ```python
   from advanced_graphing import line_plot, bar_chart, set_config
   ```

2. (Optional) Set global configurations:

   ```python
   set_config(style='seaborn-darkgrid', figsize=(12, 8), color_palette='Set2')
   ```

3. Create your plots:

   ```python
   import numpy as np

   x = np.linspace(0, 10, 100)
   y = np.sin(x)
   line_plot(x, y, title="Sine Wave", xlabel="X", ylabel="sin(x)")
   ```

For more detailed examples, refer to the `example.py` file provided with this module.

## Example Script

An `example.py` script is included, demonstrating the usage of various functions in the module. To run it:

```
python example.py
```

This will generate multiple plots showcasing different features of the module.

## Contributing

Contributions to improve the Advanced Graphing Module are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This module is built upon the excellent work of the Matplotlib, Seaborn, and Plotly teams.
- Inspired by the need for simplified, yet powerful data visualization tools in Python.
