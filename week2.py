import cv2
import numpy as np
import math

fl = 700
l = 50
w = 25
img = cv2.imread("Capture.JPG")
#cv2.imshow("Shane Dawson", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV", img_hsv)
#cv2.waitKey(0)
contWidth = 0
contHeight = 0
cx = 0
cy = 0
distance = 0

height, width, channels = img.shape

def minx(owo):
    xd = width
    for lol in range(len(owo)):
        if(owo[lol] < xd):
            xd = owo[lol]
    return xd

def maxx(ha):
    wasd = 0
    for wa in range(len(ha)):
        if(ha[wa] > wasd):
            wasd = ha[wa]
    return wasd

def miny(arr):
    min = height
    for i in range(len(arr)):
        if(arr[i] < min):
            min = arr[i]
    return min

def maxy(arr):
    max = 0
    for i in range(len(arr)):
        if(arr[i] > max):
            max = arr[i]
    return max
        

#THRESHOLD_MIN = np.array([15, 50, 50], np.uint8)
#THRESHOLD_MAX = np.array([-5, 255, 255], np.uint8)

THRESHOLD_MIN = np.array([0, 0, 240], np.uint8)
THRESHOLD_MAX = np.array([255, 255, 255], np.uint8)

frame_threshed = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)

image,contours,hierarchy = cv2.findContours(frame_threshed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cont in contours:
    epsilon = 0.1*cv2.arcLength(cont, True)
    Output_Contour = cv2.approxPolyDP(cont, epsilon, True)
    approx = cv2.approxPolyDP(cont,epsilon,True)

    if(cv2.contourArea(approx)> 500):
        xPoints = [0, 0, 0, 0]
        yPoints = [0, 0, 0, 0]
        for i in range(len(approx)):
            for j in range(len(approx[i])):
                xPoints[i] = approx[i][j][0]
        for i in range(len(approx)):
            for j in range(len(approx[i])):
                yPoints[i] = approx[i][j][1]
        contWidth = maxx(xPoints) - minx(xPoints)
        contHeight = maxy(yPoints) - miny(yPoints)
        cx = minx(xPoints) + (contWidth/2)
        cy = miny(yPoints) + (contHeight/2)
        #for j in len(approx):
        cv2.drawContours(img, contours, 0, (255, 0, 255), 10)
        
distance = (fl*w)/contWidth
print(distance)
#for cont in contours:
#
#
# if 5>4: "change to check specific parameters"
#draw contours
#print your conditions in the if statement


#cv2.drawContours(img, contours, -1, (255,0,255), 10)

cv2.imshow("contours", img)
cv2.imshow("threshed image", frame_threshed)

