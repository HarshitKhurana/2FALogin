#!/usr/bin/python

# Harshit Khurana
# hkhurana3@gmail.com
# 11.01.18

import numpy as np
import cv2 , os ,sys
import Kairos_API_verify as verifyAPI

os.system("if [ -d Images_OpenCV ]; then echo ; else mkdir Images_OpenCV/; fi;")

#print "Smile, Clicking Photo using Laptop Camera"
cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):

    #To display the captured image
#    cv2.imshow('img1',frame) # Cant show , as at booting time the screen wont be available to show the image
    cv2.imwrite('Images_OpenCV/Image.jpg',frame) # Extension can be JPG/PNG
    cv2.destroyAllWindows()
    break

#print "\nDone , Thanks"
cap.release()

# This decide atleast what % of image should match
confidence_value = 50
result = verifyAPI.verify("Images_OpenCV/Image.jpg")

if type(result) == str:
	#print "result" # ERROR

	#SHOULD KILL HERE AS WELL
	os.system("killall -u `whoami`")


elif type(result) == int:
	confidence = result
	#print confidence
	if confidence > confidence_value:
	#     	print "Yeahh, you in man"
	#      	print "Exit status 0"
	       	sys.exit(0)
	else:
	#	print "Sorry impersonator, Not Allowed"
		os.system("killall -u `whoami`")
