# How to join two images (This code is for similar images)
import cv2 as cv
import numpy as np
img = cv.imread("resources/image.jpg")

# Image can be stacked
# Horizontally 
hor_img = np.hstack((img, img))

# and vertically 
ver_img = np.vstack((img, img))
cv.imshow("vertical", ver_img)
cv.imshow("Horizontal", hor_img)

cv.waitKey(0)
cv.destroyAllWindows()