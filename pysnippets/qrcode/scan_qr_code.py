# scan_qr_code.py

import cv2
from pyzbar.pyzbar import decode
from typing import List, Optional

def scan_qr_code(image_path: str) -> Optional[List[str]]:
    """
    Scans QR codes from the provided image file and returns the decoded data.

    Args:
        image_path (str): The file path of the image containing the QR code(s).

    Returns:
        Optional[List[str]]: A list of decoded data from the QR code(s), or None if no QR codes are found.

    Example usage:
    scan_qr_code("example_qr.png") -> ["https://www.example.com"]
    """
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        return None

    qr_codes = decode(img)

    if qr_codes:
        decoded_data = []
        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')
            decoded_data.append(qr_data)
            print(f"QR Code data: {qr_data}")
        return decoded_data
    else:
        print("No QR code found")
        return None

if __name__ == "__main__":
    # Example usage
    scan_qr_code("example_qr.png")
