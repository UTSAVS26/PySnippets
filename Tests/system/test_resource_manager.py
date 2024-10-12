import unittest
from pysnippets.system.system_resource_monitor import get_cpu_usage, get_memory_usage

class TestSystemResourceMonitor(unittest.TestCase):

    def test_get_cpu_usage(self):
        cpu_usage = get_cpu_usage()
        self.assertTrue(0 <= cpu_usage <= 100)  # CPU usage should be between 0 and 100%

    def test_get_memory_usage(self):
        memory_info = get_memory_usage()
        self.assertTrue(memory_info['total_memory'] > 0)  # Total memory should be positive
        self.assertTrue(memory_info['used_memory'] > 0)  # Used memory should be positive

if __name__ == '__main__':
    unittest.main()
