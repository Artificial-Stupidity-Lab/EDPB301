import numpy as np

from djitellopy import tello

import cv2

me = tello.Tello()

me.connect()

print(me.get_battery())

me.streamon()

#me.takeoff()

cap = cv2.VideoCapture(1)

hsvVals = [0,0,188,179,33,245]

sensors = 3

threshold = 0.2

width, height = 480, 360

def thresholding(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([hsvVals[0], hsvVals[1], hsvVals[2]])

    upper = np.array([hsvVals[3], hsvVals[4], hsvVals[5]])

    mask = cv2.inRange(hsv, lower, upper)

    return mask

def getContours(imgThres, img):

    cx = 0

    contours, hieracrhy = cv2.findContours(imgThres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:

        biggest = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(biggest)

        cx = x + w // 2

        cy = y + h // 2

        cv2.drawContours(img, biggest, -1, (255, 0, 255), 7)

        cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    return cx


while True:

    #_, img = cap.read()

    img = me.get_frame_read().frame

    img = cv2.resize(img, (width, height))

    img = cv2.flip(img, 0)

    imgThres = thresholding(img)

    cx = getContours(imgThres, img)  ## For Translation

    cv2.imshow("Output", img)

    cv2.imshow("Path", imgThres)

    cv2.waitKey(1)