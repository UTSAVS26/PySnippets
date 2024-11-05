from image_augmentation_module import ImageAugmentation
import cv2
import os

# Load an image using OpenCV
image_path = r"Tests\image_processing\test_image.webp"
image = cv2.imread(image_path)

# Check if image was loaded successfully
if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Initialize the augmentation module
augmentor = ImageAugmentation(image)

# Apply various augmentations
rotated = augmentor.rotate()
flipped = augmentor.flip(mode='vertical')
scaled = augmentor.scale()
cropped = augmentor.crop((100, 100))
adjusted = augmentor.adjust_color(brightness=1.2, contrast=1.5, saturation=1.3)
resized = augmentor.resize((224, 224))
normalized = augmentor.normalize()

# Show each augmented image
rotated.show()
flipped.show()
scaled.show()
cropped.show()
adjusted.show()
resized.show()
normalized.show()

# Save the resized image in another format
output_dir = r"pysnippets\Image_Processing\processed_images"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'resized_image.png')

new_image = augmentor.change_format('PNG')
new_image.save(output_path)

print(f"Resized image saved to: {output_path}")