# How to use laptop webcam inside python 
# Step-1 Import Libraries
import cv2 as cv
import numpy as np 

# Step-2 Read camera frames  
cap = cv.VideoCapture(0) # Number of webcam can be given by this ()

# Step-3 Display the frame by frame
while(cap.isOpened()): # capture frame by frame
    ret, frame = cap.read()
    if ret == True:          # display frame 
        cv.imshow("Frame", frame)
        # to quit with q key
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

# Step-4 Close windwos easily
cap.realease()
cv.destroyAllWindows()

# Use Q for stoping webcam