from pypdf import PdfReader, PdfWriter
import os

def encrypt_pdf(input_path, output_path, user_password, owner_password):
    """Encrypt a PDF file with user and owner passwords."""
    if not os.path.isfile(input_path) or not input_path.lower().endswith('.pdf'):
        print(f"Invalid input file: {input_path}")
        return False
    
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        for page in reader.pages:
            writer.add_page(page)
        
        # Encrypt the PDF
        writer.encrypt(user_password=user_password, owner_password=owner_password, use_128bit=True)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        print("PDF encrypted successfully.")
        return True
    except Exception as e:
        print(f"Error encrypting PDF: {str(e)}")
        return False

def decrypt_pdf(input_path, output_path, password):
    """Decrypt a PDF file using the provided password."""
    if not os.path.isfile(input_path) or not input_path.lower().endswith('.pdf'):
        print(f"Invalid input file: {input_path}")
        return False
    
    try:
        reader = PdfReader(input_path)
        
        # Check if the PDF is encrypted
        if reader.is_encrypted:
            try:
                if reader.decrypt(password) != 1:
                    print("Incorrect password. Decryption failed.")
                    return False
            except Exception as e:
                print(f"Decryption failed: {str(e)}")
                return False
        else:
            print("PDF is not encrypted.")
            return False
        
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        print("PDF decrypted successfully.")
        return True
    except Exception as e:
        print(f"Error decrypting PDF: {str(e)}")
        return False