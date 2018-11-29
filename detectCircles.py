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
	circles = np.uint16(np.around(cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1 = 15, param2 = 55, minRadius = 10, maxRadius = 40)))
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

def detectCirclesImages(image, showImage = True, rectangle = False):
	img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	img = cv2.medianBlur(img, 1)
	img2 = image
	circleCenters = []
	redCenters = []
	blackCenters = []
	circles = np.uint16(np.around(cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1 = 15, param2 = 55, minRadius = 10, maxRadius = 40)))
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

def buildBoard(redCenters, blackCenters):
	print("Building Grid")
	value = np.empty((), dtype=object)
	value[()] = (0, 0)
	boardGrid = np.full((8, 8), value, dtype=object)
	circleGrid = np.full((8, 8), 0, dtype=object)

	i = 1
	j = 1
	for space in boardGrid:
		while i < 9:
			while j < 9:
				boardGrid[i-1, j-1] = [int(62 * i), int(62 * j)]
				j += 1
			i += 1
			j = 1

	#print(boardGrid)

	for index, space in enumerate(boardGrid):
		for red in redCenters:
			redX = abs(red[0] - space[index][0])
			redY = abs(red[1] - space[index][1])
			if redX <= 30 and redY <= 30:
				circleGrid[index] = 1
		for black in blackCenters:
			blackX = abs(black[0] - space[index][0])
			blackY = abs(black[1] - space[index][1])
			if blackX <= 30 and blackY <= 30:
				circleGrid[index] = 2

	print(circleGrid)

# r, b = detectCircles("board.png", showImage = True, rectangle = False)
# buildBoard(r, b)
# detectCircles("circleDetection/IMG_4075.png", True)
#detectCircles("checkers/board1/IMG_4075.JPG", True)
