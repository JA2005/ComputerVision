# In this section, we will see how to draw lines and shapes in python 
import cv2 as cv
import numpy as np # for dimensions which comes through numpy library

# First draw a canvas, np.zeros is for black and np.ones is for white 
img = np.zeros((600,600))
img1 = np.ones((600,600))

# print size
print("The size of our canvas is: ", img.shape) # This statment will give the dimensions of the image

# We can also add colors to the canvas 
colored_img = np.zeros((600,600, 3), np.uint8)
colored_img[:] = 255,0,255  # coloring complete image

# We can also color parts of the image
colored_img[150:230,100:207] = 255,169,10 # 255, 169, 10 is the colour keys

# We can also add lines
cv.line(colored_img, (0,0), (600,600), (255,0,0), 3) # A short line can be added  
#cv.line(colored_img, (0,0), (colored_img.shape[0], colored_img.shape[1]), (255,0,0), 3) # crossed line

# How to add rectangle shape
cv.rectangle(colored_img, (50,100), (300, 400), (255,255,255), 3) # if instead of 3, I use cv.FILLED), it will color rectangle
cv.putText(colored_img,"Python",(200,500), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255,2), 2)
cv.imshow("Black", img)
cv.imshow("White", img1)
cv.imshow("Colored", colored_img)

cv.waitKey(0)
cv.destroyAllWindows()
