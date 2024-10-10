import unittest
from pysnippets.system.disk_space_checker import check_disk_space
import os

class TestDiskSpaceChecker(unittest.TestCase):

    def test_check_disk_space(self):
        disk_info = check_disk_space('/')
        self.assertTrue(disk_info['total_space'] > 0)  # Total space should be positive
        self.assertTrue(disk_info['free_space'] > 0)   # Free space should be positive
        self.assertTrue(disk_info['used_space'] >= 0)  # Used space should be non-negative

    def test_invalid_path(self):
        invalid_path = '/invalidpath'
        with self.assertRaises(FileNotFoundError):
            check_disk_space(invalid_path)  # Should raise an error for invalid path

if __name__ == '__main__':
    unittest.main()
