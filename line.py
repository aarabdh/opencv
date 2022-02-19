import cv2
import os
import random
from matplotlib import pyplot as plt
import numpy as np

canvas = cv2.imread('sample.jpg')

(h, w, y) = canvas.shape
#canvas = np.zeros((1024,1024,3), np.uint8)
cv2.line(canvas, (0,0), (w,h), (255,255,255),2)
cv2.line(canvas, (w,0), (0,h), (255,255,255),2)

# Start of for loop

cv2.imshow('image', canvas)
cv2.waitKey()
#window_name = 'Image Window'

#cv2.imshow(window_name, image)

#cv2.waitKey(0)

#cv2.destroyAllWindows()
