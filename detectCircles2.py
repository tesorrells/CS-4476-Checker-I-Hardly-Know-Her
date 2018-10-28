import cv2
import numpy as np

def detectCircles(img):
	img = cv2.equalizeHist(img, 0)
	img = cv2.resize(img, (612, 816))
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
	circles = np.uint16(np.around(cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=10,param2=60,minRadius=5,maxRadius=37)))
	for i in circles[0,:]:
	    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.imshow('circles', cimg)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#detectCircles(cv2.imread("IMG_4075.png", 0))