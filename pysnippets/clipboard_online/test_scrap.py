import unittest
from unittest.mock import patch, mock_open
from package.scrap.grab import copy_to_clipboard, grab_content, show, clip, write


class TestGrabFunctions(unittest.TestCase):
    def setUp(self):
        """Set up test data that will be used across test methods"""
        self.sample_html = """
            <html>
                <body>
                    <textarea id="cl1pTextArea">Test content</textarea>
                </body>
            </html>
        """
        self.test_content = "Test content"

    @patch("subprocess.run")
    def test_copy_to_clipboard_linux(self, mock_run):
        # Mock platform to test Linux clipboard
        with patch("sys.platform", "linux"), patch(
            "shutil.which", return_value="/usr/bin/xclip"
        ):
            copy_to_clipboard("test content")

        mock_run.assert_called_once_with(
            ["xclip", "-selection", "clipboard"], input=b"test content", check=True
        )

    @patch("subprocess.run")
    def test_copy_to_clipboard_windows(self, mock_run):
        with patch("sys.platform", "win32"):
            copy_to_clipboard("test text")
            mock_run.assert_called_once_with(
                ["C:\\Windows\\System32\\clip.exe"], input=b"test text", check=True
            )

    @patch("subprocess.run")
    def test_copy_to_clipboard_macos(self, mock_run):
        with patch("sys.platform", "darwin"):
            copy_to_clipboard("test text")
            mock_run.assert_called_once_with(
                ["/usr/bin/pbcopy"], input=b"test text", check=True
            )

    @patch("builtins.print")
    @patch("package.scrap.grab.grab_content", return_value="test content")
    def test_show(self, mock_grab_content, mock_print):
        show("test-url")
        mock_print.assert_called_once_with("The content is: ", "test content")

    @patch("builtins.print")
    @patch("package.scrap.grab.grab_content", return_value="test content")
    @patch("package.scrap.grab.copy_to_clipboard")
    def test_clip(self, mock_copy_to_clipboard, mock_grab_content, mock_print):
        clip("test-url")
        mock_copy_to_clipboard.assert_called_once_with("test content")
        mock_print.assert_called_once_with("Content copied to clipboard.")

    @patch("builtins.open", new_callable=mock_open)
    @patch("package.scrap.grab.grab_content", return_value="test content")
    def test_write(self, mock_grab_content, mock_open):
        write("test-url", "test.txt")
        mock_open.assert_called_once_with("test.txt", "w")
        mock_open().write.assert_called_once_with("test content")


if __name__ == "__main__":
    unittest.main()
