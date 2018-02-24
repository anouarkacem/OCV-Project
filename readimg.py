import numpy as np
import cv2

# Read Image
img = cv2.imread("./images/opencv-logo.png")

# Initialize a window
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# Show Image on the window
cv2.imshow("Image", img)