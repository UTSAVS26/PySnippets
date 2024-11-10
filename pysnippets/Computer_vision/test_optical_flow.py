import cv2
from optical_flow import calculate_optical_flow

def test_optical_flow():
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    # Read first frame
    ret, prev_frame = cap.read()
    if not ret:
        print("Error reading video stream")
        return
    
    # Convert first frame to grayscale
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        
    while True:
        # Read next frame
        ret, next_frame = cap.read()
        if not ret:
            break
            
        # Convert to grayscale
        next_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)
            
        # Calculate optical flow
        flow, flow_vis = calculate_optical_flow(prev_gray, next_gray)
        
        # Draw flow vectors on original frame
        magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        mask = magnitude > 1  # Filter out small movements
        
        # Draw arrows for significant motion
        step = 16  # Sample every 16 pixels
        for y in range(0, flow.shape[0], step):
            for x in range(0, flow.shape[1], step):
                if mask[y, x]:
                    fx, fy = flow[y, x]
                    cv2.arrowedLine(next_frame, 
                                  (x, y),
                                  (int(x + fx), int(y + fy)),
                                  (0, 255, 0),
                                  2)
        
        # Display results
        cv2.imshow('Original with Flow', next_frame)
        cv2.imshow('Optical Flow Visualization', flow_vis)
        
        # Update previous frame
        prev_gray = next_gray.copy()
        
        # Break on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_optical_flow()