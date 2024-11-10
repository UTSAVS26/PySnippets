import cv2
import numpy as np

def detect_faces(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load the pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    return image, faces

def recognize_faces(image, face_recognizer=None, known_faces=None):
    if face_recognizer is None or known_faces is None:
        return None
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(image)[1]
    
    results = []
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(face_roi)
        results.append((label, confidence))
        
    return results

def train_face_recognizer(training_images, labels):
    """
    Train a face recognizer with labeled training images
    
    Args:
        training_images: List of training face images
        labels: List of corresponding labels for the training images
        
    Returns:
        Trained face recognizer model
    """
    # Create LBPH face recognizer
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    # Convert training images to grayscale
    training_data = []
    for img in training_images:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        training_data.append(gray)
    
    # Train the recognizer
    face_recognizer.train(training_data, np.array(labels))
    return face_recognizer

if __name__ == "__main__":
    # Load test image
    test_image = cv2.imread('test_image.jpg')
    if test_image is None:
        print("Error: Could not load test image")
        exit()
        
    # Detect faces
    result_image, detected_faces = detect_faces(test_image.copy())
    
    # Display results
    cv2.imshow('Detected Faces', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Example of face recognition (requires trained recognizer)
    # known_faces = load_known_faces()  # Load known face database
    # face_recognizer = train_face_recognizer(known_faces['images'], known_faces['labels'])
    # recognition_results = recognize_faces(test_image, face_recognizer, known_faces)
