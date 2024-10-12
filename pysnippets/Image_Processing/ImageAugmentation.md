# ImageAugmentation

ImageAugmentation is a Python class that provides various image processing and augmentation techniques. It's designed to work with both PIL (Python Imaging Library) and OpenCV images, offering a range of operations to modify and enhance images for tasks such as data augmentation in machine learning projects.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Methods](#methods)
- [Examples](#examples)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

To use the ImageAugmentation class, make sure you have the required dependencies installed. You can install them using pip:

```
pip install opencv-python numpy pillow
```

Then, simply copy the `ImageAugmentation` class into your project.

## Usage

To use the ImageAugmentation class, first import it into your Python script:

```python
from image_augmentation import ImageAugmentation
```

Then, create an instance of the class with an image:

```python
# For a PIL Image
from PIL import Image
img = Image.open('path/to/your/image.jpg')
augmenter = ImageAugmentation(img)

# For an OpenCV image
import cv2
img = cv2.imread('path/to/your/image.jpg')
augmenter = ImageAugmentation(img)
```

## Methods

The ImageAugmentation class provides the following methods:

1. `rotate(angle_range=(-30, 30))`: Rotate the image by a random angle within the given range.
2. `flip(mode='horizontal')`: Flip the image horizontally or vertically.
3. `scale(scale_factor=(0.8, 1.2))`: Scale the image by a random factor within the given range.
4. `crop(crop_size=(100, 100))`: Crop the image to the given size.
5. `adjust_color(brightness=1.0, contrast=1.0, saturation=1.0)`: Adjust the brightness, contrast, and saturation of the image.
6. `resize(size=(224, 224))`: Resize the image to the given size.
7. `change_format(format='JPEG')`: Change the image format to the specified format.
8. `normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))`: Normalize the image pixel values using the given mean and standard deviation.
9. `to_numpy()`: Convert the PIL image to a NumPy array.
10. `show()`: Display the image.

## Examples

Here are some examples of how to use the ImageAugmentation class:

```python
from image_augmentation import ImageAugmentation
from PIL import Image

# Load an image
img = Image.open('example.jpg')
augmenter = ImageAugmentation(img)

# Rotate the image
rotated_img = augmenter.rotate((-45, 45))

# Flip the image horizontally
flipped_img = augmenter.flip('horizontal')

# Scale the image
scaled_img = augmenter.scale((0.5, 1.5))

# Crop the image
cropped_img = augmenter.crop((200, 200))

# Adjust color
adjusted_img = augmenter.adjust_color(brightness=1.2, contrast=1.1, saturation=1.1)

# Resize the image
resized_img = augmenter.resize((300, 300))

# Normalize the image
normalized_img = augmenter.normalize()

# Convert to NumPy array
img_array = augmenter.to_numpy()

# Display the original image
augmenter.show()
```

## Dependencies

- OpenCV (cv2)
- NumPy
- PIL (Python Imaging Library)

## License

[Specify your chosen license here]
