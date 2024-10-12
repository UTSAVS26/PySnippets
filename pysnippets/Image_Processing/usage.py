from image_augmentation_module import ImageAugmentation
import cv2

# Load an image using OpenCV
image = cv2.imread(r"Tests\image_processing\test_image.webp")

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

# Show the augmented image
adjusted.show()

# Save the resized image to another format
new_image = augmentor.change_format('PNG')
new_image.save('pysnippets\Image_Processing\processed_images/resized_image.png')
