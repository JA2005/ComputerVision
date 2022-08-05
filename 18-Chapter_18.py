# How to split videos into frames
import cv2 as cv
cap = cv.VideoCapture("resources/video.mp4") # video is about 5 seconds (30 frames per seconds) 
frameNr = 0
while(True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"resources/frames/frame_{frameNr}.jpg", frame)
    else:
        break
    frameNr = frameNr+2
cap.release()