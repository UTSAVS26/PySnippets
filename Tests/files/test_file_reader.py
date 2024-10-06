# test_file_reader.py

import os
import unittest
from Snippets.Files.file_reader import read_file


class TestFileReader(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_file = "test_file.txt"
        with open(self.test_file, "w") as f:
            f.write("This is a test file.")

    def tearDown(self):
        # Remove the temporary file after the test
        os.remove(self.test_file)

    def test_read_file(self):
        content = read_file(self.test_file)
        self.assertEqual(content, "This is a test file.")

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file("non_existent_file.txt")


if __name__ == "__main__":
    unittest.main()
