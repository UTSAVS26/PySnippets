from PIL import Image  # Import the Python Imaging Library (PIL) to work with images

def image_to_ascii(image_path, new_width=100):
    # Characters to use for the ASCII art, ordered by brightness
    chars = "@%#*+=-:. "  # '@' is the darkest, ' ' (space) is the lightest

    # Open the image file from the given path
    img = Image.open(image_path)
    
    # Get the original dimensions of the image (width and height)
    width, height = img.size
    
    # Calculate the aspect ratio of the image (height/width)
    aspect_ratio = height / width
    
    # Calculate the new height based on the desired width, preserving the aspect ratio
    new_height = int(aspect_ratio * new_width)
    
    # Resize the image to the new dimensions and convert it to grayscale ('L' mode)
    # Grayscale simplifies the image to just brightness levels
    img = img.resize((new_width, new_height)).convert('L')
    
    # Get the pixel data from the grayscale image (each pixel has a brightness value 0-255)
    pixels = img.getdata()
    
    # Map each pixel to a character from 'chars' based on its brightness
    # Divide the pixel value by 32 (since 255/8 = ~32) to scale it into the 9-character range
    ascii_str = ''.join([chars[pixel // 32] for pixel in pixels])
    
    # Break the string into lines, each line representing a row of the image (with width = new_width)
    ascii_art = "\n".join([ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)])
    
    return ascii_art  # Return the final ASCII art string

print(image_to_ascii('path_to_image'))  # Replace 'path_to_image.jpg' with the path to your image
