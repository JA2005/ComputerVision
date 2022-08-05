# How to convert normal image into grey scale
# import library
import cv2 as cv
from cv2 import cvtColor
img = cv.imread("resources/image.jpg") 
img = cv.resize(img, (800, 600))  # to resize image 

# How to convert image into grey
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY) # BGR TO Grey

# Display code
cv.imshow("First Image", img) 
cv.imshow("Grey Image", gray_img)


# delay code
cv.waitKey(0) 
cv.destroyAllWindows() 