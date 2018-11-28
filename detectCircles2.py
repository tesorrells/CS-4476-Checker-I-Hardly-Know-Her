import cv2
import numpy as np
from glob import glob

def detectCircles(img, showImage = True):
	circleCenters = []
	redCenters = []
	blackCenters = []
	img = cv2.equalizeHist(img, 0)
	img = cv2.resize(img, (612, 816))
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
	circles = np.uint16(np.around(cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=10,param2=60,minRadius=5,maxRadius=37)))
	for i in circles[0,:]:
	    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
	    chunk = img[i[0] - i[2] + 5: i[0] + i[2] - 5, i[1] - i[2] + 5: i[1] + i[2] - 5]
	    avg = chunk.mean()
	    if avg < 110: 
	    	# red
	    	redCenters.append((i[0], i[1]))
	    else:
	    	#black
	    	blackCenters.append((i[0], i[1]))
	    circleCenters.append((i[0], i[1]))
	if showImage:
		cv2.imshow('circles', cimg)
		cv2.imwrite('circleDetection.png', cimg)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	return redCenters, blackCenters

#detectCircles(cv2.imread("IMG_4075.png", 0))
detectCircles(cv2.imread("circleDetection/IMG_4075.png", 0), True)
# images = glob('checkers/*/*.JPG')
# for i in range(len(images)):
# 	detectCircles(cv2.imread(images[i], 0))