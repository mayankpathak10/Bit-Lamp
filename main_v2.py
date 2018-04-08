# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 23:21:25 2018

@author: Darshan
"""
#Import Stuff
import dlib
import cv2
import argparse as ap
import keypress
import Talk


#Load Camera
Talk("Initializing Systems.. Loading Camera")
cam = cv2.VideoCapture(1)
if not cam.isOpened():
        print "Video device or file couldn't be opened"
        exit()
#Wait for button Press and Capture target image
Talk("Bit Lamp ready. Press button to set target")
ButtonStatus = False
while(ButtonStatus == False):
    ButtonStatues = Check_button_press()

retval, Target_img = cam.read()
if not retval:
    Talk("Cannot capture frame device")
    exit()
S1 = 90 #Base Servo
S2 = 90 #Elbow Servo
S3 = 90 #Lamp Servo
D = 20 #Delta
#Set Arbitrary Target Bounding box
h,w,chnl=Target_img.shape
lower_x = int(0.3*w)
upper_x =int(0.61*w)
lower_y = int(0.33*h)
upper_y = int(0.64*h)
prev_tracked_point = (h/2, w/2)
#points = [(0.3*w,0.33*h,0.61*w,0.64*h)]
points =[(lower_x,lower_y,upper_x,upper_y)]

#Image Tracking
img2 = img.copy()
tracker = dlib.correlation_tracker()
# Provide the tracker the initial position of the object
tracker.start_track(img, dlib.rectangle(*points[0]))
while True:
    	retval, img = cam.read()		
    #	from just_track.py import*
    	tracker.update(img)
    	rect = tracker.get_position()
    	pt1 = (int(rect.left()), int(rect.top()))
    	pt2 = (int(rect.right()), int(rect.bottom()))    
    	cv2.rectangle(img, pt1, pt2, (255, 255, 255), 3)
        trac_x = (rect.right-rect.left)/2
        trac_y = (rect.bottom-rect.top)/2
        
        #Servos Thresholds
        xT = 50 #x axis Threshold
        yT = 20 #y axis Threshold
        
        if(trac_x < ((w/2)-xT) and S1<(180-D) ):
            S1 = S1+D
        if(trac_x > ((w/2)+xT) and S1>D):
            S1 = S1-D
        
        if(trac_y < ((h/2)-xT) and S2 < (180-D)):
            S2 = S2+D
            if(S2>140 and S3 < (180-D)):
                S3 = S3+D
        if(trac_y > ((h/2)+xT) and S2 > D):
            S2 = S2-D
            if(S2<50  and S3 > D):
                S3 = S3-D
        
        #Code to Actuate the servos.
        print repr(S1),repr(S2),repr(S3)
        
                
#    	print "Object tracked at [{}, {}] \r".format(pt1, pt2), 
    	cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    	cv2.imshow("Image", img)
        
        
    
