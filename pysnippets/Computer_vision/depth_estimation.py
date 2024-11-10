import cv2
import matplotlib.pyplot as plt

def depth_estimation(left_img, right_img):
    """
    Estimate depth map from stereo images using Semi-Global Block Matching
    
    Args:
        left_img: Left stereo image
        right_img: Right stereo image
        
    Returns:
        Depth map
    """
    # Convert images to grayscale
    left_gray = cv2.cvtColor(left_img, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_img, cv2.COLOR_BGR2GRAY)
    
    # Create stereo matcher object
    stereo = cv2.StereoSGBM_create(
        minDisparity=0,
        numDisparities=16*16,
        blockSize=11,
        P1=8 * 3 * 11**2,
        P2=32 * 3 * 11**2,
        disp12MaxDiff=1,
        uniquenessRatio=10,
        speckleWindowSize=100,
        speckleRange=32
    )
    
    # Compute disparity map
    disparity = stereo.compute(left_gray, right_gray)
    
    # Normalize disparity map for visualization
    disparity_normalized = cv2.normalize(disparity, None, alpha=0, beta=255,
                                       norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    return disparity_normalized

if __name__ == "__main__":
    # Load stereo images
    left_img = cv2.imread('left_image.jpg')
    right_img = cv2.imread('right_image.jpg')
    
    if left_img is None or right_img is None:
        print("Error: Could not load images")
        exit()
        
    # Get depth map
    depth_map = depth_estimation(left_img, right_img)
    
    # Display results
    plt.figure(figsize=(12, 5))
    
    plt.subplot(131)
    plt.imshow(cv2.cvtColor(left_img, cv2.COLOR_BGR2RGB))
    plt.title('Left Image')
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(cv2.cvtColor(right_img, cv2.COLOR_BGR2RGB))
    plt.title('Right Image')
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(depth_map, cmap='hot')
    plt.title('Depth Map')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
