from pypdf import PdfReader

def read_pdf(file_path):
    """Read and extract text from a PDF file."""
    reader = PdfReader(file_path)
    text_content = []
    
    for page in reader.pages:
        text_content.append(page.extract_text())
    
    return {
        'num_pages': len(reader.pages),
        'content': text_content
    }

def read_pdf_metadata(file_path):
    """Extract metadata from a PDF file."""
    reader = PdfReader(file_path)
    return {
        'author': reader.metadata.get('/Author', None),
        'creator': reader.metadata.get('/Creator', None),
        'producer': reader.metadata.get('/Producer', None),
        'subject': reader.metadata.get('/Subject', None),
        'title': reader.metadata.get('/Title', None)
    }