# How to save HD recording of webcam 
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

# Setting resolution to HD (1280*720)
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
hd_resolution()

# for SD
def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)
sd_resolution()
 
# for Full HD 
def fhd_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)
fhd_resolution()

# Writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/cam_video.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frame_width, frame_height))

while (True):
    (ret, frame) = cap.read()
    if ret == True:
        out.write(frame)
        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()