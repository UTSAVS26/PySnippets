import unittest
import numpy as np
from advanced_graphing import (
    set_config, normalize_data, moving_average, safe_plot, line_plot, bar_chart, get_available_styles, config
)

class TestAdvancedGraphing(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        set_config(style='ggplot', figsize=(10, 6), color_palette='viridis')

    def test_normalize_data(self):
        """Test the normalization of data."""
        data = np.array([1, 2, 3, 4, 5])
        normalized = normalize_data(data)
        expected = np.array([0, 0.25, 0.5, 0.75, 1])
        np.testing.assert_array_almost_equal(normalized, expected)

    def test_moving_average(self):
        """Test the moving average calculation."""
        data = np.array([1, 2, 3, 4, 5])
        moving_avg = moving_average(data, window=3)
        expected = np.array([2, 3, 4])
        np.testing.assert_array_almost_equal(moving_avg, expected)

    def test_set_config(self):
        """Test setting configuration."""
        available_styles = get_available_styles()
        valid_style = available_styles[0]  # Use the first available style
        set_config(style=valid_style, figsize=(12, 8), color_palette='Set1')
        
        # Access the global config directly
        self.assertEqual(config.style, valid_style)
        self.assertEqual(config.figsize, (12, 8))
        self.assertEqual(config.color_palette, 'Set1')

    def test_safe_plot(self):
        """Test that safe_plot does not raise an error for valid functions."""
        try:
            safe_plot(line_plot, np.array([1, 2, 3]), np.array([1, 4, 9]), title="Test Line Plot")
            safe_plot(bar_chart, ['A', 'B', 'C'], [1, 2, 3], title="Test Bar Chart")
        except Exception as e:
            self.fail(f"safe_plot raised an exception: {str(e)}")

if __name__ == '__main__':
    unittest.main() 