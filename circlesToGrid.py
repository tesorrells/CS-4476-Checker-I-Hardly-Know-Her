# Use with detectCricles.py

import cv2
import numpy as np
from glob import glob

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
				redCenters.remove(red)
		for black in blackCenters:
			blackX = abs(black[0] - space[index][0])
			blackY = abs(black[1] - space[index][1])
			if blackX <= 30 and blackY <= 30:
				circleGrid[index[0][1]] = 2
				blackCenters.remove(black)

	print(circleGrid)
	return circleGrid
