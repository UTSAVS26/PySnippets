import unittest
from date_utils import convert_to_iso8601

class TestDateConversion(unittest.TestCase):
    def test_valid_dates(self):
        self.assertEqual(convert_to_iso8601("2024-10-06"), "2024-10-06T00:00:00")
        self.assertEqual(convert_to_iso8601("10/06/2024"), "2024-10-06T00:00:00")

    def test_invalid_date(self):
        self.assertIn("Error:", convert_to_iso8601("invalid-date"))

if __name__ == "__main__":
    unittest.main()
