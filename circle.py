import cv2
import random


def init_image(img1, width, blur):  # Initialising image width and blur
    sh = img1.shape
    wi = sh[1]
    scale = width/wi
    img_scaled = cv2.resize(img1, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    blurred = cv2.GaussianBlur(img_scaled, (blur, blur), cv2.BORDER_DEFAULT)
    return blurred


def pixel(img2, xin, yin):  # Get the BGR values of pixels
    bl = int(img2[yin, xin, 0])
    gr = int(img2[yin, xin, 1])
    re = int(img2[yin, xin, 2])
    res = (bl, gr, re)
    return res


orig = cv2.imread('sample.jpg')
canvas = init_image(orig, 1080, 7)
(h, w, z) = canvas.shape

for i in range(40000):
    rad = random.randint(0, 5)
    x = random.randint(0, w-1)
    y = random.randint(0, h-1)
    clr = pixel(canvas, x, y)
    cv2.circle(img=canvas,
               center=(x, y),
               radius=rad,
               color=clr,
               thickness=-1)

cv2.imshow('image', canvas)
cv2.imwrite('.\output\out.png', canvas)
cv2.waitKey()