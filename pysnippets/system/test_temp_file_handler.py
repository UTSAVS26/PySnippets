import tempfile
import unittest
import os
from pathlib import Path
from temp_file_handler import TempFileHandler, TempFile

class TestTempFileHandler(unittest.TestCase):
    def setUp(self):
        self.handler = TempFileHandler()

    def tearDown(self):
        self.handler.cleanup()

    def test_create_temp_file_with_content(self):
        content = "Test content"
        temp_file = self.handler.create_temp_file(content=content, suffix=".txt")
        
        self.assertIsInstance(temp_file, TempFile)
        self.assertTrue(temp_file.path.exists())
        self.assertEqual(temp_file.path.read_text(), content)
        self.assertTrue(temp_file.name.endswith(".txt"))
        self.assertEqual(temp_file.size_bytes, len(content))
        self.assertIn(temp_file, self.handler.temp_files)

    def test_create_empty_temp_file(self):
        temp_file = self.handler.create_temp_file(prefix="test_", suffix=".tmp")
        
        self.assertIsInstance(temp_file, TempFile)
        self.assertTrue(temp_file.path.exists())
        self.assertEqual(temp_file.path.read_text(), "")
        self.assertTrue(temp_file.name.startswith("test_"))
        self.assertTrue(temp_file.name.endswith(".tmp"))
        self.assertEqual(temp_file.size_bytes, 0)

    def test_custom_base_dir(self):
        custom_dir = tempfile.gettempdir()
        handler = TempFileHandler(base_dir=custom_dir)
        temp_file = handler.create_temp_file()
        
        self.assertEqual(temp_file.path.parent, Path(custom_dir))
        handler.cleanup()

    def test_cleanup(self):
        # Create multiple temp files
        temp_files = [
            self.handler.create_temp_file("content 1"),
            self.handler.create_temp_file("content 2")
        ]
        
        # Verify files exist
        for temp_file in temp_files:
            self.assertTrue(temp_file.path.exists())
        
        # Clean up
        self.handler.cleanup()
        
        # Verify files are deleted
        for temp_file in temp_files:
            self.assertFalse(temp_file.path.exists())
        self.assertEqual(len(self.handler.temp_files), 0)

    def test_context_manager(self):
        with TempFileHandler() as handler:
            temp_file = handler.create_temp_file("test content")
            self.assertTrue(temp_file.path.exists())
            file_path = temp_file.path
            
        # Verify file is deleted after context
        self.assertFalse(file_path.exists())

    def test_invalid_base_dir(self):
        with self.assertRaises(Exception):
            handler = TempFileHandler(base_dir="/nonexistent/directory")
            handler.create_temp_file()

if __name__ == '__main__':
    unittest.main()