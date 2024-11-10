import unittest

# Importing test functions from other test files
from test_property import test_dynamic_property_creation
from test_Dynamic_class import test_dynamic_functions
from test_type import test_dynamic_class_creation
from test_method import test_dynamic_method_creation
from test_attribute import test_dynamic_attribute_assignment

# Creating a test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.FunctionTestCase(test_dynamic_property_creation))
    suite.addTest(unittest.FunctionTestCase(test_dynamic_functions))
    suite.addTest(unittest.FunctionTestCase(test_dynamic_class_creation))
    suite.addTest(unittest.FunctionTestCase(test_dynamic_method_creation))
    suite.addTest(unittest.FunctionTestCase(test_dynamic_attribute_assignment))
    return suite

# Running the test suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
