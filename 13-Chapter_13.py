# Some additional functions  
import cv2 as cv
import numpy as np
img = cv.imread("resources/image.jpg")

# How to resize image
resized_img = cv.resize(img, (450, 250)) # 1st width, # 2nd hight

# How to convert original image into gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# How to make blurred image 
blurr_img = cv.GaussianBlur(img, (7, 7), 0) # 7,7 kernal size (intensity, always odd) , always odd value

# How to detect edges
edge_img = cv.Canny(img, 48, 48)

# How to set thickness of lines 
mat_kernel = np.ones((7, 7), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernel), iterations=1) # iteration means in simoe word as coating

# How to make outline thiner  
ero_img = cv.erode(dilated_img, mat_kernel, iterations=1)

cv.imshow("Original", img)
cv.imshow("Resized", resized_img)
cv.imshow("Gray", gray_img)
cv.imshow("Blurr", blurr_img)
cv.imshow("Edge", edge_img)
cv.imshow("Dilated", dilated_img)
cv.imshow("Erosion", ero_img)

cv.waitKey(0)
cv.destroyAllWindows()