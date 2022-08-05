# This section explains how to read and display image, it is important to make a folder with all the pictures or videos
# I have all my pictures in resources folder, which is a subfolder in the folder OpenCV
# The first step will be to import library which is cv2
import cv2 as cv

# Now I am going to read an image
# This line of code will only read an image 
img = cv.imread("resources/image_grey.png") 

# This line of code will show the image
cv.imshow("first image", img) # With this line, image will just blink but will not stay

# Now I want the image display for a particular time period for instance, (5000) image will stay for 5 seconds
# or I want the image to stay forever, then I can use (0) in a code below
cv.waitKey(5000) 