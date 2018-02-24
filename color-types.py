import numpy as np
import cv2

color = cv2.imread("./images/butterfly.jpg", 1)
cv2.imshow("Image", color)

# TOP LEFT CORNER Window
cv2.moveWindow("Image", 0, 0)

print(color.shape)
height, width, channels = color.shape

# Split channel into each of its components
b, g, r = cv2.split(color)

# Create uninitialized array matrix
rgb_split = np.empty([height, width*3, 3], "uint8")

# Split the image into b, g, r sepertate images
rgb_split[:, 0:width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])

cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

# convert from BGR to HSV
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

# axis=1; Make images side by side
hsv_split = np.concatenate((h, s, v), axis=1)

cv2.imshow("Split_hsv", hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()