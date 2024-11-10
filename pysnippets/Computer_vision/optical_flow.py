import cv2
import numpy as np

def calculate_optical_flow(prev_frame, next_frame):
    # Convert frames to grayscale
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    next_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate optical flow using Farneback method
    flow = cv2.calcOpticalFlowFarneback(prev_gray, next_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    # Create visualization
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    
    # Create HSV image for visualization
    hsv = np.zeros_like(prev_frame)
    hsv[..., 1] = 255  # Saturation
    
    # Use angle for hue and magnitude for value
    hsv[..., 0] = angle * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    
    # Convert HSV to BGR for visualization
    flow_visualization = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return flow, flow_visualization
