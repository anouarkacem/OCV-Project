import numpy as np
import cv2

img = cv2.imread("./images/faces.jpeg", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "./classifiers/haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(path)

# ScaleFactor: faces close to the camera, minNeighbors: nearby object detection required, minSize: minimal size of a face before its detected
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40, 40))
print(len(faces))

# x, y, height, width variables
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()