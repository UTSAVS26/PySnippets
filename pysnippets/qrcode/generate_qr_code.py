
import qrcode

def generate_qr_code(data: str, file_path: str):
    """
    Generates a QR code for the provided data and saves it as an image file.

    Args:
        data (str): The data to encode into the QR code.
        file_path (str): The file path to save the generated QR code image.

    Example usage:
    generate_qr_code("https://www.example.com", "example_qr.png")
    """
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # size of each box
        border=4,  # thickness of the border
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)

if __name__ == "__main__":
    # Example usage
    generate_qr_code("https://www.example.com", "example_qr.png")
    print("QR code generated and saved as example_qr.png")
