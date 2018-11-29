import cv2
import numpy as np
from glob import glob

def detectCircles(directory, showImage = True):
	img = cv2.imread(directory, 0)
	img = cv2.medianBlur(img, 1)
	img2 = cv2.imread(directory)
	circleCenters = []
	redCenters = []
	blackCenters = []
	circles = np.uint16(np.around(cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=100,minRadius=50,maxRadius=150)))
	for i in circles[0,:]:
	    chunk = img2[i[1] - i[2]/2: i[1] + i[2]/2, i[0] - i[2]/2: i[0] + i[2]/2, :]
	    pixels = chunk[:][:]
	    arr = np.array(pixels)
	    blue, red, green = 0, 0, 0
	    try: 
	    	for value in pixels[2]:
	    		blue += value[0]
	    		green += value[1]
	    		red += value[2]
	    	blue /= len(pixels[2])
	    	green /= len(pixels[2])
	    	red /= len(pixels[2])
	    except:
	   		print("help")
	    cv2.rectangle(img2, (i[0] - i[2]/2, i[1] - i[2]/2), (i[0] + i[2]/2, i[1] + i[2]/2), (255, 255, 0), 1)
	    if red > 70:
	    	cv2.circle(img2,(i[0],i[1]),i[2],(255,255,0),5)
	    	redCenters.append((i[0], i[1]))
	    else:
	    	#cv2.circle(img2,(i[0],i[1]),i[2],(255,255,0),5)
	    	blackCenters.append((i[0], i[1]))
	    circleCenters.append((i[0], i[1]))
	img2 = cv2.resize(img2, (612, 816))
	# cv2.rectangle(img2, (1940, 887), (3200, 2000), (100, 100, 200), 5)
	if showImage:
		cv2.imshow('circles', img2)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	return redCenters, blackCenters

detectCircles("circleDetection/IMG_4075.png", True)