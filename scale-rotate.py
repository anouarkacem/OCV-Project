import numpy as np 
import cv2

img = cv2.imread("./images/players.jpg", 1)

# Scale (0,0) refers to the absolute size, fx, fy => half img
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Scale (600,600) wanted dimensions
img_stretch = cv2.resize(img, (600, 600))

# Nearest interpolation mode instead of the default
img_stretch_near = cv2.resize(img, (600, 600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half", img_half)
cv2.imshow("Stretch", img_stretch)
cv2.imshow("Stretch_Near", img_stretch_near)


# Rotate from top left corner, -30 degress
M = cv2.getRotationMatrix2D((0, 0), -30, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("Rotated",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()