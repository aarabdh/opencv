import math
import cv2
import numpy as np
import keyboard

def isPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True


class Pointer():
    def __init__(self):
        self.coord = [0,0]
        self.stepCount = 0
        self.bR = 0
        self.bRX = 0
        self.angle = 0
    
    def move(self):
        self.stepCount = self.stepCount +1
        step = self.stepCount
        xin = self.coord[0]                 # Movement start
        yin = self.coord[1]
        if (self.angle%4 == 0):
            xin= xin+1
        elif (self.angle%4 == 1):
            yin = yin-1
        elif (self.angle%4 == 2):
            xin= xin-1
        elif (self.angle%4 == 3):
            yin = yin+1
        self.coord = [xin,yin]    # Movement end

        # bR dependent stuff
        if (self.bR == 0):
            self.angle = self.angle + 1 # Turn
            self.bRX = math.floor(math.sqrt(abs(step - 1)))
            self.bR = self.bRX
        else:
            self.bR = self.bR - 1
        

############
size = 1000
canvas = 255*np.ones((size,size,3), np.uint8)

mark = Pointer()
scale = 100
clr = (0,0,0)
clr2 = (255, 0, 0)
canvas = cv2.circle(canvas, (int(size/2),int(size/2)), 5, clr, -1)
canvas = cv2.circle(canvas, (int(size/2),int(size/2)), 13, clr, 1)

while(True):
    q = cv2.waitKey(90)

    if keyboard.is_pressed('x'):
        step = isPrime(mark.stepCount+2)
        mark.move()
        xyn = mark.coord[0]
        yyn = mark.coord[1]
        xyn = int(size/2) + (scale*xyn)
        yyn = int(size/2) + (scale*yyn)
        
        if (step):
            canvas = cv2.circle(canvas, (xyn,yyn), 5, clr2, -1)
        else:
            canvas = cv2.circle(canvas, (xyn,yyn), 1, clr, -1)
    cv2.imshow("YO", canvas)
    if q == ord("q"):
        break

cv2.destroyAllWindows()
