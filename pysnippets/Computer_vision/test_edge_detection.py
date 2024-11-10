import cv2
import numpy as np
from edge_detection import detect_edges

# Load a real test image
test_image = cv2.imread('test_image.jpg')
if test_image is None:
    # If no image found, create dummy data
    test_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Convert to grayscale
gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using imported function
edges = detect_edges(blurred)

# Display original and edges side by side
cv2.imshow('Original', test_image)
cv2.imshow('Edges', edges)

# Wait for key press and close windows
key = cv2.waitKey(0)
if key == ord('q') or key == 27:  # Exit on 'q' or ESC
    cv2.destroyAllWindows()