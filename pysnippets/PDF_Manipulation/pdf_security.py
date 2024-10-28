from pypdf import PdfReader, PdfWriter

def encrypt_pdf(input_path, output_path, user_password, owner_password):
    """Encrypt a PDF file with user and owner passwords."""
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    writer.encrypt(user_password=user_password,
                  owner_password=owner_password,
                  use_128bit=True)
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    return True

def decrypt_pdf(input_path, output_path, password):
    """Decrypt a PDF file using the provided password."""
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    if reader.is_encrypted:
        try:
            reader.decrypt(password)
        except Exception as e:
            print(f"Decryption failed: {str(e)}")
            return False
    
    for page in reader.pages:
        writer.add_page(page)
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    return True