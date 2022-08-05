# Setting of camera or video
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
cap.set(10, 100) # 10 is a brightness 
cap.set(3, 640) # 3 is width key, can be adjusted 
cap.set(4, 480) # 4 is height key
# Good to be in between 640 and 480 if u want 

while (True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()