import unittest
from unittest.mock import patch
from pysnippets.tkinter.dialogs import show_confirmation, show_error, show_info

class TestDialogs(unittest.TestCase):
    @patch('tkinter.messagebox.askyesno')
    def test_show_confirmation_yes(self, mock_askyesno):
        mock_askyesno.return_value = True
        result = show_confirmation("Confirm", "Do you want to proceed?")
        self.assertTrue(result)
        mock_askyesno.assert_called_once_with("Confirm", "Do you want to proceed?")

    @patch('tkinter.messagebox.askyesno')
    def test_show_confirmation_no(self, mock_askyesno):
        mock_askyesno.return_value = False
        result = show_confirmation("Confirm", "Do you want to proceed?")
        self.assertFalse(result)
        mock_askyesno.assert_called_once_with("Confirm", "Do you want to proceed?")

    @patch('tkinter.messagebox.showerror')
    def test_show_error(self, mock_showerror):
        show_error("Error", "An unexpected error occurred.")
        mock_showerror.assert_called_once_with("Error", "An unexpected error occurred.")

    @patch('tkinter.messagebox.showinfo')
    def test_show_info(self, mock_showinfo):
        show_info("Information", "This is an informational message.")
        mock_showinfo.assert_called_once_with("Information", "This is an informational message.")

if __name__ == '__main__':
    unittest.main() 