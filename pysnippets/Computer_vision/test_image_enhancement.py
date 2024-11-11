import cv2
from image_enhancement import enhance_image
import numpy as np

# Dummy data: Create a blank image with a dark rectangle
test_image = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.rectangle(test_image, (25, 25), (75, 75), (0, 0, 100), -1)

# Add some noise to make the image more realistic
noise = np.random.normal(0, 25, test_image.shape).astype(np.uint8)
test_image = cv2.add(test_image, noise)

# Apply image enhancement
enhanced_image = enhance_image(test_image)

# Add text labels
cv2.putText(test_image, 'Original', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(enhanced_image, 'Enhanced', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

# Display the images side by side
combined_image = np.hstack((test_image, enhanced_image))
cv2.imshow('Image Enhancement Comparison', combined_image)

# Save the results
cv2.imwrite('original_image.jpg', test_image)
cv2.imwrite('enhanced_image.jpg', enhanced_image)
cv2.imwrite('comparison.jpg', combined_image)

# Wait for key press and cleanup
key = cv2.waitKey(0)
cv2.destroyAllWindows()

# Print basic image statistics
print("Original Image Statistics:")
print(f"Mean pixel value: {np.mean(test_image):.2f}")
print(f"Standard deviation: {np.std(test_image):.2f}")
print("\nEnhanced Image Statistics:")
print(f"Mean pixel value: {np.mean(enhanced_image):.2f}")
print(f"Standard deviation: {np.std(enhanced_image):.2f}")