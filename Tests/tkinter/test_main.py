import unittest
from unittest.mock import patch
import tkinter as tk
from pysnippets.tkinter.main import main

class TestMain(unittest.TestCase):
    @patch('pysnippets.tkinter.main.show_confirmation')
    @patch('tkinter.Tk')
    def test_on_exit_confirm(self, mock_tk, mock_show_confirmation):
        mock_show_confirmation.return_value = True
        with patch.object(tk.Tk, 'destroy') as mock_destroy:
            main()
            mock_show_confirmation.assert_called()
            mock_destroy.assert_called()

    @patch('pysnippets.tkinter.main.show_confirmation')
    @patch('tkinter.Tk')
    def test_on_exit_cancel(self, mock_tk, mock_show_confirmation):
        mock_show_confirmation.return_value = False
        with patch.object(tk.Tk, 'destroy') as mock_destroy:
            main()
            mock_show_confirmation.assert_called()
            mock_destroy.assert_not_called()

if __name__ == '__main__':
    unittest.main() 