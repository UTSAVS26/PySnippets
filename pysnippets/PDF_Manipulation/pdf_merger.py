from pypdf import PdfReader, PdfWriter
import os

def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDF files into one."""
    writer = PdfWriter()
    
    try:
        for pdf in pdf_files:
            reader = PdfReader(pdf)
            for page in reader.pages:
                writer.add_page(page)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        return True
    except Exception as e:
        print(f"Error merging PDFs: {str(e)}")
        return False

def merge_pdfs_with_pages(pdf_config, output_path):
    """Merge specific pages from multiple PDFs."""
    writer = PdfWriter()
    
    try:
        for pdf_path, pages in pdf_config:
            reader = PdfReader(pdf_path)
            
            # If pages list is provided, only add specified pages
            if pages is not None:
                for page_num in pages:
                    writer.add_page(reader.pages[page_num])
            else:  # If pages is None, add all pages
                for page in reader.pages:
                    writer.add_page(page)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        return True
    except Exception as e:
        print(f"Error merging PDFs: {str(e)}")
        return False
