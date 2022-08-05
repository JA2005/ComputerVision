# How to change the resolution of webcam
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0) # cap is for capture, (0) is for webcam

# How to set resolution to HD (1280*720)
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
    hd_resolution()

#  How to set resolution to SD
def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)
sd_resolution()
 
# This is for Full HD 
def fhd_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)
fhd_resolution()

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Camer", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()