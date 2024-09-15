# Stereo Depth Map Generation

This project demonstrates how to generate a depth map from a pair of stereo images using Python's OpenCV and NumPy libraries. The depth map provides an estimation of the distance of objects from the camera by calculating disparities between two stereo images (left and right).

## Overview

The core of this project is a Python class `Depth`, which takes two stereo images (left and right) as input and generates a depth map using block matching via the `cv2.StereoSGBM_create` function. The depth map is then normalized and displayed to visually represent the depth information of the scene.

### Features

- Converts stereo images to grayscale for depth map computation.
- Uses Semi-Global Block Matching (SGBM) algorithm to compute the disparity map.
- Converts the disparity map into a depth map by considering the camera's focal length and baseline distance.
- Visualizes the resulting depth map.

## Demo

### Input Images (Left and Right)

![Left Image](data/L1.jpg) ![Right Image](data/R1.jpg)

### Depth Map (After Processing)
![Right Image](mh1.png)
The result will be a Heatmap color nearest object with yellowes color. while, Faarer object in darker red.

## Installation

To run this project, you need the following dependencies:

```bash
pip install opencv-python numpy
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/stereo-depth-map.git
   cd stereo-depth-map
   ```

2. Prepare your stereo images (`left_img.png` and `right_img.png`) and place them in the project directory.

3. Run the script:

   ```bash
   python depth_map.py
   ```

   The depth map will be displayed in a new window.

## Code Explanation

The main logic is implemented in the `Depth` class. Here's how it works:

1. **Input**: The left and right stereo images are loaded.
2. **Grayscale Conversion**: Both images are converted to grayscale.
3. **Disparity Map Calculation**: Using the `cv2.StereoSGBM_create` method, a disparity map is computed.
4. **Depth Map Calculation**: The disparity map is converted to a depth map using the formula:  
   \[
   \text{{depth}} = \frac{{\text{{focal\_length}} \times \text{{baseline}}}}{{\text{{disparity}}}}
   \]
5. **Normalization and Display**: The depth map is normalized for better visualization and displayed using OpenCV's `imshow`.

## Example

```python
import cv2
import numpy as np
from depth_map import Depth

# Load images
left_img = cv2.imread('left_img.png')
right_img = cv2.imread('right_img.png')

# Generate and display depth map
depth = Depth(left_img, right_img)
depth.get()
```
---

Make sure to replace the links for the images and include `depth_map.py` in the project folder for a complete set
