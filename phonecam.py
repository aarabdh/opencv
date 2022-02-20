import cv2
import numpy as np
url = 'URL://url.url'
cap = cv2.VideoCapture(url)

down_width = 1080
down_height = 720
down_points = (down_width, down_height)
blur = 5
while True:
    ret, frame = cap.read()
    resize = cv2.resize(frame, down_points, cv2.BORDER_DEFAULT)
    frame1 = image1 = cv2.rotate(resize, cv2.cv2.ROTATE_90_CLOCKWISE)
    frame2 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame3 = cv2.equalizeHist(frame2)
    frame4 = cv2.Laplacian(frame3, cv2.CV_64F, ksize=9)
    frame5 = 255 - frame4
    frame6 = cv2.GaussianBlur(frame5, (blur, blur), cv2.BORDER_DEFAULT)
    cv2.imshow('frame', frame6)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()