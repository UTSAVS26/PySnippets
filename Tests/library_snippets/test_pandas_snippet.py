import unittest
import pandas as pd
from library_snippets.pandas_snippet import filter, save

class TestPandasSnippet(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35]
        })

    def test_filter(self):
        """ Test filtering DataFrame by column value. """
        result = filter(self.df, 'Name', 'Alice')
        expected = pd.DataFrame({
            'Name': ['Alice'],
            'Age': [25]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_save(self):
        """ Test saving DataFrame to CSV. """
        # This test would ideally check file output, but here we'll just run the function.
        try:
            save(self.df, 'test_output.csv')
        except Exception as e:
            self.fail(f"save raised an exception {e}")

# Additional tests for other DataFrame operations can be added similarly.

if __name__ == '__main__':
    unittest.main() 