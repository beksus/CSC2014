# -*- coding: utf-8 -*-
"""
Created on Wed May 21 08:48:48 2025

@author: Beksultan
"""

import cv2
import numpy as np

# Step 1: Read the grayscale image
img = cv2.imread("cameraman.bmp", 0)

# Step 2: Get the shape and modify top-left quadrant
height, width = img.shape
img[0:height//2, 0:width//2] = 0  # Set top-left quadrant to black

# Step 3: Display the modified image
cv2.imshow("Modified Cameraman", img)

# Step 4: Wait for key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 5: Save the modified image
cv2.imwrite("new_image.png", img)
