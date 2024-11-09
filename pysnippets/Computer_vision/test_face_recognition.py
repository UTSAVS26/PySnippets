import cv2
import numpy as np
import os

def recognize_faces(image, cascade_path):
    # Check if cascade file exists
    if not os.path.exists(cascade_path):
        raise FileNotFoundError(f"Cascade file not found at {cascade_path}")
    
    # Create a copy of the image to draw on
    output_image = image.copy()
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load the face cascade classifier
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(output_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    return output_image

# Create test image with a simple face-like pattern
test_image = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.rectangle(test_image, (30, 30), (70, 70), (255, 255, 255), -1)  # Face
cv2.rectangle(test_image, (45, 40), (55, 50), (0, 0, 0), -1)  # Eyes
cv2.rectangle(test_image, (40, 60), (60, 65), (0, 0, 0), -1)  # Mouth

# Process the image with face recognition
cascade_path = 'haarcascade_frontalface_default.xml'
recognized_image = recognize_faces(test_image, cascade_path)

# Display the image
cv2.imshow('Face Recognition', recognized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()