import dlib
import cv2
import argparse as ap
import keypress
import math
#import just_track

from keypress import*
keypress.key_points()
cam = cv2.VideoCapture(1)
retval, img = cam.read()
h,w,chnl=img.shape
lower_x = int(0.3*w)
upper_x =int(0.61*w)
lower_y = int(0.33*h)
upper_y = int(0.64*h)

#points = [(0.3*w,0.33*h,0.61*w,0.64*h)]
points =[(lower_x,lower_y,upper_x,upper_y)]

#points = list(map(int,points))
#points = [math.floor(float(x)) for x in points]
#points = int(points)
print points
img2 = img.copy()
tracker = dlib.correlation_tracker()
    # Provide the tracker the initial position of the object
tracker.start_track(img, dlib.rectangle(*points[0]))
#print tracker

while True:
	retval, img = cam.read()		
#	from just_track.py import*
	tracker.update(img)
	rect = tracker.get_position()
	pt1 = (int(rect.left()), int(rect.top()))
	pt2 = (int(rect.right()), int(rect.bottom()))

	cv2.rectangle(img, pt1, pt2, (255, 255, 255), 3)
	print "Object tracked at [{}, {}] \r".format(pt1, pt2),

	cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
	cv2.imshow("Image", img)
	
	# Continue until the user presses ESC key
	if cv2.waitKey(1) == 27:
            break

 # Relase the VideoCapture object
cam.release()





