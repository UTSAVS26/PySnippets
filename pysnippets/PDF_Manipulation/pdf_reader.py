from pypdf import PdfReader
import os

def read_pdf(file_path):
    """Read and extract text from a PDF file."""
    if not os.path.isfile(file_path) or not file_path.lower().endswith('.pdf'):
        print(f"Invalid file path: {file_path}")
        return None

    try:
        reader = PdfReader(file_path)
        text_content = []

        for page in reader.pages:
            page_text = page.extract_text()
            text_content.append(page_text if page_text else "[No extractable text]")

        return {
            'num_pages': len(reader.pages),
            'content': text_content
        }
    except Exception as e:
        print(f"Error reading PDF: {str(e)}")
        return None

def read_pdf_metadata(file_path):
    """Extract metadata from a PDF file."""
    if not os.path.isfile(file_path) or not file_path.lower().endswith('.pdf'):
        print(f"Invalid file path: {file_path}")
        return None

    try:
        reader = PdfReader(file_path)
        metadata_keys = ['/Author', '/Creator', '/Producer', '/Subject', '/Title']
        
        # Use .get() directly on metadata to simplify handling missing values
        metadata = {key: reader.metadata.get(key, "Unknown") for key in metadata_keys}
        return metadata
    except Exception as e:
        print(f"Error reading PDF metadata: {str(e)}")
        return None