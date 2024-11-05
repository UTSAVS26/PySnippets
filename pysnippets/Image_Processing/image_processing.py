from PIL import Image, ImageFilter

def resize(image_path, output_path, size):
    """
    Resizes the image to the specified size.
    """
    with Image.open(image_path) as img:
        img = img.resize(size, Image.ANTIALIAS)  # Use ANTIALIAS for better quality
        img.save(output_path)

def filter_image(image_path, output_path, filter_type):
    """
    Applies a filter to the image and saves it.
    """
    with Image.open(image_path) as img:
        if filter_type == 'BLUR':
            img = img.filter(ImageFilter.BLUR)
        elif filter_type == 'CONTOUR':
            img = img.filter(ImageFilter.CONTOUR)
        img.save(output_path)

def rotate(image_path, output_path, angle):
    """
    Rotates the image by the specified angle.
    """
    with Image.open(image_path) as img:
        img = img.rotate(angle, expand=True)  # Expand to fit the new size
        img.save(output_path) 