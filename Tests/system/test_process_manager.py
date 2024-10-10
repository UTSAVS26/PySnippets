import unittest
from pysnippets.system.process_manager import start_process, stop_process, monitor_process
import psutil
import time

class TestProcessManager(unittest.TestCase):

    def test_start_process(self):
        process = start_process('python -m http.server')
        self.assertTrue(process.pid > 0)  # Check if process started and has a valid PID
        stop_process(process.pid)

    def test_stop_process(self):
        process = start_process('python -m http.server')
        self.assertTrue(stop_process(process.pid))  # Check if process was successfully stopped
        self.assertFalse(psutil.pid_exists(process.pid))  # Ensure the process no longer exists

    def test_monitor_process(self):
        process = start_process('python -m http.server')
        time.sleep(1)  # Allow some time for CPU usage to accumulate
        metrics = monitor_process(process.pid)
        self.assertTrue(metrics['cpu_usage'] >= 0)  # Check if CPU usage is reported
        self.assertTrue(metrics['memory_usage'] > 0)  # Check if memory usage is reported
        stop_process(process.pid)

if __name__ == '__main__':
    unittest.main()
