import unittest
from unittest.mock import patch
import tkinter as tk
from pysnippets.tkinter.__init__ import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = App(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_app_initialization(self):
        self.assertEqual(self.app.root.title(), "Tkinter Example App")
        self.assertEqual(self.app.root.geometry(), "300x200")
        self.assertIsInstance(self.app.label, tk.Label)
        self.assertEqual(self.app.label['text'], "Hello, Tkinter!")
        self.assertIsInstance(self.app.button, tk.Button)
        self.assertEqual(self.app.button['text'], "Click Me")

    @patch('tkinter.messagebox.showinfo')
    def test_on_button_click(self, mock_showinfo):
        self.app.on_button_click()
        mock_showinfo.assert_called_once_with("Information", "Button was clicked!")

if __name__ == '__main__':
    unittest.main() 