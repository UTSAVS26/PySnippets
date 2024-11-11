import unittest
from image_processing import resize, filter_image, rotate

class TestImageProcessing(unittest.TestCase):
    def test_resize(self):
        resize('input_image.jpg', 'output_image_resized.jpg', (100, 100))
        # Add assertions to check if the output image is as expected

    def test_filter_image(self):
        filter_image('input_image.jpg', 'output_image_filtered.jpg', 'BLUR')
        # Add assertions to check if the output image is as expected

    def test_rotate(self):
        rotate('input_image.jpg', 'output_image_rotated.jpg', 90)
        # Add assertions to check if the output image is as expected

if __name__ == "__main__":
    unittest.main() 