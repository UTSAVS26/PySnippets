from pypdf import PdfReader, PdfWriter
import os

def split_pdf(input_path, output_directory):
    """Split PDF into individual pages."""
    if not os.path.isfile(input_path) or not input_path.lower().endswith('.pdf'):
        print(f"Invalid input file: {input_path}")
        return []
    
    os.makedirs(output_directory, exist_ok=True)
    output_files = []
    try:
        reader = PdfReader(input_path)
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        
        for page_num in range(len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            
            output_path = os.path.join(output_directory, f"{base_name}_page_{page_num + 1}.pdf")
            with open(output_path, "wb") as output_file:
                writer.write(output_file)
            output_files.append(output_path)
        
        print(f"PDF split into individual pages successfully. Files saved to {output_directory}")
        return output_files
    except Exception as e:
        print(f"Error splitting PDF: {str(e)}")
        return []

def split_pdf_chunks(input_path, pages_per_chunk, output_directory):
    """Split PDF into chunks of specified size."""
    if not os.path.isfile(input_path) or not input_path.lower().endswith('.pdf'):
        print(f"Invalid input file: {input_path}")
        return []
    
    if pages_per_chunk <= 0:
        print("Pages per chunk must be a positive integer.")
        return []
    
    os.makedirs(output_directory, exist_ok=True)
    output_files = []
    try:
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        
        for chunk_start in range(0, total_pages, pages_per_chunk):
            writer = PdfWriter()
            chunk_end = min(chunk_start + pages_per_chunk, total_pages)
            
            for page_num in range(chunk_start, chunk_end):
                writer.add_page(reader.pages[page_num])
            
            chunk_index = chunk_start // pages_per_chunk + 1
            output_path = os.path.join(output_directory, f"{base_name}_chunk_{chunk_index}.pdf")
            with open(output_path, "wb") as output_file:
                writer.write(output_file)
            output_files.append(output_path)
        
        print(f"PDF split into chunks of {pages_per_chunk} pages successfully. Files saved to {output_directory}")
        return output_files
    except Exception as e:
        print(f"Error splitting PDF into chunks: {str(e)}")
        return []