import cv2
import numpy as np
from PIL import Image, ImageEnhance
import random

class ImageAugmentation:
    def __init__(self, image):
        """Initialize with a PIL or OpenCV image."""
        if isinstance(image, np.ndarray):
            self.image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        else:
            self.image = image

    def rotate(self, angle_range=(-30, 30)):
        """Rotate the image by a random angle within the given range."""
        angle = random.uniform(*angle_range)
        return self.image.rotate(angle, resample=Image.BILINEAR)

    def flip(self, mode='horizontal'):
        """Flip the image horizontally or vertically."""
        if mode == 'horizontal':
            return self.image.transpose(Image.FLIP_LEFT_RIGHT)
        elif mode == 'vertical':
            return self.image.transpose(Image.FLIP_TOP_BOTTOM)

    def scale(self, scale_factor=(0.8, 1.2)):
        """Scale the image by a random factor within the given range."""
        factor = random.uniform(*scale_factor)
        w, h = self.image.size
        new_size = (int(w * factor), int(h * factor))
        return self.image.resize(new_size, Image.BILINEAR)

    def crop(self, crop_size=(100, 100)):
        """Crop the image to the given size."""
        w, h = self.image.size
        left = random.randint(0, w - crop_size[0])
        top = random.randint(0, h - crop_size[1])
        right = left + crop_size[0]
        bottom = top + crop_size[1]
        return self.image.crop((left, top, right, bottom))

    def adjust_color(self, brightness=1.0, contrast=1.0, saturation=1.0):
        """Adjust the brightness, contrast, and saturation of the image."""
        img = ImageEnhance.Brightness(self.image).enhance(brightness)
        img = ImageEnhance.Contrast(img).enhance(contrast)
        img = ImageEnhance.Color(img).enhance(saturation)
        return img

    def resize(self, size=(224, 224)):
        """Resize the image to the given size."""
        return self.image.resize(size, Image.BILINEAR)

    def change_format(self, format='JPEG'):
        """Change the image format to the specified format."""
        img_copy = self.image.copy()
        img_copy.format = format
        return img_copy

    def normalize(self, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)):
        """Normalize the image pixel values using the given mean and std."""
        img_array = np.array(self.image) / 255.0
        normalized_img = (img_array - mean) / std
        return Image.fromarray((normalized_img * 255).astype('uint8'))

    def to_numpy(self):
        """Convert the PIL image to a NumPy array."""
        return np.array(self.image)

    def show(self):
        """Display the image."""
        self.image.show()
