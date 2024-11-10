import cv2
import numpy as np

def detect_edges(image):
    """
    Detect edges in an input image using multiple edge detection methods.
    
    Args:
        image: Input image in BGR format
        
    Returns:
        edges_combined: Combined edge detection result
    """
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Canny edge detection
    edges_canny = cv2.Canny(blurred, 100, 200)
    
    # Sobel edge detection
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    edges_sobel = np.sqrt(sobelx**2 + sobely**2)
    edges_sobel = np.uint8(edges_sobel)
    
    # Laplacian edge detection
    edges_laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
    edges_laplacian = np.uint8(np.absolute(edges_laplacian))
    
    # Combine all edge detection results
    edges_combined = cv2.bitwise_or(edges_canny, edges_sobel)
    edges_combined = cv2.bitwise_or(edges_combined, edges_laplacian)
    
    # Apply threshold to get cleaner edges
    _, edges_combined = cv2.threshold(edges_combined, 50, 255, cv2.THRESH_BINARY)
    
    return edges_combined
