import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import unittest
import logging
import matplotlib.pyplot as plt
import numpy as np
from pysnippets.graphing_snippets.advanced_graphing import (
    set_config,
    apply_config,
    reset_config,
    get_available_styles,
    line_plot,
    bar_chart,
    scatter_plot,
    pie_chart,
    heatmap,
    qq_plot,
    config,  # Import config here
)

# Ensure logging captures the error messages for testing
# logging.basicConfig(level=logging.ERROR)

class TestAdvancedGraphing(unittest.TestCase):

    def setUp(self):
        # Reset the config for each test
        config['default_style'] = 'default'
        config['default_figsize'] = (10, 6)
        config['default_color_palette'] = 'default'

    def test_set_config(self):
        set_config(style='ggplot', figsize=(12, 8), color_palette='plasma')
        self.assertEqual(config['default_style'], 'ggplot')

    def test_get_available_styles(self):
        styles = get_available_styles()
        self.assertIn('ggplot', styles)  # Check if 'ggplot' is in available styles
        # Adjust this to a style that exists in your matplotlib version
        self.assertIn('seaborn-v0_8', styles)

    def test_line_plot(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        line_plot(x, y, title="Sine Wave", xlabel="Time", ylabel="Amplitude")

    def test_bar_chart(self):
        categories = ['A', 'B', 'C']
        values = [3, 7, 5]
        bar_chart(categories, values, title="Category Values", xlabel="Categories", ylabel="Values")

    def test_scatter_plot(self):
        x = np.random.rand(100)
        y = np.random.rand(100)
        scatter_plot(x, y, title="Random Scatter Plot", xlabel="X-axis", ylabel="Y-axis")

    def test_pie_chart(self):
        labels = ['A', 'B', 'C']
        sizes = [15, 30, 45]
        pie_chart(labels, sizes, title="Pie Chart Example")

    def test_heatmap(self):
        data = np.random.rand(10, 10)
        heatmap(data, title="Random Heatmap")

    def test_qq_plot(self):
        data = np.random.normal(loc=0, scale=1, size=100)
        qq_plot(data, title="Q-Q Plot of Normal Distribution")

if __name__ == '__main__':
    unittest.main()
