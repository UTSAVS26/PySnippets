import unittest
from unittest.mock import patch
from disk_space_checker import check_disk_space

class TestDiskSpaceChecker(unittest.TestCase):
    def test_disk_space_checker(self):
        # Test with default path
        result = check_disk_space('/')
        self.assertIsInstance(result.total_space_gb, float)
        self.assertIsInstance(result.used_space_gb, float)
        self.assertIsInstance(result.free_space_gb, float)
        self.assertIsInstance(result.used_percent, float)
        self.assertIsInstance(result.free_percent, float)

    def test_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            check_disk_space('/invalid/path')

    @patch('shutil.disk_usage')
    def test_permission_error(self, mock_disk_usage):
        mock_disk_usage.side_effect = PermissionError("Permission denied for path '/root'")
        with self.assertRaises(PermissionError):
            check_disk_space('/root')

if __name__ == '__main__':
    unittest.main() 