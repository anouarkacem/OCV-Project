import numpy as np
import cv2

# 1 default colors & channels for the current image, 0 is black and white image
img = cv2.imread("./images/opencv-logo.png", 1) 

# Prints array of pixels of the current image
print(img)

# Prints the type of the image
print(type(img))

# Prints length of the current image (number of rows)
print(len(img))

# Prints values (vertical columns) of the top row
print(len(img[0]))

# Prints Number of channels found in the image
print(len(img[0][0]))

# 1V : Horizantal Rows, 2V: Columns, 3V: Number of channels
print(img.shape)

# Type of the image
print(img.dtype)

# Access pixel of 10th row, 5th column => result : pixel values
print(img[10, 5])

# Access the first channel
print(img[:, :, 0])

# Total number of pixels
print(img.size)




