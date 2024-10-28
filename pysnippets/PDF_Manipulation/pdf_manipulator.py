from pypdf import PdfReader, PdfWriter

def rotate_pdf_pages(input_path, output_path, rotation):
    """Rotate all pages in a PDF by specified degrees."""
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        page.rotate(rotation)
        writer.add_page(page)
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    return True

def crop_pdf_pages(input_path, output_path, crop_box):
    """Crop all pages in a PDF using specified coordinates."""
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
