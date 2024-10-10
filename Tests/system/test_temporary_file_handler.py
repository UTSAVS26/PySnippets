import unittest
import os
from pysnippets.system.temporary_file_handler import create_temp_file, read_temp_file, delete_temp_file


class TestTempFileHandler(unittest.TestCase):

    def test_create_and_read_temp_file(self):
        file_path = create_temp_file("Hello, World!")
        self.assertTrue(os.path.exists(file_path))  # Check if the file was created
        content = read_temp_file(file_path)
        self.assertEqual(content, "Hello, World!")  # Ensure the content is correct
        delete_temp_file(file_path)

    def test_delete_temp_file(self):
        file_path = create_temp_file("Temporary data")
        self.assertTrue(
            delete_temp_file(file_path)
        )  # File should be successfully deleted
        self.assertFalse(os.path.exists(file_path))  # Ensure the file no longer exists

    def test_read_nonexistent_temp_file(self):
        self.assertIsNone(
            read_temp_file("nonexistent_temp_file.txt")
        )  # Should return None for nonexistent file


if __name__ == "__main__":
    unittest.main()
