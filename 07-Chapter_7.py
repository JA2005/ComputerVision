# How to convert a video into grey and Black / White
import cv2 as cv
cap = cv.VideoCapture('resources/video.mp4')

while (True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #(thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY) # if you want to make your video in black abd white
    if ret == True:
        cv.imshow("Video", grayframe) # if gray is removed from grayframe, video will be in normal colors
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
