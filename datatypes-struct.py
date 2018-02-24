import numpy as np 
import cv2

# Black Image : 150px Height, 200px Width, 1 Channel, uint8 type of image (0-256 values)
black = np.zeros([150, 200, 1], 'uint8')

cv2.imshow("Black", black)

# : print all values in that pixel location
print(black[0, 0, :])

# Another Black Image
ones = np.ones([150, 200, 3], 'uint8')

cv2.imshow("Ones", ones)
print(ones[0, 0, :])

# White Image, 16 bit length image
white = np.ones([150, 200, 3], 'uint16')

# Maximize all values to make it white
white *= (2**16-1)

cv2.imshow("White", white)
print(white[0, 0, :])

# Copy the ones image matrix
color = ones.copy()

# : all pixels, Assign Color to all pixels in color matrix (BGR format, blue pixels)
color[:, :] = (255, 0, 0)

cv2.imshow("Blue", color)
print(color[0, 0, :])

# Waits for interaction from user and closes the images windows
cv2.waitKey(0)
cv2.destroyAllWindows()