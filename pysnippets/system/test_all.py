import unittest
from test_cpu_memory_monitor import TestCPUMemoryMonitor
from test_disk_space_checker import TestDiskSpaceChecker
from test_env_var_manager import TestEnvVarManager
from test_process_manager import TestProcessManager
from test_temp_file_handler import TestTempFileHandler

def run_all_tests():
    # Create test suite containing all tests
    test_suite = unittest.TestSuite()
    
    # Add test cases from each test module
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCPUMemoryMonitor))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDiskSpaceChecker))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestEnvVarManager))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestProcessManager))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTempFileHandler))

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_all_tests()
    exit(0 if success else 1)
