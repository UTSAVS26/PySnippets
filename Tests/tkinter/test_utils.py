import unittest
from unittest.mock import patch
from pysnippets.tkinter.utils import open_file_dialog, save_file_dialog

class TestUtils(unittest.TestCase):
    @patch('tkinter.filedialog.askopenfilename')
    def test_open_file_dialog_selected(self, mock_askopenfilename):
        mock_askopenfilename.return_value = '/path/to/file.txt'
        result = open_file_dialog("Select a file")
        self.assertEqual(result, '/path/to/file.txt')
        mock_askopenfilename.assert_called_once_with(title="Select a file")

    @patch('tkinter.filedialog.askopenfilename')
    def test_open_file_dialog_cancelled(self, mock_askopenfilename):
        mock_askopenfilename.return_value = ''
        result = open_file_dialog("Select a file")
        self.assertEqual(result, '')
        mock_askopenfilename.assert_called_once_with(title="Select a file")

    @patch('tkinter.filedialog.asksaveasfilename')
    def test_save_file_dialog_selected(self, mock_asksaveasfilename):
        mock_asksaveasfilename.return_value = '/path/to/save.txt'
        result = save_file_dialog("Save your file", ".txt")
        self.assertEqual(result, '/path/to/save.txt')
        mock_asksaveasfilename.assert_called_once_with(title="Save your file", defaultextension=".txt")

    @patch('tkinter.filedialog.asksaveasfilename')
    def test_save_file_dialog_cancelled(self, mock_asksaveasfilename):
        mock_asksaveasfilename.return_value = ''
        result = save_file_dialog("Save your file", ".txt")
        self.assertEqual(result, '')
        mock_asksaveasfilename.assert_called_once_with(title="Save your file", defaultextension=".txt")

if __name__ == '__main__':
    unittest.main() 