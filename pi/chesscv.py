#!/usr/bin/env python3
import cv2
import numpy as np
import matplotlib.pyplot as plt

HTTP = 'http://'
IP_ADDRESS = '100.64.73.118'
URL =  HTTP + IP_ADDRESS + ':4747/mjpegfeed?640x480'

cap = cv2.VideoCapture(URL)
pixel = (20, 60, 80)

def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y,x]
        upper = np.array([pixel[0]+10, pixel[1]-10,pixel[2]+40])
        lower = np.array([pixel[0]-10, pixel[1]-10, pixel[2]-40])
        print(pixel,lower,upper)

# Corrective actions printed in the even of failed connection.
if cap.isOpened() is not True:
    print ('Connection Failed.')

# Connection successful. Proceeding to display video stream.
while cap.isOpened() is True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    blur = cv2.blur(frame, (5, 5))
    blur2 = cv2.medianBlur(blur, 5)
    blur3 = cv2.GaussianBlur(blur2, (5, 5), 0)
    blurfinal = cv2.bilateralFilter(blur3, 9, 75, 75)
    colorhsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Trying to detect white :( 
    
    lower_white = np.array([0, 0, 0])
    upper_white = np.array([0, 0, 255])
    white_mask = cv2.inRange(colorhsv, lower_white, upper_white)
   
    #Trying to detect black :(
    invert_fr = cv2.cvtColor(~frame,cv2.COLOR_BGR2HSV)
    black_mask = cv2.inRange(invert_fr, lower_white, upper_white)
    
    #Trying to detect Blank Spaces
    upper_purple = np.array([137, 180, 87])
    lower_purple = np.array([120, 180, 7])
    purple_mask = cv2.inRange(blurfinal, lower_purple, upper_purple)

    #lower: 
#[127 190  47] [117 180   7] [137 180  87]
#upper
    #navy: hsv(240,100,100)
    #hsv(240,100,50)
    #hsv(300,100,50)
    #result = cv2.bitwise_and(frame,frame,mask=purple_mask)
    

    #pick color
    #cv2.namedWindow('hsv')
    #cv2.setMouseCallback('hsv',pick_color)

    # now click into the hsv img , and look at values:
    #image_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsv",image_hsv)


    cv2.imshow('blurframe',blurfinal)    
    cv2.imshow('purle',purple_mask)
    #cv2.imshow('result', result)

    cv2.imshow('white_mask', white_mask)
    cv2.imshow('black_mask', black_mask)
    #Exiting 
    key = cv2.waitKey(1)
    if key%256 == 32:
        break

cap.release()
cv2.destroyAllWindows()