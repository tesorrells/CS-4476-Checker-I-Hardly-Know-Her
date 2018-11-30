def buildBoard(redCenters, blackCenters):
	currentPos = [62, 62]
	redPositions = []
	blackPositions = []

	x = 1;
	y = 1;

	while x <= 8:
		x += 1
		while y <= 8:
			y += 1
			for red in redCenters:
				if red[0] < currentPos[0] and red[1] < currentPos[1]:
					redPositions.append([x , y ])
					redCenters.remove(red)
				else:
					currentPos = [62 * x, 62 * y]
		y = 1

	currentPos = [62, 62]

	x = 1;
	y = 1;

	while x <= 8:
		x += 1
		while y <= 8:
			y += 1
			for black in blackCenters:
				if black[0] < currentPos[0] and black[1] < currentPos[1]:
					blackPositions.append([x, y])
					blackCenters.remove(black)
				else:
					currentPos = [62 * x, 62 * y]
		y = 1

	print(redPositions)
	print(blackPositions)
	return redPositions, blackPositions
