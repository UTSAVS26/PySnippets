import unittest
import os
from env_var_manager import EnvVarManager

class TestEnvVarManager(unittest.TestCase):
    def setUp(self):
        self.manager = EnvVarManager()
        # Clean up any test variables that might exist
        for var in ['TEST_VAR1', 'TEST_VAR2']:
            if var in os.environ:
                del os.environ[var]

    def tearDown(self):
        # Clean up after tests
        self.manager.restore_all()
        for var in ['TEST_VAR1', 'TEST_VAR2']:
            if var in os.environ:
                del os.environ[var]

    def test_set_and_get_var(self):
        # Test setting new variable
        env_var = self.manager.set_var('TEST_VAR1', 'value1')
        self.assertEqual(env_var.name, 'TEST_VAR1')
        self.assertEqual(env_var.value, 'value1')
        self.assertIsNone(env_var.previous_value)
        
        # Test getting variable
        self.assertEqual(self.manager.get_var('TEST_VAR1'), 'value1')

    def test_update_existing_var(self):
        # Set initial value
        os.environ['TEST_VAR1'] = 'initial'
        
        # Update value
        env_var = self.manager.set_var('TEST_VAR1', 'updated')
        self.assertEqual(env_var.previous_value, 'initial')
        self.assertEqual(self.manager.get_var('TEST_VAR1'), 'updated')

    def test_delete_var(self):
        # Set and then delete variable
        self.manager.set_var('TEST_VAR1', 'value1')
        self.manager.delete_var('TEST_VAR1')
        self.assertIsNone(self.manager.get_var('TEST_VAR1'))

    def test_restore_var(self):
        # Test restoring to previous value
        os.environ['TEST_VAR1'] = 'initial'
        self.manager.set_var('TEST_VAR1', 'modified')
        self.manager.restore_var('TEST_VAR1')
        self.assertEqual(os.environ.get('TEST_VAR1'), 'initial')

        # Test restoring non-existent variable
        self.manager.restore_var('NON_EXISTENT')
        self.assertNotIn('NON_EXISTENT', os.environ)

    def test_restore_all(self):
        # Set multiple variables
        os.environ['TEST_VAR1'] = 'initial1'
        os.environ['TEST_VAR2'] = 'initial2'
        
        self.manager.set_var('TEST_VAR1', 'modified1')
        self.manager.set_var('TEST_VAR2', 'modified2')
        
        self.manager.restore_all()
        
        self.assertEqual(os.environ.get('TEST_VAR1'), 'initial1')
        self.assertEqual(os.environ.get('TEST_VAR2'), 'initial2')

    def test_context_manager(self):
        with EnvVarManager() as manager:
            manager.set_var('TEST_VAR1', 'value1')
            self.assertEqual(os.environ.get('TEST_VAR1'), 'value1')
        
        # Variable should be restored after context
        self.assertNotIn('TEST_VAR1', os.environ)

if __name__ == '__main__':
    unittest.main()