import cv2
import numpy as np
from image_segmentation import segment_image

# Create test image with two distinct areas
test_image = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.rectangle(test_image, (25, 25), (75, 75), (255, 255, 255), -1)

# Add some noise to make it more realistic
noise = np.random.normal(0, 25, test_image.shape).astype(np.uint8)
test_image = cv2.add(test_image, noise)

# Save original image
cv2.imwrite('original.jpg', test_image)

# Perform segmentation
segmented_image = segment_image(test_image)

# Display original and segmented images side by side
combined = np.hstack((test_image, segmented_image))
cv2.imshow('Original | Segmented', combined)
cv2.imwrite('segmented.jpg', segmented_image)

# Wait for key press and close windows
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()