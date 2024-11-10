import unittest
import matplotlib.pyplot as plt
from library_snippets.matplotlib_snippet import plot_line, plot_bar

class TestMatplotlibSnippet(unittest.TestCase):
    def test_plot_line(self):
        """ Test line plot creation. """
        try:
            plot_line([1, 2, 3], [1, 4, 9], 'Test Line Plot', 'x-axis', 'y-axis')
        except Exception as e:
            self.fail(f"plot_line raised an exception {e}")

    def test_plot_bar(self):
        """ Test bar plot creation. """
        try:
            plot_bar(['a', 'b', 'c'], [5, 3, 9], 'Test Bar Plot', 'Categories', 'Values')
        except Exception as e:
            self.fail(f"plot_bar raised an exception {e}")

# Additional tests for scatter, histogram, and pie can be added similarly.

if __name__ == '__main__':
    unittest.main() 