import unittest
import os
import tempfile
import shutil
from Snippets.File_Organizer.file_organizer import organize_files_by_type

class TestOrganizeFilesByType(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        # Create a few files for testing
        self.files_to_create = {
            'image1.jpg': 'image content',
            'document1.pdf': 'pdf content',
            'video1.mp4': 'video content',
            'music1.mp3': 'music content',
            'script1.py': 'print("Hello World")',
            'archive1.zip': 'zip content',
            'unrecognized_file.txt': 'unrecognized content'
        }
        for filename, content in self.files_to_create.items():
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(content)

    def tearDown(self):
        # Remove the temporary directory after the tests
        shutil.rmtree(self.test_dir)

    def test_organize_files(self):
        # Test normal behavior of organizing files
        organize_files_by_type(self.test_dir)

        # Check if the files were moved to the correct folders
        for category in ['Images', 'Documents', 'Videos', 'Music', 'Scripts', 'Archives']:
            category_path = os.path.join(self.test_dir, category)
            self.assertTrue(os.path.exists(category_path), f"{category_path} should exist.")
        
        # Check specific files in their corresponding folders
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Images', 'image1.jpg')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Documents', 'document1.pdf')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Videos', 'video1.mp4')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Music', 'music1.mp3')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Scripts', 'script1.py')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Archives', 'archive1.zip')))

    def test_invalid_folder(self):
        # Test case for invalid folder path
        with self.assertRaises(ValueError):
            organize_files_by_type('invalid_path')

if __name__ == '__main__':
    unittest.main()
