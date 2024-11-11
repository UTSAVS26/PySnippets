import cv2
import matplotlib.pyplot as plt
from depth_estimation import estimate_depth

def test_depth_estimation():
    # Load stereo image pair
    left_img = cv2.imread('data/left.jpg')
    right_img = cv2.imread('data/right.jpg')
    
    # Convert to grayscale
    left_gray = cv2.cvtColor(left_img, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_img, cv2.COLOR_BGR2GRAY)
    
    # Estimate depth map
    depth_map = estimate_depth(left_gray, right_gray)
    
    # Visualize results
    plt.figure(figsize=(12,5))
    
    plt.subplot(131)
    plt.imshow(left_img[...,::-1])
    plt.title('Left Image')
    plt.axis('off')
    
    plt.subplot(132) 
    plt.imshow(right_img[...,::-1])
    plt.title('Right Image')
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(depth_map, cmap='plasma')
    plt.title('Estimated Depth Map')
    plt.colorbar()
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test_depth_estimation()