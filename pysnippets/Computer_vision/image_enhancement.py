import cv2
import numpy as np

def enhance_image(image):
    # Input validation
    if image is None or len(image.shape) != 3:
        raise ValueError("Invalid input image")

    # Convert to YUV color space
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    
    # Enhance the luminance channel
    yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
    
    # Apply Gaussian blur to reduce noise
    yuv[:,:,0] = cv2.GaussianBlur(yuv[:,:,0], (3,3), 0)
    
    # Enhance contrast
    yuv[:,:,0] = cv2.convertScaleAbs(yuv[:,:,0], alpha=1.2, beta=5)
    
    # Convert back to BGR color space
    enhanced_image = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    
    # Apply sharpening
    kernel = np.array([[-1,-1,-1],
                      [-1, 9,-1],
                      [-1,-1,-1]])
    enhanced_image = cv2.filter2D(enhanced_image, -1, kernel)
    
    # Ensure output is in valid range
    enhanced_image = np.clip(enhanced_image, 0, 255)
    enhanced_image = enhanced_image.astype(np.uint8)
    
    return enhanced_image