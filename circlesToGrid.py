def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

def buildBoard(redCenters, blackCenters):
	currentPos = [62.5, 62.5]
	redPositions = []
	blackPositions = []

	x = 1;
	y = 1;

	while y <= 8:
		while x <= 8:
			for red in redCenters:
				if red[0] < currentPos[0] and red[1] < currentPos[1]:
					redPositions.append([x , y ])
					redCenters.remove(red)
				else:
					currentPos = [62.5 * x, 62.5 * y]
			x += 1
		x = 1
		y += 1

	x = 1;
	y = 1;

	while y <= 8:
		while x <= 8:
			for black in blackCenters:
				if black[0] < currentPos[0] and black[1] < currentPos[1]:
					blackPositions.append([x , y ])
					blackCenters.remove(black)
				else:
					currentPos = [62.5 * x, 62.5 * y]
			x += 1
		x = 1
		y += 1

	redPositions = Remove(redPositions)
	blackPositions = Remove(blackPositions)

	print(redPositions)
	print(blackPositions)
	return redPositions, blackPositions
