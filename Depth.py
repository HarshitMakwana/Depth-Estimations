import cv2
import numpy as np


class Depth:
    def __init__(self,left_image,right_image):
        self.left = left_image
        self.right = right_image
    
    def get(self):
        # Convert to grayscale
        left_gray = cv2.cvtColor(self.left, cv2.COLOR_BGR2GRAY)
        right_gray = cv2.cvtColor(self.right, cv2.COLOR_BGR2GRAY)

        # Compute disparity map
        window_size = 3
        min_disp = 0
        num_disp = 16 * 5
        stereo = cv2.StereoSGBM_create(minDisparity=min_disp,
                                        numDisparities=num_disp,
                                        blockSize=window_size,
                                        P1=8 * 3 * window_size ** 2,
                                        P2=32 * 3 * window_size ** 2,
                                        disp12MaxDiff=1,
                                        uniquenessRatio=10,
                                        speckleWindowSize=100,
                                        speckleRange=32)
        disparity = stereo.compute(left_gray, right_gray).astype(np.float32) / 16.0

        # Convert disparity map to depth map
        focal_length = 0.8  # Focal length of the camera
        baseline = 0.1  # Distance between the two cameras
        depth_map = np.zeros_like(left_gray)
        for i in range(depth_map.shape[0]):
            for j in range(depth_map.shape[1]):
                if disparity[i, j] > 0:
                    depth_map[i, j] = focal_length * baseline / disparity[i, j]

        # Normalize depth map for display
        depth_map_norm = cv2.normalize(depth_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        # Display depth map
        cv2.imshow('Depth Map', depth_map_norm)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



# Load images
left_img = cv2.imread('left_img.png')
right_img = cv2.imread('right_img.png')