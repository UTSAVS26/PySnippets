import cv2

def track_object_in_video(video_path):
    # Initialize video capture
    cap = cv2.VideoCapture(video_path)
    
    # Read first frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to read video")
        return
    
    # Select ROI (Region of Interest)
    roi = cv2.selectROI(frame)
    
    # Initialize tracker
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, roi)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Update tracker
        success, box = tracker.update(frame)
        
        if success:
            # Draw bounding box
            x, y, w, h = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display result
        cv2.imshow('Tracking', frame)
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example usage
    video_file = "sample_video.mp4"  # Replace with your video file
    track_object_in_video(video_file)
