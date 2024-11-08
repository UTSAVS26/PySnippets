import unittest
from pysnippets.tkinter.widgets import CustomEntry
import tkinter as tk

class TestCustomEntry(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

    def tearDown(self):
        self.root.destroy()

    def test_placeholder_displayed_initially(self):
        entry = CustomEntry(self.root, placeholder="Enter name")
        entry.pack()
        self.assertEqual(entry.get(), "Enter name")
        self.assertEqual(entry['fg'], 'grey')

    def test_placeholder_cleared_on_focus_in(self):
        entry = CustomEntry(self.root, placeholder="Enter name")
        entry.pack()
        entry.focus_set()
        entry.event_generate("<FocusIn>")
        self.assertEqual(entry.get(), "")
        self.assertEqual(entry['fg'], 'black')

    def test_placeholder_reappears_on_focus_out_if_empty(self):
        entry = CustomEntry(self.root, placeholder="Enter name")
        entry.pack()
        entry.focus_set()
        entry.event_generate("<FocusIn>")
        entry.event_generate("<FocusOut>")
        self.assertEqual(entry.get(), "Enter name")
        self.assertEqual(entry['fg'], 'grey')

    def test_placeholder_does_not_reappear_if_not_empty(self):
        entry = CustomEntry(self.root, placeholder="Enter name")
        entry.pack()
        entry.focus_set()
        entry.event_generate("<FocusIn>")
        entry.insert(0, "John Doe")
        entry.event_generate("<FocusOut>")
        self.assertEqual(entry.get(), "John Doe")
        self.assertEqual(entry['fg'], 'black')

if __name__ == '__main__':
    unittest.main() 