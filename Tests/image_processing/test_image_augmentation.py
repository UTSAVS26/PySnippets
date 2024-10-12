import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import cv2
from pysnippets.Image_Processing.image_augmentation_module import ImageAugmentation

def test_augmentation():
    # Load the test image
    image = cv2.imread(r"Tests\image_processing\test_image.webp")
    if image is None:
        print("Error: Could not load the test image.")
        return

    # Initialize the augmentation module
    augmentor = ImageAugmentation(image)

    # Test rotation
    rotated = augmentor.rotate()
    rotated.show()
    rotated.save(r'Tests\image_processing\output/rotated_image.jpg')

    # Test flipping
    flipped = augmentor.flip(mode='horizontal')
    flipped.show()
    flipped.save(r'Tests\image_processing\output/flipped_image.jpg')

    # Test scaling
    scaled = augmentor.scale()
    scaled.show()
    scaled.save(r'Tests\image_processing\output/scaled_image.jpg')

    # Test cropping
    cropped = augmentor.crop((100, 100))
    cropped.show()
    cropped.save(r'Tests\image_processing\output/cropped_image.jpg')

    # Test color adjustments
    adjusted = augmentor.adjust_color(brightness=1.2, contrast=1.5, saturation=1.3)
    adjusted.show()
    adjusted.save(r'Tests\image_processing\output/adjusted_image.jpg')

    # Test resizing
    resized = augmentor.resize((224, 224))
    resized.show()
    resized.save(r'Tests\image_processing\output/resized_image.jpg')

    # Test format conversion
    png_image = augmentor.change_format('PNG')
    png_image.save(r'Tests\image_processing\output/converted_image.png')

    # Test normalization
    normalized = augmentor.normalize()
    normalized.show()
    normalized.save(r'Tests\image_processing\output\normalized_image.jpg')

    print("All augmentation functions executed successfully.")

if __name__ == "__main__":
    test_augmentation()
