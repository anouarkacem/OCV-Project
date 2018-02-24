import numpy as np 
import cv2

img = cv2.imread("./images/thresh.jpg")

cv2.imshow("Original", img)

# Gaussian Blur filter (5, 55) blur values in each axis (x, y)
blur = cv2.GaussianBlur(img, (5, 55), 0)
cv2.imshow("Blur", blur)

# A Black Square
kernel = np.ones((5,5), "uint8")

# Dilate filter
dilate = cv2.dilate(img, kernel, iterations=1)

# Erode Filter
erode = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Dilate", dilate)
cv2.imshow("Erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()