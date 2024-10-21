import numpy as np
import unittest
from pysnippets.models.XGB import XGBModel  # Updated import

class TestXGBModel(unittest.TestCase):
    def test_xgb_model_initialization(self):
        model = XGBModel()  # Example usage
        self.assertIsNotNone(model)  # Simple test to check initialization