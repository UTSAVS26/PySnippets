import unittest
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from Dual_axis_line import dual_axis_line_plot
from Annonated_Heatmap import advanced_heatmap
from Boxplot_with_notches import notched_boxplot
from Stacked_Bar_Chart import stacked_bar_chart
from Violin_split import split_violin_plot
from Scatter_regression import scatter_with_regression
from ThreeD_surface import surface_plot
from Density_Shade import density_plot
from Circular_bar import circular_bar_plot
from Heatmap_cluster import clustered_heatmap
from Filled_area import filled_area_plot

class TestAdvancedVisualizations(unittest.TestCase):

    def setUp(self):
        """Set up common resources for tests."""
        self.linspace_0_10_100 = np.linspace(0, 10, 100)
        self.linspace_neg5_5_100 = np.linspace(-5, 5, 100)
        self.tips_data = sns.load_dataset("tips")
        self.iris_data = sns.load_dataset("iris")
        self.categories = ['A', 'B', 'C', 'D']
        self.values1 = [3, 6, 9, 12]
        self.values2 = [5, 4, 2, 8]
        self.labels = ['A', 'B', 'C', 'D', 'E']
        self.bar_values = [4, 6, 5, 7, 3]
        self.surface_function = lambda x, y: np.sin(np.sqrt(x**2 + y**2))

    def tearDown(self):
        """Clean up after tests."""
        plt.close('all')

    def run_plot_test(self, plot_func, *args, **kwargs):
        """Helper method to run plot functions and handle exceptions."""
        try:
            plot_func(*args, **kwargs)
        except Exception as e:
            self.fail(f"{plot_func.__name__} raised an exception: {e}")

    def test_dual_axis_line_plot(self):
        x = self.linspace_0_10_100
        y1 = np.sin(x)
        y2 = np.cos(x)
        self.run_plot_test(dual_axis_line_plot, x, y1, y2)

    def test_advanced_heatmap(self):
        data = np.random.rand(10, 12)
        self.run_plot_test(advanced_heatmap, data)

    def test_notched_boxplot(self):
        self.run_plot_test(notched_boxplot, self.tips_data, x_col='day', y_col='total_bill')

    def test_stacked_bar_chart(self):
        self.run_plot_test(stacked_bar_chart, self.categories, self.values1, self.values2)

    def test_split_violin_plot(self):
        self.run_plot_test(split_violin_plot, self.tips_data, x="day", y="total_bill", hue="sex")

    def test_scatter_with_regression(self):
        self.run_plot_test(scatter_with_regression, self.tips_data, x="total_bill", y="tip")

    def test_surface_plot(self):
        x = self.linspace_neg5_5_100
        y = self.linspace_neg5_5_100
        self.run_plot_test(surface_plot, x, y, self.surface_function)

    def test_density_plot(self):
        self.run_plot_test(density_plot, self.iris_data, col="sepal_length")

    def test_circular_bar_plot(self):
        self.run_plot_test(circular_bar_plot, self.labels, self.bar_values)

    def test_clustered_heatmap(self):
        data = np.random.rand(10, 10)
        self.run_plot_test(clustered_heatmap, data)

    def test_filled_area_plot(self):
        x = self.linspace_0_10_100
        y = np.sin(x)
        self.run_plot_test(filled_area_plot, x, y)

if __name__ == '__main__':
    unittest.main()
