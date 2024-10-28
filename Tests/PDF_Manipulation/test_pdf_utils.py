import unittest
import os
from pypdf import PdfReader
from pysnippets.PDF_Manipulation.pdf_reader import read_pdf
from pysnippets.PDF_Manipulation.pdf_splitter import split_pdf
from pysnippets.PDF_Manipulation.pdf_merger import merge_pdfs
from pysnippets.PDF_Manipulation.pdf_manipulator import rotate_pdf_pages
from pysnippets.PDF_Manipulation.pdf_security import encrypt_pdf, decrypt_pdf


class TestPdfUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a simple test PDF
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        
        cls.test_pdf = "test.pdf"
        cls.temp_dir = "temp_test_files"
        os.makedirs(cls.temp_dir, exist_ok=True)
        
        c = canvas.Canvas(cls.test_pdf, pagesize=letter)
        c.drawString(100, 750, "Test PDF Page 1")
        c.showPage()
        c.drawString(100, 750, "Test PDF Page 2")
        c.showPage()
        c.save()
    
    @classmethod
    def tearDownClass(cls):
        # Clean up test files
        if os.path.exists(cls.test_pdf):
            os.remove(cls.test_pdf)
        for file in os.listdir(cls.temp_dir):
            os.remove(os.path.join(cls.temp_dir, file))
        os.rmdir(cls.temp_dir)
    
    def test_read_pdf(self):
        result = read_pdf(self.test_pdf)
        self.assertEqual(result['num_pages'], 2)
        self.assertTrue(len(result['content']) == 2)
    
    def test_split_pdf(self):
        output_files = split_pdf(self.test_pdf, self.temp_dir)
        self.assertEqual(len(output_files), 2)
        for file in output_files:
            self.assertTrue(os.path.exists(file))
    
    def test_merge_pdfs(self):
        # Split first, then merge
        split_files = split_pdf(self.test_pdf, self.temp_dir)
        merged_pdf = os.path.join(self.temp_dir, "merged.pdf")
        
        success = merge_pdfs(split_files, merged_pdf)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(merged_pdf))
    
    def test_rotate_pdf(self):
        output_path = os.path.join(self.temp_dir, "rotated.pdf")
        success = rotate_pdf_pages(self.test_pdf, output_path, 90)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(output_path))
    
    def test_encrypt_decrypt_pdf(self):
        encrypted_pdf = os.path.join(self.temp_dir, "encrypted.pdf")
        decrypted_pdf = os.path.join(self.temp_dir, "decrypted.pdf")
        
        # Test encryption
        success = encrypt_pdf(self.test_pdf, encrypted_pdf, "user123", "owner456")
        self.assertTrue(success)
        self.assertTrue(os.path.exists(encrypted_pdf))
        
        # Test decryption
        success = decrypt_pdf(encrypted_pdf, decrypted_pdf, "user123")
        self.assertTrue(success)
        self.assertTrue(os.path.exists(decrypted_pdf))

if __name__ == '__main__':
    unittest.main()