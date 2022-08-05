# How to read a video
import cv2 as cv
cap = cv.VideoCapture('resources/video.mp4')

# This will show that video is error free, I can see the video playing 
if (cap.isOpened() == False):
    print("error in reading video")

# How to read and Play video, while loop is used, so it shows that if video is ok then show it otherwise dont. 
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()