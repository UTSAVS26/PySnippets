import unittest
import os
from pysnippets.system.environment_variable_manager import get_env_variable, set_env_variable, delete_env_variable

class TestEnvVariableManager(unittest.TestCase):

    def test_set_and_get_env_variable(self):
        set_env_variable('TEST_VAR', 'test_value')
        self.assertEqual(get_env_variable('TEST_VAR'), 'test_value')

    def test_delete_env_variable(self):
        set_env_variable('TEST_VAR', 'test_value')
        delete_env_variable('TEST_VAR')
        self.assertIsNone(get_env_variable('TEST_VAR'))  # After deletion, it should return None

    def test_get_nonexistent_variable(self):
        self.assertIsNone(get_env_variable('NONEXISTENT_VAR'))  # Should return None if not set

if __name__ == '__main__':
    unittest.main()
