from pypdf import PdfReader, PdfWriter

def rotate_pdf_pages(input_path, output_path, rotation):
    """Rotate all pages in a PDF by specified degrees."""
    if rotation % 90 != 0:
        raise ValueError("Rotation must be a multiple of 90 degrees.")
        
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        for page in reader.pages:
            page.rotate(rotation)
            writer.add_page(page)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def crop_pdf_pages(input_path, output_path, crop_box):
    """Crop all pages in a PDF using specified coordinates."""
    if len(crop_box) != 4 or not all(isinstance(coord, (int, float)) for coord in crop_box):
        raise ValueError("Crop box must be a tuple or list of four numeric values (left, bottom, right, top).")
    
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        for page in reader.pages:
            page.cropbox.left = crop_box[0]
            page.cropbox.bottom = crop_box[1]
            page.cropbox.right = crop_box[2]
            page.cropbox.top = crop_box[3]
            writer.add_page(page)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False