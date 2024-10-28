from pypdf import PdfReader, PdfWriter
import os

def split_pdf(input_path, output_directory):
    """Split PDF into individual pages."""
    reader = PdfReader(input_path)
    os.makedirs(output_directory, exist_ok=True)
    
    output_files = []
    for page_num in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        
        output_path = os.path.join(output_directory, f"page_{page_num + 1}.pdf")
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        output_files.append(output_path)
    
    return output_files

def split_pdf_chunks(input_path, pages_per_chunk):
    """Split PDF into chunks of specified size."""
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    output_files = []
    
    for chunk_start in range(0, total_pages, pages_per_chunk):
        writer = PdfWriter()
        chunk_end = min(chunk_start + pages_per_chunk, total_pages)
        
        for page_num in range(chunk_start, chunk_end):
            writer.add_page(reader.pages[page_num])
        
        output_path = f"chunk_{chunk_start//pages_per_chunk + 1}.pdf"
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        output_files.append(output_path)
    
    return output_files
