import unittest
from pysnippets.tkinter.styles import configure_styles
import tkinter as tk
from tkinter import ttk

class TestStyles(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.root.withdraw()  # Hide the main window

    def tearDown(self):
        self.root.destroy()

    def test_custom_tbutton_style(self):
        configure_styles()
        self.assertEqual(self.style.lookup('Custom.TButton', 'foreground'), 'white')
        self.assertEqual(self.style.lookup('Custom.TButton', 'background'), '#4CAF50')
        self.assertEqual(self.style.lookup('Custom.TButton', 'font'), ('Helvetica', 12, 'bold'))

    def test_custom_tbutton_active_background(self):
        configure_styles()
        map_config = self.style.map('Custom.TButton', 'background')
        self.assertIn(('active', '#45a049'), map_config)

    def test_custom_tlabel_style(self):
        configure_styles()
        self.assertEqual(self.style.lookup('Custom.TLabel', 'foreground'), '#333333')
        self.assertEqual(self.style.lookup('Custom.TLabel', 'font'), ('Helvetica', 10))

    def test_custom_tentry_style(self):
        configure_styles()
        self.assertEqual(self.style.lookup('Custom.TEntry', 'foreground'), '#000000')
        self.assertEqual(self.style.lookup('Custom.TEntry', 'font'), ('Helvetica', 10))

    def test_theme_used_is_clam(self):
        configure_styles()
        current_theme = self.style.theme_use()
        self.assertEqual(current_theme, 'clam')

if __name__ == '__main__':
    unittest.main() 