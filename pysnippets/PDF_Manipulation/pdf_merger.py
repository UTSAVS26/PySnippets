from pypdf import PdfReader, PdfWriter
import os

def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDF files into one."""
    if not pdf_files:
        print("No PDF files provided for merging.")
        return False

    writer = PdfWriter()
    
    try:
        for pdf in pdf_files:
            if not os.path.isfile(pdf) or not pdf.lower().endswith('.pdf'):
                print(f"Skipping invalid PDF file: {pdf}")
                continue
            
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
    if not pdf_config:
        print("No PDF configurations provided for merging.")
        return False

    writer = PdfWriter()
    
    try:
        for pdf_path, pages in pdf_config:
            if not os.path.isfile(pdf_path) or not pdf_path.lower().endswith('.pdf'):
                print(f"Skipping invalid PDF file: {pdf_path}")
                continue

            reader = PdfReader(pdf_path)
            total_pages = len(reader.pages)
            
            if pages is not None:
                for page_num in pages:
                    if 0 <= page_num < total_pages:
                        writer.add_page(reader.pages[page_num])
                    else:
                        print(f"Page {page_num} out of range for file {pdf_path}. Skipping.")
            else:
                for page in reader.pages:
                    writer.add_page(page)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        return True
    except Exception as e:
        print(f"Error merging PDFs: {str(e)}")
        return False