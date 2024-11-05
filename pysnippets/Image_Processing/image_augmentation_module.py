import cv2
import numpy as np
from PIL import Image, ImageEnhance
import random

class ImageAugmentation:
    def __init__(self, image, seed=None):
        """
        Initialize with a PIL or OpenCV image.
        
        Parameters:
            image (PIL.Image or np.ndarray): The image to augment, in PIL format or as a NumPy array (BGR).
            seed (int, optional): Seed for random operations to ensure reproducibility.
        """
        if seed is not None:
            random.seed(seed)
        if isinstance(image, np.ndarray):
            self.image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        else:
            self.image = image

    def rotate(self, angle_range=(-30, 30)):
        """
        Rotate the image by a random angle within the specified range.
        
        Parameters:
            angle_range (tuple): Min and max angle for rotation.
            
        Returns:
            PIL.Image: The rotated image.
        """
        angle = random.uniform(*angle_range)
        return self.image.rotate(angle, resample=Image.BILINEAR)

    def flip(self, mode='horizontal'):
        """
        Flip the image horizontally or vertically.
        
        Parameters:
            mode (str): 'horizontal' or 'vertical' for flipping direction.
            
        Returns:
            PIL.Image: The flipped image.
        """
        if mode == 'horizontal':
            return self.image.transpose(Image.FLIP_LEFT_RIGHT)
        elif mode == 'vertical':
            return self.image.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise ValueError("Mode must be 'horizontal' or 'vertical'.")

    def scale(self, scale_factor=(0.8, 1.2)):
        """
        Scale the image by a random factor within the specified range.
        
        Parameters:
            scale_factor (tuple): Min and max scaling factor.
            
        Returns:
            PIL.Image: The scaled image.
        """
        factor = random.uniform(*scale_factor)
        w, h = self.image.size
        new_size = (int(w * factor), int(h * factor))
        return self.image.resize(new_size, Image.BILINEAR)

    def crop(self, crop_size=(100, 100)):
        """
        Crop the image to the specified size, randomly within the image bounds.
        
        Parameters:
            crop_size (tuple): The width and height of the crop.
            
        Returns:
            PIL.Image: The cropped image.
        """
        w, h = self.image.size
        if crop_size[0] > w or crop_size[1] > h:
            raise ValueError("Crop size must be smaller than the image dimensions.")
        left = random.randint(0, w - crop_size[0])
        top = random.randint(0, h - crop_size[1])
        return self.image.crop((left, top, left + crop_size[0], top + crop_size[1]))

    def adjust_color(self, brightness=1.0, contrast=1.0, saturation=1.0):
        """
        Adjust the brightness, contrast, and saturation of the image.
        
        Parameters:
            brightness (float): Brightness factor.
            contrast (float): Contrast factor.
            saturation (float): Saturation factor.
            
        Returns:
            PIL.Image: The color-adjusted image.
        """
        img = ImageEnhance.Brightness(self.image).enhance(brightness)
        img = ImageEnhance.Contrast(img).enhance(contrast)
        img = ImageEnhance.Color(img).enhance(saturation)
        return img

    def resize(self, size=(224, 224)):
        """
        Resize the image to the specified dimensions.
        
        Parameters:
            size (tuple): The target width and height.
            
        Returns:
            PIL.Image: The resized image.
        """
        return self.image.resize(size, Image.BILINEAR)

    def change_format(self, format='JPEG'):
        """
        Change the format of the image.
        
        Parameters:
            format (str): Desired format, e.g., 'JPEG' or 'PNG'.
            
        Returns:
            PIL.Image: The image with updated format.
        """
        img_copy = self.image.copy()
        img_copy.format = format
        return img_copy

    def normalize(self, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)):
        """
        Normalize the image pixel values using specified mean and standard deviation.
        
        Parameters:
            mean (tuple): Mean values for RGB channels.
            std (tuple): Standard deviation for RGB channels.
            
        Returns:
            PIL.Image: The normalized image.
        """
        img_array = np.array(self.image) / 255.0
        normalized_img = (img_array - mean) / std
        return Image.fromarray((normalized_img * 255).astype('uint8'))

    def to_numpy(self):
        """
        Convert the PIL image to a NumPy array.
        
        Returns:
            np.ndarray: Image as a NumPy array.
        """
        return np.array(self.image)

    def show(self):
        """
        Display the image.
        """
        self.image.show()

    def add_noise(self, noise_level=0.1):
        """
        Add random Gaussian noise to the image.
        
        Parameters:
            noise_level (float): Standard deviation of Gaussian noise.
            
        Returns:
            PIL.Image: The noisy image.
        """
        img_array = np.array(self.image)
        noise = np.random.normal(0, noise_level * 255, img_array.shape).astype('uint8')
        noisy_img = np.clip(img_array + noise, 0, 255).astype('uint8')
        return Image.fromarray(noisy_img)