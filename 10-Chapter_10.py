# Converting webcam video into different colors; black & white and gray
from tkinter import Frame
import cv2 as cv
import numpy as np 
cap = cv.VideoCapture(0)
while(True):
    (ret, frame) = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY) # if you want to make your video in black and white
    cv.imshow("OriginalCam", frame)
    cv.imshow("GrayCam", gray_frame)
    cv.imshow("BinaryCam", binary)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv.destroyAllWindows()