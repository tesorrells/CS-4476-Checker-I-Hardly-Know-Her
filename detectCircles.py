import cv2
import numpy as np
from glob import glob

def detectCircles(directory, showImage = True, rectangle = False):
	img = cv2.imread(directory, 0)
	img = cv2.medianBlur(img, 1)
	img2 = cv2.imread(directory)
	circleCenters = []
	redCenters = []
	blackCenters = []
	circles = np.uint16(np.around(cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1 = 20, param2 = 47, minRadius = 10, maxRadius = 40)))
	for i in circles[0,:]:
	    chunk = img2[i[1] - int(i[2]/2): i[1] + int(i[2]/2), i[0] - int(i[2]/2): i[0] + int(i[2]/2), :]
	    pixels = chunk[:][:]
	    blue, red, green = 0, 0, 0
	    for value in pixels[2]:
	    	blue += value[0]
	    	green += value[1]
	    	red += value[2]
	    blue /= len(pixels[2])
	    green /= len(pixels[2])
	    red /= len(pixels[2])
	    if rectangle:
	    	cv2.rectangle(img2, (i[0] - int(i[2]/2), i[1] - int(i[2]/2)), (i[0] + int(i[2]/2), i[1] + int(i[2]/2)), (255, 255, 0), 1)
	    cv2.circle(img2, (i[0], i[1]), i[2], (0,255,0), 5)
	    if 2 * red / (1.0 * blue + green) > 1.5:
	    	cv2.circle(img2, (i[0], i[1]), i[2], (100,100,255), 5)
	    	redCenters.append((i[0], i[1]))
	    else:
	    	cv2.circle(img2, (i[0], i[1]), i[2], (255, 255, 0), 5)
	    	blackCenters.append((i[0], i[1]))
	    circleCenters.append((i[0], i[1]))
	if showImage:
		cv2.imshow('circles', img2)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	return redCenters, blackCenters

def detectCirclesImages(image, showImage = True, rectangle = False):
	img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	img = cv2.medianBlur(img, 1)
	img2 = image
	circleCenters = []
	redCenters = []
	blackCenters = []
	circles = np.uint16(np.around(cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1 = 20, param2 = 47, minRadius = 10, maxRadius = 40)))
	for i in circles[0,:]:
	    chunk = img2[i[1] - int(i[2]/2): i[1] + int(i[2]/2), i[0] - int(i[2]/2): i[0] + int(i[2]/2), :]
	    pixels = chunk[:][:]
	    blue, red, green = 0, 0, 0
	    for value in pixels[2]:
	    	blue += value[0]
	    	green += value[1]
	    	red += value[2]
	    blue /= len(pixels[2])
	    green /= len(pixels[2])
	    red /= len(pixels[2])
	    if rectangle:
	    	cv2.rectangle(img2, (i[0] - int(i[2]/2), i[1] - int(i[2]/2)), (i[0] + int(i[2]/2), i[1] + int(i[2]/2)), (255, 255, 0), 1)
	    if 2 * red / (1.0 * blue + green) > 1.5:
	    	cv2.circle(img2, (i[0], i[1]), i[2], (100,100,255), 5)
	    	redCenters.append((i[0], i[1]))
	    else:
	    	cv2.circle(img2, (i[0], i[1]), i[2], (255, 255, 0), 5)
	    	blackCenters.append((i[0], i[1]))
	    circleCenters.append((i[0], i[1]))
	if showImage:
		cv2.imshow('circles', img2)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	return redCenters, blackCenters

# detectCircles("board.png", True, True)