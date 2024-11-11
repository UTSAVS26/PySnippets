import qrcode
from typing import Optional

def generate_qr_code(
    data: str,
    file_path: str,
    error_correction: Optional[str] = "L",
    fill_color: str = "black",
    back_color: str = "white"
):
    """
    Generates a QR code for the provided data and saves it as an image file.

    Args:
        data (str): The data to encode into the QR code.
        file_path (str): The file path to save the generated QR code image.
        error_correction (Optional[str]): Error correction level - one of 'L', 'M', 'Q', 'H'.
        fill_color (str): The color to fill the QR code. Default is 'black'.
        back_color (str): The background color of the QR code. Default is 'white'.

    Example usage:
    generate_qr_code("https://www.example.com", "example_qr.png", error_correction="H", fill_color="blue", back_color="yellow")
    """
    
    # Map user-friendly error correction levels to qrcode.constants
    error_correction_levels = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }
    
    # Set the error correction level, defaulting to 'L' if an invalid option is provided
    correction = error_correction_levels.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_L)
    
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=correction,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image of the QR code with specified colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the image
    img.save(file_path)
    print(f"QR code generated and saved as {file_path}")

if __name__ == "__main__":
    # Example usage with custom options
    generate_qr_code(
        "https://www.example.com",
        "example_qr.png",
        error_correction="H",
        fill_color="blue",
        back_color="yellow"
    )