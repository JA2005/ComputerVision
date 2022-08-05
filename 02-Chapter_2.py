# Here in this section, I will use code to resize an image 
# import library 
import cv2 as cv

# Read image, just to read as I will not see image with this command
img = cv.imread("resources/image.jpg") 

# I am using "img" for resizing, so I will name the resized img as img1
img1 = cv.resize(img, (800, 600))  # to resize image 

# Now I want to see both the images, the old one and the resized one
cv.imshow("First Image", img) # Just a blink, image didnt stay
cv.imshow("Second Image", img1)

# I want image to stay for a specifed time, as I mentioned in Chapter_01
cv.waitKey(0) # Image will display forever, time can be changed as mentioned previously 
cv.destroyAllWindows() # This command is used to close all the windows