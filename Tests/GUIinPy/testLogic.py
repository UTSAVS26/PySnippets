import unittest
from gui_logic import handle_input

class TestGuiLogic(unittest.TestCase):

    def test_handle_input_with_text(self):
        self.assertEqual(handle_input("Hello"), "You entered: Hello")

    def test_handle_input_empty(self):
        self.assertEqual(handle_input(""), "Please enter some text!")

if __name__ == '__main__':
    unittest.main()
