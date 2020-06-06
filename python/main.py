import cv2
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import ship_detection as sd



#--------------------------------------------------------------
#
#	VIDEO TO IMAGES
#
#--------------------------------------------------------------

# cap = cv2.VideoCapture( "/home/dando/Workspace/AntiShip/data/seq3_bigBoat.mp4" )
# c = 1
# while (True):
# 	ret, frame = cap.read()
# 	if( ret == False ):
# 		print ("Failed to read frame")
# 		break

# 	name = "/home/dando/Workspace/AntiShip/data/full/seq3_frames/img_" + str(c) + ".png"
# 	cv2.imwrite( name, frame )
# 	print( name )
# 	c = c + 1



#--------------------------------------------------------------
#
#	FLICK TEST
#
#--------------------------------------------------------------

cap = cv2.VideoCapture( "/home/dando/Workspace/AntiShip/data/seq3_bigBoat.mp4" )

while True:
	ret, frame = cap.read()
	if( ret == False ):
		print ("Failed to read frame")
		break

	gray = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY )