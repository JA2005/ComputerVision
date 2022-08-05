# How to convert an image into Black and white 
import cv2 as cv
img = cv.imread("resources/image.jpg") 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)   
cv.imshow('original', img) # "original" is the name of the window, second is image
cv.imshow('gray', gray) 
cv.imshow('Black and white', binary)
cv.waitKey(0) 
cv.destroyAllWindows() 