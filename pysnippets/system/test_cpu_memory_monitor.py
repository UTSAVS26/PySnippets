import unittest
from cpu_memory_monitor import monitor_system

class TestCPUMemoryMonitor(unittest.TestCase):
    def test_monitor_system(self):
        # Test basic functionality
        result = monitor_system()
        
        # Test CPU percentage is within valid range
        self.assertIsInstance(result.cpu_percent, float)
        self.assertGreaterEqual(result.cpu_percent, 0)
        self.assertLessEqual(result.cpu_percent, 100)
        
        # Test memory values are valid
        self.assertIsInstance(result.memory_total_gb, float)
        self.assertIsInstance(result.memory_used_gb, float) 
        self.assertIsInstance(result.memory_free_gb, float)
        self.assertIsInstance(result.memory_percent, float)
        
        # Test memory calculations
        self.assertGreater(result.memory_total_gb, 0)
        self.assertGreaterEqual(result.memory_used_gb, 0)
        self.assertGreaterEqual(result.memory_free_gb, 0)
        self.assertGreaterEqual(result.memory_percent, 0)
        self.assertLessEqual(result.memory_percent, 100)
        
        # Test memory values add up correctly (within rounding margin)
        self.assertAlmostEqual(
            result.memory_used_gb + result.memory_free_gb,
            result.memory_total_gb,
            delta=0.1
        )

if __name__ == '__main__':
    unittest.main()