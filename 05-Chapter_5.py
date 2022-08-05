# Saving and writing an image 
import cv2 as cv
from cv2 import imwrite
img = cv.imread("resources/image.jpg") 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)   
binary = cv.resize(binary, (500, 500))
imwrite('resources/Image_gray.png', gray)
imwrite('resources/Image_bw.png', binary)
cv.waitKey(0) 
cv.destroyAllWindows() 