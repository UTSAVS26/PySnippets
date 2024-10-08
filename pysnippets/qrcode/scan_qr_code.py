# scan_qr_code.py

import cv2
from pyzbar.pyzbar import decode

def scan_qr_code(image_path: str):
    """
    Scans a QR code from the provided image file and returns the decoded data.

    Args:
        image_path (str): The file path of the image containing the QR code.

    Returns:
        str: The decoded data from the QR code, or None if no QR code is found.

    Example usage:
    scan_qr_code("example_qr.png") -> "https://www.example.com"
    """
    img = cv2.imread(image_path)
    qr_codes = decode(img)

    if qr_codes:
        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')
            print(f"QR Code data: {qr_data}")
            return qr_data
    else:
        print("No QR code found")
        return None

if __name__ == "__main__":
    # Example usage
    scan_qr_code("example_qr.png")
