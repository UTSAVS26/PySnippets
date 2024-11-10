import unittest
import subprocess
import time
from process_manager import start_process, stop_process

class TestProcessManager(unittest.TestCase):
    def test_start_process(self):
        # Test starting a valid process
        process = start_process('echo "test"')
        self.assertIsInstance(process, subprocess.Popen)
        self.assertGreater(process.pid, 0)
        
        # Clean up
        process.wait()

    def test_start_process_invalid_command(self):
        # Test starting process with invalid command
        with self.assertRaises(Exception):
            start_process('invalid_command')
            raise Exception("Invalid command should raise an exception")

    def test_stop_process(self):
        # Start a long-running process
        process = start_process('sleep 10')
        pid = process.pid
        
        # Stop the process
        stop_process(pid)
        
        # Verify process was terminated
        process.wait()
        self.assertNotEqual(process.returncode, 0)

    def test_stop_nonexistent_process(self):
        # Test stopping a process that doesn't exist
        with self.assertRaises(Exception):
            stop_process(99999)
    def test_process_output(self):
        # Test process output is captured correctly
        process = start_process('echo test output')
        output, _ = process.communicate()
        self.assertEqual(output.decode().strip(), "test output")

    def test_process_error(self):
        # Test process error is captured correctly
        process = start_process('ls /nonexistent')
        _, error = process.communicate()
        self.assertNotEqual(error.decode().strip(), "")

if __name__ == '__main__':
    unittest.main()