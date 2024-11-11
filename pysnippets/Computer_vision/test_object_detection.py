import cv2
import numpy as np
from object_detection import detect_objects

# Dummy data: Create an image with random shapes
test_image = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.rectangle(test_image, (20, 20), (80, 80), (0, 255, 0), -1)  # Simulated object

# Detect objects in the image
detected_objects = detect_objects(test_image)

# Draw bounding boxes around detected objects
output_image = test_image.copy()
if detected_objects:
    for (x, y, w, h) in detected_objects:
        # Draw rectangle around detected object
        cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # Add label
        cv2.putText(output_image, 'Object', (x, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Display the original and detected objects
cv2.imshow('Original Image', test_image)
cv2.imshow('Object Detection', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()