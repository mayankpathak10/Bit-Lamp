import dlib
import cv2
import argparse as ap
import keypress
#import just_track

from keypress import*
keypress.key_points()
cam = cv2.VideoCapture(1)
retval, img = cam.read()

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





