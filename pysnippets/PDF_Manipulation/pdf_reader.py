from pypdf import PdfReader

def read_pdf(file_path):
    """Read and extract text from a PDF file."""
    reader = PdfReader(file_path)
    text_content = [page.extract_text() for page in reader.pages]
    
    return {
        'num_pages': len(reader.pages),
        'content': text_content
    }

def read_pdf_metadata(file_path):
    """Extract metadata from a PDF file."""
    reader = PdfReader(file_path)
    return {key: reader.metadata.get(key, None) for key in ['/Author', '/Creator', '/Producer', '/Subject', '/Title']}